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
from app.routers import assessment, attempts, auth as auth_router, explain, ingestion, students, topic_chat, topics, tutor

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


@app.on_event("startup")
def seed_official_topics() -> None:
    """Pre-populate every official 2027 Division B event as a topic, so a
    coach starts with the real competition slate instead of having to type
    each one in by hand -- the "+ New topic" flow (routers/topics.py) still
    exists for a coach who wants a narrower custom topic on top of one of
    these (e.g. splitting "Dynamic Planet" into sub-topics).

    Assembled from soinc.org's 2027 Division B event slate (not scraped live
    -- this app has no route to that site at build time; WebFetch to
    soinc.org/scioly.org is blocked in this environment, so this was built
    from search-result snippets, not a direct read of the rules PDFs) -- a
    coach should still sanity-check names/groupings against the official
    page. Protein Builders and Code Craze are both trial events as of this
    writing (see their overview notes below) and may not run at every
    tournament -- everything else here was corroborated as a current,
    confirmed Division B event.

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
        ("Ping Pong Parachute", "Build event: launch rockets that release a ping-pong ball on a parachute, scored on airborne (hang) time.", "practical"),
        ("Write It Do It", "Practical communication event: one partner writes instructions describing a structure, and the other builds it from the instructions alone.", "practical"),
        ("Protein Builders", "Trial event: build a physical model of a protein on-site from provided backbone and amino-acid pieces, judged on structural accuracy. Trial status -- confirm it's running at your tournament.", "practical"),
        ("Code Craze", "Trial event: on-computer quiz and coding activities (programming basics, AI/ML, cryptography) run through the CodeHS platform. Trial status -- confirm it's running at your tournament, and that students can bring a Chrome-capable laptop.", "test_practical"),
    ]

    # (see docstring on the 5 overview_* fields on Topic in models.py) --
    # keyed by exact catalog name above, used both for new inserts and to
    # backfill any existing row whose overview is still empty.
    overview_content: dict[str, dict[str, str]] = {
        "Dynamic Planet": {
            "what": "An Earth science event, run as a written exam or rotating stations, that goes deep on one Earth-process topic that changes each season.",
            "learn": "The water cycle, groundwater and aquifers, water tables, watersheds and stream systems, and water-budget calculations -- plus general map- and graph-reading skills applied to that topic.",
            "assessed": "Teams of 2, roughly 50 minutes, either a rotating station test (samples/displays/models) or a sit-down written exam depending on the tournament. A Class II calculator and a binder of notes are allowed.",
            "theme_2027": "Earth's Fresh Waters (freshwater hydrology). This event rotates its topic on a multi-year cycle (past years: oceanography, glaciers, tectonics) -- confirm the exact 2027 scope on soinc.org.",
            "notes": "Any binder is allowed (tabs, sheet protectors, lamination all fine), so a well-organized binder matters as much as raw memorization. Because the topic rotates, last year's binder is only partly reusable.",
        },
        "Meteorology": {
            "what": "A written (occasionally station-based) exam on atmospheric science and weather, with a yearly sub-focus.",
            "learn": "How severe weather forms and behaves -- thunderstorms, tornadoes, hurricanes, hail, derechos -- plus reading station models, weather maps, soundings, and satellite/radar imagery, and weather calculations (dew point, heat index, wind chill) in metric units.",
            "assessed": "Teams of 2, roughly 50 minutes, mostly a sit-down written test heavy on chart/map interpretation; some invitationals add stations. Two non-graphing calculators are typically allowed; answers generally need metric units and correct significant figures.",
            "theme_2027": "Severe Storms. Confirm the exact scope (e.g. whether hurricanes and winter storms are both included) on soinc.org.",
            "notes": "Resource allowances here are broader than most events (loose notes/binders/folders, not just one sheet) -- worth double-checking the current wording since it's unusually generous.",
        },
        "Remote Sensing": {
            "what": "A written/station event on how remote sensing works and on interpreting satellite and aerial imagery, data, and maps of Earth systems.",
            "learn": "The electromagnetic spectrum and how sensors detect radiation, interpreting true- and false-color imagery, basic mapping/coordinate/scale principles, and applications like weather tracking, land-use change, disaster response, and agriculture monitoring.",
            "assessed": "Teams of 2, roughly 50 minutes, primarily a written test built around interpreting provided images, maps, and data. Teams may bring a three-ring binder plus up to 2 calculators, 2 rulers, and 2 protractors.",
            "theme_2027": "Doesn't rotate a headline theme the way Dynamic Planet or Meteorology do -- content centers on core remote-sensing principles and current applications. Confirm if any application area is emphasized for 2027.",
            "notes": "Shares image/map-literacy skills with Dynamic Planet and Meteorology, so many coaches train these three together.",
        },
        "Rocks and Minerals": {
            "what": "A station-based identification event where teams examine physical rock and mineral specimens (sometimes photos/data) and identify them, plus answer formation/concept questions.",
            "learn": "Mineral identification properties (hardness, luster, streak, cleavage vs. fracture), the rock cycle, and distinguishing igneous, sedimentary, and metamorphic rocks by texture, composition, and formation process.",
            "assessed": "Teams of 2, timed station rotation (no returning to prior stations). IDs are limited to the official National Rocks and Minerals List and make up roughly 30-50% of points; other stations test concepts even without a specimen (key properties given instead).",
            "theme_2027": "Doesn't rotate a yearly theme -- content and the specimen list stay fairly stable, though the official list can be revised slightly each year. Confirm the current list on soinc.org.",
            "notes": "One of the most specimen-ID-heavy events -- hands-on practice with real samples matters more than pictures. Allowed: a binder, one magnifying glass, one commercial field guide (tabbed/annotated), an annotated copy of the official list, and a calculator.",
        },
        "Solar System": {
            "what": "A written (occasionally station-based) exam on solar system science, following a 2-year rotating focus between planetary formation/structure and habitability.",
            "learn": "For the habitability year: what makes a world potentially habitable (liquid water, atmosphere, magnetic field, habitable-zone location), exoplanet detection methods (transit, radial velocity, spectroscopy), and comparing solar-system bodies to known exoplanet systems, plus calculations like Kepler's laws and equilibrium temperature.",
            "assessed": "Teams of 2, roughly 50 minutes, written exam with data/graph interpretation and calculation-heavy questions; a calculator and resource sheet/binder are typically allowed.",
            "theme_2027": "Habitability within and beyond the Solar System -- Year 2 of the current 2-year rotation (Year 1 covered planet formation and structure). Confirm the exact wording/scope on soinc.org, since rotation years can shift.",
            "notes": "More math/physics-calculation-heavy than the other Earth/space events -- a good fit for students who like applying formulas over pure memorization.",
        },
        "Anatomy & Physiology": {
            "what": "A written test and/or lab-practical station event on human body systems, following a 4-year rotation through different organ systems (2-3 systems per year).",
            "learn": "For 2027: the respiratory, digestive, and immune systems -- structures and functions, how the systems interrelate, and common disorders/diseases affecting each.",
            "assessed": "Teams of 2, roughly 50 minutes. Can run as a sit-down written test or as lab-practical stations with models, diagrams, specimens, or data-collection tasks.",
            "theme_2027": "Respiratory, Digestive, and Immune systems -- Year 3 of the current 4-year rotation (2026 covered Nervous, Sense Organs, and Endocrine). Worth a final confirm on soinc.org.",
            "notes": "One double-sided 8.5x11 resource sheet is typically allowed. Station formats often lean on picture/diagram/model-based structure ID, not just written recall -- easy to under-prepare for.",
        },
        "Disease Detectives": {
            "what": "A life-science event on epidemiology -- investigating disease outbreaks and interpreting public health data, typically built around one detailed case-study scenario.",
            "learn": "Epidemiological study design (cohort, case-control, cross-sectional), the steps of outbreak investigation, modes of disease transmission, and calculating/interpreting rates like attack rate, relative risk, and odds ratio from tables and graphs.",
            "assessed": "Teams of 2, roughly 50 minutes. May run as a written exam, stations, or both -- commonly built around a single outbreak scenario mixing concept and calculation questions.",
            "theme_2027": "No named rotating theme like the geoscience events -- the specific outbreak/disease used changes yearly, but the epidemiology skillset tested is stable.",
            "notes": "One of the more statistics-heavy life science events (2x2 tables, relative risk, odds ratio, sensitivity/specificity) -- budget real calculation practice, not just vocabulary.",
        },
        "Heredity": {
            "what": "A written, sit-down exam on genetics -- problem-solving with crosses and pedigrees plus conceptual questions on DNA and inheritance.",
            "learn": "Mendelian inheritance (mono- and dihybrid Punnett squares), non-Mendelian patterns (incomplete dominance, codominance, sex-linked traits), pedigree analysis, and DNA structure, replication, and mutation basics.",
            "assessed": "Teams of 2, roughly 50 minutes, sit-down written exam mixing short-answer concepts with cross/pedigree problems.",
            "theme_2027": "Doesn't rotate -- core genetics content stays essentially the same year to year.",
            "notes": "Typically one double-sided 8.5x11 resource sheet allowed. Overlaps closely with a standard intro biology genetics unit; rewards students who like probability/logic puzzles.",
        },
        "Botany": {
            "what": "A written exam and/or lab-station event on general plant biology, sometimes involving live or preserved specimens.",
            "learn": "Plant anatomy and physiology (photosynthesis, transpiration, tissue types), plant diversity and classification (algae vs. vascular, monocot vs. dicot, gymnosperm vs. angiosperm), and basic plant ecology and adaptations.",
            "assessed": "Teams of 2, roughly 50 minutes. Can run as a sit-down exam or lab stations with live/preserved specimens, slides, microscopes, images, and data tables.",
            "theme_2027": "No rotating sub-focus -- broad general botany each season rather than one narrow yearly topic. Confirm if any group/process is emphasized for 2027.",
            "notes": "Lab coats and goggles are commonly required when specimens are used at stations. One double-sided 8.5x11 resource sheet is typically allowed.",
        },
        "Water Quality": {
            "what": "A non-build, knowledge-and-skills event on freshwater aquatic environments, combined with a hands-on task using a student-built salinometer/hydrometer.",
            "learn": "Freshwater ecology (food webs, population/community dynamics, nutrient cycling), aquatic chemistry and its effects on organisms, water treatment processes, watershed management issues, and building/using a simple water-testing tool.",
            "assessed": "Teams of 2, roughly 50 minutes. Scoring combines a written/station test with a hands-on salinometer task; one double-sided 8.5x11 reference sheet, two non-programmable calculators, and a student-built salinometer allowed. Eye protection required during testing.",
            "theme_2027": "Core content areas (freshwater ecology, aquatic chemistry, water treatment, invasive species) are stable year to year -- confirm any specific 2027 emphasis or salinometer task changes on soinc.org.",
            "notes": "Teams that actually build and calibrate a working salinometer, and practice with real pH/dissolved-oxygen/turbidity kits and macroinvertebrate ID, do noticeably better than pure memorizers.",
        },
        "Hovercraft": {
            "what": "A build event: design, construct, and calibrate a self-propelled, air-levitated vehicle that carries nickels down a track, brought complete to competition.",
            "learn": "Aerodynamic lift via an air cushion, propulsion system design (motors, propellers/impellers, batteries, switches), weight distribution and stability, and iterative calibration using test data.",
            "assessed": "Run-based scoring, typically on how quickly/consistently the hovercraft travels the track; devices are impounded and inspected (including propeller safety shielding) before runs. Teams of 2; each run is seconds long, with calibration/practice time given.",
            "theme_2027": "Recent rules specify a bounding box in ready-to-run configuration and a set nickel payload count -- confirm this year's exact dimensions and track length on soinc.org, as these numbers are commonly revised.",
            "notes": "Propeller/impeller shielding (must block a 3/8\" dowel) is a common impound failure point -- build safety guards in from the start. Performance drifts with battery charge and track friction, so practice a repeatable pre-run calibration routine.",
        },
        "Circuit Lab": {
            "what": "A knowledge-and-skills event, not a build event -- a written test plus hands-on circuit-building/measurement tasks using equipment supplied on site.",
            "learn": "DC circuit fundamentals: Ohm's Law, series and parallel circuit analysis, resistor color codes, basic capacitor behavior, reading/building circuit diagrams, and multimeter use for voltage/current/resistance.",
            "assessed": "Teams of 2, roughly 50 minutes. Score combines a written test (multiple choice, true/false, calculations) with hands-on station tasks scored on correct measurements and analysis.",
            "theme_2027": "Core DC circuit content is stable year to year -- check soinc.org for the exact 2027 topic list and any allowed reference-sheet rules.",
            "notes": "Offered separately for Division B and Division C with different topic depth -- make sure any practice materials used are the Division B version, not C. Hands-on multimeter/breadboard practice matters as much as theory.",
        },
        "Thermodynamics": {
            "what": "A build event: construct an insulating device ahead of time to minimize heat loss from a container of hot water, plus a written test on thermodynamics concepts.",
            "learn": "Heat transfer mechanisms (conduction, convection, radiation), insulation material selection and thermal conductivity trade-offs, calorimetry and specific heat, and timed data collection/graphing.",
            "assessed": "The device is tested by how much a set volume of hot water cools over a fixed window, combined with a written test score. Teams of 2; device is impounded pre-test; Division B's cooling/test window is commonly around 25 minutes.",
            "theme_2027": "Recent seasons used a roughly 60-75 degrees C starting range and a 250 mL beaker with 75-125 mL water fill -- confirm exact 2027 figures on soinc.org, as starting temperature and timing are frequently adjusted.",
            "notes": "Build and destructively test multiple insulation prototypes at home under conditions matching the real setup (same water volume, similar starting temp, a real thermometer and timer) to build real design intuition.",
        },
        "Boomilever": {
            "what": "A build event: construct a lightweight cantilevered wood truss structure that mounts to a vertical Testing Wall and supports a heavy load at a set distance from the wall.",
            "learn": "Cantilever and truss structural design, material properties of balsa and basswood (compression/tension strength), glue-joint technique, and optimizing weight-to-strength ratio rather than just raw strength.",
            "assessed": "Scored on structural efficiency (load supported relative to the structure's own weight), with a required maximum load (recently around 15 kg) the structure must hold without failing. Teams of 2; the load test itself takes just a few minutes.",
            "theme_2027": "Recent rules specified a span around 40-45 cm, wood cross-section capped near 1/4\" x 1/4\", and a target load around 15 kg -- confirm exact 2027 span, wall geometry, and load numbers on soinc.org.",
            "notes": "Glue-joint failure and excess glue weight are the most common pitfalls -- build and destructively load-test several iterations before finalizing a competition structure, with eye protection during testing.",
        },
        "Elastic Launch Glider": {
            "what": "A build event: construct a lightweight free-flight model glider launched by an elastic (rubber band) launcher, built and test-flown well ahead of competition.",
            "learn": "Aerodynamics of lift, drag, and stability (wing shape, dihedral, center-of-gravity placement), lightweight airframe construction, and the iterative trimming/tuning process for a stable flight path.",
            "assessed": "Score is based on total or best flight time across a limited number of official flights (commonly up to 3) within a set flight period (commonly around 6 minutes); mass and size are checked at impound. Teams of 2.",
            "theme_2027": "Recent limits were near 15 g mass and roughly 30 cm wingspan/fuselage length -- confirm exact 2027 mass/wingspan/length limits and launch-handle rules on soinc.org.",
            "notes": "Needs a high-ceiling practice space (gym or large hall) for realistic test flights. Trimming for stable flight takes many repeated sessions; gliders are fragile, so bring spares and a repair kit.",
        },
        "Roller Coaster": {
            "what": "A build event: design and build a gravity-only marble/ball roller coaster track ahead of time, run at competition to match a target time revealed on the spot -- no external power source allowed.",
            "learn": "Conservation of energy (gravitational potential to kinetic), track and curve design to control ball speed, the effects of friction and momentum, and estimation skills for hitting a target run time.",
            "assessed": "Teams typically learn a Target Time on competition day and are scored on how close their ball's actual run time comes to it (often with an asymmetric penalty for running long vs. short), alongside build/design criteria. Teams of 2.",
            "theme_2027": "The gravity-only, reveal-and-match-target-time format is stable across recent seasons -- confirm the exact scoring formula and any track footprint/height limits on soinc.org.",
            "notes": "Teams sometimes get a short window to adjust their track once the target time is revealed, so practicing quick, repeatable adjustments is valuable. Plan for a sturdy carrying case -- a track that's both rigid and transportable is a real logistical challenge.",
        },
        "Scrambler": {
            "what": "A build event: a device powered solely by a falling mass carries a raw egg along a track as quickly as possible and stops it safely at a Terminal Barrier without breaking it.",
            "learn": "Energy conversion (a falling mass's potential energy driving, then arresting, a vehicle), momentum and braking/deceleration mechanism design, mechanical linkages and gearing, and cushioning/protection design for a fragile payload.",
            "assessed": "Score combines run speed with stopping accuracy relative to the Terminal Barrier; the egg must survive intact for the run to count. Falling mass is capped (recently 2.00 kg) and impounded separately from the vehicle. Teams of 2; each run is seconds long.",
            "theme_2027": "Recent rules capped the falling mass near 2.00 kg and the device bounding box around 100 x 50 x 100 cm -- confirm exact 2027 numbers on soinc.org.",
            "notes": "The self-contained automatic stopping mechanism is usually the hardest engineering problem here. Practice with real or dummy eggs repeatedly to dial in stopping repeatability, and bring spare eggs/cushioning to competition.",
        },
        "Crime Busters": {
            "what": "A hands-on forensic-science lab event: given a crime scenario, physical evidence, and a suspect list, teams run qualitative chemistry and pattern-evidence tests at stations to solve the case.",
            "learn": "Qualitative analysis of unknown powders, solids, and liquids; polymer/plastic identification; paper chromatography of inks; and pattern evidence analysis (fingerprints, footprints, tire prints).",
            "assessed": "Teams of 2, roughly 50 minutes. Rotate through lab stations, record test results, then use those plus scenario clues to answer questions and identify a suspect. One double-sided 8.5x11 reference sheet and up to two Class II calculators allowed.",
            "theme_2027": "No confirmed year-specific scenario twist -- the core station content (powders/solids, polymers, chromatography, prints) is consistent with past seasons; check the station list against the current rules manual.",
            "notes": "Powder/solid qualitative analysis is typically the highest-weighted section -- drilling flame tests, solubility, and simple chemical ID pays off most.",
        },
        "Food Science": {
            "what": "A combined written-test-and-lab event: teams answer questions on food science concepts and run hands-on experiments or quality evaluations tied to a food category that changes each season.",
            "learn": "Food chemistry fundamentals (macronutrients, preservation, spoilage/safety) and sensory/quality testing methods, applied to the current season's food category.",
            "assessed": "Teams of 2, mixing written test questions with practical/lab tasks scored against a rubric or answer key; roughly 50 minutes in past seasons (not separately reconfirmed for 2027).",
            "theme_2027": "Indications point to milk and dairy products for 2027 -- unconfirmed against the actual rules PDF, so verify before finalizing study materials.",
            "notes": "The food-category focus rotates each season, so prior years' study guides won't directly transfer -- get the actual current rules/test packet before planning.",
        },
        "Codebusters": {
            "what": "A written cryptography event: teams decode a packet of encrypted messages using classical cipher systems, under time pressure and without electronic decoding aids.",
            "learn": "Manual cryptanalysis (frequency analysis, letter-pattern recognition) across Division B's roughly 13 cipher types, including Aristocrat and Patristocrat substitution ciphers, Baconian, Atbash/Caesar shift ciphers, Vigenere, and Pigpen.",
            "assessed": "Teams of 2, roughly 50 minutes. Scoring allows a small number of free errors, penalizes additional errors, and awards time bonuses for fast solves; calculators permitted.",
            "theme_2027": "The confirmed 2027 change is the addition of the Homophonic Cipher to Division B's cipher list.",
            "notes": "The Hill (matrix) cipher is Division C-only, so Division B doesn't need matrix math for it. Scoring rewards speed and accuracy, so timed drilling with online cipher-practice tools is high-value prep.",
        },
        "Experimental Design": {
            "what": "A lab-based event: teams get a prompt and materials on-site and must design, carry out, and write up an original experiment entirely during the event period.",
            "learn": "Full scientific-method skills: writing a testable question and hypothesis, identifying/controlling variables, building data tables, graphing results, basic statistics, and claim-evidence-reasoning and error analysis.",
            "assessed": "Teams of 2, roughly 50 minutes, scored against an official checklist covering research question, hypothesis, variables, materials, data, graphs, statistics, analysis, conclusion, and future-experimentation recommendations.",
            "theme_2027": "No rotating yearly theme -- the prompt and materials are freshly assigned on-site each competition. Get the current checklist PDF in case point weightings changed.",
            "notes": "Since the exact prompt is unknown in advance, the best prep is repeated timed practice designing and running quick experiments while filling out the official checklist format.",
        },
        "Ping Pong Parachute": {
            "what": "A build event: design and build up to two small rockets ahead of time, bring them to the tournament, and launch a ping-pong ball on a parachute to keep it airborne as long as possible without hitting the ceiling.",
            "learn": "Aerodynamics and parachute design basics (drag, descent rate, stability), simple rocket propulsion fundamentals, and iterative build-test-refine practice.",
            "assessed": "A limited number of launch attempts per team, timed for airborne (hang) time. Teams of 2; devices must meet size/safety specs checked at check-in (unaltered standard ping-pong ball, parachute attached with tape only).",
            "theme_2027": "Promoted from a 2026 trial event to a full Division B and C event for 2027 -- worth double-checking the newly released rules closely, since specs (ceiling limits, launcher construction, number of attempts) commonly shift between a trial and full-event version.",
            "notes": "Bring required eye protection/safety gear and backup parts -- typically only two devices are allowed. Because it's newly stabilized as a full event, expect less standardized rule interpretation across regions than long-running build events.",
        },
        "Write It Do It": {
            "what": "A communication event: one teammate examines a pre-built object and writes instructions for reconstructing it (words/numerals only, no drawings or symbols), while the other, who never sees the original, rebuilds it solely from those instructions.",
            "learn": "Precise technical/descriptive writing, spatial reasoning and vocabulary for describing 3D construction, and careful literal reading and sequencing of written instructions under time pressure.",
            "assessed": "The writer gets about 25 minutes to write the description; a builder from another team gets about 20 minutes to reconstruct the object from it alone. Teams of 2; scoring compares the rebuild to the original piece-by-piece, plus instruction clarity.",
            "theme_2027": "Objects are typically built from inexpensive materials (straws, foam balls, paper cups, popsicle sticks) or construction sets (K'Nex, LEGO, Lincoln Logs, Tinkertoys) -- no 2027-specific format change found.",
            "notes": "Drill students on using only allowed vocabulary (precise spatial/directional terms, no symbols or diagrams) and describing steps in a strict, unambiguous order.",
        },
        "Protein Builders": {
            "what": "A trial event where a team builds a physical model of a short polypeptide chain on-site from provided backbone and amino-acid sidechain materials.",
            "learn": "How amino acid side-chain chemistry (polarity, charge, size) determines protein folding and secondary/tertiary structure, and how structure relates to function.",
            "assessed": "Teams build a physical model at the tournament and are evaluated on structural accuracy and understanding of how amino acid properties drive structure and function; exact scoring rubric and time limit weren't confirmed in available sources.",
            "theme_2027": "Trial event for the 2026-27 season, not yet a confirmed full Division B event -- it may not be offered at every tournament.",
            "notes": "Confirm directly with your regional/state tournament whether this is running this season before investing prep time -- trial events run at organizer discretion. (This app previously listed this event as \"Protein Modeling\", which is actually the Division C name -- corrected here.)",
        },
        "Code Craze": {
            "what": "A trial event: an on-computer quiz-and-coding assessment run through the CodeHS platform, rather than a paper test or build event.",
            "learn": "Introductory computer science across roughly four modules: programming/coding concepts, AI and machine learning basics, cryptography, and Python coding fundamentals.",
            "assessed": "Participants complete quiz and coding activities on CodeHS using Chrome on a laptop they must bring themselves, assessed across the four modules. Only CodeHS-provided resources may be used -- outside resources or copied code can mean disqualification.",
            "theme_2027": "Confirmed present on the 2027 Division B trial-event slate, continuing pilot status -- per Science Olympiad's trial-event process it needs broader piloting before becoming an official current event.",
            "notes": "As a trial event it's only offered where a tournament chooses to run it -- confirm availability with your tournament director. Notably requires a Chrome-capable laptop per student, unlike any other event on this list.",
        },
    }

    db = SessionLocal()
    try:
        _rename_protein_modeling_to_protein_builders()

        existing_names = {row[0] for row in db.query(models.Topic.name)}
        for name, description, assessment_type in catalog:
            overview = overview_content.get(name, {})
            if name not in existing_names:
                db.add(
                    models.Topic(
                        event_name=name,
                        name=name,
                        description=description,
                        assessment_type=assessment_type,
                        overview_what=overview.get("what", ""),
                        overview_learn=overview.get("learn", ""),
                        overview_assessed=overview.get("assessed", ""),
                        overview_theme_2027=overview.get("theme_2027", ""),
                        overview_notes=overview.get("notes", ""),
                    )
                )
        db.commit()

        # Backfill: rows seeded before this overview content existed. Only
        # touches a row whose overview is still completely empty, so it
        # never clobbers anything a coach has since edited.
        for name, overview in overview_content.items():
            topic = db.query(models.Topic).filter(models.Topic.name == name, models.Topic.parent_topic_id.is_(None)).first()
            if topic is not None and not topic.overview_what:
                topic.overview_what = overview.get("what", "")
                topic.overview_learn = overview.get("learn", "")
                topic.overview_assessed = overview.get("assessed", "")
                topic.overview_theme_2027 = overview.get("theme_2027", "")
                topic.overview_notes = overview.get("notes", "")
        db.commit()
    finally:
        db.close()


@app.on_event("startup")
def seed_solar_system_deep_dive() -> None:
    """One-time content correction + deep-dive setup for Solar System, from
    the actual scioly.org wiki page (fetched by the coach as a PDF -- direct
    fetches to scioly.org are blocked from this environment). Unlike
    seed_official_topics's overview backfill (which only fills empty
    fields), this unconditionally overwrites Solar System's description and
    overview_* with the corrected content, since this is an explicit,
    sourced correction, not a first-time fill. Idempotent for the resource/
    sub-topic creation via name checks, so re-running on every startup is
    safe and doesn't duplicate them.
    """
    db = SessionLocal()
    try:
        topic = (
            db.query(models.Topic)
            .filter(models.Topic.name == "Solar System", models.Topic.parent_topic_id.is_(None))
            .first()
        )
        if topic is None:
            return

        topic.description = (
            "Written knowledge test on the Sun, planets, moons, and other bodies in our solar "
            "system; the 2027 rotation focuses on habitability within and beyond the Solar System."
        )
        topic.overview_what = (
            "A sit-down knowledge event (no hands-on task), run in Division B since 2006. Teams "
            "of 2 take a written test on solar system science; the specific focus rotates most seasons."
        )
        topic.overview_learn = (
            "Star and planet formation/evolution as background for habitability; what makes a "
            "world potentially habitable, plus related exoplanet types (Hot Jupiters, Hot "
            "Neptunes, Cold Jupiters) and concepts like tidal locking; Kepler's laws of planetary "
            "motion, escape velocity, and other orbital mechanics; core facts about the Sun, the "
            "8 planets, moons, dwarf planets/Plutoids, asteroids, comets, the Kuiper Belt, and the "
            "Oort Cloud; solar and lunar eclipses; key astronomers (Copernicus, Galileo, Kepler, "
            "Tycho Brahe, Halley, Tombaugh) and major missions (Voyager, Cassini, New Horizons, "
            "JWST, and others)."
        )
        topic.overview_assessed = (
            "Teams of 2, about 50 minutes, entirely a written/sit-down test -- no hands-on "
            "component. Two note sheets plus writing utensils are allowed (no calculator listed "
            "on the official resource list). The event often includes questions not explicitly on "
            "the official rules sheet, so broad general knowledge pays off, not just the listed topics."
        )
        topic.overview_theme_2027 = (
            "Habitability within and beyond the Solar System -- confirmed on the official wiki's "
            "year-by-year topics table for the 2027 season (2026 was Planet Formation and "
            "Structure; 2023 was also Habitability). Note: as of the wiki snapshot this was "
            "sourced from, its background-content sections still mostly cover planet/star/asteroid "
            "formation and evolution -- likely carried over from last year's topic -- so supplement "
            "with dedicated habitability research (habitable zones, biosignatures, exoplanet "
            "detection methods) rather than relying on that section alone."
        )
        topic.overview_notes = (
            "This event often asks about things not on the official rules sheet -- a good "
            "reference book and a well-organized note sheet (the community wiki suggests OneNote, "
            "Google Slides, or Canva to fit lots of text and diagrams on one page) reportedly helps "
            "get a top-ten finish. Useful outside links: NASA's Solar System site "
            "(solarsystem.nasa.gov) and the ALMA Observatory site."
        )

        if not db.query(models.Resource).filter(
            models.Resource.topic_id == topic.id, models.Resource.title == "scioly.org wiki: Solar System (event page)"
        ).first():
            db.add(
                models.Resource(
                    topic_id=topic.id,
                    type="text",
                    title="scioly.org wiki: Solar System (event page)",
                    source_url="https://scioly.org/wiki/Solar_System",
                    raw_text=(
                        "EVENT INFO: Division B, 2 participants, ~50 minutes, written/sit-down test. "
                        "Allowed resources: two note sheets, writing utensils (no calculator). "
                        "First appearance 2006; topic rotates most years.\n\n"
                        "TOPIC BY YEAR: 2027 Habitability | 2026 Planet Formation and Structure | "
                        "2023 Habitability | 2022/2019/2018 Terrestrial Bodies | 2015/2014 "
                        "Extraterrestrial Water | 2011/2010/2007/2006 No particular topic.\n\n"
                        "ORIGINS OF THE SOLAR SYSTEM: formed ~4.57 billion years ago from a nebula "
                        "collapsing around a protosun. Heavier rocky material gravitated inward, "
                        "lighter gas moved outward, giving 4 inner rocky terrestrial planets "
                        "(Mercury, Venus, Earth, Mars) and 4 outer Jovian gas/ice giants (Jupiter, "
                        "Saturn, Uranus, Neptune). Leftover material between Mars and Jupiter formed "
                        "the asteroid belt; leftovers at the far edges formed the Oort Cloud and "
                        "Kuiper Belt, source of many comets and dwarf planets (Pluto, Ceres, Eris, "
                        "Haumea, Makemake, and candidate Sedna).\n\n"
                        "THE SUN: diameter 1,392,000 km, mass 1.989x10^30 kg, luminosity "
                        "3.846x10^33 erg/s, composition ~74% hydrogen/25% helium. Holds 99.8% of "
                        "the solar system's mass. Layers (outside in, with temperature): Corona "
                        "(1,000,000 C), Transition Region, Chromosphere, Photosphere (6,000 C), "
                        "Convection Zone (1,000,000 C), Radiative Zone (2,000,000 C), Core "
                        "(15,000,000 C). Produces heat via hydrogen fusion.\n\n"
                        "PLANETS TABLE (orbit period / rotation period / distance from Sun): "
                        "Mercury 87.97 days / 58.6 days / 0.39 AU. Venus 224.7 days / 243 days / "
                        "0.72 AU. Earth 365.25 days / 1 day / 1 AU. Mars 686.98 days / 1.03 days / "
                        "1.52 AU. Jupiter 11.86 years / 0.41 days / 5.2 AU. Saturn 29.46 years / "
                        "0.41667 days / 9.54 AU. Uranus 84.01 years / 0.71833 days / 19.18 AU "
                        "(discovered 1781). Neptune 164.9 years / 0.67125 days / 30.06 AU "
                        "(discovered 1846).\n\n"
                        "DWARF PLANETS & PLUTOIDS: a dwarf planet has enough gravity to be round "
                        "but hasn't cleared its orbital neighborhood, and isn't a moon. A Plutoid "
                        "is a dwarf planet orbiting beyond Neptune -- the four official Plutoids are "
                        "Pluto, Haumea, Makemake, and Eris. Sedna is a plutoid candidate (not yet "
                        "official) with an ~11,518-year, highly eccentric orbit.\n\n"
                        "SMALL BODIES: Asteroids are small, rocky, airless bodies mostly in the main "
                        "belt between Mars and Jupiter; types include C (dark, carbon-rich), S "
                        "(silicate), M (metal-rich), and several rarer classes. Comets are icy "
                        "bodies (nucleus, coma, tail) from the colder outer solar system; periodic "
                        "comets return in under ~200 years, non-periodic (long-period) comets can "
                        "take thousands to millions of years. The Kuiper Belt (30-50 AU from the "
                        "Sun) holds leftover debris from solar system formation. The Oort Cloud is "
                        "a vast, distant cloud (mass ~40 Earths) believed to be the source of many "
                        "comets and asteroids.\n\n"
                        "MOONS: Earth has 1 moon. Mars has 2 (Phobos, Deimos). Jupiter's four "
                        "Galilean moons are Io, Europa, Ganymede, and Callisto (discovered by "
                        "Galileo, 1610) -- Jupiter has 79+ moons total. Saturn has 60+ moons "
                        "(Titan is the largest, discovered by Huygens in 1655). Uranus's major "
                        "moons include Miranda, Ariel, Umbriel, Titania, and Oberon. Neptune's "
                        "largest moon is Triton (retrograde orbit). Pluto's largest moon is Charon.\n\n"
                        "HOT JUPITERS, HOT NEPTUNES & COLD JUPITERS (2027 habitability-relevant "
                        "exoplanet types): Hot Jupiters are gas giant exoplanets in extremely close, "
                        "hot orbits (often just days), 0.36-13.6 Jupiter masses, easiest to detect "
                        "via radial velocity/Doppler wobble, sometimes tidally locked. Hot Neptunes "
                        "are smaller, less gas-rich, denser-cored, ice-giant-type exoplanets, often "
                        "closer than 1 AU to their star. Cold Jupiters are gas giants like Hot "
                        "Jupiters but orbiting beyond the frost/snow line, cold enough to freeze "
                        "water/ammonia/methane into ice.\n\n"
                        "KEPLER'S LAWS OF PLANETARY MOTION: (1) every planet's orbit is an ellipse "
                        "with the Sun at one focus; (2) a line from the Sun to a planet sweeps equal "
                        "areas in equal time (planets move faster near the Sun); (3) the square of "
                        "the orbital period is proportional to the cube of the semi-major axis "
                        "(p^2 = a^3). Newton's law of gravitation: F = G*m1*m2/r^2. Escape velocity: "
                        "Ev = sqrt(2GM/R), where G = 6.67x10^-11 N*m^2/kg^2.\n\n"
                        "TIDAL LOCKING, SHEPHERDING, RESONANCE & TROJANS: tidal locking is when one "
                        "side of a body always faces another (e.g. the Moon and Earth). Shepherd "
                        "moons keep a planetary ring's particles confined via gravity (e.g. Saturn's "
                        "Pan and Prometheus). Orbital resonance is when two bodies' periods relate "
                        "by a simple integer ratio (e.g. Neptune:Pluto is 2:3; Jupiter's moons Io, "
                        "Europa, Ganymede are in a 1:2:4 Laplace resonance). Trojans share an orbit "
                        "with a larger body without colliding, sitting 60 degrees ahead or behind it.\n\n"
                        "ECLIPSES: a lunar eclipse occurs when Earth passes between the Sun and "
                        "Moon (always at full moon) -- types are penumbral, total penumbral, "
                        "partial, and total (up to ~107 minutes of totality). A solar eclipse occurs "
                        "when the Moon passes between Earth and the Sun (always at new moon) -- "
                        "types are total, annular (Moon appears smaller than the Sun), hybrid, and "
                        "partial.\n\n"
                        "FAMOUS ASTRONOMERS: Aristarchus (first proposed a heliocentric system); "
                        "Nicholas Copernicus (1473-1543, developed the heliocentric model); Tycho "
                        "Brahe (1546-1601, precise planetary/stellar measurements, discovered a "
                        "1572 supernova); Galileo Galilei (1564-1642, discovered Jupiter's four "
                        "largest moons, observed Venus's phases, improved the telescope); Johannes "
                        "Kepler (1571-1630, developed the laws of planetary motion, was Tycho "
                        "Brahe's assistant); Edmond Halley (1656-1742, first to calculate a comet's "
                        "orbit -- Halley's Comet); Clyde Tombaugh (1906-1997, discovered Pluto in "
                        "1930).\n\n"
                        "NOTABLE MISSIONS: Voyager 1 & 2 (1977-, flybys of the outer planets); "
                        "Galileo (1989-2003, Jupiter system); Cassini (1997-2017, Saturn system); "
                        "New Horizons (2006-, first Pluto flyby in 2015, later the Kuiper Belt); "
                        "Dawn (2007-2018, Vesta and Ceres); Lunar Reconnaissance Orbiter (2009-, "
                        "the Moon); Juno (2011-, Jupiter); BepiColombo (2018-, Mercury); Hubble "
                        "(1990-) and JWST (2021-) space telescopes."
                    ),
                )
            )

        chapters = [
            (
                "Solar System: Star & Planet Formation",
                "How stars and planets form and evolve, from protoplanetary disk to terrestrial "
                "and Jovian planets, plus asteroid and Kuiper Belt/Oort Cloud origins -- background "
                "for this year's habitability focus.",
                (
                    "PLANETARY EVOLUTION: planets form, change, and develop under gravity, heat, "
                    "impacts, and interactions with their star, starting in a protoplanetary disk "
                    "of gas and dust. Dust grains collide and stick (accretion) into planetesimals, "
                    "then protoplanets. Hot inner regions only allow rock/metal to survive (rocky "
                    "planets); cold outer regions retain ices and gas, allowing gas/ice giants to "
                    "form. After forming, planets evolve internally (volcanism, tectonics, magnetic "
                    "fields driven by leftover formation heat, radioactive decay, and tidal forces) "
                    "and their atmospheres evolve based on gravity, temperature, volcanic "
                    "outgassing, and stellar radiation/wind.\n\n"
                    "STAR FORMATION: begins in a cold, dense nebula region that collapses under its "
                    "own gravity into a protostar, which heats up via gravitational contraction. "
                    "Once the core is hot/dense enough, sustained hydrogen fusion begins (main "
                    "sequence). Low-to-moderate mass stars (like the Sun) later expand into red "
                    "giants, shed their outer layers, and leave a white dwarf core. High-mass stars "
                    "become red supergiants and end in a supernova, leaving a neutron star or black "
                    "hole.\n\n"
                    "PLANET FORMATION: from leftover material in the protoplanetary disk. The "
                    "temperature gradient determines composition -- hot inner disk gives rocky "
                    "terrestrial planets (Mercury, Venus, Earth, Mars); cooler outer disk lets ices "
                    "condense too, letting massive cores attract gas into Jovian gas giants "
                    "(Jupiter, Saturn, Uranus, Neptune). Planetary orbits may have migrated over "
                    "time (e.g. the 'Nice Model').\n\n"
                    "ASTEROID FORMATION: asteroids are leftover planetesimals that never accreted "
                    "into a full planet, mostly in the main belt between Mars and Jupiter, where "
                    "Jupiter's gravity disrupted further accretion. Ongoing collisions have shaped "
                    "their size distribution; composition varies by original formation temperature "
                    "(C-type carbon-rich, S-type silicate, M-type metal-rich, and others)."
                ),
            ),
            (
                "Solar System: Bodies, Moons & Small Bodies",
                "Core facts about the Sun, the 8 planets, dwarf planets/Plutoids, asteroid and "
                "comet types, and the major moon systems.",
                (
                    "THE SUN: diameter 1,392,000 km, mass 1.989x10^30 kg (99.8% of the solar "
                    "system's mass), ~74% hydrogen/25% helium, produces energy via hydrogen fusion "
                    "in its core (15,000,000 C), radiating out through the radiative zone, "
                    "convective zone, photosphere (6,000 C), and corona (1,000,000 C).\n\n"
                    "PLANETS: 4 inner rocky terrestrial planets (Mercury, Venus, Earth, Mars) "
                    "between the Sun and the asteroid belt; 4 outer Jovian gas/ice giants (Jupiter, "
                    "Saturn, Uranus, Neptune) beyond it. Orbit periods range from Mercury's 88 days "
                    "to Neptune's 165 years; rotation periods range from Jupiter's 10-hour day to "
                    "Venus's 243-day day (longer than its year).\n\n"
                    "DWARF PLANETS & PLUTOIDS: a dwarf planet is round from its own gravity but "
                    "hasn't cleared its orbital neighborhood. A Plutoid is a dwarf planet beyond "
                    "Neptune -- the four official Plutoids are Pluto, Haumea, Makemake, and Eris. "
                    "Sedna is a plutoid candidate, not yet official, with an extremely long, "
                    "eccentric orbit.\n\n"
                    "SMALL BODIES: asteroids (rocky, airless, mostly in the main belt) come in "
                    "types like C (dark, carbon-rich), S (silicate, brighter), and M (metal-rich). "
                    "Comets (icy nucleus/coma/tail) are periodic (under ~200-year orbits) or "
                    "non-periodic/long-period (thousands to millions of years). The Kuiper Belt "
                    "(30-50 AU out) and the far more distant Oort Cloud are leftover-debris "
                    "reservoirs and the source of many comets.\n\n"
                    "MOONS: Earth has 1 (the Moon); Mars has 2 (Phobos, Deimos, discovered 1877). "
                    "Jupiter's Galilean moons -- Io, Europa, Ganymede, Callisto -- were discovered "
                    "by Galileo in 1610; Jupiter has 79+ moons total. Saturn's largest moon Titan "
                    "was discovered by Huygens in 1655; Saturn has 60+ moons. Uranus's major moons "
                    "include Miranda, Ariel, Umbriel, Titania, and Oberon. Neptune's largest moon "
                    "Triton orbits retrograde. Pluto's largest moon is Charon."
                ),
            ),
            (
                "Solar System: Habitability & Exoplanet Types",
                "What makes a world potentially habitable, and related exoplanet categories -- "
                "Hot Jupiters, Hot Neptunes, Cold Jupiters, and tidal locking. This year's (2027) "
                "event theme.",
                (
                    "2027 THEME: Solar System's focus this season is habitability within and beyond "
                    "the Solar System. As of the source wiki snapshot, dedicated habitability "
                    "content (habitable zones, biosignatures, exoplanet detection methods) wasn't "
                    "fully written up yet -- supplement this with outside research; the exoplanet "
                    "categories below are the clearest habitability-adjacent content available on "
                    "the page.\n\n"
                    "HOT JUPITERS: gas giant exoplanets in extremely close, hot orbits around their "
                    "star (often just days), temperatures over 1000K, sometimes tidally locked. "
                    "Mass range 0.36-13.6 Jupiter masses (a commonly tested fact). Easiest exoplanet "
                    "type to detect, via the radial velocity/Doppler wobble method, due to their "
                    "large mass and tight orbit.\n\n"
                    "HOT NEPTUNES: similar to Hot Jupiters but smaller, with less atmosphere and "
                    "denser cores (stripped by radiation) -- more ice-giant-like (containing water, "
                    "ammonia, methane) than the mostly hydrogen/helium Hot Jupiters. Can orbit as "
                    "close as ~1 AU from their star.\n\n"
                    "COLD JUPITERS: gas giants like Hot Jupiters but orbiting beyond the frost/snow "
                    "line -- the distance from a young star at which volatile compounds "
                    "(water, ammonia, methane) freeze into ice grains.\n\n"
                    "TIDAL LOCKING: when one side of a body always faces another body it orbits "
                    "(e.g. the Moon always shows Earth the same face). Relevant to habitability "
                    "since a tidally locked planet has permanent day and night sides, which affects "
                    "climate and where liquid water could persist."
                ),
            ),
            (
                "Solar System: Orbital Mechanics, Eclipses & History",
                "Kepler's laws, escape velocity, resonance and Trojans, solar/lunar eclipse types, "
                "and the astronomers and missions that shaped our understanding of the solar system.",
                (
                    "NEWTON'S LAWS & GRAVITATION: (1) an object at rest/in motion stays that way "
                    "unless acted on by an outside force; (2) F = m*a; (3) every action has an "
                    "equal and opposite reaction. Law of gravitation: F = G*m1*m2/r^2.\n\n"
                    "KEPLER'S LAWS OF PLANETARY MOTION: (1) every planet's orbit is an ellipse with "
                    "the Sun at one focus; (2) a line from the Sun to a planet sweeps equal areas in "
                    "equal time, so planets move fastest near the Sun; (3) the square of the "
                    "orbital period is proportional to the cube of the semi-major axis (p^2 = a^3).\n\n"
                    "ESCAPE VELOCITY: Ev = sqrt(2GM/R), where G is the gravitational constant "
                    "(6.67x10^-11 N*m^2/kg^2), M is the planet's mass in kg, and R is its radius in "
                    "meters (watch unit conversions -- radius is usually given in km).\n\n"
                    "TIDAL LOCKING, SHEPHERDING, RESONANCE & TROJANS: tidal locking is one side of "
                    "a body always facing another (Moon-Earth; Pluto-Charon are mutually locked). "
                    "Shepherd moons (e.g. Saturn's Pan, Prometheus) use gravity to keep a ring's "
                    "particles confined. Orbital resonance is a simple integer ratio between two "
                    "bodies' periods (Neptune:Pluto 2:3; Jupiter's Io:Europa:Ganymede 1:2:4, a "
                    "Laplace resonance). Trojans share an orbit with a larger body 60 degrees ahead "
                    "or behind it without colliding.\n\n"
                    "ECLIPSES: lunar eclipses (Earth between Sun and Moon, always full moon) are "
                    "penumbral, total penumbral, partial, or total (up to ~107 minutes of "
                    "totality). Solar eclipses (Moon between Earth and Sun, always new moon) are "
                    "total, annular (Moon looks smaller than the Sun), hybrid, or partial.\n\n"
                    "ASTRONOMERS: Aristarchus (first proposed heliocentrism); Copernicus "
                    "(1473-1543, developed the heliocentric model); Tycho Brahe (1546-1601, precise "
                    "measurements, discovered a 1572 supernova); Galileo (1564-1642, discovered "
                    "Jupiter's 4 largest moons, observed Venus's phases); Kepler (1571-1630, laws "
                    "of planetary motion, was Tycho's assistant); Halley (1656-1742, first to "
                    "calculate a comet's orbit); Tombaugh (1906-1997, discovered Pluto in 1930).\n\n"
                    "MISSIONS: Voyager 1 & 2 (1977-, outer planet flybys); Galileo (1989-2003, "
                    "Jupiter); Cassini (1997-2017, Saturn); New Horizons (2006-, first Pluto flyby "
                    "2015); Dawn (2007-2018, Vesta and Ceres); Juno (2011-, Jupiter); BepiColombo "
                    "(2018-, Mercury); Hubble (1990-) and JWST (2021-) telescopes."
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
                        title="scioly.org wiki: Solar System (excerpt for this chapter)",
                        source_url="https://scioly.org/wiki/Solar_System",
                        raw_text=chapter_text,
                    )
                )

        db.commit()
    finally:
        db.close()


@app.on_event("startup")
def seed_thermodynamics_deep_dive() -> None:
    """One-time content correction + deep-dive setup for Thermodynamics,
    from the actual scioly.org wiki page (coach-supplied PDF). Same pattern
    as seed_solar_system_deep_dive -- unconditionally overwrites the topic's
    description/overview with corrected content, then idempotently seeds a
    grounding resource plus 4 real deep-dive chapters.

    Important finding this correction is built around: the wiki explicitly
    flags that the *device* task changed for 2027 -- the classic "insulate
    a 250mL beaker of hot water" task (used through the 2018/2019 seasons)
    is described as a past version, and the page doesn't fully detail what
    replaces it as of this snapshot. The written-test content (the four
    laws, gas laws, Carnot cycle, conversions, history) is unaffected by
    that change and is what most of the deep-dive chapters below cover.
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

        topic.description = (
            "Teams build a device to collect and retain heat -- the classic \"insulate a beaker "
            "of hot water\" task changed for 2027, so confirm the current device task on soinc.org "
            "-- and take a written test on thermodynamics concepts."
        )
        topic.overview_what = (
            "A Division B and C build/lab event (impounded device + written test), first run in "
            "2012 (as \"Keep the Heat\" in Division B), returning in 2018, 2019, and 2027. Teams "
            "of 2 build a heat-retention device ahead of time and bring it to the tournament, "
            "testing it while also taking a written exam."
        )
        topic.overview_learn = (
            "The four laws of thermodynamics (zeroth through third) and thermodynamic systems/"
            "processes (open/closed/isolated/adiabatic; isobaric/isochoric/isothermal/adiabatic/"
            "isentropic); gas laws (Boyle's, Charles's, Gay-Lussac's, Avogadro's, the combined and "
            "ideal gas law) and the Carnot cycle (its 4 steps, efficiency, entropy); heat/"
            "temperature unit conversions and key equations (Joule's Laws, Gibbs' free energy, "
            "linear/area/volume expansion); the historical figures behind thermodynamics (Joule, "
            "Carnot, Clausius, Kelvin, Maxwell, Nernst, Celsius, Fahrenheit)."
        )
        topic.overview_assessed = (
            "Teams of 2, about 50 minutes, eye protection required. The written test draws 3 "
            "questions from each of 5 subject areas (thermodynamic systems/zeroth law/"
            "temperature; phases of matter/ideal gas law; heat transfer/specific heat; "
            "thermodynamic laws & the Carnot cycle; history of thermodynamics), plus "
            "State/National-only material (blackbody radiation, Stefan-Boltzmann law, third law). "
            "Device testing is impounded and scored alongside the test. Allowed resources: one "
            "hole-punched 3-ring binder of any size (sheets removable), tools/supplies, writing "
            "utensils, and two Class III calculators."
        )
        topic.overview_theme_2027 = (
            "Important change for 2027: the device task itself changed from the long-running "
            "classic version. Previously (through 2019), teams insulated a 250 mL beaker of hot "
            "water for a fixed time window (25 minutes in Division B, starting at 60-75 C). The "
            "wiki explicitly flags the 2027 version as \"very different\" but doesn't fully detail "
            "the new device task as of this snapshot -- confirm the actual 2027 device "
            "requirements and scoring on soinc.org/thermodynamics-b before building anything. The "
            "written-test content (the four laws, gas laws, Carnot cycle, conversions) is stable "
            "and unaffected by this change."
        )
        topic.overview_notes = (
            "Eye protection is required. The device must be easy to disassemble for post-event "
            "inspection. In the pre-2027 device format, two identical, unaltered glass/plastic "
            "beakers were required and the device had to fit a size cube (20 cm for Division B) -- "
            "confirm whether this still applies under the 2027 rules. This event was called \"Hot "
            "House\" (1988-1991) and \"Keep the Heat\" (Division B, 1992-1995 and 2012-2013) before "
            "becoming \"Thermodynamics\" -- older study materials under either name likely describe "
            "the outdated device task, so double-check any inherited notes against the current "
            "rules."
        )

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
    to add real deep-dive chapters once those specifics exist.
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

        topic.description = (
            "Build event: design, construct, and calibrate a self-propelled, air-levitated "
            "hovercraft that travels down a track -- no written test (removed from the current "
            "rules), pure build/run scoring."
        )
        topic.overview_what = (
            "A Division B and C build event, first appearing in 2017. Teams of 2 design, build, "
            "and calibrate ahead of time a self-propelled, air-levitated vehicle, then run it down "
            "a track at competition. It must actually levitate on its air cushion -- if it doesn't, "
            "it's judged a wheeled/sliding vehicle instead of a hovercraft, and event supervisors "
            "may check this if they suspect it isn't truly levitating."
        )
        topic.overview_learn = (
            "Aerodynamic lift via an air cushion, propulsion system design (motor, propeller/"
            "impeller, battery, switch), weight distribution and stability, and iterative "
            "calibration -- testing and adjusting the device using real run data before "
            "competition day. Specific construction dimensions, materials, and scoring formulas "
            "for the 2027 season weren't available on the wiki source this was built from (see "
            "note below) -- pull those from the official rules."
        )
        topic.overview_assessed = (
            "Teams of 2, about 8 minutes, eye protection required (Category B), device and notes "
            "both impounded before running. No written test component in the current rules (this "
            "event used to be a dual lab with a test portion; that's been removed). Allowed at "
            "competition: the vehicle itself, papers/notes (also impounded), tools/supplies, spare "
            "parts, and two Class III calculators."
        )
        topic.overview_theme_2027 = (
            "Confirmed current for 2027 (Division B and C both). Note: the scioly.org wiki page "
            "this was sourced from is largely unfilled for this season -- its construction-"
            "parameters, competition-parameters, design-tips, and scoring sections are still "
            "literal placeholder text (\"Add current construction parameters here!\"), not real "
            "numbers. Get exact dimensions, weight/power limits, the track layout, and the scoring "
            "formula from the official 2027 rules PDF at soinc.org/hovercraft-b before building "
            "anything -- this app hasn't been given those specifics yet."
        )
        topic.overview_notes = (
            "The core eligibility check -- it must genuinely levitate on an air cushion, not just "
            "roll or slide -- is worth emphasizing early, since a non-levitating device can be "
            "disqualified even if it otherwise performs well. Both the vehicle and any notes "
            "brought to competition are impounded, so plan for a supervised, hands-off wait before "
            "the run."
        )

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

        topic.description = (
            "Written test (occasionally stations) on interpreting meteorological data, graphs, "
            "charts, tables, and images; the 2027 focus topic is Severe Storms. Division B only -- "
            "no Division C equivalent."
        )
        topic.overview_what = (
            "A Division B-only Earth Science event (first run 2003) testing meteorological "
            "principles and data interpretation. Its focus topic rotates yearly among Everyday "
            "Weather, Severe Storms, and Climate -- each gets one year before the rotation moves "
            "on -- though some foundational meteorology knowledge (atmosphere, pressure, wind, "
            "water vapor) applies regardless of the year's topic. Usually a written test or "
            "slide-based test; occasionally run as rotating stations."
        )
        topic.overview_learn = (
            "Foundational atmospheric science that applies every year: atmosphere composition and "
            "layers (troposphere through exosphere), pressure systems (cyclones/anticyclones, "
            "pressure gradient force), the Coriolis effect, and the water vapor/cloud/precipitation "
            "cycle (saturation, dew point, condensation, deposition). For 2027 specifically: Severe "
            "Storms -- the wiki names Thunderstorms, Hurricanes, Winter Storms, Mid-Latitude "
            "Cyclones, and Atmospheric Rivers as its sub-topics, though their detailed content "
            "lives on separate wiki pages not included in this source."
        )
        topic.overview_assessed = (
            "Teams of 2, about 50 minutes. Question formats include multiple choice, true/false, "
            "matching, diagram labeling, short answer, and free response -- generally no penalty "
            "for wrong answers, so answering everything (even a guess) is usually worth it. As of "
            "the 2023-24 season, teams may bring one binder of any size with information in any "
            "form (written or typed) plus two stand-alone Class II calculators of any type -- a "
            "notably permissive resource policy compared to most other events."
        )
        topic.overview_theme_2027 = (
            "Severe Storms -- confirmed both by the event description's own wording and by the "
            "wiki's topic-rotation table (2026 Everyday Weather, 2027 Severe Storms, Climate next "
            "in the cycle). The wiki names Thunderstorms, Hurricanes, Winter Storms, Mid-Latitude "
            "Cyclones, and Atmospheric Rivers as this topic's sub-pages, but their content lives on "
            "separate wiki pages this source didn't include -- treat that as a study checklist, and "
            "get the actual storm-science content from those pages, a meteorology textbook, or "
            "soinc.org/meteorology-b directly."
        )
        topic.overview_notes = (
            "Since teams can split the binder-lookup work between partners, prepping a "
            "well-organized, tabbed/labeled binder matters as much as raw knowledge -- the wiki "
            "specifically recommends including diagrams (Coriolis effect, atmosphere layers, cloud "
            "types, classification systems). A general meteorology textbook covering all three "
            "rotation topics is worth having even after the focus topic changes, since foundational "
            "questions can still appear. Free resources: soinc.org/meteorology-b and NOAA's "
            "Science Olympiad education page."
        )

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
