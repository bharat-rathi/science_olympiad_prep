"""Unit 3 -- Giant Planets & Small Bodies: the four giants with their moons
and rings (including the wiki's moon tables), the ocean worlds, and the
dwarf planets, asteroids, comets and meteors. Same lesson-chapter format as
lessons_unit1.py.
"""

from app.content.solar_system.svg import BLUE, GAS, GOLD, GREEN, ICE, PURPLE, RED, ROCK

UNIT3 = [
    # ------------------------------------------------------------------ 9
    {
        "unit": 3,
        "name": "Solar System: Giant Planets, Their Moons & Rings",
        "description": "Jupiter, Saturn, Uranus and Neptune up close; regular vs. irregular moons; every major moon with its discoverer (from the wiki tables); rings; the four Galilean moons -- Callisto, Ganymede, Europa and Io -- and the tidal heating that powers them.",
        "goals": [
            "Describe each giant planet and its ring and moon system.",
            "Tell regular moons from irregular (captured) moons.",
            "Name the big moons of each planet and who discovered them.",
            "Compare the four Galilean moons and explain tidal heating.",
        ],
        "sections": [
            {
                "heading": "The four giants",
                "body": (
                    "The giant (Jovian) planets have no solid surface. Fly down into one and the gas just gets thicker, "
                    "hotter and more squeezed until it acts like a liquid, with a small, dense core deep inside.\n\n"
                    "• JUPITER (5.2 AU) is the largest planet -- 142,984 km across, more massive than all the other planets "
                    "combined. A Jupiter day is only about 10 hours, the shortest of any planet. Its cloud stripes hide giant "
                    "storms; the GREAT RED SPOT is a storm bigger than Earth. Deep inside, hydrogen is squeezed so hard it "
                    "becomes a liquid metal, which makes Jupiter's enormous magnetic field.\n"
                    "• SATURN (9.54 AU) is famous for its bright rings. With a density of only 0.7 g/cm3, it is the least "
                    "dense planet -- it would float in water.\n"
                    "• URANUS (19.18 AU) was discovered by William Herschel on March 13, 1781 -- the first planet found with "
                    "a telescope. It is tipped over by 98 degrees, so it rolls around the Sun on its side; its rings and moons "
                    "are tipped along with it. Uranus and Neptune are often called ICE GIANTS because they contain lots of "
                    "water, ammonia and methane 'ices'; methane gas gives them their blue-green color.\n"
                    "• NEPTUNE (30.06 AU) was discovered on September 23, 1846, after mathematicians predicted where it "
                    "should be from the way it tugged on Uranus. It has the fastest winds in the Solar System. Its year lasts "
                    "164.8 Earth years.\n\n"
                    "Each giant is like the center of its own mini solar system, with dozens of moons and a set of rings. "
                    "Because they formed out where it is cold, the moons and rings contain lots of water ice -- often mixed "
                    "with dark, carbon-rich (ORGANIC) material, so many are both icy AND dark."
                ),
            },
            {
                "heading": "Regular and irregular moons",
                "body": (
                    "Moons come in two kinds:\n\n"
                    "• REGULAR moons (about a quarter of them) orbit 'politely': in the same direction the planet spins, "
                    "close to the planet, in the plane of its equator. They probably formed together with the planet, from a "
                    "disk around it.\n"
                    "• IRREGULAR moons (the majority) orbit BACKWARD (retrograde), or on very stretched (ECCENTRIC) or tilted "
                    "(INCLINED) orbits, usually far from the planet. They were probably wandering objects that the planet's "
                    "gravity captured.\n\n"
                    "Moon counts keep climbing as telescopes find tiny new ones, so different sources disagree. The reader's "
                    "newest numbers: Jupiter 97, Saturn at least 274 (128 small ones announced in early 2025!), Uranus 29, "
                    "Neptune 16. The older scioly.org wiki lists Jupiter 79, Saturn 60 and Uranus 27. Know both -- and that "
                    "the number keeps growing. In all, about 430 moons are known around planets and dwarf planets. Only "
                    "Mercury and Venus have none."
                ),
            },
            {
                "heading": "Moon roll call (from the wiki tables)",
                "body": (
                    "• EARTH: the Moon -- 384,400 km away, 3,476 km across, orbits in 27.322 days.\n"
                    "• MARS: Phobos (9,270 km from Mars, 28 x 23 x 20 km, orbit 0.319 days) and Deimos (23,460 km, 16 x 12 x "
                    "10 km, 1.263 days) -- both discovered by Asaph Hall in 1877. They are lumpy, probably captured asteroids.\n"
                    "• JUPITER: the four GALILEAN MOONS, discovered by Galileo in 1610 -- Io (orbit 1.769 days), Europa "
                    "(3.551 days), Ganymede (7.155 days) and Callisto (16.689 days).\n"
                    "• SATURN: Titan (discovered by Christiaan Huygens in 1655; 5,150 km across; 15.945-day orbit) is the "
                    "giant. Others: Iapetus (1671), Rhea (1672), Tethys and Dione (1684) -- all found by Giovanni Cassini; "
                    "Mimas and Enceladus (1789, William Herschel); Hyperion (1848, Bond); Phoebe (1898, Pickering -- it orbits "
                    "backward); Atlas (1980, R. Terrile).\n"
                    "• URANUS: the five major moons are Miranda (1948, Gerard Kuiper), Ariel and Umbriel (1851, William "
                    "Lassell), and Titania and Oberon (1787, William Herschel). Most Uranus moons are named after characters "
                    "from Shakespeare.\n"
                    "• NEPTUNE: Triton (1846, William Lassell -- just weeks after Neptune itself) is big and orbits BACKWARD. "
                    "Nereid was found in 1949 by Gerard Kuiper; Voyager 2 found six more in 1989 (Naiad, Thalassa, Despina, "
                    "Galatea, Larissa, Proteus), and the tiny Hippocamp was found in 2013.\n"
                    "• PLUTO (a dwarf planet): Charon (1978, James Christy) plus four small moons -- Nix and Hydra (2005), "
                    "Kerberos (2011) and Styx (2012)."
                ),
                "infographic": "moon_census",
            },
            {
                "heading": "Rings",
                "body": (
                    "All four giants have rings, made of countless separate pieces each orbiting the planet like a tiny "
                    "moon. They circle the planet's equator.\n\n"
                    "• SATURN'S rings are by far the brightest: broad and flat, with gaps, made mostly of water-ice chunks the "
                    "size of ping-pong balls, tennis balls and basketballs, swirling around like a traffic jam. They are huge "
                    "but extremely thin.\n"
                    "• URANUS' 11 rings (discovered in 1977) are narrow ribbons of dark material with wide gaps between them.\n"
                    "• JUPITER has a faint ring, and NEPTUNE has narrow, faint, dark rings.\n\n"
                    "Small SHEPHERD MOONS use their gravity to keep ring particles in tight bands, like sheepdogs herding a "
                    "flock (see 'Orbit Tricks & Eclipses')."
                ),
            },
            {
                "heading": "Meet the Galilean moons",
                "body": (
                    "Jupiter's four big moons were explored by the Galileo spacecraft (in orbit 1995-2003) and more recently "
                    "by Juno. From Jupiter outward, remember 'I Eat Green Carrots': Io, Europa, Ganymede, Callisto. Io and "
                    "Europa are about the size of our Moon; Ganymede and Callisto are about the size of Mercury.\n\n"
                    "Their numbers (diameter / density / how much sunlight they reflect, called ALBEDO):\n"
                    "• Our Moon (for comparison): 3,476 km / 3.3 / 12%\n"
                    "• Io: 3,640 km / 3.5 / 60%\n"
                    "• Europa: 3,130 km / 3.0 / 70%\n"
                    "• Ganymede: 5,270 km / 1.9 / 40%\n"
                    "• Callisto: 4,820 km / 1.8 / 20%\n\n"
                    "Notice the pattern: Io and Europa (close in) are dense and rocky; Ganymede and Callisto (farther out) "
                    "have low densities, so they are about half ice. It is the Solar System's rocky-inside, icy-outside "
                    "pattern in miniature -- the inner part of Jupiter's disk was warmer."
                ),
                "infographic": "galilean_moons",
            },
            {
                "heading": "Callisto and Ganymede",
                "body": (
                    "CALLISTO, the outermost, is about 2 million km from Jupiter and orbits in 17 days. It is TIDALLY LOCKED: "
                    "its day equals its month, so one face always points at Jupiter. At noon it is only 130 K (-143 C), so ice "
                    "never melts or evaporates. It is almost Mercury's size but has only a third of its mass, so it must be "
                    "icy inside. Surprisingly, Callisto never fully separated into layers -- it froze before it could finish "
                    "differentiating. Its surface is crowded with craters, and it has been geologically dead for more than 4 "
                    "billion years. Ice that cold is as hard as rock; close-ups show 80-100 m icy spires slowly crumbling as "
                    "dark dust slides downhill.\n\n"
                    "GANYMEDE is the largest moon in the Solar System -- bigger than the planet Mercury. About a quarter of its "
                    "surface is old and cratered; the rest is younger, cut by long ridges and grooves where the icy crust "
                    "cracked, flooded and was squeezed (some craters were even split apart). On Ganymede, darker means older "
                    "and lighter means younger -- the reverse of our Moon. Unlike Callisto, Ganymede IS layered: a rocky core "
                    "about the size of our Moon under an icy mantle and crust. It even has its own magnetic field, a sign of a "
                    "partly melted interior, and very likely a layer of liquid salty water deep inside. Why is it so different "
                    "from Callisto? Probably because it is closer to Jupiter and has been heated by tides."
                ),
            },
            {
                "heading": "Tidal heating -- and Io, the volcano moon",
                "body": (
                    "A TIDAL FORCE happens because gravity pulls harder on the near side of an object than on the far side, "
                    "stretching it. Jupiter's moons are caught in a gravity 'dance' with Jupiter and with each other that keeps "
                    "squeezing and relaxing their insides. Bend a paper clip back and forth quickly and it gets warm; flexing a "
                    "moon makes heat the same way. This is TIDAL HEATING, and the closer a moon is to Jupiter, the stronger it "
                    "is.\n\n"
                    "IO is our Moon's near-twin in size and density, yet it is the most volcanic world in the Solar System. "
                    "Voyager 1 saw 8 volcanoes erupting in March 1979, and 6 were still going when Voyager 2 passed four months "
                    "later. Galileo found more than 50 eruptions in 1997 alone, more than 100 recently active volcanoes, and "
                    "PLUMES (fountains of gas and dust) hundreds of km high. The lava is hot molten rock like Earth's, but when "
                    "it hits frozen sulfur and sulfur dioxide, giant plumes shoot up and colorful sulfur 'snow' falls up to "
                    "1,000 km away -- orange is sulfur, white is sulfur dioxide. (Carl Sagan joked that Io looks like it needs "
                    "a shot of penicillin.)\n\n"
                    "Why so hot? Io is about as far from Jupiter as our Moon is from Earth, but Jupiter is more than 300 times "
                    "as massive as Earth, so it stretches Io into a slight egg shape with a bulge several km high. Europa and "
                    "Ganymede keep tugging Io's orbit into a slight oval (they are in a 1:2:4 orbital resonance), so Io moves "
                    "nearer and farther and gets flexed over and over -- like a wire coat hanger bent back and forth. Over "
                    "billions of years this melted Io's insides and drove away its water.\n\n"
                    "THE BIG PATTERN: going inward from Callisto to Io, the moons get rockier, hotter and more active. Just as "
                    "a planet's character depends on its distance from the Sun, a moon's character depends on its distance "
                    "from its giant planet. Europa, between Io and Ganymede, gets just enough heating to keep a hidden ocean "
                    "liquid -- the star of the next chapter."
                ),
                "infographic": "tidal_heating",
            },
        ],
        "word_bank": [
            ("Jovian planet", "A giant planet made mostly of gas, liquid and ice: Jupiter, Saturn, Uranus, Neptune."),
            ("Ice giant", "Uranus or Neptune -- giant planets with lots of water, ammonia and methane 'ices' inside."),
            ("Great Red Spot", "A giant storm on Jupiter, bigger than Earth, that has lasted hundreds of years."),
            ("Metallic hydrogen", "Hydrogen squeezed so hard deep inside Jupiter and Saturn that it acts like a liquid metal."),
            ("Organic", "Containing carbon-based molecules (not necessarily alive)."),
            ("Regular moon", "A moon that orbits in the same direction as its planet spins, close in and near its equator."),
            ("Irregular moon", "A moon on a backward, stretched or tilted orbit far from its planet -- probably captured."),
            ("Eccentric orbit", "An orbit that is stretched out into a long oval instead of a circle."),
            ("Inclined orbit", "An orbit tilted compared with the planet's equator or the Solar System's plane."),
            ("Galilean moons", "Jupiter's four largest moons -- Io, Europa, Ganymede, Callisto -- discovered by Galileo in 1610."),
            ("Albedo", "How much sunlight a surface reflects. Fresh ice has a high albedo; dark rock a low one."),
            ("Tidal force", "The stretching effect caused because gravity pulls harder on the near side of an object than the far side."),
            ("Tidal heating", "Heat made inside a moon as tidal forces keep flexing it."),
            ("Tidally locked", "Spinning exactly once per orbit, so the same side always faces the planet."),
            ("Plume", "A tall fountain of gas, dust or ice shooting out of a world."),
            ("Orbital resonance", "When orbit times form a simple ratio (like 1:2:4), so bodies line up and tug each other regularly."),
            ("Shepherd moon", "A small moon whose gravity keeps ring particles in a narrow band."),
            ("Ring", "A flat band of countless small pieces of ice and rock orbiting a planet's equator."),
        ],
        "key_facts": [
            "Jupiter: 5.2 AU, 142,984 km, ~10-hour day, Great Red Spot. Saturn: 9.54 AU, density 0.7 (would float).",
            "Uranus: 19.18 AU, tilted 98 degrees, discovered March 13, 1781 (Herschel). Neptune: 30.06 AU, discovered Sept 23, 1846.",
            "Moon counts (reader): Jupiter 97, Saturn 274+, Uranus 29, Neptune 16. Older wiki: 79, 60, 27.",
            "Phobos and Deimos: 1877, A. Hall. Galilean moons: 1610, Galileo. Titan: 1655, Huygens. Triton: 1846, Lassell (retrograde).",
            "Uranus' 5 major moons: Miranda, Ariel, Umbriel, Titania, Oberon. Charon: 1978, J. Christy.",
            "Galilean moons (in to out): Io 3,640 km/3.5; Europa 3,130/3.0; Ganymede 5,270/1.9 (largest moon); Callisto 4,820/1.8.",
            "Io: >100 active volcanoes; Io-Europa-Ganymede 1:2:4 resonance keeps its orbit oval -> tidal heating.",
        ],
        "quick_check": [
            ("What is the difference between a regular and an irregular moon?", "Regular moons orbit close in, forward, near the equator (formed with the planet); irregular moons are far out on backward, stretched or tilted orbits (captured)."),
            ("Which is the largest moon in the Solar System?", "Ganymede (5,270 km across), Jupiter's moon -- bigger than Mercury."),
            ("Why are Io and Europa rocky but Ganymede and Callisto icy?", "The inner part of Jupiter's disk was warmer, so ice couldn't collect there -- the same pattern as the planets around the Sun."),
            ("Why is Io so volcanic?", "Tidal heating: Jupiter's huge gravity flexes Io, and Europa and Ganymede keep its orbit oval so the flexing never stops."),
            ("Who discovered Titan, and when?", "Christiaan Huygens, in 1655."),
            ("Why is Uranus unusual?", "It is tipped over by 98 degrees, so it spins on its side, and its rings and moons are tipped too."),
        ],
        "cards": [
            {
                "term": "The four giants",
                "badge": ("J S U N", "giants", GAS),
                "analogy": "Each giant is the 'sun' of its own mini solar system of moons and rings.",
                "explanation": "Jupiter (largest, 10-hour day, Great Red Spot), Saturn (bright rings, density 0.7), Uranus (tipped 98 degrees, found 1781), Neptune (fastest winds, found 1846 by prediction). No solid surfaces.",
                "why": "Giant planets fail as habitats but their moons are top targets for life.",
            },
            {
                "term": "Regular vs. irregular moons",
                "badge": ("2 KINDS", "of moons", "#a39e93"),
                "analogy": "Regular moons walk in line with the class; irregular moons wandered in from another school.",
                "explanation": "About a quarter are regular (forward, close, near the equator). Most are irregular (backward, stretched or tilted orbits, far out) and were probably captured.",
                "why": "Captured moons like Triton show bodies can move between systems.",
            },
            {
                "term": "Moon discoverers",
                "badge": ("WHO?", "found it", GOLD),
                "analogy": "Like a 'who found it first' leaderboard for moons.",
                "explanation": "Galileo 1610 (Io, Europa, Ganymede, Callisto); Huygens 1655 (Titan); Cassini 1671-1684 (Iapetus, Rhea, Tethys, Dione); Herschel 1787-1789 (Titania, Oberon, Mimas, Enceladus); Lassell 1846-1851 (Triton, Ariel, Umbriel); Hall 1877 (Phobos, Deimos); Kuiper (Miranda 1948, Nereid 1949); Christy 1978 (Charon).",
                "why": "Discovery questions come straight from the wiki tables.",
            },
            {
                "term": "Rings",
                "badge": ("RINGS", "all 4", ICE),
                "analogy": "A highway jammed with ice cubes from ping-pong-ball to basketball size.",
                "explanation": "All four giants have rings of countless orbiting pieces. Saturn's are bright water ice; Uranus' 11 rings (found 1977) are narrow and dark; Jupiter's and Neptune's are faint. Shepherd moons keep edges sharp.",
                "why": "Rings and shepherd moons show how gravity sculpts disks -- like planet-forming disks.",
            },
            {
                "term": "Galilean moons data",
                "badge": ("I-E-G-C", "in order", GOLD),
                "analogy": "From Jupiter outward: 'I Eat Green Carrots'.",
                "explanation": "Io 3,640 km / density 3.5; Europa 3,130 / 3.0; Ganymede 5,270 / 1.9; Callisto 4,820 / 1.8. Rocky inside, icy outside -- Jupiter's inner disk was warmer.",
                "why": "Density and order questions are very common.",
            },
            {
                "term": "Callisto",
                "badge": ("dead", "4 Gyr", "#6d6459"),
                "analogy": "A frozen time capsule -- nothing has changed for over 4 billion years.",
                "explanation": "Outermost Galilean moon, 17-day orbit, tidally locked, 130 K at noon. Icy, never fully layered (froze too soon), covered in craters, geologically dead.",
                "why": "The baseline: weakest tidal heating = no activity.",
            },
            {
                "term": "Ganymede",
                "badge": ("5,270", "km", "#a39e93"),
                "analogy": "The king of moons -- bigger than Mercury, with its own magnetic shield.",
                "explanation": "Largest moon in the Solar System. Old dark cratered areas plus younger grooved terrain; layered (rock core, ice mantle); has a magnetic field and very likely a hidden salty ocean.",
                "why": "One of the 'ocean worlds'.",
            },
            {
                "term": "Tidal heating & Io",
                "badge": ("FLEX", "= heat", RED),
                "analogy": "Bend a paper clip back and forth fast and it gets warm.",
                "explanation": "Jupiter's gravity flexes its moons; Europa and Ganymede keep Io's orbit oval (1:2:4 resonance), so Io is constantly kneaded: 100+ volcanoes, sulfur plumes hundreds of km high. Activity increases from Callisto inward to Io.",
                "why": "Tidal heating lets oceans exist far from the Sun's warmth.",
            },
        ],
    },
    # ------------------------------------------------------------------ 10
    {
        "unit": 3,
        "name": "Solar System: Ocean Worlds -- Europa, Enceladus, Titan & Triton",
        "description": "Moons with hidden oceans and strange weather: Europa's ice shell and chemical 'battery', Enceladus' geysers, Titan's methane rain and lakes (Huygens and Dragonfly), Triton's backward orbit, and ice volcanoes.",
        "goals": [
            "Explain how tidal heating keeps oceans liquid far from the Sun.",
            "Give the evidence for oceans on Europa and Enceladus.",
            "Describe Titan's atmosphere and methane cycle, and its missions.",
            "Tell Titan from Triton, and explain 'life as we don't know it'.",
        ],
        "sections": [
            {
                "heading": "Far from the Sun, but not dead",
                "body": (
                    "Scientists once expected the moons of the outer Solar System, getting only a trickle of sunlight, to be "
                    "frozen, 'geologically dead' balls. Spacecraft proved them wrong. Tidal heating -- the squeezing by their "
                    "giant planets -- keeps the insides of some moons warm enough for liquid water. Six or more icy moons may "
                    "have hidden OCEANS under their ice. These OCEAN WORLDS are among the best places to search for life, "
                    "because life as we know it needs liquid water.\n\n"
                    "Earth and Europa both have large oceans (Europa's is under thick ice), Enceladus sprays its ocean into "
                    "space, Ganymede very likely has one, and Titan may hide one deep inside."
                ),
                "infographic": "ocean_worlds",
            },
            {
                "heading": "Europa: the ocean under the ice",
                "body": (
                    "Europa is mostly rock (density 3.0) but wrapped in a shell of ice. Its icy surface has very few craters, "
                    "so it is young -- no more than a few million years old in places. Europa erases craters faster than Earth "
                    "does!\n\n"
                    "The smooth ice is crisscrossed by cracks and ridges thousands of km long, often in doubled or tripled "
                    "lines like a freeway. In regions like Conamara Chaos, blocks of ice look like icebergs that drifted, "
                    "rotated and froze in place again. Unlike Lowell's fake Martian canals, Europa's lines are real: they are "
                    "the kind of cracks that form when an ice shell floats on liquid water.\n\n"
                    "More evidence: as Europa moves through Jupiter's magnetic field, it creates a small magnetic field of its "
                    "own (an INDUCED magnetic field), and its 'signature' matches a SALTY LIQUID OCEAN -- salty water conducts "
                    "electricity. The ocean may be tens of kilometers to perhaps 100 km deep, holding more water than all of "
                    "Earth's oceans. The ice shell might be about 1 to 20 km thick (2024 Juno data suggest it could be twice "
                    "that). Tidal heating keeps the ocean liquid, and there could even be warm springs on the seafloor.\n\n"
                    "NASA's EUROPA CLIPPER launched in October 2024 and arrives at Jupiter in 2030. It will not orbit Europa, "
                    "because Jupiter's intense radiation would fry its electronics; instead it makes many quick, close "
                    "flybys. Its job: study the ocean and ice shell, and find places where ocean material has reached the "
                    "surface."
                ),
            },
            {
                "heading": "Europa's chemical battery",
                "body": (
                    "Water alone isn't enough for life -- life also needs ENERGY. Sunlight can't reach through kilometers of "
                    "ice, so any life in Europa's ocean would need CHEMICAL energy. Think of a flashlight battery, which needs "
                    "a plus end and a minus end:\n\n"
                    "• One end: water reacting with hot rock on the seafloor (as at Earth's HYDROTHERMAL VENTS -- underwater "
                    "hot springs) makes REDUCING chemicals: molecules that easily give away tiny particles called ELECTRONS.\n"
                    "• The other end: OXIDIZING chemicals -- molecules that easily accept electrons. The Galileo mission found "
                    "plenty of oxidizers on Europa's icy surface, made by radiation.\n\n"
                    "Connect the two and energy flows, like closing a circuit. On Earth, when hot vent fluids meet oxygen-rich "
                    "seawater, the energy released feeds whole communities of tube worms, clams and microbes in total "
                    "darkness. So a big question for Europa is whether surface chemicals can mix down through the ice into "
                    "the ocean. Its young, active surface makes that possible. Many scientists think Europa is the most likely "
                    "place beyond Earth to find life."
                ),
            },
            {
                "heading": "Enceladus: the geyser moon",
                "body": (
                    "Enceladus is a small moon of Saturn, only about 500 km across (discovered by William Herschel in 1789). "
                    "In 2005 the Cassini spacecraft discovered PLUMES -- geysers of water vapor and ice grains -- spraying from "
                    "cracks near its south pole, about 250 kg of material every second.\n\n"
                    "The ice grains contain SALTS, a strong sign that they come from a liquid-water ocean under tens of "
                    "kilometers of ice. That ocean seems to touch and react with a rocky core -- something life would "
                    "probably need (though it is not enough by itself). Saturn's tides probably supply the heat.\n\n"
                    "Best of all, the plumes deliver free ocean samples into space. A spacecraft just has to fly through them "
                    "to test whether Enceladus' ocean is habitable -- or even inhabited. Enceladus may have the most "
                    "accessible liquid water in the Solar System."
                ),
            },
            {
                "heading": "Titan: a strange copy of Earth",
                "body": (
                    "Titan, Saturn's largest moon (5,150 km across, density 1.9, discovered by Huygens in 1655), is the ONLY "
                    "moon with a thick atmosphere. Its air is mostly nitrogen -- like ours -- plus about 5% METHANE (the gas in "
                    "natural gas stoves). It is actually thicker than Earth's air at the surface.\n\n"
                    "High up, ultraviolet sunlight breaks nitrogen and methane apart, and the pieces recombine into complex "
                    "carbon-rich (organic) compounds called THOLINS, plus molecules like hydrogen cyanide, cyanogen and "
                    "cyanoacetylene. Tholins wrap Titan in a thick orange HAZE (smog), and heavier particles drift down and "
                    "pile into dunes. Titan is a natural chemistry lab, maybe a bit like early Earth before life.\n\n"
                    "Why nitrogen? Titan formed with plenty of ammonia, methane and nitrogen, and it is far too cold (94 K, "
                    "-179 C) for carbon dioxide or water to stay as gas -- so nitrogen ended up as the main ingredient."
                ),
            },
            {
                "heading": "Methane rain, Huygens and Dragonfly",
                "body": (
                    "Titan has a 'water cycle' -- but with methane. Methane evaporates from big lakes near the poles, forms "
                    "clouds, falls as rain, and flows down river valleys back into lakes and seas of liquid methane and "
                    "ETHANE. Cassini's radar saw the lakes through the haze, and sunlight 'glinting' off a perfectly flat "
                    "surface proved they are liquid. Titan is the only world besides Earth known to have stable liquid on its "
                    "surface.\n\n"
                    "THE HUYGENS LANDING. NASA's Cassini spacecraft (at Saturn 2004-2017) carried a passenger built by the "
                    "European Space Agency: the HUYGENS probe. On January 14, 2005, Huygens parachuted through the haze and "
                    "landed -- the first and only landing on a moon in the outer Solar System. It found a flat plain strewn "
                    "with 'boulders' of water ice, as hard as rock at 94 K. The sky was deep orange and sunlight 1,000 times "
                    "dimmer than on Earth (but still 100 times brighter than full moonlight). Photos from its descent showed "
                    "drainage channels, so Huygens seemed to sit on the shore of an old lake. It sent data for about 90 "
                    "minutes before the cold won.\n\n"
                    "DRAGONFLY. NASA's Dragonfly, a nuclear-powered drone with rotors, is planned to launch in 2027. It will fly "
                    "from place to place in Titan's thick air and low gravity, studying the PREBIOTIC CHEMISTRY -- the chemistry "
                    "that might come before life. Balloons and even a boat for Titan's lakes have also been proposed."
                ),
                "infographic": "titan_cycle",
            },
            {
                "heading": "Life as we don't know it?",
                "body": (
                    "Titan is far too cold for liquid water at its surface, and too cold for most of the chemistry our kind of "
                    "life uses. But what if a totally different kind of carbon-based life could use liquid methane the way we "
                    "use water? This idea is called 'LIFE AS WE DON'T KNOW IT'. Finding it would be even more amazing than "
                    "finding life like ours on Mars, because it would show life can work in more than one way. Titan may be "
                    "the best place in the Solar System to look for it -- and it may also hide a liquid-water ocean deep "
                    "inside."
                ),
            },
            {
                "heading": "Triton and ice volcanoes",
                "body": (
                    "Don't mix up TITAN (Saturn) with TRITON (Neptune)! Triton is Neptune's largest moon: 2,720 km across "
                    "with a density of 2.1 g/cm3, so it is roughly 75% rock and 25% water ice. It reflects about 80% of "
                    "sunlight and has the coldest surface of any world our spacecraft have visited. It orbits Neptune "
                    "BACKWARD (retrograde) -- very unusual for a big moon -- and has a thin atmosphere. Voyager 2 saw active "
                    "eruptions there in 1989. Triton was probably a dwarf planet, like Pluto, that Neptune captured.\n\n"
                    "Outer Solar System worlds show CRYOVOLCANISM ('cold volcanoes'): instead of melted rock, they erupt water "
                    "and other ices -- think Enceladus' plumes and Triton's geysers. Io is in between, with sulfur compounds "
                    "mixed with its hot lava."
                ),
            },
        ],
        "word_bank": [
            ("Ocean world", "A world with a large body of liquid water, often hidden under ice."),
            ("Subsurface ocean", "An ocean hidden beneath a layer of ice or rock."),
            ("Induced magnetic field", "A magnetic field created in a moon when it moves through a planet's magnetic field; salty water makes a strong one."),
            ("Electron", "A tiny particle with a negative charge that zips around atoms. Moving electrons carry energy."),
            ("Reducing chemicals", "Chemicals that easily give away electrons -- one 'end' of a chemical battery."),
            ("Oxidizing chemicals", "Chemicals that easily grab electrons, like oxygen -- the other 'end' of a chemical battery."),
            ("Hydrothermal vent", "A hot spring on the seafloor where heated, mineral-rich water gushes out."),
            ("Geyser", "A fountain of water and steam that shoots up from underground."),
            ("Methane", "A gas made of carbon and hydrogen (CH4). On Titan it is liquid and falls as rain."),
            ("Ethane", "A hydrocarbon similar to methane; Titan's lakes contain both."),
            ("Hydrocarbon", "A molecule made only of hydrogen and carbon atoms, like methane."),
            ("Tholins", "Orange-brown carbon-rich gunk made when sunlight breaks up and rebuilds molecules in Titan's air."),
            ("Haze", "A thin layer of smog or tiny particles in the air."),
            ("Prebiotic chemistry", "Chemistry that builds the ingredients of life, before life itself exists."),
            ("Probe", "A spacecraft sent into a planet's or moon's atmosphere or onto its surface to take measurements."),
            ("Life as we don't know it", "Possible life using a different liquid than water (like methane on Titan) or different chemistry."),
            ("Cryovolcanism", "'Cold volcanoes' that erupt water, ammonia or other ices instead of molten rock."),
        ],
        "key_facts": [
            "Six or more icy moons may have liquid oceans, kept warm by tidal heating.",
            "Europa: few craters (surface a few million years old), induced magnetic field = salty ocean; ice shell ~1-20 km; Europa Clipper launched Oct 2024, arrives 2030 (flybys).",
            "Enceladus: ~500 km; Cassini (2005) found south-polar plumes ~250 kg/s with salts -> ocean.",
            "Titan: 5,150 km; nitrogen + ~5% methane; tholin haze; methane/ethane lakes and rain; 94 K (-179 C).",
            "Huygens landed on Titan January 14, 2005 -- the only landing in the outer Solar System; worked ~90 minutes.",
            "Dragonfly: drone to Titan, launch 2027, prebiotic chemistry.",
            "Triton: 2,720 km, density 2.1, retrograde orbit, coldest surface visited, Voyager 2 eruptions 1989, probably captured.",
        ],
        "quick_check": [
            ("How can moons so far from the Sun have liquid water?", "Tidal heating: the giant planet's gravity keeps flexing them, making heat inside."),
            ("Give two pieces of evidence for Europa's ocean.", "Its young surface with cracks like floating ice, and its induced magnetic field, which matches a salty liquid layer."),
            ("Why doesn't Europa Clipper orbit Europa?", "Jupiter's radiation is so intense it would destroy the electronics, so Clipper makes quick flybys instead."),
            ("Why is Enceladus such an easy place to sample an ocean?", "Its plumes spray ocean material into space -- a spacecraft can just fly through them."),
            ("What falls as rain on Titan?", "Liquid methane (with ethane), forming rivers and lakes."),
            ("Titan vs. Triton: which orbits Neptune, and which has a thick atmosphere?", "Triton orbits Neptune (backward); Titan orbits Saturn and has the thick nitrogen atmosphere."),
        ],
        "cards": [
            {
                "term": "Ocean worlds",
                "badge": ("6+", "icy moons", BLUE),
                "analogy": "Snow globes turned inside out -- liquid water sealed under a shell of ice.",
                "explanation": "Tidal heating keeps water liquid inside six or more icy moons. Europa and Enceladus are the top targets; Ganymede and Titan likely have deep oceans too.",
                "why": "Tidal heating extends habitability far beyond the Sun's habitable zone.",
            },
            {
                "term": "Europa's ocean",
                "badge": ("OCEAN", "under ice", "#e8e2d0"),
                "analogy": "A frozen pond with a thick lid -- but the pond is a whole global ocean.",
                "explanation": "Few craters, long cracks and ridges, Conamara Chaos 'icebergs', and an induced magnetic field all point to a salty ocean under ~1-20 km of ice. Europa Clipper arrives 2030.",
                "why": "Many scientists' #1 place to find life beyond Earth.",
            },
            {
                "term": "Europa's chemical battery",
                "badge": ("+ / −", "energy", GOLD),
                "analogy": "Life in a dark ocean runs like a flashlight battery: it needs a + end and a − end.",
                "explanation": "Seafloor rock-water reactions (like Earth's hydrothermal vents) make reducing chemicals; radiation makes oxidizers on the surface. If they mix, chemical energy could feed life.",
                "why": "Habitable = water + energy + raw materials.",
            },
            {
                "term": "Enceladus' plumes",
                "badge": ("250", "kg/s", ICE),
                "analogy": "A tiny moon with a cracked shell spraying ocean water like a shaken soda bottle.",
                "explanation": "~500 km moon of Saturn. Cassini (2005) found plumes of vapor and salty ice (~250 kg/s) from a hidden ocean touching rock. Flying through them samples the ocean.",
                "why": "Maybe the most accessible liquid water in the Solar System.",
            },
            {
                "term": "Titan",
                "badge": ("N₂", "+5% CH₄", GAS),
                "analogy": "A smoggy orange world where it rains natural gas.",
                "explanation": "Only moon with a thick atmosphere (nitrogen + ~5% methane). Tholin haze, methane rain, rivers and lakes of methane and ethane. 94 K.",
                "why": "A natural lab for prebiotic chemistry and 'life as we don't know it'.",
            },
            {
                "term": "Huygens & Dragonfly",
                "badge": ("2005", "Jan 14", BLUE),
                "analogy": "A parachuting robot landing on an icy beach, and a robot dragonfly to follow.",
                "explanation": "Huygens (carried by Cassini) landed on Titan January 14, 2005 -- the only outer Solar System landing -- and found ice 'boulders' under an orange sky. Dragonfly, a drone, launches in 2027.",
                "why": "Mission dates are favorite test questions.",
            },
            {
                "term": "Triton",
                "badge": ("2,720", "km", "#9fd6e8"),
                "analogy": "A runaway that Neptune caught -- it still orbits the 'wrong way'.",
                "explanation": "Neptune's largest moon: retrograde orbit, coldest surface visited, thin air, eruptions seen by Voyager 2 in 1989; probably a captured dwarf planet. Don't confuse it with Titan!",
                "why": "The classic Titan-vs-Triton mix-up question.",
            },
        ],
    },
    # ------------------------------------------------------------------ 11
    {
        "unit": 3,
        "name": "Solar System: Dwarf Planets, Asteroids, Comets & Meteors",
        "description": "The small bodies: what makes a planet vs. a dwarf planet vs. a Plutoid, Pluto, Eris, Ceres and Sedna, the Kuiper Belt and Oort Cloud, every asteroid type (C, S, M and the rare classes), comets and their tails, and meteors vs. meteorites.",
        "goals": [
            "Use the three rules to decide whether something is a planet, a dwarf planet or a Plutoid.",
            "Describe the Kuiper Belt and Oort Cloud and what lives there.",
            "Name the main asteroid types and what they tell us.",
            "Describe a comet's parts and the two kinds of comet orbits.",
            "Tell a meteoroid, meteor and meteorite apart.",
        ],
        "sections": [
            {
                "heading": "Planet, dwarf planet or Plutoid?",
                "body": (
                    "In 2006 astronomers agreed on rules. A PLANET must:\n"
                    "1. orbit the Sun,\n"
                    "2. be big enough for its own gravity to pull it into a round shape, and\n"
                    "3. have 'CLEARED ITS NEIGHBORHOOD' -- its gravity is strong enough that anything that comes close gets "
                    "pulled in, flung away or captured into orbit.\n\n"
                    "A DWARF PLANET passes rules 1 and 2 but fails rule 3: it shares its orbit with lots of other objects. "
                    "It also must not be a moon (a SATELLITE) of something else. The five known dwarf planets are Ceres, "
                    "Pluto, Eris, Haumea and Makemake.\n\n"
                    "A PLUTOID is a dwarf planet whose orbit is farther out than Neptune's (its average distance, or "
                    "SEMI-MAJOR AXIS, is bigger than Neptune's). The four official Plutoids are Pluto, Haumea, Makemake and "
                    "Eris. Ceres lives in the asteroid belt, so it is a dwarf planet but NOT a Plutoid.\n\n"
                    "Objects beyond Neptune are called TRANS-NEPTUNIAN OBJECTS (TNOs). Pluto was the first one found (by Clyde "
                    "Tombaugh in 1930); more than 3,900 are known now. Pluto was called the ninth planet until 2006."
                ),
                "infographic": "dwarf_planets",
            },
            {
                "heading": "Pluto, Eris, Ceres and Sedna",
                "body": (
                    "• PLUTO is a small icy world with five known moons. Its biggest moon, CHARON, is so large compared to "
                    "Pluto that the two are tidally locked to EACH OTHER -- each always shows the other the same face, like "
                    "dancers holding hands. Pluto spins tipped on its side, its orbit is tilted out of the planets' plane, and "
                    "it crosses inside Neptune's orbit -- but a 2:3 orbital resonance with Neptune means they never collide. "
                    "NASA's NEW HORIZONS flew past Pluto in July 2015 and found a surprisingly active world, including a "
                    "bright, smooth plain of nitrogen ice (Sputnik Planitia).\n"
                    "• ERIS is about Pluto's size and has at least one moon. Its discovery helped trigger the 2006 debate about "
                    "what a planet is.\n"
                    "• CERES, nearly 1,000 km across, is the largest object in the asteroid belt and the only dwarf planet in "
                    "the inner Solar System. The Dawn spacecraft orbited it (and the big asteroid Vesta) between 2011 and "
                    "2018.\n"
                    "• SEDNA is a PLUTOID CANDIDATE -- big enough to be a dwarf planet, but not yet officially one. It is about "
                    "1,600 km (995 miles) across and has an extremely stretched orbit that takes about 11,518 years! Its "
                    "closest point to the Sun (PERIHELION) is in the outer Kuiper Belt; its farthest point (APHELION) may reach "
                    "the inner Oort Cloud. We found it partly by luck: it was near perihelion and just barely bright enough to "
                    "see. Near aphelion it would have stayed hidden for thousands of years. No moons have been found -- at that "
                    "distance they would be too dim to see."
                ),
            },
            {
                "heading": "The Kuiper Belt and the Oort Cloud",
                "body": (
                    "THE KUIPER BELT (say 'KAI-per') is a flat, donut-shaped ring of icy objects beyond Neptune, about 30 to "
                    "50 AU from the Sun. It is a bit like the asteroid belt, but much bigger and made mostly of ice. Its "
                    "objects are leftovers from the Solar System's formation that never became planets. Pluto, Haumea, "
                    "Makemake and many SHORT-PERIOD comets come from here. New Horizons, the first spacecraft to visit the "
                    "Kuiper Belt, flew past Pluto in 2015 and then the small object ARROKOTH (once nicknamed 2014 MU69) on New "
                    "Year's Day 2019.\n\n"
                    "THE OORT CLOUD is a gigantic, roughly spherical shell of icy objects surrounding the whole Solar System, "
                    "far beyond the Kuiper Belt. It marks the outer edge of where the Sun's gravity still matters. It is so "
                    "spread out that comets inside it can be tens of millions of km apart, and all its objects together "
                    "probably have only about 40 times Earth's mass. Its comets are easily nudged by passing stars, which can "
                    "fling them into deep space or send them falling toward the Sun as LONG-PERIOD comets. Many comets (and "
                    "some asteroids) probably came from here. No spacecraft has reached it."
                ),
                "infographic": "small_bodies",
            },
            {
                "heading": "Asteroids and the asteroid alphabet",
                "body": (
                    "ASTEROIDS are small, rocky, airless bodies that orbit the Sun. They range from less than 10 m across up to "
                    "Ceres, nearly 1,000 km wide. They are usually cratered and lumpy (only the biggest are round), they "
                    "follow oval paths around the Sun, and some tumble as they spin. Most live in the MAIN ASTEROID BELT "
                    "between Mars and Jupiter, where Jupiter's strong gravity stopped them from building a planet. Since then, "
                    "collisions have broken many apart, creating ASTEROID FAMILIES (groups of pieces from one broken parent). "
                    "Some asteroids cross Earth's orbit (like Eros), and some share Jupiter's orbit as TROJANS.\n\n"
                    "Astronomers sort asteroids into TYPES by their color, brightness (albedo) and SPECTRUM (the pattern of "
                    "colors in the light they reflect), which reveals what they are made of. Their makeup depends on how hot it "
                    "was where they formed. The big three:\n"
                    "• C-TYPE: dark, carbon-rich and PRIMITIVE (barely changed since the Solar System formed) -- the most "
                    "common.\n"
                    "• S-TYPE: made of SILICATE (stony) minerals; brighter.\n"
                    "• M-TYPE: metal-rich, like iron-nickel.\n"
                    "The rarer types from the wiki table: E (very bright, enstatite / iron-free silicates), P (dark, "
                    "primitive), D (very dark, organic-rich), V (basaltic, i.e. volcanic -- like Vesta), Q (fresh silicate "
                    "surfaces), A (rich in the green mineral olivine), B (blue, hydrated -- with water in its minerals), G "
                    "(C-type with ultraviolet features), F (C-type without UV features), R (rare, olivine plus pyroxene), T "
                    "(dark, featureless), L (moderately red), K (silicate-rich, subtle features), X (featureless -- needs "
                    "albedo to classify) and I (an in-between S/M mixture).\n\n"
                    "Missions: NEAR-Shoemaker orbited and landed on Eros; Japan's HAYABUSA (2003-2010) visited the S-type "
                    "asteroid Itokawa and brought a sample back to Earth; Dawn orbited Vesta and Ceres; other spacecraft have "
                    "landed on Ryugu and Bennu."
                ),
                "infographic": "asteroid_types",
            },
            {
                "heading": "Comets: dirty snowballs with tails",
                "body": (
                    "COMETS are icy bodies made of ice, dust, rock and frozen gases like carbon dioxide, carbon monoxide, "
                    "ammonia and methane -- 'dirty snowballs'. They formed in the cold outer Solar System and are stored in the "
                    "Kuiper Belt and Oort Cloud. A comet has three main parts:\n"
                    "• NUCLEUS: the solid, icy core, usually just a few km across.\n"
                    "• COMA: as the comet nears the Sun, heat turns its ice straight into gas (sublimation), making a glowing, "
                    "fuzzy cloud around the nucleus.\n"
                    "• TAIL(S): the SOLAR WIND (a stream of particles from the Sun) and the pressure of sunlight push gas and "
                    "dust away, making one or two long tails. Tails always point AWAY from the Sun, not behind the comet.\n\n"
                    "Comets travel on very stretched orbits:\n"
                    "• PERIODIC (short-period) comets return in less than about 200 years, so they have been seen many times "
                    "throughout history -- like Halley's Comet (about every 76 years).\n"
                    "• NON-PERIODIC (long-period) comets have huge oval or even open orbits and may take thousands or millions "
                    "of years to return, if ever. Most are seen only once in recorded history.\n\n"
                    "Missions: Rosetta orbited comet 67P and photographed its gas jets, and Deep Impact (2005) smashed an "
                    "impactor into comet Tempel 1 to dig up fresh material from inside. Comets may have delivered water and "
                    "organic molecules to the young Earth."
                ),
            },
            {
                "heading": "Meteoroids, meteors and meteorites",
                "body": (
                    "Space is full of small bits of rock and dust (COSMIC DUST), much of it left behind by comets and "
                    "crumbling asteroids. Three similar words describe them at different stages:\n\n"
                    "• METEOROID: the small rock or dust grain while it is still out in space.\n"
                    "• METEOR: the bright streak of light when it zooms into our air and burns up -- a 'shooting star'. Millions "
                    "happen every day!\n"
                    "• METEORITE: a piece that survives the fall and lands on the ground.\n\n"
                    "When Earth passes through a comet's dust trail, we get a METEOR SHOWER: lots of meteors that seem to come "
                    "from one spot in the sky. Meteorites come as irons (iron-nickel metal), stony-irons and stones. The most "
                    "primitive stones, CARBONACEOUS meteorites like Murchison and Allende, date back 4.5 billion years and "
                    "contain organic molecules -- including amino acids and sugars made in space."
                ),
            },
        ],
        "word_bank": [
            ("Cleared its neighborhood", "When a planet's gravity has swept its orbit clear by pulling in, flinging away or capturing nearby objects."),
            ("Dwarf planet", "A round body orbiting the Sun that has NOT cleared its orbit and is not a moon: Ceres, Pluto, Eris, Haumea, Makemake."),
            ("Satellite", "Any object that orbits a planet -- a moon is a natural satellite."),
            ("Plutoid", "A dwarf planet that orbits beyond Neptune: Pluto, Haumea, Makemake and Eris."),
            ("Semi-major axis", "Half the long width of an oval orbit -- basically the object's average distance from the Sun."),
            ("Trans-Neptunian object (TNO)", "Any object orbiting the Sun beyond Neptune."),
            ("Plutoid candidate", "An object that may be a Plutoid but isn't official yet, like Sedna."),
            ("Perihelion", "The point in an orbit closest to the Sun."),
            ("Aphelion", "The point in an orbit farthest from the Sun."),
            ("Kuiper Belt", "A flat ring of icy objects 30-50 AU from the Sun, beyond Neptune."),
            ("Oort Cloud", "A huge, distant sphere of icy objects surrounding the Solar System; home of long-period comets."),
            ("Asteroid", "A small, rocky, airless body orbiting the Sun, mostly between Mars and Jupiter."),
            ("Asteroid family", "A group of asteroids that are pieces of one bigger asteroid that broke apart."),
            ("Trojan", "A small body sharing a planet's orbit, 60 degrees ahead of or behind it."),
            ("Spectrum", "The rainbow pattern of colors in light; it reveals what an object is made of."),
            ("Primitive", "Barely changed since the Solar System formed."),
            ("Silicate", "A rocky mineral containing silicon and oxygen -- the main stuff of stony rocks."),
            ("Olivine", "A green silicate mineral common in the Earth's mantle and some asteroids."),
            ("Pyroxene", "A common silicate mineral found in volcanic rocks."),
            ("Hydrated", "Containing water locked inside the minerals."),
            ("Comet", "An icy 'dirty snowball' that grows a glowing coma and tails when it nears the Sun."),
            ("Nucleus (comet)", "The solid icy core of a comet."),
            ("Coma", "The glowing cloud of gas and dust around a comet's nucleus."),
            ("Solar wind", "A stream of charged particles blowing out from the Sun."),
            ("Periodic comet", "A comet that returns in less than about 200 years, like Halley's Comet."),
            ("Non-periodic comet", "A long-period comet that takes thousands to millions of years to return, if ever."),
            ("Meteoroid", "A small rock or dust grain traveling in space."),
            ("Meteor shower", "Many meteors in one night when Earth passes through a comet's dust trail."),
            ("Carbonaceous meteorite", "A primitive, carbon-rich meteorite that can contain organic molecules like amino acids."),
        ],
        "key_facts": [
            "Planet: orbits Sun + round + cleared its neighborhood. Dwarf planet: fails 'cleared', not a moon.",
            "Dwarf planets: Ceres, Pluto, Eris, Haumea, Makemake. Plutoids (beyond Neptune): Pluto, Haumea, Makemake, Eris.",
            "Sedna: Plutoid candidate, ~1,600 km (995 mi), ~11,518-year orbit, no known moons.",
            "Pluto: found 1930 (Tombaugh); 5 moons; Charon mutually tidally locked; New Horizons flyby July 2015; Arrokoth Jan 1, 2019.",
            "Kuiper Belt: 30-50 AU. Oort Cloud: vast shell, ~40 Earth masses, source of long-period comets.",
            "Asteroid types: C (dark, carbon, most common), S (silicate, brighter), M (metal) + E, P, D, V, Q, A, B, G, F, R, T, L, K, X, I.",
            "Comet parts: nucleus, coma, tail(s) pointing away from the Sun. Periodic < 200 years; non-periodic = thousands-millions.",
            "Meteoroid (in space) -> meteor (streak) -> meteorite (lands).",
        ],
        "quick_check": [
            ("Why is Pluto a dwarf planet and not a planet?", "It is round and orbits the Sun, but it hasn't cleared its neighborhood -- it shares its zone with many Kuiper Belt objects."),
            ("Is Ceres a Plutoid?", "No. It is a dwarf planet, but it orbits in the asteroid belt, not beyond Neptune."),
            ("Why don't Pluto and Neptune crash, even though their orbits cross?", "They are in a 2:3 orbital resonance that keeps them from ever meeting."),
            ("Which way does a comet's tail point?", "Away from the Sun, pushed by the solar wind and sunlight -- not necessarily behind the comet."),
            ("What do C, S and M stand for in asteroid types?", "C = carbon-rich (dark), S = silicate/stony (brighter), M = metal-rich."),
            ("A space rock lands in your backyard. Is it a meteor or a meteorite?", "A meteorite -- the meteor was its glowing streak through the sky."),
        ],
        "cards": [
            {
                "term": "Dwarf planet",
                "badge": ("2006", "rules", ICE),
                "analogy": "A kid big enough to be round but who hasn't cleaned up their room (their orbit) yet.",
                "explanation": "Orbits the Sun, round from its own gravity, but has NOT cleared its neighborhood, and isn't a moon. Five known: Ceres, Pluto, Eris, Haumea, Makemake.",
                "why": "Planet vs. dwarf planet definitions are favorite test questions.",
            },
            {
                "term": "Plutoids & Sedna",
                "badge": ("TNO", "past Neptune", PURPLE),
                "analogy": "Plutoids are the dwarf planets who live in the far-out suburbs past Neptune.",
                "explanation": "Plutoid = dwarf planet orbiting beyond Neptune: Pluto, Haumea, Makemake, Eris. Sedna is a candidate (~1,600 km) with an ~11,518-year, very stretched orbit.",
                "why": "Know which dwarf planets are Plutoids (not Ceres!).",
            },
            {
                "term": "Pluto & Charon",
                "badge": ("2015", "New Horizons", ICE),
                "analogy": "Dancers spinning while holding hands, always facing each other.",
                "explanation": "Found 1930 by Tombaugh; 5 moons; Charon and Pluto are mutually tidally locked; 2:3 resonance with Neptune. New Horizons flew by in July 2015, then Arrokoth in 2019.",
                "why": "Connects history, resonance and tidal locking.",
            },
            {
                "term": "Kuiper Belt & Oort Cloud",
                "badge": ("30-50", "AU", ICE),
                "analogy": "The Solar System's deep freezers.",
                "explanation": "Kuiper Belt: flat icy ring beyond Neptune (30-50 AU), home of Pluto and short-period comets. Oort Cloud: vast distant shell (~40 Earth masses) of long-period comets, nudged by passing stars.",
                "why": "Where comets -- and maybe Earth's water -- came from.",
            },
            {
                "term": "Asteroid types",
                "badge": ("C-S-M", "+ rare", ROCK),
                "analogy": "Crumbs left after the planets were baked -- each kind tells part of the recipe.",
                "explanation": "C (dark, carbon-rich, most common), S (stony silicate, brighter), M (metal-rich). Rare types include V (basaltic, like Vesta), D (very dark, organic-rich), B (blue, hydrated) and A (olivine-rich).",
                "why": "Asteroids preserve the original ingredients, including water and organics.",
            },
            {
                "term": "Comets",
                "badge": ("ICE", "comets", ICE),
                "analogy": "Dirty snowballs that sprout glowing tails when they visit the Sun.",
                "explanation": "Nucleus, coma and tails pointing away from the Sun. Periodic comets return in < 200 years (Halley's); non-periodic comets take thousands to millions of years.",
                "why": "Comets may have delivered water and organics to young Earth.",
            },
            {
                "term": "Meteoroid, meteor, meteorite",
                "badge": ("ZOOM", "shooting star", GOLD),
                "analogy": "In space it's a meteoroid, in the sky it's a meteor, on the ground it's a meteorite.",
                "explanation": "Millions of meteors burn up daily; meteor showers come from comet dust trails. Carbonaceous meteorites (Murchison, Allende) carry amino acids and sugars from space.",
                "why": "Meteorites are real samples of the early Solar System.",
            },
        ],
    },
]
