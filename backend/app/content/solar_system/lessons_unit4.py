"""Unit 4 -- Gravity & the Sky: Newton's and Kepler's laws with worked
calculations, escape velocity, and the "orbit tricks" (tidal locking,
shepherd moons, resonance, Trojans) plus every kind of eclipse. Same
lesson-chapter format as lessons_unit1.py.
"""

from app.content.solar_system.svg import BLUE, GAS, GOLD, ICE, PURPLE, RED, ROCK, SUN

UNIT4 = [
    # ------------------------------------------------------------------ 12
    {
        "unit": 4,
        "name": "Solar System: Gravity & Kepler's Laws",
        "description": "Newton's three laws of motion and his law of gravity, why the Moon doesn't fall down, Kepler's three laws (ellipses, equal areas, p² = a³) with step-by-step practice, and how to calculate escape velocity.",
        "goals": [
            "State Newton's three laws of motion with everyday examples.",
            "Use Newton's law of gravity to compare forces.",
            "Explain Kepler's three laws and the parts of an ellipse.",
            "Calculate a planet's year or distance with p^2 = a^3.",
            "Calculate escape velocity, watching the units.",
        ],
        "sections": [
            {
                "heading": "Newton's three laws of motion",
                "body": (
                    "Isaac Newton described how everything moves -- from soccer balls to planets -- with three laws.\n\n"
                    "1. INERTIA: an object at rest stays at rest, and an object in motion keeps moving in a straight line at "
                    "the same speed, unless an outside FORCE (a push or a pull) acts on it. A hockey puck slides a long way on "
                    "smooth ice because almost nothing slows it down.\n"
                    "2. F = m x a: FORCE equals MASS times ACCELERATION (a change in speed or direction). Push harder and "
                    "something speeds up more; heavier things need a bigger push to speed up the same amount.\n"
                    "3. ACTION AND REACTION: for every action there is an equal and opposite reaction. A rocket pushes hot gas "
                    "out backward, so the gas pushes the rocket forward -- that is how rockets work even in empty space.\n\n"
                    "Forces are measured in NEWTONS (N). One newton is about the weight of a small apple."
                ),
            },
            {
                "heading": "Newton's law of universal gravitation",
                "body": (
                    "Newton realized that the force pulling an apple to the ground is the same force holding the Moon in orbit: "
                    "GRAVITY. Every object with mass pulls on every other object:\n\n"
                    "F = G x m1 x m2 / r^2\n\n"
                    "• F is the force of gravity between the two objects (in newtons).\n"
                    "• m1 and m2 are their masses (in kg).\n"
                    "• r is the distance between their centers (in meters).\n"
                    "• G is the GRAVITATIONAL CONSTANT, a tiny fixed number: 6.67 x 10^-11 N m^2/kg^2.\n\n"
                    "What the formula means in plain words:\n"
                    "• More mass = more pull. Double one mass and the force doubles.\n"
                    "• More distance = MUCH less pull, because distance is squared. Double the distance and the force drops to "
                    "1/4 (because 2^2 = 4). Triple it and the force drops to 1/9. This is called an INVERSE-SQUARE law.\n"
                    "• Gravity is mutual: Earth pulls on the Moon and the Moon pulls on Earth just as hard. A star and its "
                    "planet both circle their shared balance point (the CENTER OF MASS) -- which is how we discover planets "
                    "around other stars!"
                ),
            },
            {
                "heading": "Why doesn't the Moon fall down?",
                "body": (
                    "It does -- all the time! Imagine throwing a ball sideways from a very tall mountain. It curves down and "
                    "lands. Throw it faster and it lands farther away. Throw it fast enough and, as it falls, Earth's curved "
                    "surface curves away beneath it just as fast -- so it keeps falling but never lands. That endless 'falling "
                    "around' is an ORBIT.\n\n"
                    "By Newton's first law the Moon 'wants' to fly off in a straight line, and gravity keeps bending its path "
                    "into a curve. Speed sideways + gravity inward = orbit. Astronauts on the space station float not because "
                    "there is no gravity, but because they and their station are falling around Earth together."
                ),
            },
            {
                "heading": "Kepler's first law: orbits are ellipses",
                "body": (
                    "Johannes Kepler worked out three laws of planetary motion from Tycho Brahe's careful measurements of Mars. "
                    "(He first tried to make circles fit, and failed!)\n\n"
                    "LAW 1: The orbit of every planet is an ELLIPSE, with the Sun at one of its two FOCI.\n\n"
                    "An ellipse is a stretched or flattened circle. Its parts:\n"
                    "• The MAJOR AXIS is the longest line across it; the MINOR AXIS is the shortest.\n"
                    "• The SEMI-MAJOR AXIS (a) is half the major axis -- the planet's average distance from the Sun.\n"
                    "• The two FOCI (one is a FOCUS) are special points on the major axis. For any point on the ellipse, the "
                    "distances to the two foci always add up to the same total. (Draw one with two pins, a loop of string and "
                    "a pencil!)\n"
                    "• ECCENTRICITY measures how stretched the ellipse is: 0 is a perfect circle; close to 1 is a long, thin "
                    "oval.\n\n"
                    "The Sun sits at one focus, not in the center. The planets' orbits are close to circles but never perfect "
                    "circles; many comets have very eccentric orbits. The closest point to the Sun is PERIHELION; the farthest "
                    "is APHELION."
                ),
            },
            {
                "heading": "Kepler's second law: equal areas in equal times",
                "body": (
                    "LAW 2: A line joining a planet and the Sun sweeps out equal AREAS in equal amounts of time.\n\n"
                    "Imagine a string from the Sun to the planet, painting the area it sweeps across as the planet moves. In "
                    "one month near the Sun, the string is short, so to paint the same area as in one month far away, the "
                    "planet must travel a longer stretch of its orbit. So:\n"
                    "• Near the Sun (perihelion), a planet moves FASTEST.\n"
                    "• Far from the Sun (aphelion), it moves SLOWEST.\n\n"
                    "It's like a kid on a swing: fastest at the bottom, slowest at the top. Earth is actually closest to the "
                    "Sun in early January, so it moves a little faster then."
                ),
            },
            {
                "heading": "Kepler's third law: p^2 = a^3 (with practice)",
                "body": (
                    "LAW 3: The square of a planet's orbital period is proportional to the cube of its semi-major axis. For "
                    "anything orbiting the Sun, using years and AU, this becomes the simple rule:\n\n"
                    "p^2 = a^3\n\n"
                    "• p = the orbital PERIOD (the time for one orbit) in Earth years.\n"
                    "• a = the semi-major axis (average distance) in AU.\n"
                    "• To find p: p = the square root of a^3 (also written a^(3/2)).\n"
                    "• To find a: a = the cube root of p^2 (also written p^(2/3)).\n"
                    "• Comparing two planets: (p1/p2)^2 = (a1/a2)^3.\n\n"
                    "WORKED EXAMPLES:\n"
                    "• Mars, a = 1.52 AU: a^3 = 1.52 x 1.52 x 1.52 = 3.51. p = square root of 3.51 = 1.87 years. The real "
                    "value is 1.88 years -- it works!\n"
                    "• Jupiter, a = 5.20 AU: a^3 = 140.6, so p = 11.86 years. Exactly right.\n"
                    "• Neptune, a = 30.06 AU: p = about 164.8 years.\n"
                    "• Going backward: an asteroid takes 8 years to orbit. p^2 = 64, and the cube root of 64 is 4, so a = 4 "
                    "AU.\n\n"
                    "The farther out a planet is, the longer its year -- and Kepler found the exact rule. Newton later showed "
                    "WHY it works, using gravity. With the star's mass included, the same law turns an exoplanet's year "
                    "(measured from transits or wobbles) into its distance from its star."
                ),
                "infographic": "kepler_laws",
            },
            {
                "heading": "Escape velocity: how fast to leave for good?",
                "body": (
                    "Throw a ball up and gravity brings it back. Throw it faster and it goes higher. ESCAPE VELOCITY is the "
                    "speed something needs to escape a planet's gravity completely and never fall back (ignoring air):\n\n"
                    "Ev = square root of (2 x G x M / R)\n\n"
                    "• G = 6.67 x 10^-11 N m^2/kg^2\n"
                    "• M = the planet's mass in KILOGRAMS\n"
                    "• R = the planet's radius in METERS -- a common trap! Radius is usually given in km, so multiply by 1,000 "
                    "first. Forgetting this changes your answer hugely.\n\n"
                    "WORKED EXAMPLE (Earth): M = 5.97 x 10^24 kg, R = 6,378 km = 6.378 x 10^6 m.\n"
                    "2 x G x M = 2 x 6.67 x 10^-11 x 5.97 x 10^24 = 7.96 x 10^14.\n"
                    "Divide by R: 7.96 x 10^14 / 6.378 x 10^6 = 1.25 x 10^8.\n"
                    "Square root: about 11,200 m/s = 11.2 km/s -- over 40,000 km per hour!\n\n"
                    "Venus needs 10.4 km/s and Mars only 5.0 km/s. Gas atoms are always zooming around; on a world with a low "
                    "escape velocity, more of them reach escape speed and drift off into space. That is one reason small "
                    "worlds like Mars and the Moon lost most or all of their air."
                ),
            },
        ],
        "word_bank": [
            ("Force", "A push or a pull, measured in newtons (N)."),
            ("Newton (N)", "The unit of force -- about the weight of a small apple."),
            ("Inertia", "The tendency of an object to keep doing what it's doing (staying still or moving straight) unless a force acts."),
            ("Acceleration", "Any change in speed or direction."),
            ("Gravity", "The pull every object with mass has on every other object."),
            ("Gravitational constant (G)", "A fixed number in Newton's gravity formula: 6.67 x 10^-11 N m^2/kg^2."),
            ("Inverse-square law", "A rule where something weakens with the square of distance: twice as far = 1/4 as strong."),
            ("Center of mass", "The balance point between two objects that they both orbit around."),
            ("Ellipse", "A stretched or flattened circle -- the shape of every orbit."),
            ("Focus", "One of two special points inside an ellipse; the Sun sits at one of them (plural: foci)."),
            ("Major axis", "The longest line across an ellipse, through both foci."),
            ("Minor axis", "The shortest line across an ellipse."),
            ("Semi-major axis", "Half the major axis -- a planet's average distance from the Sun (a in p^2 = a^3)."),
            ("Eccentricity", "How stretched an ellipse is: 0 is a perfect circle, close to 1 is a long thin oval."),
            ("Perihelion", "The point in an orbit closest to the Sun, where a planet moves fastest."),
            ("Aphelion", "The point in an orbit farthest from the Sun, where a planet moves slowest."),
            ("Orbital period", "The time it takes to complete one orbit (p in p^2 = a^3)."),
            ("Square root", "The number that, multiplied by itself, gives your number: the square root of 9 is 3."),
            ("Cube root", "The number that, multiplied by itself three times, gives your number: the cube root of 64 is 4."),
            ("Escape velocity", "The speed needed to break free of a world's gravity for good."),
        ],
        "key_facts": [
            "Newton: (1) inertia, (2) F = m x a, (3) equal and opposite reaction.",
            "Gravity: F = G m1 m2 / r^2, G = 6.67 x 10^-11 N m^2/kg^2. Double the distance -> 1/4 the force.",
            "Kepler 1: ellipse with the Sun at one focus. Kepler 2: equal areas in equal times (fastest at perihelion).",
            "Kepler 3: p^2 = a^3 (years, AU). p = a^(3/2); a = p^(2/3). Mars: 1.52 AU -> 1.88 y; Jupiter: 5.20 AU -> 11.86 y.",
            "Escape velocity: Ev = sqrt(2GM/R) with M in kg and R in METERS. Earth 11.2, Venus 10.4, Mars 5.0 km/s.",
        ],
        "quick_check": [
            ("If the distance between two objects doubles, what happens to the gravity between them?", "It drops to 1/4 (inverse-square law)."),
            ("Where in its orbit does a planet move fastest, and which law says so?", "At perihelion (closest to the Sun) -- Kepler's second law."),
            ("A comet's semi-major axis is 4 AU. What is its period?", "p^2 = 4^3 = 64, so p = 8 years."),
            ("An asteroid orbits the Sun every 27 years. How far away is it on average?", "p^2 = 729; the cube root of 729 is 9, so a = 9 AU."),
            ("What is the most common mistake when calculating escape velocity?", "Using the radius in km instead of meters (multiply km by 1,000)."),
            ("Why does a rocket work in empty space?", "Newton's third law: it pushes exhaust backward, and the exhaust pushes the rocket forward."),
        ],
        "cards": [
            {
                "term": "Newton's three laws",
                "badge": ("F=ma", "Newton", BLUE),
                "analogy": "Kick a ball on ice: it keeps sliding (1), a harder kick sends it faster (2), and your foot feels the kick back (3).",
                "explanation": "(1) Objects keep doing what they're doing unless a force acts. (2) F = m x a. (3) Every action has an equal and opposite reaction.",
                "why": "The foundation for every orbit and escape-velocity question.",
            },
            {
                "term": "Law of gravitation",
                "badge": ("1/r²", "gravity", PURPLE),
                "analogy": "Gravity is like every object's invisible magnet -- the pull fades fast with distance.",
                "explanation": "F = G m1 m2 / r^2, G = 6.67 x 10^-11. Double a mass -> double the force; double the distance -> 1/4 the force. Gravity is mutual, so stars wobble around the center of mass.",
                "why": "Expect plug-in and 'what if' questions.",
            },
            {
                "term": "Orbits = falling around",
                "badge": ("FALL", "+ sideways", ICE),
                "analogy": "A ball thrown so fast that the ground curves away before it can land.",
                "explanation": "The Moon is always falling toward Earth, but it moves sideways so fast that it keeps missing. Sideways speed + gravity = orbit.",
                "why": "Explains why astronauts float.",
            },
            {
                "term": "Kepler 1: ellipses",
                "badge": ("ELLIPSE", "1st law", GOLD),
                "analogy": "A race track shaped like a squashed circle, with the Sun sitting off to one side.",
                "explanation": "Orbits are ellipses with the Sun at one focus. Semi-major axis = average distance; eccentricity 0 = circle, near 1 = long oval. Perihelion closest, aphelion farthest.",
                "why": "Ellipse vocabulary shows up in comet and exoplanet questions.",
            },
            {
                "term": "Kepler 2: equal areas",
                "badge": ("=AREA", "2nd law", GOLD),
                "analogy": "A kid on a swing: fastest at the bottom, slowest at the top.",
                "explanation": "A line from the Sun to a planet sweeps equal areas in equal times, so the planet moves fastest at perihelion and slowest at aphelion.",
                "why": "Classic 'where is the planet fastest?' question.",
            },
            {
                "term": "Kepler 3: p² = a³",
                "badge": ("p²=a³", "3rd law", GOLD),
                "analogy": "The farther out your lane, the longer each lap -- with an exact formula.",
                "explanation": "p in years, a in AU. Mars: 1.52^3 = 3.51, sqrt = 1.87 y. Jupiter: 5.2^3 = 140.6 -> 11.86 y. Reverse: p = 8 y -> a = 4 AU.",
                "why": "One of the most-calculated formulas on the test.",
            },
            {
                "term": "Escape velocity",
                "badge": ("11.2", "km/s Earth", RED),
                "analogy": "How hard you'd have to throw a ball so it never comes back down.",
                "explanation": "Ev = sqrt(2GM/R) with M in kg and R in meters. Earth 11.2 km/s, Venus 10.4, Mars 5.0. Low escape velocity lets gas leak away.",
                "why": "A favorite calculation -- watch the km-to-m trap.",
            },
        ],
    },
    # ------------------------------------------------------------------ 13
    {
        "unit": 4,
        "name": "Solar System: Orbit Tricks & Eclipses",
        "description": "Tidal locking, shepherd moons (with the wiki's table), orbital resonance and the Laplace resonance, Trojans at L4 and L5, and every kind of lunar and solar eclipse -- umbra, penumbra, antumbra, annular, hybrid and the rare selenehelion.",
        "goals": [
            "Explain tidal locking and give examples.",
            "Explain shepherd moons, orbital resonance and Trojans, with examples from the wiki tables.",
            "Describe the parts of a shadow (umbra, penumbra, antumbra).",
            "Name every type of lunar and solar eclipse and when each can happen.",
        ],
        "sections": [
            {
                "heading": "Tidal locking",
                "body": (
                    "Why do we always see the same face of the Moon? Long ago the Moon spun faster. Earth's gravity raised "
                    "tidal bulges on it, and the rubbing (tidal friction) slowed its spin until it turned exactly once per "
                    "orbit -- one rotation takes as long as one revolution (27.3 days). Now one side always faces Earth. This "
                    "is TIDAL LOCKING.\n\n"
                    "• Many moons are tidally locked to their planets, like Jupiter's Callisto (17-day day and 17-day orbit).\n"
                    "• Two objects of similar size can lock to EACH OTHER: Pluto and Charon always show each other the same "
                    "face, like dancers holding hands.\n"
                    "• Planets very close to their stars -- like many hot Jupiters and planets around dim red dwarf stars -- "
                    "may be tidally locked to their star, with a side of endless day and a side of endless night. That matters "
                    "a lot for whether they could support life."
                ),
            },
            {
                "heading": "Shepherd moons",
                "body": (
                    "A SHEPHERD MOON orbits near the edge of a ring and uses its gravity to keep the ring's particles in a "
                    "tight band, stopping them from spreading out -- like a sheepdog keeping a flock together. The wiki's "
                    "table of shepherd moons:\n\n"
                    "• JUPITER: Metis, Adrastea, Amalthea and Thebe.\n"
                    "• SATURN: Pan, Daphnis, Atlas, Prometheus, Pandora, Aegaeon, and many tiny 'moonlets'. (Prometheus and "
                    "Pandora guard the narrow F ring; Pan and Daphnis clear gaps inside the main rings.)\n"
                    "• URANUS: Cordelia and Ophelia, which guard its narrow epsilon ring.\n\n"
                    "Young planets do the same thing in the dusty disks around newborn stars: they carve gaps and herd dust "
                    "into rings and arcs that telescopes can see."
                ),
            },
            {
                "heading": "Orbital resonance",
                "body": (
                    "ORBITAL RESONANCE happens when the orbit times of two bodies form a simple whole-number ratio, so they "
                    "line up at the same spots again and again and tug on each other each time -- like pushing a swing at "
                    "exactly the right moment every time. Small, regular tugs add up to big effects. The wiki's examples:\n\n"
                    "• 2:3 -- NEPTUNE and PLUTO: Neptune orbits three times while Pluto orbits twice (Neptune's period is 2/3 of "
                    "Pluto's). This keeps them from ever colliding, even though Pluto's orbit crosses inside Neptune's.\n"
                    "• 1:2 -- Saturn's moons MIMAS and TETHYS.\n"
                    "• 1:2 -- Saturn's moons ENCELADUS and DIONE.\n"
                    "• 3:4 -- Saturn's moons TITAN and HYPERION.\n"
                    "• 1:2:4 -- Jupiter's moons IO, EUROPA and GANYMEDE: for every 1 orbit of Ganymede, Europa makes 2 and Io "
                    "makes 4.\n\n"
                    "When three or more bodies are in resonance together, it is called a LAPLACE RESONANCE. Io, Europa and "
                    "Ganymede are the only known example. Their regular tugs keep Io's orbit slightly oval, which powers its "
                    "tidal heating and volcanoes. In a few hundred million years, Callisto may join in to make a 1:2:4:8 "
                    "resonance (Callisto orbiting once for every 2 Ganymede, 4 Europa and 8 Io orbits)."
                ),
                "infographic": "resonance_table",
            },
            {
                "heading": "Trojans and Lagrange points",
                "body": (
                    "TROJANS are a special 1:1 resonance: a small body shares the SAME orbit as a bigger one, but never "
                    "collides with it, because it rides 60 degrees ahead of or 60 degrees behind it. Those two spots are "
                    "balance points called the LAGRANGIAN POINTS L4 (ahead) and L5 (behind), where the pulls of the Sun and the "
                    "planet work together to hold small objects in place.\n\n"
                    "• Mars, Jupiter and Neptune all share their orbits with Trojan asteroids. Jupiter has thousands.\n"
                    "• Saturn's moons have smaller Trojan moons: Telesto and Calypso share an orbit with Tethys, and Helene and "
                    "Polydeuces share an orbit with Dione."
                ),
                "infographic": "orbit_tricks",
            },
            {
                "heading": "Shadows: umbra, penumbra and antumbra",
                "body": (
                    "Eclipses are all about shadows, and a shadow from a big light like the Sun has parts:\n"
                    "• UMBRA: the dark center of the shadow, where the light is completely blocked.\n"
                    "• PENUMBRA: the lighter outer part of the shadow, where the light is only partly blocked.\n"
                    "• ANTUMBRA: the region beyond the tip of the umbra (when the blocking object looks smaller than the light "
                    "source), where you see a bright ring of light around the blocker.\n\n"
                    "Two more words: the Moon's orbit is an ellipse, so its distance from Earth changes. PERIGEE is when the "
                    "Moon is closest to Earth (it looks a bit bigger); APOGEE is when it is farthest (it looks a bit smaller). "
                    "Likewise Earth is at PERIHELION when closest to the Sun (the Sun looks slightly bigger) and APHELION when "
                    "farthest."
                ),
            },
            {
                "heading": "Lunar eclipses",
                "body": (
                    "A LUNAR ECLIPSE happens when Earth passes directly between the Sun and the Moon, so Earth's shadow falls "
                    "on the Moon. Since Earth must be in the middle, it can only happen at a FULL MOON. Anyone on the night "
                    "side of Earth can see it, and it is safe to look at.\n\n"
                    "Types of lunar eclipse:\n"
                    "• PENUMBRAL: the Moon passes through Earth's penumbra only, so it dims slightly.\n"
                    "• TOTAL PENUMBRAL: the Moon passes entirely within the penumbra; the edge nearest the umbra can look darker.\n"
                    "• PARTIAL: part of the Moon enters Earth's umbra.\n"
                    "• TOTAL: the whole Moon is inside the umbra, often glowing a coppery red (sunlight bent through Earth's air "
                    "reaches it). TOTALITY can last up to about 107 minutes -- longest when the Moon is near apogee, because "
                    "it moves more slowly then.\n"
                    "• SELENEHELION (also called a 'horizontal eclipse'): the rare sight of the eclipsed Moon and the Sun in the "
                    "sky at the same time, just after sunrise or just before sunset. It shouldn't be possible, since they are "
                    "on opposite sides of Earth -- but Earth's air bends (REFRACTS) light near the horizon, making both appear "
                    "a little higher than they really are. The name comes from the Greek Selene (Moon goddess) and Helios (Sun)."
                ),
            },
            {
                "heading": "Solar eclipses",
                "body": (
                    "A SOLAR ECLIPSE happens when the Moon passes between Earth and the Sun, blocking some or all of the "
                    "Sun's light. It can only happen at a NEW MOON. Why not every month? The Moon's orbit is tilted about 5 "
                    "degrees compared with Earth's orbit (the ECLIPTIC), so usually the Moon passes a bit above or below the "
                    "Sun. Eclipses only happen when a new moon occurs right where the Moon's orbit crosses the ecliptic.\n\n"
                    "Types of solar eclipse:\n"
                    "• TOTAL: the Moon completely covers the Sun's disk and the glowing corona appears. It is seen only from the "
                    "narrow PATH OF TOTALITY inside the Moon's umbra. Total eclipses are more likely when the Moon is near "
                    "perigee (looks bigger) and when Earth is near aphelion (the Sun looks smaller).\n"
                    "• ANNULAR: the Moon is near apogee, so it looks a little smaller than the Sun and leaves a bright 'ring of "
                    "fire' around it. It is seen from inside the antumbra, and is more likely when Earth is near perihelion.\n"
                    "• HYBRID: total from some places on Earth and annular from others -- rare.\n"
                    "• PARTIAL: the Moon covers only part of the Sun. It is seen from the large area under the Moon's penumbra, "
                    "outside the path of a total or annular eclipse. Some eclipses are only ever partial, because the umbra "
                    "passes above the poles and misses Earth.\n\n"
                    "SAFETY: never look at the Sun, even during most of an eclipse, without certified eclipse glasses. Only "
                    "during the brief moments of totality is the Sun's bright surface fully covered."
                ),
                "infographic": "eclipses",
            },
        ],
        "word_bank": [
            ("Tidal locking", "When a body spins exactly once per orbit, so the same side always faces its partner."),
            ("Tidal friction", "Rubbing inside a body caused by tides, which slows its spin."),
            ("Shepherd moon", "A small moon whose gravity keeps a ring's particles in a narrow band."),
            ("Moonlet", "A very small moon, often found inside a planet's rings."),
            ("Orbital resonance", "When two bodies' orbit times form a simple whole-number ratio (like 1:2), so they line up and tug each other regularly."),
            ("Ratio", "A comparison of two numbers, like 2:3 (two for every three)."),
            ("Laplace resonance", "A resonance between three or more bodies -- only Io, Europa and Ganymede (1:2:4) are known."),
            ("Trojan", "A small body sharing a bigger body's orbit, 60 degrees ahead of or behind it."),
            ("Lagrangian points", "Balance points in an orbit (L4 ahead, L5 behind) where small objects can stay put."),
            ("Eclipse", "When one object blocks light from reaching another by moving into its path or shadow."),
            ("Umbra", "The darkest, central part of a shadow, where the light is completely blocked."),
            ("Penumbra", "The lighter outer part of a shadow, where light is partly blocked."),
            ("Antumbra", "The area beyond the tip of the umbra, where an annular 'ring of fire' eclipse is seen."),
            ("Perigee", "The point in the Moon's orbit closest to Earth."),
            ("Apogee", "The point in the Moon's orbit farthest from Earth."),
            ("Totality", "The part of an eclipse when the light is completely blocked."),
            ("Selenehelion", "A rare sight of an eclipsed Moon and the Sun above the horizon at the same time, thanks to the air bending light."),
            ("Refraction", "The bending of light as it passes through air, water or glass."),
            ("Ecliptic", "The flat plane of Earth's orbit around the Sun (and the Sun's yearly path across our sky)."),
            ("Annular eclipse", "A solar eclipse where the Moon looks smaller than the Sun, leaving a bright ring."),
            ("Hybrid eclipse", "A solar eclipse that looks total from some places and annular from others."),
            ("Path of totality", "The narrow track on Earth where a total solar eclipse can be seen."),
        ],
        "key_facts": [
            "Tidal locking: Moon (27.3 d), Callisto, Pluto-Charon (mutual).",
            "Shepherd moons: Jupiter -- Metis, Adrastea, Amalthea, Thebe; Saturn -- Pan, Daphnis, Atlas, Prometheus, Pandora, Aegaeon, moonlets; Uranus -- Cordelia, Ophelia.",
            "Resonances: Neptune:Pluto 2:3; Mimas:Tethys 1:2; Enceladus:Dione 1:2; Titan:Hyperion 3:4; Io:Europa:Ganymede 1:2:4 (Laplace).",
            "Trojans: 60 degrees ahead/behind at L4/L5. Mars, Jupiter, Neptune; Telesto & Calypso (Tethys), Helene & Polydeuces (Dione).",
            "Lunar eclipse: full moon only. Types: penumbral, total penumbral, partial, total (up to ~107 min), selenehelion.",
            "Solar eclipse: new moon only (Moon's orbit tilted ~5 degrees). Types: total (umbra), annular (antumbra), hybrid, partial (penumbra).",
            "Total solar more likely at perigee / Earth near aphelion; annular more likely at apogee / Earth near perihelion.",
        ],
        "quick_check": [
            ("Why do we always see the same side of the Moon?", "It is tidally locked: it rotates once in exactly the time it takes to orbit Earth."),
            ("What does a 2:3 resonance between Neptune and Pluto mean?", "Neptune orbits the Sun 3 times for every 2 orbits of Pluto, so they never meet even though their orbits cross."),
            ("Where do Trojans sit?", "60 degrees ahead of or behind a larger body in the same orbit, at the L4 and L5 points."),
            ("Why can a lunar eclipse only happen at a full moon?", "Earth must be between the Sun and the Moon, and that lineup is a full moon."),
            ("What makes an annular eclipse different from a total one?", "The Moon is near apogee and looks smaller than the Sun, so a ring of sunlight stays visible."),
            ("How can you see the Sun and an eclipsed Moon at the same time?", "A selenehelion: Earth's atmosphere refracts light near the horizon, lifting both into view just after sunrise or before sunset."),
        ],
        "cards": [
            {
                "term": "Tidal locking",
                "badge": ("LOCKED", "same face", ICE),
                "analogy": "Dancers spinning while holding hands -- always facing their partner.",
                "explanation": "Tidal friction slowed the spin until one rotation = one orbit. The Moon, Callisto, and Pluto-Charon (mutually). Close-in exoplanets may have permanent day and night sides.",
                "why": "Tidal locking affects the climate and habitability of close-in planets.",
            },
            {
                "term": "Shepherd moons",
                "badge": ("HERD", "rings", PURPLE),
                "analogy": "Sheepdogs keeping a flock of ring particles in a neat line.",
                "explanation": "Saturn: Pan, Daphnis, Atlas, Prometheus, Pandora, Aegaeon. Jupiter: Metis, Adrastea, Amalthea, Thebe. Uranus: Cordelia, Ophelia.",
                "why": "Young planets 'shepherd' dust into rings and gaps around new stars.",
            },
            {
                "term": "Orbital resonance",
                "badge": ("2:3", "Neptune:Pluto", GAS),
                "analogy": "Pushing a swing at exactly the right moment every time.",
                "explanation": "Simple-ratio orbit times: Neptune:Pluto 2:3; Mimas:Tethys and Enceladus:Dione 1:2; Titan:Hyperion 3:4.",
                "why": "Resonances keep orbits stable and pump tidal heating.",
            },
            {
                "term": "Laplace resonance",
                "badge": ("1:2:4", "Io-E-G", GOLD),
                "analogy": "Three runners who meet at the same spot every lap.",
                "explanation": "Three or more bodies in resonance. Only known: Io, Europa, Ganymede (1:2:4). It keeps Io's orbit oval and its volcanoes going; Callisto may join (1:2:4:8).",
                "why": "Links orbital mechanics to tidal heating and ocean worlds.",
            },
            {
                "term": "Trojans",
                "badge": ("60°", "L4 / L5", ROCK),
                "analogy": "Cars driving in the same lane as a big truck, always the same distance ahead or behind.",
                "explanation": "A 1:1 resonance: small bodies 60 degrees ahead (L4) or behind (L5) a larger one. Mars, Jupiter, Neptune have Trojan asteroids; Tethys and Dione have Trojan moons.",
                "why": "A frequent vocabulary question.",
            },
            {
                "term": "Shadow parts",
                "badge": ("UMBRA", "penumbra", BLUE),
                "analogy": "Stand under a lamp: the darkest middle of your shadow, and the fuzzy edge around it.",
                "explanation": "Umbra = full shadow; penumbra = partial shadow; antumbra = beyond the umbra's tip (ring of light). Perigee/apogee = Moon closest/farthest from Earth.",
                "why": "You need these words to name each eclipse type.",
            },
            {
                "term": "Lunar eclipses",
                "badge": ("FULL", "moon only", RED),
                "analogy": "Earth 'photobombing' the sunlight that normally lights the Moon.",
                "explanation": "Earth between Sun and Moon, full moon only. Penumbral, total penumbral, partial, total (red Moon, up to ~107 min), and the rare selenehelion.",
                "why": "Eclipse types are classic short-answer questions.",
            },
            {
                "term": "Solar eclipses",
                "badge": ("NEW", "moon only", SUN),
                "analogy": "The Moon briefly holding its hand up in front of the Sun.",
                "explanation": "Moon between Earth and Sun, new moon only, near where its 5-degree-tilted orbit crosses the ecliptic. Total (umbra, corona visible), annular (antumbra, ring of fire), hybrid, partial (penumbra).",
                "why": "Know which phase goes with which eclipse.",
            },
        ],
    },
]
