import logging
from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy import text
from starlette.middleware.sessions import SessionMiddleware

from app import auth, models
from app.config import settings
from app.db import SessionLocal, engine
from app.routers import assessment, attempts, auth as auth_router, explain, ingestion, topic_chat, topics, tutor

# INFO so llm/client.py's per-call logging (label, effort, char counts) shows
# up in Render's logs -- the app's cheapest way to see LLM call volume.
logging.basicConfig(level=logging.INFO)


def _ensure_column(table: str, column: str, ddl_type: str) -> None:
    """Add a column create_all won't add to an already-existing table.

    Dialect-aware: production runs Postgres (Neon), local dev defaults to
    SQLite (see README) -- the "does this column already exist" check needs
    different introspection per dialect, since PRAGMA is SQLite-only. The
    ALTER TABLE ADD COLUMN statement itself is portable across both and
    needs no branching.
    """
    with engine.connect() as conn:
        if engine.dialect.name == "sqlite":
            existing = {row[1] for row in conn.execute(text(f"PRAGMA table_info({table})"))}
        else:
            existing = {
                row[0]
                for row in conn.execute(
                    text("SELECT column_name FROM information_schema.columns WHERE table_name = :table"),
                    {"table": table},
                )
            }
        if column not in existing:
            conn.execute(text(f"ALTER TABLE {table} ADD COLUMN {column} {ddl_type}"))
            conn.commit()


def _migrate_coach_table_to_google_auth() -> None:
    """One-time: the old password-based `coaches` table (password_hash NOT
    NULL, no email/google_sub) can't be patched with ALTER TABLE ADD COLUMN
    alone -- password_hash needs to go away and email needs to become the
    required field. Production had zero rows in this table when this was
    written, so it's safe to just drop and let create_all below recreate it
    with the new schema, instead of writing a real data migration for
    accounts that don't exist yet. A no-op once the table already has the
    new schema (or doesn't exist yet at all).

    SQLite-only: a fresh Postgres database never has the old schema to begin
    with, so there's nothing to migrate away from there -- skip entirely.
    """
    if engine.dialect.name != "sqlite":
        return
    with engine.connect() as conn:
        existing = {row[1] for row in conn.execute(text("PRAGMA table_info(coaches)"))}
        if existing and "email" not in existing:
            conn.execute(text("DROP TABLE IF EXISTS coach_sessions"))
            conn.execute(text("DROP TABLE IF EXISTS coaches"))
            conn.commit()


_migrate_coach_table_to_google_auth()
models.Base.metadata.create_all(bind=engine)

# SQLite's permissive type affinity accepts a bare 0/1 literal for a boolean
# column default; Postgres needs a real boolean literal.
_bool_default = "0" if engine.dialect.name == "sqlite" else "false"

_ensure_column("topics", "created_by_coach_id", "INTEGER")
_ensure_column("assessments", "created_by_coach_id", "INTEGER")
_ensure_column("topics", "content_published", f"BOOLEAN DEFAULT {_bool_default}")
_ensure_column("topics", "story_md", "TEXT DEFAULT ''")
_ensure_column("concept_terms", "analogy", "TEXT DEFAULT ''")
_ensure_column("concept_terms", "image_data_url", "TEXT DEFAULT ''")
_ensure_column("concept_terms", "why_it_matters", "TEXT DEFAULT ''")
_ensure_column("coaches", "llm_provider", "VARCHAR(20)")
_ensure_column("coaches", "llm_api_key_encrypted", "TEXT")
_ensure_column("coaches", "google_drive_refresh_token_encrypted", "TEXT")
_ensure_column("resources", "error_message", "TEXT DEFAULT ''")
_ensure_column("topics", "assessment_type", "VARCHAR(20) DEFAULT 'test'")

# One-time backfill: the original demo seed (below) predates assessment_type
# and always used this exact name, so any pre-existing "Roller Coaster" row
# just got defaulted to 'test' by the ALTER TABLE above -- wrong, it's a
# build event. Only touches rows still sitting at that default, so it won't
# clobber a coach who already set this explicitly.
with engine.connect() as conn:
    conn.execute(
        text("UPDATE topics SET assessment_type = 'practical' WHERE name = 'Roller Coaster' AND assessment_type = 'test'")
    )
    conn.commit()


def _fail_orphaned_pending_resources() -> None:
    """Video/audio resources are processed by a FastAPI BackgroundTask
    (see routers/ingestion.py), which does not survive a process restart --
    if the app is starting up fresh, nothing could still be working on a
    resource that's status="pending" from before this boot, so it's
    guaranteed orphaned (a crash, a redeploy, an OOM kill mid-transcription).
    Left as "pending" it looks identical to "still processing" to a coach,
    with no way to tell the difference or know to retry -- mark it failed
    immediately instead, on every boot.
    """
    db = SessionLocal()
    try:
        stuck = db.query(models.Resource).filter(models.Resource.status == "pending").all()
        for r in stuck:
            r.status = "failed"
            r.error_message = "Processing was interrupted by a server restart -- remove this and try again."
        if stuck:
            db.commit()
    finally:
        db.close()


_fail_orphaned_pending_resources()

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


# On Render's Free instance type (512 MB RAM), reading a huge upload fully
# into memory before we get a chance to reject it can OOM-kill the process --
# the browser then sees the connection just die mid-request ("Failed to
# fetch"), not a clean error. Checking Content-Length here rejects oversized
# requests before Starlette ever reads the body, for every endpoint, not
# just the upload one.
#
# Uploads now stream straight to disk (see routers/ingestion.py,
# stream_upload_to_temp) instead of being buffered in memory as one bytes
# object, so this ceiling is about a sane per-file limit, not memory safety --
# 120MB comfortably covers real image-heavy resource PDFs (~80-90MB seen so far).
MAX_REQUEST_BYTES = 120 * 1024 * 1024


