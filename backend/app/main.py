import logging
from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy import text
from starlette.middleware.sessions import SessionMiddleware

from app import auth, models
from app.config import settings
from app.content.deterministic import publish_deterministic_content
from app.content.official_rules import RULES_2027, apply_official_rules
from app.content.solar_system.seed import seed_solar_system_learning_content
from app.db import SessionLocal, engine
from app.routers import assessment, attempts, auth as auth_router, explain, ingestion, lessons, students, topic_chat, topics, tutor

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


def _migrate_student_table_to_google_auth() -> None:
    """One-time: the old username+PIN `students` table (username/password_hash
    NOT NULL, no email/google_sub) can't be patched with ALTER TABLE ADD
    COLUMN alone -- mirrors _migrate_coach_table_to_google_auth above. Drop
    and let create_all below recreate it with the new schema. Any student
    accounts added under the old PIN system need to be re-added (this time
    by email) after this runs; CASCADE also drops the FK from attempts/
    topic_chat_messages.student_id, not those tables themselves.
    """
    with engine.connect() as conn:
        if engine.dialect.name == "sqlite":
            existing = {row[1] for row in conn.execute(text("PRAGMA table_info(students)"))}
        else:
            existing = {
                row[0]
                for row in conn.execute(
                    text("SELECT column_name FROM information_schema.columns WHERE table_name = 'students'")
                )
            }
        if existing and "email" not in existing:
            cascade = "" if engine.dialect.name == "sqlite" else " CASCADE"
            conn.execute(text(f"DROP TABLE IF EXISTS student_sessions{cascade}"))
            conn.execute(text(f"DROP TABLE IF EXISTS students{cascade}"))
            conn.commit()


_migrate_coach_table_to_google_auth()
_migrate_student_table_to_google_auth()
models.Base.metadata.create_all(bind=engine)

# SQLite's permissive type affinity accepts a bare 0/1 literal for a boolean
# column default; Postgres needs a real boolean literal.
_bool_default = "0" if engine.dialect.name == "sqlite" else "false"

_ensure_column("topics", "created_by_coach_id", "INTEGER")
_ensure_column("assessments", "created_by_coach_id", "INTEGER")
_ensure_column("topics", "content_published", f"BOOLEAN DEFAULT {_bool_default}")
_ensure_column("topics", "story_md", "TEXT DEFAULT ''")
_ensure_column("topics", "open_to_all_students", f"BOOLEAN DEFAULT {_bool_default}")
_ensure_column("topics", "story_origin", "VARCHAR(20) DEFAULT ''")
_ensure_column("topics", "lesson_json", "JSON")
_ensure_column("resources", "deterministic", f"BOOLEAN DEFAULT {_bool_default}")
_ensure_column("resources", "chunks_indexed", f"BOOLEAN DEFAULT {_bool_default}")
_ensure_column("concept_terms", "origin", "VARCHAR(20) DEFAULT 'ai'")
_ensure_column("concept_terms", "analogy", "TEXT DEFAULT ''")
_ensure_column("concept_terms", "image_data_url", "TEXT DEFAULT ''")
_ensure_column("concept_terms", "why_it_matters", "TEXT DEFAULT ''")
_ensure_column("coaches", "llm_provider", "VARCHAR(20)")
_ensure_column("coaches", "llm_api_key_encrypted", "TEXT")
_ensure_column("coaches", "google_drive_refresh_token_encrypted", "TEXT")
_ensure_column("resources", "error_message", "TEXT DEFAULT ''")
_ensure_column("topics", "assessment_type", "VARCHAR(20) DEFAULT 'test'")
_ensure_column("attempts", "student_id", "INTEGER")
_ensure_column("topic_chat_messages", "student_id", "INTEGER")
_ensure_column("topics", "parent_topic_id", "INTEGER")
_ensure_column("topics", "overview_what", "TEXT DEFAULT ''")
_ensure_column("topics", "overview_learn", "TEXT DEFAULT ''")
_ensure_column("topics", "overview_assessed", "TEXT DEFAULT ''")
_ensure_column("topics", "overview_theme_2027", "TEXT DEFAULT ''")
_ensure_column("topics", "overview_notes", "TEXT DEFAULT ''")

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
async def attach_identity(request: Request, call_next):
    """Resolve the session cookie to a Coach or a Student (if either) for
    every request. Only attaches request.state.coach/student -- it does NOT
    block unauthenticated requests; the frontend gate (App.tsx) handles that
    for every page now that students have real accounts too. Coach-only
    endpoints still enforce login themselves via auth.require_coach; see
    routers/topics.py, ingestion.py, explain.py, and assessment.py for where
    that's applied.

    One cookie, two tables: the token is looked up in CoachSession first,
    then StudentSession, since a browser is signed in as at most one of the
    two at a time (see auth.py's create_session/create_student_session).
    """
    token = request.cookies.get(auth.SESSION_COOKIE_NAME)
    coach = None
    student = None
    if token:
        db = SessionLocal()
        try:
            coach = auth.get_coach_from_token(db, token)
            if coach is None:
                student = auth.get_student_from_token(db, token)
        finally:
            db.close()
    request.state.coach = coach
    request.state.student = student

    return await call_next(request)


app.include_router(auth_router.router)
app.include_router(topics.router)
app.include_router(ingestion.router)
app.include_router(explain.router)
app.include_router(assessment.router)
app.include_router(attempts.router)
app.include_router(tutor.router)
app.include_router(topic_chat.router)
app.include_router(lessons.router)
app.include_router(students.router)


def _rename_protein_modeling_to_protein_builders() -> None:
    """One-time correction: "Protein Modeling" is actually the Division C
    (high school) event name -- Division B's analog is a differently-named
    trial event, "Protein Builders". Renames any existing row rather than
    leaving a stale duplicate; a coach's resources/concepts/assessments stay
    attached since those link by topic_id, not name. No-op once already
    renamed, and never touches a row a coach separately created named
    "Protein Modeling" on purpose (rare, but checked via the join).
    """
    with engine.connect() as conn:
        conn.execute(
            text(
                "UPDATE topics SET name = 'Protein Builders', event_name = 'Protein Builders' "
                "WHERE name = 'Protein Modeling' AND parent_topic_id IS NULL"
            )
        )
        conn.commit()


def _apply_official_event_name_corrections() -> None:
    """One-time correction: two catalog entries didn't exactly match
    soinc.org's official 2027 Division B event names -- "Elastic Launch
    Glider" is actually "Elastic Launched Glider", and "Anatomy &
    Physiology" is actually "Anatomy and Physiology". Renames any existing
    row rather than leaving a stale duplicate; a coach's resources/
    concepts/assessments stay attached since those link by topic_id, not
    name. No-op once already renamed.
    """
    corrections = [
        ("Elastic Launch Glider", "Elastic Launched Glider"),
        ("Anatomy & Physiology", "Anatomy and Physiology"),
    ]
    with engine.connect() as conn:
        for old_name, new_name in corrections:
            conn.execute(
                text(
                    "UPDATE topics SET name = :new_name, event_name = :new_name "
                    "WHERE name = :old_name AND parent_topic_id IS NULL"
                ),
                {"old_name": old_name, "new_name": new_name},
            )
        conn.commit()


@app.on_event("startup")
def _remove_unconfirmed_trial_events() -> None:
    """One-time cleanup: "Protein Builders" and "Code Craze" were seeded by
    an earlier version of this app despite being unconfirmed Division B
    trial events (not on soinc.org's confirmed 2027 roster). They're no
    longer in seed_official_topics's catalog, so this removes any row
    already seeded for either name -- but only if a coach hasn't actually
    put anything on it (a resource, concept, assessment, schedule entry,
    chapter, chat message, student assignment, or published/edited story).
    If there's real content, the row is left alone; deleting a coach's work
    isn't a "fix". No-op once already removed.
    """
    db = SessionLocal()
    try:
        for name in ("Protein Builders", "Code Craze"):
            topic = (
                db.query(models.Topic)
                .filter(models.Topic.name == name, models.Topic.parent_topic_id.is_(None))
                .first()
            )
            if topic is None:
                continue
            has_content = (
                db.query(models.Resource).filter(models.Resource.topic_id == topic.id).first() is not None
                or db.query(models.Diagram).filter(models.Diagram.topic_id == topic.id).first() is not None
                or db.query(models.ConceptTerm).filter(models.ConceptTerm.topic_id == topic.id).first() is not None
                or db.query(models.ScheduleEntry).filter(models.ScheduleEntry.topic_id == topic.id).first() is not None
                or db.query(models.Assessment).filter(models.Assessment.topic_id == topic.id).first() is not None
                or db.query(models.TopicChatMessage).filter(models.TopicChatMessage.topic_id == topic.id).first() is not None
                or db.query(models.StudentTopic).filter(models.StudentTopic.topic_id == topic.id).first() is not None
                or db.query(models.Topic).filter(models.Topic.parent_topic_id == topic.id).first() is not None
                or topic.content_published
                or bool(topic.story_md.strip())
            )
            if has_content:
                continue
            db.delete(topic)
        db.commit()
    finally:
        db.close()


