import logging
from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy import text
from starlette.middleware.sessions import SessionMiddleware

from app import auth, models
from app.config import settings
from app.db import SessionLocal, engine
from app.routers import assessment, attempts, auth as auth_router, explain, ingestion, topics, tutor

# INFO so llm/client.py's per-call logging (label, effort, char counts) shows
# up in Render's logs -- the app's cheapest way to see LLM call volume.
logging.basicConfig(level=logging.INFO)


def _ensure_column(table: str, column: str, ddl_type: str) -> None:
    """Add a column create_all won't add to an already-existing table.

    SQLite-specific (PRAGMA table_info) -- fine since we're deliberately on
    SQLite at this scale (see README); revisit if that ever changes.
    """
    with engine.connect() as conn:
        existing = {row[1] for row in conn.execute(text(f"PRAGMA table_info({table})"))}
        if column not in existing:
            conn.execute(text(f"ALTER TABLE {table} ADD COLUMN {column} {ddl_type}"))
            conn.commit()


def _migrate_coach_table_to_google_auth() -> None:
    """One-time: the old password-based `coaches` table (password_hash NOT
    NULL, no email/google_sub) can't be patched with ALTER TABLE ADD COLUMN
    alone -- password_hash needs to go away and email needs to become the
    required field. Production has zero rows in this table (confirmed before
    writing this), so it's safe to just drop and let create_all below
    recreate it with the new schema, instead of writing a real data
    migration for accounts that don't exist yet. A no-op once the table
    already has the new schema (or doesn't exist yet at all).
    """
    with engine.connect() as conn:
        existing = {row[1] for row in conn.execute(text("PRAGMA table_info(coaches)"))}
        if existing and "email" not in existing:
            conn.execute(text("DROP TABLE IF EXISTS coach_sessions"))
            conn.execute(text("DROP TABLE IF EXISTS coaches"))
            conn.commit()


_migrate_coach_table_to_google_auth()
models.Base.metadata.create_all(bind=engine)

_ensure_column("topics", "created_by_coach_id", "INTEGER")
_ensure_column("assessments", "created_by_coach_id", "INTEGER")
_ensure_column("topics", "content_published", "BOOLEAN DEFAULT 0")
_ensure_column("topics", "story_md", "TEXT DEFAULT ''")
_ensure_column("concept_terms", "analogy", "TEXT DEFAULT ''")
_ensure_column("concept_terms", "image_data_url", "TEXT DEFAULT ''")

app = FastAPI(title="Science Olympiad Coach")

# Only for Authlib's OAuth state/nonce during the Google login handshake
# (routers/auth.py) -- separate from our own CoachSession cookie
# (app/auth.py), which is what actually tracks logged-in state afterward.
# https_only follows PUBLIC_BASE_URL rather than the request scheme because
# Render terminates TLS in front of us; the app itself only ever sees http.
app.add_middleware(
    SessionMiddleware,
    secret_key=settings.session_secret,
    same_site="lax",
    https_only=settings.public_base_url.startswith("https://"),
)

# No CORS middleware needed: in dev, Vite's proxy (frontend/vite.config.ts)
# forwards /api to this server; in production this server serves the built
# frontend itself (below). Both cases are same-origin.


@app.middleware("http")
async def attach_coach_session(request: Request, call_next):
    """Resolve the session cookie to a Coach (if any) for every request.

    Only attaches request.state.coach -- it does NOT block unauthenticated
    requests. Coaches and students share this API: coaches log in to author
    content, students never log in at all (they just enter a name per
    attempt). Individual coach-only endpoints enforce login themselves via
    the auth.require_coach dependency; see routers/topics.py, ingestion.py,
    explain.py, and assessment.py for where that's applied.
    """
    token = request.cookies.get(auth.SESSION_COOKIE_NAME)
    coach = None
    if token:
        db = SessionLocal()
        try:
            coach = auth.get_coach_from_token(db, token)
        finally:
            db.close()
    request.state.coach = coach

    return await call_next(request)


app.include_router(auth_router.router)
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
