"""The structured study plan for the Solar System event.

Built from the two coach-supplied sources -- the Solar System source reader
(OpenStax Astronomy 2e excerpts) and the scioly.org Solar System wiki page
-- after removing duplicates: every fact is taught in exactly one chapter,
and the chapters are ordered so each one only uses ideas from earlier ones.
Four chapters in lessons_2027.py fill what those sources missed from the
2027 Division B rules (named exoplanet systems, habitability math, water
and extremophiles, the mission list).
The plan itself is shown to students on the Solar System event page.
"""

from app.content.solar_system.lessons_2027 import (
    EXTRASOLAR_SYSTEMS,
    HABITABILITY_MATH,
    MISSIONS_2027,
    WATER_AND_EXTREMOPHILES,
)
from app.content.solar_system.lessons_unit1 import UNIT1
from app.content.solar_system.lessons_unit2 import UNIT2
from app.content.solar_system.lessons_unit3 import UNIT3
from app.content.solar_system.lessons_unit4 import UNIT4
from app.content.solar_system.lessons_unit5 import UNIT5
from app.content.solar_system.lessons_unit6 import UNIT6

UNITS = [
    {
        "number": 1,
        "title": "Space Basics",
        "summary": "The toolkit: distances and units, orbits and seasons, density, the Sun and the lives of stars, and how our Solar System was born.",
    },
    {
        "number": 2,
        "title": "Rocky Worlds",
        "summary": "Earth inside and out, how life changed it, why the rocky planets evolved so differently, then Venus and Mars in depth.",
    },
    {
        "number": 3,
        "title": "Giant Planets & Small Bodies",
        "summary": "The four giants and every major moon, the ocean worlds where life might hide, and the dwarf planets, asteroids, comets and meteors.",
    },
    {
        "number": 4,
        "title": "Gravity & the Sky",
        "summary": "Newton's and Kepler's laws with practice calculations, escape velocity, orbit tricks (tidal locking, resonance, Trojans) and eclipses.",
    },
    {
        "number": 5,
        "title": "Habitability Beyond the Solar System",
        "summary": "The 2027 theme: planets forming around other stars, how exoplanets are found, the exoplanet zoo, the habitable zone and its math, the search for life, water and extremophiles, and the three named systems -- TRAPPIST-1, Kepler-452 and LHS 1140.",
    },
    {
        "number": 6,
        "title": "People & Missions",
        "summary": "The astronomers who figured it all out and the spacecraft and telescopes that explored it, with dates -- then how missions are designed and all 16 missions on the 2027 list.",
    },
]

# Unit 5 order: forming, finding, zoo, habitable zone, [math], astrobiology,
# [water & extremophiles], [the three named systems, which use all of it].
UNIT5_FULL = UNIT5[:4] + [HABITABILITY_MATH] + UNIT5[4:] + [WATER_AND_EXTREMOPHILES, EXTRASOLAR_SYSTEMS]
UNIT6_FULL = UNIT6 + [MISSIONS_2027]

CHAPTERS = UNIT1 + UNIT2 + UNIT3 + UNIT4 + UNIT5_FULL + UNIT6_FULL

INTRO = (
    "Welcome to Solar System! This study plan turns two sources -- the Solar System source reader (OpenStax "
    "Astronomy 2e) and the scioly.org Solar System wiki, plus extra chapters covering everything else on the 2027 "
    f"rules -- into {len(CHAPTERS)} chapters in {len(UNITS)} units. Every fact appears in exactly one chapter, and each "
    "chapter builds on the ones before it, so start at Chapter 1 and work forward."
)

HOW_TO_STUDY = [
    "Read the Lesson tab slowly. Tap any underlined word to see what it means, and tap a picture to zoom in.",
    "Check the Word bank tab for every new science word in the chapter.",
    "Use the Flashcards to review, then try the Quick check questions before peeking at the answers.",
    "Copy the 'Note-sheet facts' onto your note sheet -- you are allowed two in the competition.",
    "Stuck? Type your question in 'Ask a question'. It searches the lessons first, and you can ask the AI tutor if the lessons don't answer it.",
    "2027's theme is habitability: Units 2, 3 and 5 matter most, but tests often ask about everything, so cover it all.",
    "No calculators are allowed in 2027 -- practice the Habitability Math chapter's scaling tricks by hand.",
]


def plan_json() -> dict:
    """The Solar System event's study plan, stored as the parent topic's
    lesson_json (kind "plan") and rendered on its student page."""
    return {
        "kind": "plan",
        "intro": INTRO,
        "how_to_study": HOW_TO_STUDY,
        "units": [
            {
                **unit,
                "chapters": [
                    {"name": chapter["name"], "description": chapter["description"]}
                    for chapter in CHAPTERS
                    if chapter["unit"] == unit["number"]
                ],
            }
            for unit in UNITS
        ],
    }