@app.on_event("startup")
def seed_official_topics() -> None:
    """Pre-populate every official 2027 Division B event as a topic, so a
    coach starts with the real competition slate instead of having to type
    each one in by hand -- the "+ New topic" flow (routers/topics.py) still
    exists for a coach who wants a narrower custom topic on top of one of
    these (e.g. splitting "Dynamic Planet" into sub-topics).

    The slate matches the 2027 Division B Rules Manual. "Protein Builders"
    and "Code Craze" are deliberately left off -- the manual prints them
    only as trial events, not part of the national roster (see
    `_remove_unconfirmed_trial_events` above, which also cleans up any row
    seeded for them by an earlier version of this app).

    Matched by `name`, so this is a no-op for any event a coach has already
    got (e.g. by name colliding with a manually created topic). Rules text
    is filled in afterwards by apply_official_rules_2027.
    """
    # Every confirmed event, grouped as before. Description, assessment_type
    # ("test" = written only, "practical" = hands-on/build only,
    # "test_practical" = both) and the overview_* rules all come from
    # content/official_rules.py (the 2027 Division B Rules Manual), which
    # apply_official_rules re-applies on every startup.
    catalog = [
        # Earth & Space Science
        "Dynamic Planet", "Meteorology", "Remote Sensing", "Rocks and Minerals", "Solar System",
        # Technology & Engineering
        "Hovercraft", "Circuit Lab", "Thermodynamics", "Boomilever", "Elastic Launched Glider",
        "Roller Coaster", "Scrambler",
        # Life, Personal & Social Science
        "Anatomy and Physiology", "Disease Detectives", "Heredity", "Botany", "Water Quality",
        # Inquiry & Nature of Science
        "Crime Busters", "Food Science", "Codebusters", "Experimental Design", "Ping Pong Parachute",
        "Write It Do It",
    ]

    db = SessionLocal()
    try:
        _rename_protein_modeling_to_protein_builders()
        _apply_official_event_name_corrections()

        existing_names = {row[0] for row in db.query(models.Topic.name)}
        for name in catalog:
            if name not in existing_names:
                rules = RULES_2027[name]
                db.add(
                    models.Topic(
                        event_name=name,
                        name=name,
                        description=rules["description"],
                        assessment_type=rules["assessment_type"],
                    )
                )
        db.commit()
    finally:
        db.close()


