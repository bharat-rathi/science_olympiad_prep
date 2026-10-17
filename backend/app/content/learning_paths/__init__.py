"""Per-event learning paths: the topics for each event, in order, each one
building on the ones before it (the structure oly-spark.app uses for its
event pages). The lesson text is our own, written against the 2027 rules in
content/official_rules.py.

Solar System is deliberately absent -- its chapters live in
content/solar_system and are not touched by these paths. Hovercraft's path
is in content/study_notes_2027.py (HOVERCRAFT_PATH_CHAPTERS).
"""

from app.content.learning_paths import earth, inquiry, life, physical, tech

EVENT_PATHS: dict[str, list[tuple[str, str, str]]] = {
    # Life, Personal & Social Science
    "Anatomy and Physiology": life.ANATOMY_AND_PHYSIOLOGY,
    "Botany": life.BOTANY,
    "Disease Detectives": life.DISEASE_DETECTIVES,
    "Heredity": life.HEREDITY,
    "Water Quality": life.WATER_QUALITY,
    # Earth & Space Science
    "Dynamic Planet": earth.DYNAMIC_PLANET,
    "Meteorology": earth.METEOROLOGY,
    "Remote Sensing": earth.REMOTE_SENSING,
    "Rocks and Minerals": earth.ROCKS_AND_MINERALS,
    # Physical Science & Chemistry
    "Circuit Lab": physical.CIRCUIT_LAB,
    "Crime Busters": physical.CRIME_BUSTERS,
    "Food Science": physical.FOOD_SCIENCE,
    "Thermodynamics": physical.THERMODYNAMICS,
    # Technology & Engineering
    "Boomilever": tech.BOOMILEVER,
    "Elastic Launched Glider": tech.ELASTIC_LAUNCHED_GLIDER,
    "Roller Coaster": tech.ROLLER_COASTER,
    "Scrambler": tech.SCRAMBLER,
    # Inquiry & Nature of Science
    "Codebusters": inquiry.CODEBUSTERS,
    "Experimental Design": inquiry.EXPERIMENTAL_DESIGN,
    "Ping Pong Parachute": inquiry.PING_PONG_PARACHUTE,
    "Write It Do It": inquiry.WRITE_IT_DO_IT,
}

assert "Solar System" not in EVENT_PATHS
