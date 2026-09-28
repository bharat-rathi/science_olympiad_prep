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