@app.on_event("startup")
def seed_thermodynamics_deep_dive() -> None:
    """One-time content correction + deep-dive setup for Thermodynamics,
    from the actual scioly.org wiki page (coach-supplied PDF): idempotently
    seeds a grounding resource plus 4 deep-dive chapters. The event's
    rules (including the new 2027 heat-collection device) live in
    content/official_rules.py; the chapters cover the written test, which
    the device change doesn't affect.
    """
    db = SessionLocal()
    try:
        topic = (
            db.query(models.Topic)
            .filter(models.Topic.name == "Thermodynamics", models.Topic.parent_topic_id.is_(None))
            .first()
        )
        if topic is None:
            return

        # Rules (description + overview_*) come from content/official_rules.py.

        if not db.query(models.Resource).filter(
            models.Resource.topic_id == topic.id, models.Resource.title == "scioly.org wiki: Thermodynamics (event page)"
        ).first():
            db.add(
                models.Resource(
                    topic_id=topic.id,
                    type="text",
                    title="scioly.org wiki: Thermodynamics (event page)",
                    source_url="https://scioly.org/wiki/Thermodynamics",
                    raw_text=(
                        "EVENT INFO: Division B & C, 2 participants, eye protection required, "
                        "device impounded, ~50 minutes. Allowed resources: one hole-punched 3-ring "
                        "binder of any size (sheets removable), tools, supplies, writing utensils, "
                        "two Class III calculators. First run 2012, returned 2018/2019/2027; topic "
                        "rotates in the sense that the DEVICE task has changed over the event's "
                        "history (see below), though the written-test content is stable.\n\n"
                        "WRITTEN TEST STRUCTURE (2027 rules): 3 questions from each of 5 areas -- "
                        "(1) thermodynamic systems, zeroth law, definition of temperature, "
                        "temperature scales/conversions, heat units; (2) phases of matter, phase "
                        "transitions, phase diagrams, latent and sensible heat, ideal gas law; "
                        "(3) heat transfer, thermal conductivity, heat capacity, specific heat; "
                        "(4) thermodynamic laws and processes (Carnot cycle and efficiency, "
                        "adiabatic, isothermal), the first and second laws; (5) history of "
                        "thermodynamics -- Kelvin, Joseph Black, Joule, Carnot, Planck, Clausius, "
                        "Boltzmann, Maxwell. State/National only: radiant exitance, blackbody "
                        "radiation, Stefan-Boltzmann law, third law. Division C State/National "
                        "only: entropy and enthalpy.\n\n"
                        "THE FOUR LAWS OF THERMODYNAMICS: Zeroth Law -- if two systems are each in "
                        "thermal equilibrium with a third, they're in thermal equilibrium with each "
                        "other (defines temperature without invoking entropy). First Law -- a "
                        "closed system's change in internal energy equals heat added minus work "
                        "done by the system (dU = Q - W); conservation of energy. Second Law -- "
                        "heat cannot spontaneously flow from colder to hotter; entropy of an "
                        "isolated system tends to increase. Third Law -- the entropy of a perfect "
                        "crystal approaches zero as temperature approaches absolute zero, and "
                        "absolute zero itself can never actually be reached.\n\n"
                        "GAS LAWS: Gay-Lussac's Law (P/T = constant at fixed volume); Boyle's Law "
                        "(PV = constant at fixed temperature); Charles's Law (V/T = constant at "
                        "fixed pressure); Avogadro's Law (relates volume and amount of gas at fixed "
                        "P and T); the Combined Gas Law (P1V1/T1 = P2V2/T2); the Ideal Gas Law "
                        "(PV = nRT); van der Waals' equation (a real-gas correction to the ideal "
                        "gas law accounting for intermolecular attraction and molecular volume). "
                        "Also: Hess' Law (heat of a chemical process is the same whether it happens "
                        "in one step or several) and Le Chatelier's Principle (a system reacts to "
                        "absorb an imposed change).\n\n"
                        "HEAT THEORIES: the obsolete caloric theory held that heat is a weightless "
                        "fluid ('caloric') that flows from hot to cold substances (proposed by "
                        "Antoine Lavoisier, 1770s). The valid kinetic theory holds that matter is "
                        "made of molecules in constant random motion, with average kinetic energy "
                        "proportional to temperature; all gas laws are derivable from it. James "
                        "Clerk Maxwell is considered its father.\n\n"
                        "CARNOT CYCLE: a theoretical, maximally-efficient (but not physically "
                        "achievable) heat engine cycle with 4 steps: (1) isothermal expansion "
                        "against a hot reservoir, (2) reversible adiabatic expansion, (3) isothermal "
                        "compression against a cold reservoir, (4) adiabatic compression back to "
                        "the start. Efficiency: eta = 1 - Tc/Th = 1 - Q2/Q1. The cycle's entropy "
                        "change is zero overall (the two adiabatic steps are isentropic); Carnot's "
                        "Principle states no engine between two fixed-temperature reservoirs can "
                        "exceed the efficiency of this reversible cycle.\n\n"
                        "JOULE'S LAWS: First Law -- heat dissipated by a resistive component is "
                        "Q = I^2*R*t (links electrical engineering to thermodynamics via P = I^2*R "
                        "and P = VI). Second Law -- the internal energy of an ideal gas depends "
                        "only on its temperature, not its volume or pressure.\n\n"
                        "THERMODYNAMIC SYSTEMS & PROCESSES: Open (matter, heat, and work can cross "
                        "the boundary); Closed (heat and work can cross, matter can't); Isolated "
                        "(nothing crosses); Diathermic (only heat crosses); Adiabatic-boundary "
                        "system (heat can't cross, everything else can). Processes: isobaric "
                        "(constant pressure), isochoric/isometric (constant volume, no work done), "
                        "isothermal (constant temperature), adiabatic (no heat added/removed), "
                        "isentropic (constant entropy).\n\n"
                        "KEY CONSTANTS & CONVERSIONS: gas constant R = 8.314 J/(mol*K); Boltzmann's "
                        "constant = 1.38x10^-23 J/K; Avogadro's constant = 6.02x10^23; absolute "
                        "zero = 0 K = -273.15 C = -459.67 F. Temperature conversions: "
                        "K = C + 273.15; F = (9/5)C + 32; C = (5/9)(F-32). Energy conversions: "
                        "1 BTU ~ 1,055 J; 1 small calorie ~ 4.2 J; 1 large Calorie (kcal) ~ 4,200 J "
                        "= 1,000 small calories.\n\n"
                        "VOCABULARY: Entropy -- a measure of a system's randomness / energy "
                        "unavailable to do work. Enthalpy -- total energy content of a system. "
                        "Gibbs' Free Energy (deltaG = deltaH - T*deltaS) -- the energy available to "
                        "do useful work; positive deltaG means a non-spontaneous (endergonic) "
                        "reaction, negative means spontaneous (exergonic). Latent heat -- heat that "
                        "changes a substance's phase without changing its temperature. Sensible "
                        "heat -- heat that changes temperature without changing phase. Specific "
                        "heat / heat capacity -- energy needed to raise 1 kg of a substance by 1 C. "
                        "Thermal equilibrium -- two objects/systems at the same temperature "
                        "exchanging no net heat.\n\n"
                        "HISTORY: James Prescott Joule (1818-1889) linked electrical and thermal "
                        "energy, leading to the first law. Sadi Carnot (1796-1832), \"Father of "
                        "Thermodynamics,\" first analyzed heat engines (the Carnot Cycle). Rudolf "
                        "Clausius (1822-1888) first stated the second law and introduced entropy "
                        "(1865). Walther Nernst (1864-1941) developed the third law (Nobel Prize "
                        "1920). James Clerk Maxwell (1831-1879) formulated the kinetic theory and "
                        "devised the \"Maxwell's Demon\" thought experiment. William Thomson/Lord "
                        "Kelvin (1824-1907) determined absolute zero and coined the word "
                        "\"thermodynamics.\" Daniel Fahrenheit (1686-1736) invented the mercury "
                        "thermometer and his namesake scale. Anders Celsius (1701-1744) proposed "
                        "the Celsius scale. Galileo (1564-1642) built the first open thermometer.\n\n"
                        "DEVICE (pre-2027 classic version -- confirm against the current rules): "
                        "teams built a device to insulate a 250 mL glass/plastic beaker filled with "
                        "75-125 mL of hot water (60-75 C start), aiming to lose the least heat over "
                        "a set time (25 min for Division B). The device had to fit a 20 cm cube "
                        "(Division B) / 15 cm cube (Division C) and allow beaker insertion/removal "
                        "and a temperature-probe access hole. Scoring combined a plot-completeness "
                        "score, a heat-retention score (internal vs. external control-beaker "
                        "temperature ratio), a prediction-accuracy score, and an optional ice-water "
                        "bonus."
                    ),
                )
            )

        chapters = [
            (
                "Thermodynamics: Laws & Systems",
                "The four laws of thermodynamics, plus the types of thermodynamic systems "
                "(open/closed/isolated) and processes (isobaric/isothermal/adiabatic/etc).",
                (
                    "THE FOUR LAWS: Zeroth -- if two systems are each in thermal equilibrium with "
                    "a third, they're in equilibrium with each other; defines temperature without "
                    "invoking entropy. First -- dU = Q - W (a closed system's internal energy "
                    "change equals heat added minus work done); conservation of energy. Second -- "
                    "heat cannot spontaneously flow from colder to hotter; entropy of an isolated "
                    "system tends to increase (illustrated by a steam engine losing usable heat as "
                    "it approaches its surroundings' temperature). Third -- the entropy of a "
                    "perfect crystal approaches zero as temperature approaches absolute zero, and "
                    "absolute zero can never actually be reached (an object always loses heat to a "
                    "colder one in ever-smaller, asymptotic amounts).\n\n"
                    "THERMODYNAMIC SYSTEMS: a system is a defined region analyzed via "
                    "thermodynamics; everything else is its surroundings, separated by a boundary "
                    "(fixed, movable, imaginary, or real). Open systems let matter, heat, and work "
                    "all cross the boundary. Closed systems let heat and work cross but not matter "
                    "(a closed system's boundary can additionally be adiabatic -- blocks heat -- or "
                    "rigid -- blocks work). Isolated systems let nothing cross, so they trend "
                    "toward thermodynamic equilibrium. Diathermic systems let only heat cross.\n\n"
                    "THERMODYNAMIC PROCESSES: isobaric (constant pressure, e.g. a movable piston "
                    "held at atmospheric pressure); isochoric/isometric (constant volume, so the "
                    "system does zero work -- e.g. a sealed can heated in a fire); isothermal "
                    "(constant temperature, e.g. a system in a constant-temperature bath); "
                    "adiabatic (no heat added or removed -- the boundary is a thermal insulator); "
                    "isentropic (constant entropy -- identical to adiabatic for a reversible "
                    "process).\n\n"
                    "BRANCHES OF THERMODYNAMICS: Classical (macroscopic, measurable properties); "
                    "Statistical (molecular/atomic scale, explains classical behavior from "
                    "microscopic interactions); Chemical (thermodynamics of chemical reactions); "
                    "Equilibrium (how a system's matter/energy change as it approaches "
                    "equilibrium); Non-Equilibrium (systems not in thermal equilibrium)."
                ),
            ),
            (
                "Thermodynamics: Gas Laws & Heat Theories",
                "Boyle's, Charles's, Gay-Lussac's, and the combined/ideal gas laws; the obsolete "
                "caloric theory vs. the valid kinetic theory of heat; Joule's Laws.",
                (
                    "GAS LAWS: Gay-Lussac's Law -- P/T = constant at fixed volume (pressure "
                    "proportional to Kelvin temperature). Boyle's Law -- PV = constant at fixed "
                    "temperature (volume inversely proportional to pressure). Charles's Law -- "
                    "V/T = constant at fixed pressure (volume proportional to Kelvin temperature). "
                    "Avogadro's Law -- relates volume and amount of gas at fixed pressure and "
                    "temperature. The Combined Gas Law merges these: P1V1/T1 = P2V2/T2 (useful for "
                    "two-state problems -- discard any variable not given). The Ideal Gas Law -- "
                    "PV = nRT -- combines all of them for any gas. Van der Waals' equation corrects "
                    "the ideal gas law for real gases by accounting for intermolecular attraction "
                    "(a/V^2 term) and molecular volume (b term).\n\n"
                    "OTHER LAWS: Hess' Law -- the heat evolved/absorbed in a chemical process is "
                    "the same whether it happens in one step or several (law of constant heat "
                    "summation). Le Chatelier's Principle -- a system responds to an imposed change "
                    "in a way that absorbs/counteracts it.\n\n"
                    "HEAT THEORIES: The caloric theory (obsolete, proposed by Antoine Lavoisier in "
                    "the 1770s) held heat is a weightless fluid ('caloric') that flows from hot to "
                    "cold substances and is conserved -- its only correct assumption was that heat "
                    "is weightless. The kinetic theory (valid, first modeled by August Kronig in "
                    "1856, developed further by James Clerk Maxwell) holds that matter is made of "
                    "molecules in constant random motion, colliding elastically, with average "
                    "kinetic energy proportional to temperature; all gas laws can be derived from "
                    "it.\n\n"
                    "JOULE'S LAWS: First -- heat dissipated by a resistive component is "
                    "Q = I^2*R*t, linking electrical engineering (P = I^2*R = VI) to "
                    "thermodynamics. Second -- an ideal gas's internal energy depends only on its "
                    "temperature, not its volume or pressure."
                ),
            ),
            (
                "Thermodynamics: The Carnot Cycle & Entropy",
                "The Carnot Cycle's 4 steps, its key equations for work/heat/temperature/entropy, "
                "efficiency, and the Maxwell's Demon thought experiment.",
                (
                    "THE CARNOT CYCLE is a theoretical, maximally efficient (but not physically "
                    "achievable) heat engine cycle, foundational to the four laws. It's "
                    "theoretical because it's reversible (real engines aren't) and involves zero "
                    "net entropy change (real processes always increase entropy somewhere).\n\n"
                    "THE 4 STEPS: (1) Isothermal Expansion -- gas in contact with a hot reservoir "
                    "expands, doing work, at constant temperature. (2) Reversible Adiabatic "
                    "Expansion -- gas continues expanding with no heat exchange, losing internal "
                    "energy and cooling. (3) Isothermal Compression -- gas in contact with a cold "
                    "reservoir is compressed at constant temperature, releasing heat to the cold "
                    "reservoir. (4) Adiabatic Compression -- gas is compressed with no heat "
                    "exchange, raising its temperature back to the start.\n\n"
                    "KEY EQUATIONS: Efficiency eta = 1 - Q2/Q1 = 1 - Tc/Th (Q1 = heat absorbed from "
                    "the hot reservoir, Q2 = heat released to the cold reservoir). Work "
                    "W = Q1 - Q2 = Q1*(1 - Tc/Th). Entropy change per isothermal step: "
                    "deltaS_hot = Q1/Th, deltaS_cold = -Q2/Tc -- and since the cycle is reversible, "
                    "the total change is zero (deltaS = 0), meaning Q2/Q1 = Tc/Th. The two "
                    "adiabatic steps are isentropic (zero entropy change each).\n\n"
                    "CARNOT'S PRINCIPLE (Sadi Carnot): no heat engine operating between two "
                    "fixed-temperature reservoirs can be more efficient than a reversible engine -- "
                    "because real heat transfer always loses some energy to the surroundings. This "
                    "is effectively a restatement/proof of the second law.\n\n"
                    "MAXWELL'S DEMON is a thought experiment (by James Clerk Maxwell) imagining a "
                    "tiny creature sorting fast/slow gas molecules through a trapdoor to create a "
                    "hot side and cold side without doing work -- seemingly violating the second "
                    "law. The resolution: the demon must expend energy to observe molecules and "
                    "gains entropy operating the door, so total system entropy still increases; no "
                    "real violation of the second law has ever been found."
                ),
            ),
            (
                "Thermodynamics: Conversions, Vocabulary & History",
                "Temperature/energy unit conversions, key constants and equations, core "
                "vocabulary, and the historical figures who developed thermodynamics.",
                (
                    "TEMPERATURE CONVERSIONS: K = C + 273.15. F = (9/5)*C + 32. C = (5/9)*(F-32). "
                    "Absolute zero = 0 K = -273.15 C = -459.67 F.\n\n"
                    "ENERGY UNIT CONVERSIONS: 1 British Thermal Unit (BTU) ~ 1,055 J. 1 small "
                    "calorie ~ 4.2 J. 1 large Calorie (kcal) ~ 4,200 J = 1,000 small calories. "
                    "1 Joule = 1 N*m = 1 kg*m^2/s^2 = 1 W*s = 1 V*A*s = 1 V*Coulomb.\n\n"
                    "KEY CONSTANTS: gas constant R = 8.314 J/(mol*K). Boltzmann's constant = "
                    "1.38x10^-23 J/K. Avogadro's constant = 6.02x10^23. Electron volt = "
                    "1.60217646x10^-19 J. 101.325 kPa = 760 torr = 1 atm.\n\n"
                    "KEY VOCABULARY: Entropy -- heat energy unavailable to do work; a measure of a "
                    "system's randomness. Enthalpy -- a system's total energy content. Gibbs' Free "
                    "Energy (deltaG = deltaH - T*deltaS) -- the energy available to do useful "
                    "work; positive means a non-spontaneous/endergonic reaction, negative means "
                    "spontaneous/exergonic. Latent heat -- heat that changes phase without "
                    "changing temperature. Sensible heat -- heat that changes temperature without "
                    "changing phase or volume. Specific heat/heat capacity -- energy to raise 1 kg "
                    "of a substance 1 C. Thermal equilibrium -- no net heat exchange between "
                    "objects at the same temperature. Quasistatic process -- a hypothetical, "
                    "always-stable process despite ongoing changes. Phlogiston and Caloric -- both "
                    "obsolete, discredited 'substance' theories of combustion/heat.\n\n"
                    "HISTORY: James Prescott Joule (1818-1889) linked electrical and thermal "
                    "energy, leading to the first law; the Joule unit is named for him. Sadi "
                    "Carnot (1796-1832), \"Father of Thermodynamics,\" first analyzed heat engines "
                    "in his 1824 work, giving us the Carnot Cycle. Rudolf Clausius (1822-1888) "
                    "first stated the second law (1850) and introduced entropy (1865). Walther "
                    "Nernst (1864-1941) developed the third law, winning the 1920 Nobel Prize. "
                    "James Clerk Maxwell (1831-1879) formulated the kinetic theory of heat and the "
                    "Maxwell's Demon thought experiment. William Thomson/Lord Kelvin (1824-1907) "
                    "determined absolute zero, coined \"thermodynamics,\" and has the Kelvin scale "
                    "named for him. Daniel Fahrenheit (1686-1736) invented the mercury thermometer "
                    "and his namesake scale. Anders Celsius (1701-1744) proposed the Celsius "
                    "scale. Galileo Galilei (1564-1642) built the first open thermometer."
                ),
            ),
        ]

        for chapter_name, chapter_description, chapter_text in chapters:
            existing = (
                db.query(models.Topic)
                .filter(models.Topic.name == chapter_name, models.Topic.parent_topic_id == topic.id)
                .first()
            )
            if existing is None:
                sub_topic = models.Topic(
                    event_name=topic.event_name,
                    name=chapter_name,
                    description=chapter_description,
                    assessment_type=topic.assessment_type,
                    parent_topic_id=topic.id,
                )
                db.add(sub_topic)
                db.flush()
                db.add(
                    models.Resource(
                        topic_id=sub_topic.id,
                        type="text",
                        title="scioly.org wiki: Thermodynamics (excerpt for this chapter)",
                        source_url="https://scioly.org/wiki/Thermodynamics",
                        raw_text=chapter_text,
                    )
                )

        db.commit()
    finally:
        db.close()


