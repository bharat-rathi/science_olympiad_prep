"""Solar System learning chapters 15-16: gravity/orbits/eclipses and the
astronomers and missions behind the science.

These absorb the four older wiki-excerpt chapters ("Star & Planet
Formation", "Bodies, Moons & Small Bodies", "Habitability & Exoplanet
Types", "Orbital Mechanics, Eclipses & History") so the Solar System event
has one de-duplicated set of chapters. Facts come from the scioly.org wiki
excerpts the coach supplied plus the source reader (OpenStax Astronomy 2e);
the few widely known extras (who discovered Uranus and Neptune, Earth's
mass for the escape-velocity example) are marked as such in the text.
Same dict shape and plain-text rules as chapters_a.py.
"""

from app.content.solar_system.svg import BLUE, GAS, GOLD, ICE, PURPLE, RED, ROCK, SUN

CHAPTERS_C = [
    # ------------------------------------------------------------------ 15
    {
        "name": "Solar System: Gravity, Orbits & Eclipses",
        "description": "Newton's laws and gravity, Kepler's three laws (with p² = a³ practice), escape velocity, tidal locking, shepherd moons, orbital resonance, Trojans, and every type of solar and lunar eclipse.",
        "source_title": "Source notes: Orbital mechanics and eclipses (scioly.org Solar System wiki + OpenStax Astronomy 2e)",
        "infographics": ["kepler_laws", "orbit_tricks", "eclipses"],
        "source_text": (
            "NEWTON'S LAWS: (1) an object at rest or in motion stays that way unless acted on by an outside force; (2) F = m*a; "
            "(3) every action has an equal and opposite reaction. LAW OF GRAVITATION: F = G*m1*m2/r^2, G = 6.67x10^-11 N*m^2/kg^2. "
            "Gravity is mutual: a star and planet both orbit their common center of mass.\n"
            "KEPLER'S LAWS: (1) every planet's orbit is an ellipse with the Sun at one focus; (2) a line from the Sun to a planet "
            "sweeps equal areas in equal times -- planets move fastest near the Sun; (3) the square of the orbital period is "
            "proportional to the cube of the semi-major axis: p^2 = a^3 (p in years, a in AU, for bodies orbiting the Sun). "
            "Kepler's laws + Newton's gravity let astronomers weigh planets (via moons and spacecraft) and turn an exoplanet's "
            "period into its distance. The faster inner disk material (Kepler's laws) explains why the inner solar nebula was hot.\n"
            "ESCAPE VELOCITY: Ev = sqrt(2GM/R), M in kg, R in meters (convert km!). Earth 11.2 km/s, Venus 10.4, Mars 5.0 (Table "
            "10.1). Light atoms move fastest and leak from atmospheres -- low escape velocity helps explain Mars' thin air.\n"
            "TIDAL LOCKING: one side of a body always faces the body it orbits (our Moon; Callisto; Pluto and Charon are mutually "
            "locked). Tidal friction slows spins (Venus' slow rotation may come from solar tides). A tidally locked planet has a "
            "permanent day side and night side.\n"
            "SHEPHERD MOONS: small moons whose gravity keeps ring particles confined (Saturn's Pan and Prometheus; Uranus' narrow "
            "rings). Planets in young disks act the same way, carving gaps and arcs.\n"
            "ORBITAL RESONANCE: two bodies' periods in a simple whole-number ratio, so they tug each other at the same points "
            "again and again. Neptune:Pluto = 3:2 (Pluto orbits twice for every three Neptune orbits); Io:Europa:Ganymede = "
            "1:2:4 (a Laplace resonance) -- keeps Io's orbit eccentric, powering tidal heating.\n"
            "TROJANS: bodies sharing an orbit with a larger body, 60 degrees ahead of or behind it, without colliding.\n"
            "ECLIPSES: lunar eclipse = Earth between Sun and Moon, only at full moon; types penumbral, total penumbral, partial, "
            "total (totality up to ~107 minutes). Solar eclipse = Moon between Earth and Sun, only at new moon; types total, "
            "annular (Moon looks smaller than the Sun -- a 'ring of fire'), hybrid (annular in some places, total in others), "
            "partial. Shadow parts: umbra (full shadow), penumbra (partial shadow)."
        ),
        "story": (
            "THE INVISIBLE GLUE\n\n"
            "Why does the Moon go around Earth instead of flying off into space? Why does a planet close to the Sun race around "
            "while a far one crawls? The answers come from two giants of science: Isaac Newton and Johannes Kepler.\n\n"
            "NEWTON'S THREE LAWS OF MOTION\n"
            "1. Things keep doing what they're doing. A resting object stays put and a moving object keeps moving in a straight "
            "line -- unless a force acts on it.\n"
            "2. Force = mass x acceleration (F = ma). A bigger push makes things speed up more; heavier things are harder to push.\n"
            "3. Every action has an equal and opposite reaction. A rocket pushes gas backward, so the gas pushes the rocket forward.\n\n"
            "NEWTON'S LAW OF GRAVITY\n"
            "Every bit of mass pulls on every other bit: F = G x m1 x m2 / r^2, where G = 6.67 x 10^-11 N m^2/kg^2. Two things "
            "matter: more mass means more pull, and more distance means MUCH less pull -- double the distance and the pull drops "
            "to one quarter. Gravity is mutual: Earth pulls the Moon and the Moon pulls Earth. A planet even makes its star "
            "wobble around their shared center of mass -- that's how we find exoplanets!\n\n"
            "Why doesn't the Moon fall down? It IS falling -- but it's also moving sideways so fast that it keeps missing Earth. "
            "That endless 'falling around' is an orbit.\n\n"
            "KEPLER'S THREE LAWS (worked out from Tycho Brahe's careful measurements)\n"
            "1. ELLIPSES: every planet's orbit is an ellipse (a stretched circle) with the Sun at one focus -- not in the center.\n"
            "2. EQUAL AREAS: a line from the Sun to the planet sweeps out equal areas in equal times. So a planet speeds up near "
            "the Sun and slows down far away -- like a skater pulling in her arms.\n"
            "3. p^2 = a^3: the square of a planet's year (p, in Earth years) equals the cube of its average distance (a, in AU). "
            "Try it with Mars: a = 1.52 AU, so a^3 = 3.51, and p = square root of 3.51 = 1.87 years. The table says 1.88 -- it works! "
            "Jupiter: 5.20^3 = 140.6, square root = 11.86 years. Exactly right.\n"
            "Astronomers use these laws to 'weigh' planets by watching their moons and spacecraft, and to turn an exoplanet's year "
            "into its distance from its star.\n\n"
            "ESCAPE VELOCITY\n"
            "How fast must you throw something so it never comes back? That's escape velocity: Ev = square root of (2GM/R). Watch "
            "your units -- mass in kg and radius in METERS (multiply km by 1,000). For Earth (using its well-known mass, 5.97 x "
            "10^24 kg, and radius 6,378 km), you get about 11.2 km/s -- over 40,000 km per hour! Venus needs 10.4 km/s and Mars "
            "only 5.0 km/s. Gas atoms are tiny things zooming around; on a world with low escape velocity, more of them escape, "
            "which helps explain why Mars kept only a thin atmosphere.\n\n"
            "TIDAL LOCKING\n"
            "Why do we always see the same face of the Moon? Earth's tides slowed the Moon's spin until it turned exactly once "
            "per orbit. Now one side always faces Earth -- it's TIDALLY LOCKED. Pluto and Charon are locked to EACH OTHER, like "
            "dancers holding hands. Jupiter's moon Callisto is locked too. For planets, locking matters for life: a tidally "
            "locked planet has a side of endless day and a side of endless night.\n\n"
            "ORBIT TRICKS\n"
            "• SHEPHERD MOONS: tiny moons like Saturn's Pan and Prometheus herd ring particles with their gravity, keeping ring "
            "edges sharp. Uranus' narrow rings are probably shepherded too, and young planets carve gaps in dusty disks the same way.\n"
            "• ORBITAL RESONANCE: when two orbits fit a simple ratio, the bodies tug each other at the same spots again and again, "
            "like pushing a swing at the right moment. Pluto orbits twice for every three Neptune orbits (3:2), so they never "
            "crash even though their paths cross. Io, Europa and Ganymede are in a 1:2:4 pattern called a Laplace resonance -- "
            "the regular tugs keep Io's orbit oval, which powers its volcanoes.\n"
            "• TROJANS: small bodies that share a planet's orbit, riding 60 degrees ahead of or behind it, without ever colliding.\n\n"
            "ECLIPSES -- SHADOW PLAY\n"
            "Shadows have two parts: the dark UMBRA (full shadow) and the lighter PENUMBRA (partial shadow).\n"
            "LUNAR ECLIPSE: Earth gets between the Sun and the Moon, so Earth's shadow falls on the Moon. It can only happen at FULL "
            "MOON. Types: penumbral (Moon only in the light shadow), total penumbral, partial (part of the Moon in the umbra) and "
            "total (the whole Moon in the umbra, often glowing red). Totality can last up to about 107 minutes.\n"
            "SOLAR ECLIPSE: the Moon gets between Earth and the Sun, so the Moon's shadow falls on Earth. It can only happen at NEW "
            "MOON. Types: total (the Moon covers the whole Sun), annular (the Moon is a bit farther away, looks smaller, and leaves a "
            "'ring of fire'), hybrid (annular in some places, total in others) and partial. Never look at the Sun without proper "
            "eclipse glasses!"
        ),
        "concepts": [
            {
                "term": "Newton's three laws of motion",
                "badge": ("F=ma", "Newton", BLUE),
                "analogy": "Kick a soccer ball on ice: it keeps sliding (law 1), a harder kick sends it faster (law 2), and your foot feels the kick back (law 3).",
                "explanation": "(1) An object at rest stays at rest and an object in motion stays in motion in a straight line unless acted on by an outside force (inertia). (2) F = m x a: force equals mass times acceleration, so a bigger force gives a bigger acceleration and a more massive object needs more force. (3) For every action there is an equal and opposite reaction -- a rocket pushes exhaust backward and is pushed forward. Orbits come from law 1 plus gravity: a moon would fly off in a straight line, but gravity keeps bending its path into a curve.",
                "why": "The foundation for every orbit, escape-velocity and gravity question.",
            },
            {
                "term": "Newton's law of gravitation",
                "badge": ("1/r²", "gravity", PURPLE),
                "analogy": "Gravity is like a magnet that every object has -- bigger objects have stronger 'magnets', and the pull fades fast with distance.",
                "explanation": "F = G x m1 x m2 / r^2, where G = 6.67 x 10^-11 N m^2/kg^2, m1 and m2 are the two masses (kg) and r is the distance between their centers (m). Doubling either mass doubles the force; doubling the distance cuts it to 1/4 (inverse-square). Gravity is mutual: two bodies orbit their common center of mass, which is why a planet makes its star wobble (the Doppler method). Using Kepler's laws plus Newton's gravity, astronomers measured planet masses centuries ago from their moons, and today from passing spacecraft.",
                "why": "Expect plug-in calculations -- practice scientific notation.",
            },
            {
                "term": "Kepler's first law: ellipses",
                "badge": ("ELLIPSE", "1st law", GOLD),
                "analogy": "An orbit is like a race track shaped like a slightly squashed circle, with the Sun sitting off to one side.",
                "explanation": "Every planet's orbit is an ellipse with the Sun at one focus (not the center). How stretched an ellipse is = its eccentricity: 0 is a perfect circle, closer to 1 is very stretched. The planets' orbits are nearly circular; many exoplanets and comets have highly eccentric orbits. Half the long axis of the ellipse is the semi-major axis (a), the planet's average distance -- the number used in the third law.",
                "why": "Eccentricity shows up in exoplanet and comet questions.",
            },
            {
                "term": "Kepler's second law: equal areas",
                "badge": ("=AREA", "2nd law", GOLD),
                "analogy": "A planet is like a kid on a swing: fastest at the bottom (closest to the Sun), slowest at the top (farthest away).",
                "explanation": "A line joining the Sun and a planet sweeps out equal areas in equal intervals of time. Near the Sun the line is short, so the planet must move faster to sweep the same area; far from the Sun it moves slower. So every planet speeds up at perihelion (closest point) and slows at aphelion (farthest point). The same idea explains why inner disk material moved faster than outer material in the young solar nebula.",
                "why": "Classic 'where is the planet fastest?' question.",
            },
            {
                "term": "Kepler's third law: p² = a³",
                "badge": ("p²=a³", "3rd law", GOLD),
                "analogy": "The farther out your lane on the track, the longer each lap takes -- and Kepler found the exact formula.",
                "explanation": "The square of the orbital period equals the cube of the semi-major axis: p^2 = a^3, with p in Earth years and a in AU (for bodies orbiting the Sun). Check with real data: Mars a = 1.52 AU -> a^3 = 3.51 -> p = sqrt(3.51) = 1.87 years (table: 1.88). Jupiter a = 5.20 AU -> a^3 = 140.6 -> p = 11.86 years. Neptune a = 30.06 -> p = 164.8 years. For exoplanets, the time between transits (or one Doppler wobble) gives p, and Kepler's law (with the star's mass) gives the planet's distance.",
                "why": "One of the most-calculated formulas on Solar System tests.",
            },
            {
                "term": "Escape velocity",
                "badge": ("11.2", "km/s Earth", RED),
                "analogy": "Escape velocity is how hard you'd need to throw a ball so it never falls back down.",
                "explanation": "Ev = sqrt(2GM/R), with G = 6.67 x 10^-11 N m^2/kg^2, M the planet's mass in kg and R its radius in METERS (convert km x 1,000). Earth: using its well-known mass 5.97 x 10^24 kg and radius 6.378 x 10^6 m, Ev = sqrt(2 x 6.67e-11 x 5.97e24 / 6.378e6) = about 11,200 m/s = 11.2 km/s. Table values: Earth 11.2, Venus 10.4, Mars 5.0 km/s. A low escape velocity lets fast-moving light gas atoms leak away, part of why small worlds lose their atmospheres.",
                "why": "A favorite calculation -- the unit conversion is the usual trap.",
            },
            {
                "term": "Tidal locking",
                "badge": ("LOCKED", "same face", ICE),
                "analogy": "Like dancers spinning while holding hands, a tidally locked moon always faces its partner.",
                "explanation": "Tidal locking is when one side of a body always faces the body it orbits, because tidal friction has slowed its spin until one rotation equals one orbit. Examples: our Moon (we always see the same face), Jupiter's Callisto (its 17-day day equals its 17-day orbit), and Pluto and Charon, which are mutually locked (each always shows the other the same face). Close-in exoplanets (like many hot Jupiters) may be tidally locked to their stars, with a permanent day side and night side.",
                "why": "Tidal locking affects climate and habitability of close-in planets.",
            },
            {
                "term": "Shepherd moons",
                "badge": ("HERD", "rings", PURPLE),
                "analogy": "Shepherd moons are sheepdogs keeping a flock of ring particles in a neat line.",
                "explanation": "Shepherd moons are small moons whose gravity confines a planetary ring's particles, keeping ring edges sharp. Examples: Saturn's Pan and Prometheus. Uranus' narrow, dark rings are thought to be held in place by small, mostly unseen moons. Young planets do the same thing in dusty disks around new stars, sweeping gaps and gathering dust into arcs we can see (HL Tau, Fomalhaut).",
                "why": "Links ring physics to planet detection in disks.",
            },
            {
                "term": "Orbital resonance",
                "badge": ("1:2:4", "resonance", GAS),
                "analogy": "Like pushing a swing at the same moment every time -- small regular tugs add up to a big effect.",
                "explanation": "Orbital resonance happens when two (or more) bodies' orbital periods form a simple whole-number ratio, so they line up and tug each other at the same points over and over. Neptune and Pluto are in a 3:2 resonance (Pluto orbits twice for every three Neptune orbits), which keeps them from colliding even though Pluto crosses Neptune's orbit. Jupiter's moons Io, Europa and Ganymede are in a 1:2:4 Laplace resonance; the repeated tugs keep Io's orbit slightly eccentric, which drives Io's tidal heating and volcanoes.",
                "why": "Connects orbital mechanics to tidal heating and ocean worlds.",
            },
            {
                "term": "Trojans",
                "badge": ("60°", "Trojans", ROCK),
                "analogy": "Trojans are like cars driving in the same lane as a big truck, always staying the same distance ahead or behind.",
                "explanation": "Trojans are small bodies that share an orbit with a larger body without colliding, sitting about 60 degrees ahead of or behind it. These are stable points where the gravity of the Sun and the planet balance out. Jupiter has many Trojan asteroids leading and trailing it.",
                "why": "A frequent vocabulary question alongside resonance and shepherding.",
            },
            {
                "term": "Lunar eclipses",
                "badge": ("FULL", "moon only", RED),
                "analogy": "A lunar eclipse is Earth 'photobombing' the sunlight that normally lights up the Moon.",
                "explanation": "A lunar eclipse happens when Earth passes between the Sun and the Moon, so Earth's shadow falls on the Moon. It can only happen at full moon. Earth's shadow has a dark central umbra and a lighter outer penumbra. Types: penumbral (Moon passes only through the penumbra -- subtle dimming), total penumbral (whole Moon inside the penumbra), partial (part of the Moon enters the umbra), and total (whole Moon inside the umbra, often coppery red). Totality can last up to about 107 minutes.",
                "why": "Eclipse types and conditions are classic short-answer questions.",
            },
            {
                "term": "Solar eclipses",
                "badge": ("NEW", "moon only", SUN),
                "analogy": "A solar eclipse is the Moon briefly holding its hand up in front of the Sun.",
                "explanation": "A solar eclipse happens when the Moon passes between Earth and the Sun, so the Moon's shadow falls on Earth. It can only happen at new moon. Types: total (the Moon completely covers the Sun's disk), annular (the Moon is farther from Earth, so it looks smaller than the Sun and leaves a bright 'ring of fire'), hybrid (annular in some places and total in others along the path), and partial (the Moon covers only part of the Sun). Never look at the Sun without certified eclipse glasses.",
                "why": "Know which eclipse happens at which moon phase -- a very common question.",
            },
        ],
    },
    # ------------------------------------------------------------------ 16
    {
        "name": "Solar System: Astronomers & Space Missions",
        "description": "The people who figured out the solar system -- from Aristarchus and Copernicus to Galileo, Kepler, Halley, Tombaugh and Carl Sagan -- and the spacecraft that explored it, from Mariner 2 to JWST, Europa Clipper and Dragonfly.",
        "source_title": "Source notes: Famous astronomers and missions (scioly.org Solar System wiki + OpenStax Astronomy 2e)",
        "infographics": ["astronomer_timeline", "mission_timeline"],
        "source_text": (
            "ASTRONOMERS: Aristarchus (ancient Greece) -- first proposed a Sun-centered (heliocentric) system. Nicolaus Copernicus "
            "(1473-1543) -- developed the heliocentric model. Tycho Brahe (1546-1601) -- precise planetary and stellar measurements; "
            "discovered a supernova in 1572. Galileo Galilei (1564-1642) -- improved the telescope, discovered Jupiter's four largest "
            "moons (1610), observed Venus' full set of phases (proof Venus orbits the Sun). Johannes Kepler (1571-1630) -- Tycho's "
            "assistant; laws of planetary motion. Christiaan Huygens -- discovered Titan (1655). Edmond Halley (1656-1742) -- first "
            "to calculate a comet's orbit (Halley's Comet). Uranus discovered 1781 (by William Herschel -- widely known) and Neptune "
            "in 1846 (predicted by Urbain Le Verrier, seen by Johann Galle -- widely known); Mars' moons Phobos and Deimos found 1877. "
            "Giovanni Schiaparelli (1835-1910) -- 'canali' on Mars (1877). Percival Lowell (1855-1916) -- Martian 'canals', founded "
            "Lowell Observatory (Flagstaff, 1894) where Pluto was found. Clyde Tombaugh (1906-1997) -- discovered Pluto in 1930. "
            "Carl Sagan (1934-1996) -- Venus greenhouse, Mars dust, Pioneer plaque and Voyager records, Cosmos. Michel Mayor and "
            "Didier Queloz -- first exoplanet around a Sun-like star (51 Pegasi b, 1995; Nobel Prize 2019). Stanley Miller and "
            "Harold Urey -- origin-of-life experiments (1950s).\n"
            "MISSIONS (from the wiki and source reader): Mariner 2 (1962, first Venus flyby); Venera 7 (1970, first landing that sent "
            "data from Venus); Pioneer and Voyager 1 & 2 (Voyager launched 1977; outer-planet flybys; Voyager 2 saw Triton's "
            "eruptions in 1989; Voyager 1's 'Pale Blue Dot'); Viking (Mars orbiters/landers, 'Face on Mars'); Magellan (radar map of "
            "Venus); Hubble Space Telescope (1990-); Galileo (1989-2003, Jupiter, Galilean moons); Mars Pathfinder; Mars Global "
            "Surveyor; Cassini-Huygens (1997-2017, Saturn; Huygens landed on Titan Jan 14, 2005); NEAR-Shoemaker (orbited and landed "
            "on asteroid Eros); Spirit and Opportunity (Mars 2004); Rosetta (comet 67P); New Horizons (launched 2006, Pluto flyby "
            "July 2015, then Arrokoth); Dawn (2007-2018, Vesta and Ceres); CoRoT (2007-2012); Phoenix (2008, Mars polar ice); Kepler "
            "(2009-2018); Lunar Reconnaissance Orbiter (2009-, the Moon); Juno (2011-, Jupiter); Curiosity (2012, Gale crater); "
            "BepiColombo (2018-, Mercury); TESS; Perseverance (Jezero crater) with the Ingenuity helicopter; JWST (2021-); Europa "
            "Clipper (launched Oct 2024, arrives 2030); Dragonfly (launch 2027, Titan)."
        ),
        "story": (
            "THE DETECTIVES OF THE SKY\n\n"
            "Everything you know about the solar system was figured out by curious people -- and, later, by the robots they built. "
            "Here's the story in order.\n\n"
            "PUTTING THE SUN IN THE MIDDLE\n"
            "• ARISTARCHUS (ancient Greece) was the first to suggest that Earth goes around the Sun -- a heliocentric system. Almost "
            "nobody believed him for nearly 2,000 years!\n"
            "• NICOLAUS COPERNICUS (1473-1543) developed a full Sun-centered model of the solar system.\n"
            "• TYCHO BRAHE (1546-1601) measured planet and star positions more precisely than anyone before -- without a telescope -- "
            "and spotted a new star (a supernova) in 1572.\n"
            "• JOHANNES KEPLER (1571-1630), Tycho's assistant, used Tycho's data to discover the three laws of planetary motion "
            "(ellipses, equal areas, p^2 = a^3).\n"
            "• GALILEO GALILEI (1564-1642) improved the telescope and pointed it at the sky. In 1610 he discovered Jupiter's four big "
            "moons (Io, Europa, Ganymede, Callisto -- the Galilean moons) and saw that Venus shows a full set of phases, which proved "
            "Venus orbits the Sun.\n\n"
            "FINDING NEW WORLDS\n"
            "• CHRISTIAAN HUYGENS discovered Saturn's moon Titan in 1655 -- the Huygens probe that landed on Titan is named for him.\n"
            "• EDMOND HALLEY (1656-1742) was the first to calculate a comet's orbit and predict its return -- Halley's Comet.\n"
            "• URANUS was discovered in 1781 (by William Herschel) and NEPTUNE in 1846 (predicted with math by Urbain Le Verrier and "
            "spotted by Johann Galle) -- the only planets found with telescopes.\n"
            "• Mars' tiny moons Phobos and Deimos were found in 1877, the same year GIOVANNI SCHIAPARELLI reported 'canali' on Mars.\n"
            "• PERCIVAL LOWELL built his observatory in Flagstaff, Arizona (1894), and wrongly believed Martians built canals. But his "
            "observatory found something real: in 1930 CLYDE TOMBAUGH discovered Pluto there.\n\n"
            "MODERN HEROES\n"
            "• CARL SAGAN (1934-1996) showed Venus is a runaway greenhouse, explained Mars' dust storms, put messages on the Pioneer "
            "and Voyager spacecraft, and shared science with 500 million people through his TV series Cosmos.\n"
            "• STANLEY MILLER and HAROLD UREY (1950s) made building blocks of life in a flask.\n"
            "• MICHEL MAYOR and DIDIER QUELOZ found the first planet around a Sun-like star (51 Pegasi b) in 1995 and won the 2019 "
            "Nobel Prize.\n\n"
            "ROBOT EXPLORERS -- A MISSION TOUR\n"
            "• VENUS: Mariner 2 (1962) made the first flyby; Venera 7 (1970) was the first to land and send data; Magellan mapped it "
            "with radar.\n"
            "• THE MOON: Apollo astronauts walked on it; the Lunar Reconnaissance Orbiter (2009-) maps it.\n"
            "• MARS: Viking orbiters and landers; Pathfinder; Mars Global Surveyor; rovers Spirit and Opportunity (2004), Curiosity "
            "(2012) and Perseverance, whose little helicopter Ingenuity made the first powered flight on another planet; Phoenix "
            "(2008) dug up polar ice.\n"
            "• MERCURY: BepiColombo (2018-) is on its way.\n"
            "• JUPITER: Galileo (1989-2003) toured the Galilean moons; Juno (2011-) studies the giant planet; Europa Clipper (launched "
            "October 2024) arrives in 2030.\n"
            "• SATURN: Cassini (1997-2017) studied Saturn, its rings, Titan and Enceladus' geysers; its Huygens probe landed on Titan "
            "on January 14, 2005. Dragonfly launches to Titan in 2027.\n"
            "• THE OUTER EDGE: Pioneer and Voyager 1 & 2 (launched 1977) flew past the giant planets and are leaving the solar "
            "system; Voyager 2 saw eruptions on Triton (1989) and Voyager 1 took the 'Pale Blue Dot' photo. New Horizons (launched "
            "2006) flew past Pluto in July 2015 and then visited Arrokoth.\n"
            "• SMALL BODIES: NEAR-Shoemaker orbited and landed on asteroid Eros; Dawn (2007-2018) orbited Vesta and Ceres; Rosetta "
            "visited comet 67P.\n"
            "• TELESCOPES IN SPACE: Hubble (1990-), CoRoT (2007-2012), Kepler (2009-2018), TESS, and the James Webb Space Telescope "
            "(JWST, 2021-), which studies planet-forming disks and exoplanet atmospheres in infrared."
        ),
        "concepts": [
            {
                "term": "Aristarchus and Copernicus",
                "badge": ("SUN", "in the middle", SUN),
                "analogy": "Like realizing the whole class doesn't revolve around you -- everyone revolves around the teacher's desk.",
                "explanation": "Aristarchus, in ancient Greece, was the first person known to propose a heliocentric (Sun-centered) system, with Earth orbiting the Sun. Nicolaus Copernicus (1473-1543) developed the heliocentric model in detail, putting the Sun -- not Earth -- at the center of the planets' orbits. This idea later became the Copernican principle: Earth is not in a special place in the universe.",
                "why": "Who-proposed-what history questions are common on tests.",
            },
            {
                "term": "Tycho Brahe and Johannes Kepler",
                "badge": ("DATA", "+ laws", GOLD),
                "analogy": "Tycho collected the puzzle pieces; Kepler put the puzzle together.",
                "explanation": "Tycho Brahe (1546-1601) made the most precise measurements of planet and star positions of his time, without a telescope, and discovered a supernova in 1572. Johannes Kepler (1571-1630) was Tycho's assistant; using Tycho's data he discovered the three laws of planetary motion: elliptical orbits with the Sun at a focus, equal areas in equal times, and p^2 = a^3.",
                "why": "Know which scientist goes with which discovery.",
            },
            {
                "term": "Galileo Galilei",
                "badge": ("1610", "telescope", BLUE),
                "analogy": "Galileo was the first to really 'zoom in' on the sky -- and it changed everything.",
                "explanation": "Galileo (1564-1642) improved the telescope and used it to discover Jupiter's four largest moons in 1610 -- Io, Europa, Ganymede and Callisto, now called the Galilean moons. He observed that Venus goes through a full range of phases like the Moon, which proved Venus orbits the Sun and supported Copernicus' Sun-centered model, showing Earth is not the center of the solar system.",
                "why": "Galilean moons + Venus phases are core facts.",
            },
            {
                "term": "Huygens, Halley and new planets",
                "badge": ("1781", "Uranus", ICE),
                "analogy": "Each new discovery was like finding another room in a house you thought you knew.",
                "explanation": "Christiaan Huygens discovered Saturn's largest moon Titan in 1655 (the Titan lander is named for him). Edmond Halley (1656-1742) was the first to calculate a comet's orbit and predict its return -- Halley's Comet. Uranus was discovered in 1781 (by William Herschel) and Neptune in 1846 (predicted mathematically by Urbain Le Verrier and seen by Johann Galle) -- the two planets found only after the telescope was invented. Mars' moons Phobos and Deimos were found in 1877.",
                "why": "Discovery dates are popular quick-answer questions.",
            },
            {
                "term": "Lowell, Tombaugh and Pluto",
                "badge": ("1930", "Pluto", PURPLE),
                "analogy": "Lowell went looking for Martians and his observatory found a whole new world instead.",
                "explanation": "Percival Lowell (1855-1916) built his observatory in Flagstaff, Arizona in 1894 to study the (imaginary) Martian canals, and also searched for a ninth planet. In 1930 Clyde Tombaugh (1906-1997) discovered Pluto at Lowell Observatory -- the name's first letters match Lowell's initials. Pluto is now classed as a dwarf planet and a Plutoid; New Horizons flew past it in July 2015.",
                "why": "Connects history to dwarf-planet facts.",
            },
            {
                "term": "Carl Sagan",
                "badge": ("Sagan", "1934-1996", PURPLE),
                "analogy": "Carl Sagan was astronomy's best storyteller -- like a science teacher for the whole planet.",
                "explanation": "Born in Brooklyn in 1934. He calculated that Venus' thick atmosphere acts like a giant greenhouse; showed Mars' seasonal changes were wind-blown dust, not plants; served on many mission teams; got a message plaque onto Pioneer and audio-video records onto Voyager; helped found The Planetary Society; simulated early-Earth 'primordial soup' chemistry; modeled 'nuclear winter'. Books: Cosmos, The Cosmic Connection, Pale Blue Dot, The Demon-Haunted World, the novel Contact. His TV series Cosmos reached ~500 million people in 60 countries, and he inspired Neil deGrasse Tyson.",
                "why": "His Venus greenhouse work is the root of today's runaway-greenhouse habitability story.",
            },
            {
                "term": "Inner planet missions",
                "badge": ("VENUS", "MARS", "#e0603a"),
                "analogy": "Robot explorers are our eyes and hands on worlds too dangerous for people to visit.",
                "explanation": "Venus: Mariner 2 (1962, first flyby), Venera 7 (1970, first to land and send data), Pioneer Venus, Magellan (radar mapping). Mercury: Mariner 10 imaged it; BepiColombo (2018-) is headed there. Moon: Apollo astronauts walked on it and returned soil; Lunar Reconnaissance Orbiter (2009-). Mars: Viking orbiters and landers, Pathfinder, Mars Global Surveyor, rovers Spirit and Opportunity (2004), Phoenix lander (2008, dug up polar water ice), Curiosity (2012, Gale crater) and Perseverance (Jezero crater) with the Ingenuity helicopter drone.",
                "why": "Missions-and-targets matching is a standard test section.",
            },
            {
                "term": "Outer planet missions",
                "badge": ("VOYAGER", "1977", GAS),
                "analogy": "Voyager 1 and 2 are like message-in-a-bottle explorers still sailing out of the solar system.",
                "explanation": "Pioneer and Voyager 1 & 2 (launched 1977) flew past the outer planets and carry messages for anyone who finds them; Voyager 2 saw eruptions on Triton (1989) and Voyager 1 took the 'Pale Blue Dot' image. Galileo (1989-2003) orbited Jupiter and toured the Galilean moons; Juno (2011-) orbits Jupiter. Cassini (1997-2017) orbited Saturn, found Enceladus' geysers, and carried ESA's Huygens probe, which landed on Titan on January 14, 2005. New Horizons (launched 2006) made the first Pluto flyby in July 2015, then visited Arrokoth in the Kuiper Belt. Coming up: Europa Clipper (launched Oct 2024, arrives 2030) and Dragonfly to Titan (launch 2027).",
                "why": "Current and upcoming missions tie directly to the 2027 habitability theme.",
            },
            {
                "term": "Small-body missions",
                "badge": ("EROS", "Ceres, 67P", ROCK),
                "analogy": "These missions are like geologists visiting the leftover building blocks of the planets.",
                "explanation": "NEAR-Shoemaker orbited the asteroid Eros for a year and then landed on it. Dawn (2007-2018) orbited the large asteroid Vesta and the dwarf planet Ceres. Rosetta orbited comet 67P (Churyumov-Gerasimenko), photographing gas jets, and landed a probe. Other spacecraft have landed on asteroids Itokawa, Ryugu and Bennu. New Horizons visited the Kuiper Belt object Arrokoth.",
                "why": "Asteroids and comets preserve the solar system's original ingredients.",
            },
            {
                "term": "Space telescopes",
                "badge": ("JWST", "2021", BLUE),
                "analogy": "Space telescopes are like going above the clouds of a foggy city to see the stars clearly.",
                "explanation": "Hubble Space Telescope (1990-) imaged planet-forming disks in the Orion Nebula and much more. CoRoT (2007-2012) and Kepler (2009-2018) hunted transiting exoplanets; TESS now surveys bright nearby stars. The James Webb Space Telescope (JWST, 2021-) observes in infrared: it found molecules like benzene and acetic acid in planet-forming disks, imaged Fomalhaut's three dust belts, and studies exoplanet atmospheres. Telescopes in space avoid the blurring of Earth's atmosphere.",
                "why": "JWST, Kepler and TESS are central to 'habitability beyond the Solar System'.",
            },
        ],
    },
]