@app.middleware("http")
async def limit_request_size(request: Request, call_next):
    content_length = request.headers.get("content-length")
    if content_length and int(content_length) > MAX_REQUEST_BYTES:
        return JSONResponse(
            status_code=413,
            content={"detail": f"That file is too large (max {MAX_REQUEST_BYTES // (1024 * 1024)}MB)."},
        )
    return await call_next(request)


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
app.include_router(topic_chat.router)


@app.on_event("startup")
def seed_official_topics() -> None:
    """Pre-populate every official 2027 Division B event as a topic, so a
    coach starts with the real competition slate instead of having to type
    each one in by hand -- the "+ New topic" flow (routers/topics.py) still
    exists for a coach who wants a narrower custom topic on top of one of
    these (e.g. splitting "Dynamic Planet" into sub-topics).

    Assembled from soinc.org's 2027 Division B event slate (not scraped live
    -- this app has no route to that site at build time) -- a coach should
    still sanity-check names/groupings against the official page, especially
    Code Craze, which was still a trial event as of this writing and may not
    count toward the official 23-event slate the rest of this list assumes.

    Matched by `name`, so this is a no-op for any event a coach has already
    got (e.g. by editing one of these, or by name colliding with a manually
    created topic) -- never overwrites existing rows.
    """
    # (name, description, assessment_type) -- assessment_type is one of
    # "test" (written exam only), "practical" (hands-on/build, no separate
    # written exam), or "test_practical" (both).
    catalog = [
        # Earth & Space Science
        ("Dynamic Planet", "Written test on Earth science processes; the 2027 rotation focuses on fresh water systems -- rivers, lakes, groundwater, and watersheds.", "test"),
        ("Meteorology", "Written test on atmospheric science and weather; the 2027 rotation focuses on severe storms -- thunderstorms, tornadoes, and hurricanes.", "test"),
        ("Remote Sensing", "Written test on interpreting satellite and aerial imagery to study Earth's surface, atmosphere, and oceans.", "test"),
        ("Rocks and Minerals", "Written test on identifying and classifying rocks and minerals and understanding the processes that form them.", "test"),
        ("Solar System", "Written test on the Sun, planets, moons, and other bodies that make up our solar system.", "test"),
        # Technology & Engineering (build events)
        ("Hovercraft", "Build event: design and build a hovercraft that travels a course, scored on performance criteria like distance and time.", "practical"),
        ("Circuit Lab", "Combines a written test on circuit theory with a hands-on task building and analyzing real circuits.", "test_practical"),
        ("Thermodynamics", "Build a device that insulates a container of hot water for as long as possible, plus a written test on heat and thermodynamics concepts.", "test_practical"),
        ("Boomilever", "Build a lightweight wood structure that cantilevers from a wall and holds as much weight as possible before breaking.", "practical"),
        ("Elastic Launch Glider", "Build and launch a glider using stored elastic (rubber band) energy, scored on flight time and/or accuracy.", "practical"),
        ("Roller Coaster", "Build a device that transports a marble/ball through a course using only gravity and track design, applying concepts of energy conservation and forces.", "practical"),
        ("Scrambler", "Build a device that carries an egg across a set distance as fast as possible, stopping just short of a wall without breaking it.", "practical"),
        # Life, Personal & Social Science
        ("Anatomy & Physiology", "Written test on human body systems; the 2027 rotation focuses on the digestive, immune, and respiratory systems.", "test"),
        ("Disease Detectives", "Written test on epidemiology -- how diseases spread through a population and how outbreaks are investigated and controlled.", "test"),
        ("Heredity", "Written test on genetics -- inheritance patterns, Punnett squares, pedigrees, and molecular genetics.", "test"),
        ("Botany", "Written test on plant biology -- structure, physiology, classification, and ecology.", "test"),
        ("Water Quality", "Written test on aquatic ecosystems and water testing; the 2027 rotation focuses on marine and estuary environments.", "test"),
        # Inquiry & Nature of Science
        ("Crime Busters", "Hands-on forensic lab event (chemical tests, fingerprint analysis, and more) combined with a written test, applied to solving a mock crime scenario.", "test_practical"),
        ("Food Science", "Hands-on food science lab tasks combined with a written test on food chemistry, nutrition, and food safety.", "test_practical"),
        ("Codebusters", "Written test: decode cryptograms and ciphers (Aristocrats, Patristocrats, and other classical ciphers) under time pressure.", "test"),
        ("Experimental Design", "Hands-on event: design, carry out, and write up a controlled experiment using materials provided on the spot.", "practical"),
        ("Ping Pong Parachute", "Build a parachute-and-capsule device that protects and slows the descent of a dropped ping pong ball.", "practical"),
        ("Write It Do It", "Practical communication event: one partner writes instructions describing a structure, and the other builds it from the instructions alone.", "practical"),
        ("Protein Modeling", "Build a physical 3D model of a given protein or molecule from a supplied description, judged for structural accuracy.", "practical"),
        # Trial event as of this writing -- verify it's on the current official slate
        ("Code Craze", "Quiz and coding activities testing computer science concepts -- programming basics, AI/ML, and cryptography. Still a trial event as of this writing; confirm it's on the current official slate.", "test_practical"),
    ]

    db = SessionLocal()
    try:
        existing_names = {row[0] for row in db.query(models.Topic.name)}
        for name, description, assessment_type in catalog:
            if name in existing_names:
                continue
            db.add(
                models.Topic(
                    event_name=name,
                    name=name,
                    description=description,
                    assessment_type=assessment_type,
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