@app.on_event("startup")
def seed_hovercraft_content() -> None:
    """One-time content correction for Hovercraft (Division B), from the
    actual scioly.org wiki page (coach-supplied PDF, same source as the
    Solar System / Thermodynamics corrections).

    Deliberately does NOT seed deep-dive chapters like those two did: this
    wiki page is largely unfilled for the 2027 season -- its construction/
    competition-parameters, design-tips, and scoring sections are still
    literal community placeholders ("Add current construction parameters
    here!"), not real numbers. Inventing specific build dimensions or
    scoring formulas not actually on the page would violate the same
    "deterministic, sourced content only" instruction this whole feature is
    built around. What IS confirmed and worth correcting: the written-exam
    portion no longer exists (pure build/run event now), participants,
    eye protection, impound, allowed resources, and time. A coach with the
    actual 2027 rules PDF (soinc.org/hovercraft-b) can prompt a follow-up
    to add real deep-dive chapters once those specifics exist. The rules
    themselves (dimensions, Target Time scoring, nickel loads) now come
    from the 2027 Rules Manual via content/official_rules.py.
    """
    db = SessionLocal()
    try:
        topic = (
            db.query(models.Topic)
            .filter(models.Topic.name == "Hovercraft", models.Topic.parent_topic_id.is_(None))
            .first()
        )
        if topic is None:
            return

        # Rules (description + overview_*) come from content/official_rules.py.

        if not db.query(models.Resource).filter(
            models.Resource.topic_id == topic.id, models.Resource.title == "scioly.org wiki: Hovercraft (event page)"
        ).first():
            db.add(
                models.Resource(
                    topic_id=topic.id,
                    type="text",
                    title="scioly.org wiki: Hovercraft (event page)",
                    source_url="https://scioly.org/wiki/Hovercraft",
                    raw_text=(
                        "EVENT INFO: Division B & C, Physics/Build category, 2 participants, eye "
                        "protection Category B, device and notes both impounded, ~8 minutes. "
                        "Allowed at competition: one vehicle (impounded), papers/notes (impounded), "
                        "tools/supplies, spare parts, two Class III calculators. First appearance "
                        "2017, returned for 2027; the wiki lists this event as rotating.\n\n"
                        "FORMAT: Hovercraft is a build event for the 2026-2027 season -- design, "
                        "build, and calibrate a self-propelled, air-levitated vehicle ahead of the "
                        "tournament, then run it down a track without it stopping along the way. "
                        "The device MUST actually levitate; if it doesn't, it's considered a "
                        "regular (non-hovering) vehicle instead, and this may be checked by event "
                        "supervisors if there's any suspicion. Formerly (prior seasons) this event "
                        "was a dual lab with both a written-test portion and a build portion -- for "
                        "the current rules, the written exam does not exist anymore; it's build/run "
                        "only.\n\n"
                        "NOT YET DOCUMENTED ON THIS WIKI SNAPSHOT (community placeholders as of "
                        "this page's last edit): specific construction parameters (size/weight/"
                        "power limits, allowed materials), competition parameters (track "
                        "dimensions/layout), design tips & strategy, and the scoring formula. Get "
                        "these from the official Division B rules at soinc.org/hovercraft-b."
                    ),
                )
            )

        db.commit()
    finally:
        db.close()


