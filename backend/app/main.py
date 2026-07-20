import base64
import binascii
import secrets
from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse, Response
from fastapi.staticfiles import StaticFiles

from app import models
from app.config import settings
from app.db import SessionLocal, engine
from app.routers import assessment, attempts, explain, ingestion, topics, tutor

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Science Olympiad Coach")

# No CORS middleware needed: in dev, Vite's proxy (frontend/vite.config.ts)
# forwards /api to this server; in production this server serves the built
# frontend itself (below). Both cases are same-origin.


@app.middleware("http")
async def require_coach_auth(request: Request, call_next):
    """Gate the whole app behind one shared password once it's deployed.

    Deliberately a single shared secret, not per-coach accounts -- cheapest
    to build for a ~13-person known group, at the cost of a plain browser
    Basic Auth prompt instead of a styled login page. Disabled entirely when
    COACH_PASSWORD is unset (local dev's default).
    """
    if not settings.coach_password or request.url.path == "/api/health":
        return await call_next(request)

    unauthorized = Response(
        status_code=401,
        headers={"WWW-Authenticate": 'Basic realm="Science Olympiad Coach"'},
    )

    auth_header = request.headers.get("authorization", "")
    if not auth_header.startswith("Basic "):
        return unauthorized

    try:
        decoded = base64.b64decode(auth_header.removeprefix("Basic ")).decode("utf-8")
        _, _, supplied_password = decoded.partition(":")
    except (binascii.Error, UnicodeDecodeError):
        return unauthorized

    if not secrets.compare_digest(supplied_password, settings.coach_password):
        return unauthorized

    return await call_next(request)


app.include_router(topics.router)
app.include_router(ingestion.router)
app.include_router(explain.router)
app.include_router(assessment.router)
app.include_router(attempts.router)
app.include_router(tutor.router)


@app.on_event("startup")
def seed_demo_topic() -> None:
    db = SessionLocal()
    try:
        exists = db.query(models.Topic).filter(models.Topic.name == "Roller Coaster").first()
        if not exists:
            db.add(
                models.Topic(
                    event_name="Roller Coaster",
                    name="Roller Coaster",
                    description=(
                        "Division B/C event: teams design and build a roller coaster that "
                        "transports a marble/ball through a course, applying concepts of "
                        "energy conservation, forces, and track design."
                    ),
                )
            )
            db.commit()
    finally:
        db.close()


@app.get("/api/health")
def health():
    return {"status": "ok"}


# Serve the built frontend, if present (production deploy / `npm run build`
# locally). In local dev without a build, this directory won't exist and the
# app just serves the API -- run the frontend separately with `npm run dev`.
FRONTEND_DIST = Path(__file__).resolve().parent.parent.parent / "frontend" / "dist"

if FRONTEND_DIST.exists():
    app.mount("/assets", StaticFiles(directory=FRONTEND_DIST / "assets"), name="frontend-assets")

    @app.get("/{full_path:path}")
    def serve_frontend(full_path: str, request: Request):
        # React Router owns every non-/api path client-side -- always hand back
        # index.html and let it decide what to render, rather than 404ing on
        # e.g. /coach/1 which has no matching file on disk. A mistyped /api/*
        # path still 404s normally instead of silently returning HTML.
        if full_path.startswith("api/"):
            raise HTTPException(404, "Not found")
        return FileResponse(FRONTEND_DIST / "index.html")