@app.on_event("startup")
def seed_meteorology_deep_dive() -> None:
    """One-time content correction + deep-dive setup for Meteorology
    (Division B only -- no Division C equivalent exists), from the actual
    scioly.org wiki page (coach-supplied PDF, same pattern as the Solar
    System / Thermodynamics corrections).

    Confirms the 2027 focus topic is Severe Storms (the wiki's topic-
    rotation table shows 2026 Everyday Weather / 2027 Severe Storms /
    Climate next) -- matching the event description's own wording. The main
    wiki page only covers foundational atmosphere/pressure/wind/water-vapor
    content in depth and *links out* to separate sub-pages for each
    rotating topic's specifics (e.g. Severe Storms' Thunderstorms,
    Hurricanes, Winter Storms, Mid-Latitude Cyclones, Atmospheric Rivers)
    without their content inline -- those sub-pages weren't fetched, so the
    Severe Storms chapter below is a sourced checklist of what to study,
    not fabricated storm-specific facts, consistent with keeping every
    chapter's content traceable to what was actually on the page.
    """
    db = SessionLocal()
    try:
        topic = (
            db.query(models.Topic)
            .filter(models.Topic.name == "Meteorology", models.Topic.parent_topic_id.is_(None))
            .first()
        )
        if topic is None:
            return

        # Rules (description + overview_*) come from content/official_rules.py.

        if not db.query(models.Resource).filter(
            models.Resource.topic_id == topic.id, models.Resource.title == "scioly.org wiki: Meteorology (event page)"
        ).first():
            db.add(
                models.Resource(
                    topic_id=topic.id,
                    type="text",
                    title="scioly.org wiki: Meteorology (event page)",
                    source_url="https://scioly.org/wiki/Meteorology",
                    raw_text=(
                        "EVENT INFO: Division B only (no Division C equivalent), 2 participants, "
                        "~50 minutes. Allowed resources (2023-24 rules onward): one binder of any "
                        "size with information in any form, two stand-alone Class II calculators, "
                        "writing utensils. First run 2003; the EVENT doesn't rotate in/out, but its "
                        "focus TOPIC rotates yearly among Everyday Weather, Severe Storms, and "
                        "Climate.\n\n"
                        "TOPIC ROTATION (from the wiki's table): 2010 Everyday Weather / 2011 "
                        "Severe Storms / 2012 Climate. 2013/2014/2015 same pattern. 2016/2017/2018 "
                        "same pattern. 2019/2020-21/2022 same pattern. 2023/2024/2025 same "
                        "pattern. 2026 Everyday Weather / 2027 Severe Storms / (Climate next).\n\n"
                        "TEST FORMAT: usually a written test or a slideshow-based test; "
                        "occasionally rotating stations. Question types: multiple choice, true/"
                        "false, matching, diagram labeling, short answer, free response. Tip from "
                        "the wiki: split the binder-lookup work between partners to save time; "
                        "there's typically no penalty for wrong answers, so attempt every "
                        "question.\n\n"
                        "BASIC METEOROLOGICAL INFORMATION (applies across all 3 rotating topics):\n"
                        "- Atmosphere: mostly nitrogen and oxygen gas; key variables are "
                        "temperature, pressure, and humidity. Layers bottom to top: Troposphere "
                        "(where most weather occurs), Stratosphere, Mesosphere, Thermosphere, "
                        "Exosphere.\n"
                        "- Pressure: the weight of the atmosphere over an area; greatest at the "
                        "surface, decreases exponentially with altitude. Low-pressure areas are "
                        "cyclones; high-pressure areas are anticyclones.\n"
                        "- Wind: driven by pressure differences (pressure gradient force), flowing "
                        "from high to low pressure. The Coriolis effect (from Earth's rotation) "
                        "deflects wind right in the Northern Hemisphere, left in the Southern "
                        "Hemisphere. Surface friction can reduce wind speed.\n"
                        "- Water vapor & clouds: water vapor enters the atmosphere via evaporation, "
                        "then condenses (to liquid droplets) or deposits (to ice crystals) to form "
                        "clouds; large enough droplets/crystals fall as precipitation. Air is "
                        "'saturated' when it holds the maximum water vapor possible at its "
                        "temperature (warmer air holds more). Rising air expands and cools; the "
                        "temperature at which it becomes saturated is the dew point.\n"
                        "- Instruments: historically thermometers, barometers (pressure), and rain "
                        "gauges; modern methods include satellites, radar, and weather balloons/"
                        "radiosondes, with data plotted on maps and specialized charts.\n\n"
                        "2027 TOPIC (SEVERE STORMS) SUB-PAGES NAMED BY THE WIKI (content not "
                        "included in this source -- study checklist only): Thunderstorms, "
                        "Hurricanes, Winter Storms, Mid-Latitude Cyclones, Atmospheric Rivers."
                    ),
                )
            )

        chapters = [
            (
                "Meteorology: Atmosphere Basics",
                "Atmosphere composition and layers -- foundational content that applies no matter "
                "which topic is in rotation.",
                (
                    "ATMOSPHERE COMPOSITION: almost all atmospheric gas is nitrogen and oxygen. "
                    "Key variables to track are temperature, pressure, and humidity (water vapor "
                    "content).\n\n"
                    "LAYERS OF THE ATMOSPHERE (bottom to top): Troposphere -- where most weather "
                    "patterns occur. Stratosphere. Mesosphere. Thermosphere. Exosphere -- the "
                    "outermost layer."
                ),
            ),
            (
                "Meteorology: Pressure & Wind",
                "Cyclones and anticyclones, pressure gradient force, and the Coriolis effect -- "
                "foundational content that applies no matter which topic is in rotation.",
                (
                    "PRESSURE: think of atmospheric pressure as the weight of the atmosphere over "
                    "an area. It's greatest at the surface and decreases exponentially with "
                    "altitude; it also varies horizontally over time. Low-pressure areas are called "
                    "cyclones; high-pressure areas are called anticyclones.\n\n"
                    "WIND: driven by horizontal pressure differences, which create a pressure "
                    "gradient force that pushes wind from high pressure toward low pressure. Wind "
                    "in motion is deflected -- to the right in the Northern Hemisphere, to the left "
                    "in the Southern Hemisphere -- due to Earth's rotation; this is the Coriolis "
                    "effect. Friction, especially near the surface, can also reduce wind speed."
                ),
            ),
            (
                "Meteorology: Water Vapor, Clouds & Instruments",
                "The evaporation-condensation-precipitation cycle, saturation and dew point, and "
                "the instruments used to measure weather -- foundational content that applies no "
                "matter which topic is in rotation.",
                (
                    "WATER VAPOR & CLOUDS: water vapor (the gaseous state of water) typically "
                    "enters the atmosphere through evaporation of surface liquid water. In the "
                    "atmosphere it can condense into liquid cloud droplets or deposit directly into "
                    "solid ice crystals; these can grow (including by joining with other droplets/"
                    "crystals) and eventually fall as precipitation once large enough. Water vapor "
                    "makes up roughly 0% to 4-5% of air and is a 'variable gas' -- warmer air can "
                    "hold more of it. Air is 'saturated' when it holds the maximum water vapor "
                    "possible at its temperature; any more forms liquid droplets or ice crystals.\n\n"
                    "DEW POINT: rising air expands (matching the surrounding air's decreasing "
                    "pressure) and cools as a result. The temperature at which the air's actual "
                    "water vapor content equals the maximum it can hold is the dew point -- further "
                    "rising/cooling past that point forms cloud droplets or ice crystals.\n\n"
                    "INSTRUMENTS: historically, thermometers, barometers (measure atmospheric "
                    "pressure), and rain gauges. Modern methods include satellites, radar, and "
                    "weather balloons/radiosondes, with the resulting data plotted on maps and "
                    "specialized charts."
                ),
            ),
            (
                "Meteorology: 2027 Topic -- Severe Storms",
                "This year's rotating focus topic. The wiki names these sub-topics but their "
                "detailed content lives on separate pages not included in this source -- treat "
                "this as a study checklist, not a complete reference.",
                (
                    "CONFIRMED 2027 FOCUS: Severe Storms (per both the event's own description and "
                    "the wiki's topic-rotation table: 2026 Everyday Weather, 2027 Severe Storms, "
                    "Climate next in the 3-year cycle).\n\n"
                    "NAMED SUB-TOPICS (per the wiki's own Severe Storms page list -- study these "
                    "specifically, using a meteorology textbook, the linked scioly.org sub-pages, "
                    "or soinc.org/meteorology-b for the actual content, since it wasn't included in "
                    "this source): Thunderstorms. Hurricanes. Winter Storms. Mid-Latitude Cyclones. "
                    "Atmospheric Rivers.\n\n"
                    "All of this builds on the foundational atmosphere/pressure/wind/water-vapor "
                    "material in the other three chapters -- severe storms are, at their core, "
                    "extreme expressions of those same underlying processes (pressure gradients, "
                    "moisture, instability)."
                ),
            ),
        ]

        for chapter_name, chapter_description, chapter_text in chapters:
            existing = (
                db.query(models.Topic)
                .filter(models.Topic.name == chapter_name, models.Topic.parent_topic_id == topic.id)
                .first()
            )
            if existing is None:
                sub_topic = models.Topic(
                    event_name=topic.event_name,
                    name=chapter_name,
                    description=chapter_description,
                    assessment_type=topic.assessment_type,
                    parent_topic_id=topic.id,
                )
                db.add(sub_topic)
                db.flush()
                db.add(
                    models.Resource(
                        topic_id=sub_topic.id,
                        type="text",
                        title="scioly.org wiki: Meteorology (excerpt for this chapter)",
                        source_url="https://scioly.org/wiki/Meteorology",
                        raw_text=chapter_text,
                    )
                )

        db.commit()
    finally:
        db.close()


@app.on_event("startup")
def seed_botany_deep_dive() -> None:
    """One-time content correction + deep-dive setup for Botany (Division B
    focus, per the coach's standing instruction), from the actual
    scioly.org wiki page (coach-supplied PDF, same pattern as the prior
    corrections).

    IMPORTANT: the wiki page explicitly marks a "Division C Concepts"
    section partway through, covering Nutrient Deficiencies and Plant
    Diseases -- everything after that marker is Division-C-only material
    and is deliberately excluded from both the grounding resource and all
    deep-dive chapters below. Only content before that marker (plant
    groups/classification, anatomy/reproduction, photosynthesis/ecology,
    human uses, history) is shared between B and C and included here.
    Note the 2027 Division B Rules Manual does list plant diseases and
    nutrient deficiencies for Division B; the event's rules overview
    (content/official_rules.py) says so, but these wiki chapters predate it.

    Also confirms Botany is brand new as an official national event for
    2027 -- it ran as a trial event since 2020 and replaces Entomology on
    the national roster, so (unlike some other events) there's no yearly
    rotating focus topic to track.
    """
    db = SessionLocal()
    try:
        topic = (
            db.query(models.Topic)
            .filter(models.Topic.name == "Botany", models.Topic.parent_topic_id.is_(None))
            .first()
        )
        if topic is None:
            return

        # Rules (description + overview_*) come from content/official_rules.py.

        if not db.query(models.Resource).filter(
            models.Resource.topic_id == topic.id, models.Resource.title == "scioly.org wiki: Botany (event page, Division B scope)"
        ).first():
            db.add(
                models.Resource(
                    topic_id=topic.id,
                    type="text",
                    title="scioly.org wiki: Botany (event page, Division B scope)",
                    source_url="https://scioly.org/wiki/Botany",
                    raw_text=(
                        "EVENT INFO: Division B & C, 2 participants, ~50 minutes, written exam "
                        "only. Allowed resources: one 8.5x11 note sheet (both sides), a calculator "
                        "(the page's summary box says two Class II calculators; its body text says "
                        "one -- verify current rules), writing utensils. Trial event since 2020 "
                        "(first run at New Jersey regionals); becomes an official national event "
                        "for the first time in 2027, replacing Entomology. NOTE: this excerpt "
                        "excludes everything the wiki marks as \"Division C Concepts\" (nutrient "
                        "deficiencies and plant diseases) -- Division B is not tested on that "
                        "material.\n\n"
                        "ALGAE VS. MULTICELLULAR PLANTS: algae can be unicellular or multicellular "
                        "and typically live underwater; plants are multicellular and thrive on "
                        "land. Algae are nonvascular and lack connective tissues, leaves, stems, "
                        "and roots, unlike plants.\n\n"
                        "MONOCOTS VS. DICOTS: seed-bearing plants are classified by cotyledon "
                        "count -- monocots have one, dicots have two. Leaf venation: monocots have "
                        "parallel veins, dicots have branching veins. Stem structure: monocots' "
                        "vascular bundles are scattered around the stem; dicots' form a ring near "
                        "the edge. Root systems: monocots typically have a fibrous root system "
                        "(many small branching roots); dicots typically have a taproot (one thick "
                        "central root with smaller branches). Floral patterns: monocot flower parts "
                        "usually come in multiples of 3; dicot flower parts usually come in "
                        "multiples of 4 or 5.\n\n"
                        "EMBRYOPHYTES VS. CRYPTOGAMS: Embryophytes are land plants that nurture "
                        "the young sporophyte inside the gametophyte's tissue -- nonvascular plants "
                        "(mosses, liverworts, hornworts), seedless vascular plants (ferns, "
                        "lycophytes), gymnosperms (conifers, cycads), and angiosperms (flowering "
                        "plants). Cryptogams reproduce via spores rather than seeds/flowers -- "
                        "thallophytes (fungi, bacteria, algae), bryophytes (nonvascular plants), "
                        "and pteridophytes (seedless vascular plants).\n\n"
                        "WOODY VS. HERBACEOUS PLANTS: woody plants are generally long-lived "
                        "perennials with secondary growth and a lignin-reinforced woody stem; they "
                        "go dormant (growth slows/stops) in winter rather than dying back, and "
                        "practice self-pruning of unneeded branches/leaves. Herbaceous plants "
                        "(herbs) lack a permanent woody stem, grow mostly via primary (lengthwise) "
                        "growth, and are annuals (1-year life cycle), biennials (2-year), or "
                        "perennials (2+ years, dying back to a small underground portion each "
                        "year); fast-growing annual herbs are often pioneer species in ecological "
                        "succession.\n\n"
                        "VASCULAR PLANT ANATOMY: two key systems -- the shoot system (stem and "
                        "leaves, above ground) and the root system (below ground) -- are "
                        "interdependent (shoot needs roots for water/minerals, roots need the "
                        "shoot for food/energy). Four main organ systems: stem (connects leaves to "
                        "roots via the xylem and phloem), roots (anchor the plant, absorb water/"
                        "nutrients), leaves (photosynthesize), and reproductive organs (enable "
                        "sexual or asexual reproduction).\n\n"
                        "REPRODUCTION -- ALTERNATION OF GENERATIONS: plants alternate between a "
                        "diploid sporophyte stage and a haploid gametophyte stage, which can look "
                        "identical (isomorphic, e.g. some algae) or different (heteromorphic, e.g. "
                        "angiosperms). In most nonvascular plants the gametophyte dominates; in "
                        "seed plants the sporophyte dominates and the gametophyte is reduced (in "
                        "most angiosperms, to just a few cells). Sporophytes produce sporangia, "
                        "which produce haploid spores that develop into gametophytes; gametophytes "
                        "produce gametangia (archegonia = female gametes, antheridia = male "
                        "gametes -- not present in all plants, e.g. angiosperms have neither). Two "
                        "gametes fuse into a zygote, which develops into a new sporophyte. "
                        "Homosporous plants produce one spore type (hermaphroditic gametophytes); "
                        "heterosporous plants (e.g. pines) produce two types -- larger female "
                        "megaspores and smaller male microspores.\n\n"
                        "LIFE CYCLES: Moss (bryophyte) -- spores disperse to favorable spots and "
                        "germinate into protonemata (branched filaments anchored by rhizoids, not "
                        "roots), which bud into male and female gametophytes; flagellated sperm "
                        "swim through water to fertilize eggs, forming a zygote that grows into a "
                        "sporophyte (seta + capsule) still attached to and dependent on the female "
                        "gametophyte; meiosis inside the capsule produces new spores, released when "
                        "the capsule matures. Fern (pterophyte) -- similar dispersal/protonemata "
                        "steps, but most ferns are homosporous with a single bisexual gametophyte "
                        "producing antheridia and archegonia at different times; the resulting "
                        "sporophyte grows true leaves, with sori (spore clusters) on their "
                        "undersides. Gymnosperms (non-flowering seed plants, e.g. conifers) -- "
                        "microspores and megaspores form on cone structures called strobili; wind "
                        "carries pollen to the megasporangiate strobili, and roughly a year after "
                        "pollination fertilization occurs, followed by wind-dispersed seed release. "
                        "Angiosperms (flowering plants) -- microsporogenesis (anther) and "
                        "megasporogenesis (ovule) produce spores; pollination (via wind, insects, "
                        "etc.) leads to double fertilization unique to angiosperms, where one sperm "
                        "fertilizes the egg and the other fuses with polar nuclei to form the "
                        "triploid endosperm; the ovary wall then develops into fruit (exocarp/"
                        "mesocarp/endocarp).\n\n"
                        "PHOTOSYNTHESIS: occurs in chloroplasts (outer/inner membranes, thylakoids, "
                        "stroma). Light-dependent reactions happen in the thylakoid membranes, "
                        "converting sunlight and water into ATP, NADPH, and oxygen. Light-"
                        "independent reactions (the Calvin cycle) happen in the stroma, converting "
                        "CO2, ATP, and NADPH into G3P (using the enzyme RuBisCO).\n\n"
                        "ENERGY & NUTRIENT CYCLES: plants are primary producers -- Gross Primary "
                        "Productivity (GPP) is the total energy they generate; Net Primary "
                        "Productivity (NPP) is what's left after their own respiration, available "
                        "to herbivores/decomposers. The 10% Rule (Lindeman's Efficiency): on "
                        "average only ~10% of stored energy passes to the next trophic level, the "
                        "rest lost as heat/movement/waste. Carbon cycle: plants fix atmospheric CO2 "
                        "via RuBisCO in the Calvin Cycle, release some back via respiration, and "
                        "buried undecayed matter can become peat/coal over geologic time. Nitrogen "
                        "cycle: bacteria fix N2 into usable ammonium/nitrate for plant roots to "
                        "assimilate; decomposers recycle it, and denitrifying bacteria return excess "
                        "back to atmospheric N2. Water cycle: transpiration moves water up through "
                        "the xylem and out through leaf stomata. Phosphorus cycle: plants absorb "
                        "soil phosphate directly, or via mycorrhizal fungal symbiosis (fungi trade "
                        "phosphate for photosynthetic carbohydrates).\n\n"
                        "HUMAN & ANIMAL USES OF PLANTS: fibers (cotton seed hairs, phloem stem "
                        "fibers, monocot leaf fibers) and wood (from the vascular cambium) for "
                        "textiles/construction/paper. Endosperm (triploid, nutrient-rich tissue in "
                        "seeds) is the main starch source in cereal grains. Bulbs (short stem + "
                        "fleshy modified leaves) and corms (solid swollen stem tissue, e.g. taro) "
                        "and storage roots (e.g. sweet potatoes, carrots, cassava, sugar beets) "
                        "store nutrients and feed both animals and humans. Medicines: aspirin "
                        "(from willow bark), quinine (from cinchona tree bark, treats malaria), and "
                        "digitalis (from foxglove, treats heart failure) are all plant-derived.\n\n"
                        "PLANT COMPETITION: plants compete for light (canopy height, leaf area/"
                        "orientation), water (deep taproots vs. wide fibrous roots), and nutrients "
                        "(root absorption speed, mycorrhizal associations). Exploitation competition "
                        "(indirect) is consuming a resource before neighbors can access it; "
                        "interference competition (direct) is physically or chemically inhibiting a "
                        "neighbor's growth -- allelopathy (releasing toxic allelochemicals to "
                        "suppress nearby germination/growth) is a specific form of interference "
                        "competition.\n\n"
                        "HISTORY: Theophrastus (371-286 BCE, student of Aristotle, \"father of "
                        "botany,\" wrote Historia Plantarum). Pedanius Dioscorides (40-90 CE, wrote "
                        "De Materia Medica, foundational to pharmacology). Pliny the Elder (23-79 "
                        "CE, wrote Naturalis Historia, died in the Vesuvius eruption). Al-Dinawari "
                        "(828-896 CE, founder of Arab botany). Leonhart Fuchs (1501-1556, the genus "
                        "Fuchsia is named for him). Jan Ingenhousz (1730-1799, proved plants need "
                        "sunlight to produce oxygen). Carl Linnaeus (1707-1778, \"father of "
                        "taxonomy,\" established binomial nomenclature). Gregor Mendel (1822-1884, "
                        "pea plant genetics, dominant/recessive genes). George Washington Carver "
                        "(1864-1943, promoted crop rotation, found many uses for peanuts/sweet "
                        "potatoes). Melvin Calvin (1911-1997, mapped the Calvin Cycle using "
                        "carbon-14 tracing). Katherine Esau (1898-1997, pioneering plant anatomist, "
                        "definitive textbooks on plant structure)."
                    ),
                )
            )

        chapters = [
            (
                "Botany: Plant Groups & Classification",
                "Algae vs. multicellular plants, monocots vs. dicots, embryophytes vs. "
                "cryptogams, and woody vs. herbaceous plants -- shared Division B/C content.",
                (
                    "ALGAE VS. MULTICELLULAR PLANTS: algae can be unicellular or multicellular and "
                    "typically live underwater; plants are multicellular and thrive on land. Algae "
                    "are nonvascular and lack connective tissues, leaves, stems, and roots, unlike "
                    "plants.\n\n"
                    "MONOCOTS VS. DICOTS: classified by cotyledon count in the seed -- monocots "
                    "have one, dicots have two. Leaf venation: monocots have parallel veins, "
                    "dicots have branching veins. Stem structure: monocots' vascular bundles are "
                    "scattered around the stem; dicots' form a ring near the edge. Root systems: "
                    "monocots typically have a fibrous root system; dicots typically have a "
                    "taproot. Floral patterns: monocot flower parts usually come in multiples of "
                    "3; dicot flower parts usually come in multiples of 4 or 5.\n\n"
                    "EMBRYOPHYTES VS. CRYPTOGAMS: Embryophytes are land plants that nurture the "
                    "young sporophyte inside the gametophyte's tissue -- nonvascular plants "
                    "(mosses, liverworts, hornworts), seedless vascular plants (ferns, "
                    "lycophytes), gymnosperms, and angiosperms. Cryptogams reproduce via spores "
                    "rather than seeds/flowers -- thallophytes (fungi, bacteria, algae), "
                    "bryophytes, and pteridophytes.\n\n"
                    "WOODY VS. HERBACEOUS PLANTS: woody plants are long-lived perennials with "
                    "secondary growth and a lignin-reinforced stem, going dormant in winter rather "
                    "than dying back, and practicing self-pruning. Herbaceous plants (herbs) lack "
                    "a permanent woody stem, grow mainly via primary growth, and are annuals, "
                    "biennials, or perennials that die back to a small underground portion each "
                    "year; fast-growing annual herbs are often pioneer species in succession."
                ),
            ),
            (
                "Botany: Anatomy, Morphology & Reproduction",
                "Vascular plant anatomy (shoot/root systems, xylem/phloem) and reproduction "
                "(alternation of generations, the life cycles of mosses, ferns, gymnosperms, and "
                "angiosperms) -- shared Division B/C content.",
                (
                    "VASCULAR PLANT ANATOMY: two interdependent systems -- the shoot system (stem "
                    "and leaves, above ground) and the root system (below ground); the shoot needs "
                    "roots for water/minerals, roots need the shoot for food/energy. Four main "
                    "organ systems: stem (connects leaves to roots via xylem and phloem), roots "
                    "(anchor the plant, absorb water/nutrients), leaves (photosynthesize), and "
                    "reproductive organs.\n\n"
                    "ALTERNATION OF GENERATIONS: plants alternate between a diploid sporophyte "
                    "stage and a haploid gametophyte stage (isomorphic/identical in some algae, "
                    "heteromorphic/different in angiosperms). Nonvascular plants have a dominant "
                    "gametophyte; seed plants have a dominant sporophyte with a reduced "
                    "gametophyte. Sporophytes produce sporangia -> haploid spores -> gametophytes; "
                    "gametophytes produce gametangia (archegonia = female, antheridia = male, not "
                    "present in all plants) whose gametes fuse into a zygote -> new sporophyte. "
                    "Homosporous plants produce one spore type; heterosporous plants (e.g. pines) "
                    "produce distinct female megaspores and male microspores.\n\n"
                    "LIFE CYCLES: Moss (bryophyte) -- spores germinate into protonemata (anchored "
                    "by rhizoids, not roots), which bud into male/female gametophytes; "
                    "flagellated sperm swim through water to fertilize eggs, forming a sporophyte "
                    "(seta + capsule) still dependent on the female gametophyte; meiosis inside the "
                    "capsule produces the next generation of spores. Fern (pterophyte) -- similar, "
                    "but most are homosporous with a single bisexual gametophyte producing "
                    "antheridia/archegonia at different times; sporophytes grow true leaves with "
                    "sori (spore clusters) underneath. Gymnosperms -- microspores/megaspores form "
                    "on cone-like strobili; wind carries pollen, and fertilization follows roughly "
                    "a year after pollination, ending in wind-dispersed seeds. Angiosperms -- "
                    "microsporogenesis (anther) and megasporogenesis (ovule) lead to pollination "
                    "and double fertilization (unique to angiosperms): one sperm fertilizes the "
                    "egg, the other fuses with polar nuclei to form the triploid endosperm; the "
                    "ovary wall becomes the fruit."
                ),
            ),
            (
                "Botany: Photosynthesis & Plant Ecology",
                "Chloroplast structure and the light/Calvin cycle reactions, plants' role in "
                "energy and nutrient cycles, and plant competition -- shared Division B/C content.",
                (
                    "PHOTOSYNTHESIS: occurs in chloroplasts (outer/inner membranes, thylakoids, "
                    "stroma). Light-dependent reactions happen in the thylakoid membranes, turning "
                    "sunlight and water into ATP, NADPH, and oxygen. Light-independent reactions "
                    "(the Calvin cycle) happen in the stroma, turning CO2, ATP, and NADPH into G3P "
                    "(via the enzyme RuBisCO).\n\n"
                    "ENERGY FLOW: plants are primary producers. Gross Primary Productivity (GPP) "
                    "is their total energy generated; Net Primary Productivity (NPP) is what's "
                    "left after their own respiration, available to herbivores/decomposers. The "
                    "10% Rule (Lindeman's Efficiency): on average only ~10% of stored energy "
                    "passes to the next trophic level.\n\n"
                    "NUTRIENT CYCLES: Carbon -- plants fix atmospheric CO2 via RuBisCO in the "
                    "Calvin Cycle, release some back via respiration; buried undecayed matter can "
                    "become peat/coal over geologic time. Nitrogen -- bacteria fix N2 into usable "
                    "ammonium/nitrate for roots to assimilate; decomposers recycle it, denitrifying "
                    "bacteria return excess to atmospheric N2. Water -- transpiration moves water "
                    "up through the xylem and out through leaf stomata. Phosphorus -- plants "
                    "absorb soil phosphate directly or via mycorrhizal fungal symbiosis.\n\n"
                    "PLANT COMPETITION: plants compete for light (canopy height, leaf area/"
                    "orientation), water (deep taproots vs. wide fibrous roots), and nutrients "
                    "(root absorption speed, mycorrhizal associations). Exploitation competition "
                    "(indirect) consumes a resource before neighbors can access it; interference "
                    "competition (direct) physically/chemically inhibits a neighbor -- allelopathy "
                    "(releasing toxic allelochemicals to suppress nearby germination/growth) is a "
                    "specific form of interference competition."
                ),
            ),
            (
                "Botany: Uses of Plants & History",
                "How humans and animals use plants (fibers, food, medicine) and the key "
                "historical figures in botany -- shared Division B/C content.",
                (
                    "USES OF PLANTS: Fibers -- surface fibers (e.g. cotton seed hairs) for "
                    "textiles, stem fibers (from phloem sclerenchyma, high tensile strength), leaf "
                    "fibers (from monocot leaf vascular bundles), and wood (from the vascular "
                    "cambium) for timber/construction/paper. Food storage structures -- endosperm "
                    "(triploid, nutrient-rich seed tissue) is the main starch source in cereal "
                    "grains; bulbs (short stem + fleshy modified leaves) and corms (solid swollen "
                    "stem tissue, e.g. taro); storage roots (e.g. sweet potatoes, carrots, cassava, "
                    "sugar beets) that both humans and wild animals rely on. Medicines -- aspirin "
                    "(from willow bark), quinine (from cinchona tree bark, treats malaria), and "
                    "digitalis (from foxglove, treats heart failure) are all plant-derived.\n\n"
                    "IMPORTANT PEOPLE IN BOTANY: Theophrastus (371-286 BCE, \"father of botany,\" "
                    "wrote Historia Plantarum). Pedanius Dioscorides (40-90 CE, De Materia Medica, "
                    "foundational to pharmacology). Pliny the Elder (23-79 CE, Naturalis Historia). "
                    "Al-Dinawari (828-896 CE, founder of Arab botany). Leonhart Fuchs (1501-1556, "
                    "genus Fuchsia named for him). Jan Ingenhousz (1730-1799, proved plants need "
                    "sunlight to produce oxygen). Carl Linnaeus (1707-1778, \"father of "
                    "taxonomy,\" binomial nomenclature). Gregor Mendel (1822-1884, pea plant "
                    "genetics). George Washington Carver (1864-1943, crop rotation, peanut/sweet "
                    "potato uses). Melvin Calvin (1911-1997, mapped the Calvin Cycle). Katherine "
                    "Esau (1898-1997, pioneering plant anatomist)."
                ),
            ),
        ]

        for chapter_name, chapter_description, chapter_text in chapters:
            existing = (
                db.query(models.Topic)
                .filter(models.Topic.name == chapter_name, models.Topic.parent_topic_id == topic.id)
                .first()
            )
            if existing is None:
                sub_topic = models.Topic(
                    event_name=topic.event_name,
                    name=chapter_name,
                    description=chapter_description,
                    assessment_type=topic.assessment_type,
                    parent_topic_id=topic.id,
                )
                db.add(sub_topic)
                db.flush()
                db.add(
                    models.Resource(
                        topic_id=sub_topic.id,
                        type="text",
                        title="scioly.org wiki: Botany (excerpt for this chapter, Division B scope)",
                        source_url="https://scioly.org/wiki/Botany",
                        raw_text=chapter_text,
                    )
                )

        db.commit()
    finally:
        db.close()


@app.on_event("startup")
def seed_solar_system_learning_chapters() -> None:
    """Kid-friendly Solar System learning chapters (flashcards, stories,
    infographics) from the coach-supplied 2027 source reader -- deterministic
    content, no LLM calls. Registered after seed_official_topics so the
    "Solar System" parent row already exists; see app/content/solar_system."""
    seed_solar_system_learning_content()


@app.on_event("startup")
def apply_official_rules_2027() -> None:
    """Registered after every per-event seed above: writes each official
    event's description and rules overview from the 2027 Division B Rules
    Manual, overriding any older summary. See app/content/official_rules.py."""
    apply_official_rules()


@app.on_event("startup")
def publish_deterministic() -> None:
    """Registered last so every seed above has run: publishes all
    deterministic (app-shipped, sourced) content as-is to every student --
    official events' rules overviews and source notes, and each sourced
    chapter inside its event. See app/content/deterministic.py."""
    publish_deterministic_content()


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
