"""Unit 6 -- People & Missions: the astronomers who figured out the Solar
System and the spacecraft and telescopes that explored it (the wiki's full
mission table with dates, plus the missions the source reader mentions).
Same lesson-chapter format as lessons_unit1.py.
"""

from app.content.solar_system.svg import BLUE, GAS, GOLD, ICE, PURPLE, ROCK, SUN

UNIT6 = [
    # ------------------------------------------------------------------ 19
    {
        "unit": 6,
        "name": "Solar System: Astronomers & Space Missions",
        "description": "The people -- Aristarchus, Copernicus, Tycho Brahe, Galileo, Kepler, Huygens, Halley, Herschel, Tombaugh, Sagan and more -- and the missions, with the wiki's launch and end dates: Voyager, Galileo, Cassini-Huygens, New Horizons, Dawn, Juno, Hayabusa, Deep Impact, BepiColombo, LRO, Hubble, ALMA, JWST and what's coming next.",
        "goals": [
            "Match each famous astronomer with their discovery.",
            "Match each mission with its target, dates and big result.",
            "Explain how the Sun-centered model replaced the Earth-centered one.",
        ],
        "sections": [
            {
                "heading": "From an Earth-centered to a Sun-centered universe",
                "body": (
                    "For most of history, people believed Earth sat still at the center of everything, with the Sun, Moon "
                    "and planets circling it. This is the GEOCENTRIC model ('geo' = Earth). Changing to the HELIOCENTRIC model "
                    "('helios' = Sun), with the Sun in the middle, took about 2,000 years.\n\n"
                    "• ARISTARCHUS (ancient Greece) was the first to put forward a Sun-centered system. After studying solar "
                    "and lunar eclipses, he correctly reasoned that the Sun is at the center. Almost nobody believed him.\n"
                    "• NICOLAUS COPERNICUS (1473-1543), a Polish astronomer, developed a full heliocentric model: the Sun lies "
                    "near the center and Earth revolves around it, not the other way around. It wasn't proven until Galileo, "
                    "and wasn't widely accepted for many years after that. He also lectured on astronomy in Rome.\n"
                    "• TYCHO BRAHE (1546-1601), a Danish astronomer, made the most precise measurements of planet positions -- "
                    "and of more than 700 stars -- of his time, without a telescope. In 1572 he discovered a SUPERNOVA near the "
                    "constellation Cassiopeia. The king of Denmark was so impressed that he paid for a large observatory on the "
                    "island of Ven. Tycho invented his own in-between model (the TYCHONIC SYSTEM): every planet except Earth "
                    "orbits the Sun, while the Sun and Moon orbit Earth.\n"
                    "• JOHANNES KEPLER (1571-1630), a German astronomer, at first tried to explain planet motion with circles. "
                    "He became Tycho's assistant (they did not get along!), and Tycho gave him the hard job of understanding "
                    "Mars' orbit. That task led Kepler to his three LAWS OF PLANETARY MOTION -- ellipses, equal areas, and "
                    "p^2 = a^3.\n"
                    "• GALILEO GALILEI (1564-1642), born in Pisa, Italy, started out studying medicine but switched to "
                    "mathematics. He improved the telescope, discovered Jupiter's four largest moons in 1610 (the Galilean "
                    "moons), and saw that Venus has a full set of phases -- proof that Venus orbits the Sun. He strongly "
                    "supported the heliocentric model, which upset the Church, and he was sentenced to house arrest. He is "
                    "called 'the father of modern observational astronomy'. He went blind near the end of his life, possibly "
                    "from looking at the Sun."
                ),
                "infographic": "astronomer_timeline",
            },
            {
                "heading": "Finding new worlds",
                "body": (
                    "• CHRISTIAAN HUYGENS discovered Saturn's moon Titan in 1655. The Huygens probe that landed on Titan is "
                    "named after him.\n"
                    "• GIOVANNI CASSINI discovered four of Saturn's moons (Iapetus 1671, Rhea 1672, Tethys and Dione 1684). The "
                    "Cassini mission is named after him.\n"
                    "• EDMOND HALLEY (1656-1742), a British astronomer who studied Isaac Newton's ideas at Oxford, was the first "
                    "to calculate a comet's orbit. In his 1705 book 'Synopsis of Cometary Astronomy' he predicted the comet "
                    "would return. It appeared in 1758, just as he said (after his death), and was named Halley's Comet.\n"
                    "• WILLIAM HERSCHEL discovered URANUS on March 13, 1781 -- the first planet found with a telescope -- plus "
                    "its moons Titania and Oberon (1787) and Saturn's Mimas and Enceladus (1789).\n"
                    "• NEPTUNE was discovered on September 23, 1846, after Urbain Le Verrier used math to predict where it "
                    "should be (from how it tugged on Uranus) and Johann Galle spotted it. William Lassell found its moon "
                    "Triton weeks later.\n"
                    "• ASAPH HALL found Mars' moons Phobos and Deimos in 1877 -- the same year GIOVANNI SCHIAPARELLI reported "
                    "'canali' on Mars, which PERCIVAL LOWELL turned into the myth of Martian canals.\n"
                    "• CLYDE TOMBAUGH (1906-1997) began with a homemade 9-inch telescope, drawing Jupiter and Saturn. He sent "
                    "his drawings to Lowell Observatory in Arizona and was hired. His job was to find the mysterious 'Planet X' "
                    "-- and in 1930 he discovered Pluto. He went on to find comets and star clusters too.\n"
                    "• GERARD KUIPER found Uranus' moon Miranda (1948) and Neptune's Nereid (1949); the Kuiper Belt is named "
                    "after him. JAMES CHRISTY found Pluto's moon Charon in 1978."
                ),
            },
            {
                "heading": "Modern scientists",
                "body": (
                    "• CARL SAGAN (1934-1996) showed that Venus' thick atmosphere acts like a giant greenhouse, explained that "
                    "Mars' seasonal color changes were wind-blown dust (not plants), put messages on the Pioneer and Voyager "
                    "spacecraft (the Voyager 'Golden Records'), helped found The Planetary Society, and shared science with "
                    "about 500 million people through his TV series Cosmos. He also asked Voyager 1 to turn around and take the "
                    "'Pale Blue Dot' photo of Earth.\n"
                    "• STANLEY MILLER and HAROLD UREY (1950s) made building blocks of life in a flask (see the Astrobiology "
                    "chapter).\n"
                    "• MICHEL MAYOR and DIDIER QUELOZ found the first planet around a Sun-like star, 51 Pegasi b, in 1995 and won "
                    "the 2019 Nobel Prize in physics.\n"
                    "• ENRICO FERMI, a physicist, asked 'Where is everybody?' -- the Fermi paradox."
                ),
            },
            {
                "heading": "Missions to the outer planets and beyond",
                "body": (
                    "Test writers often ask about missions that aren't even on the rules, so it pays to know them. Dates are "
                    "from the scioly.org wiki's mission table.\n\n"
                    "• VOYAGER 1 (launched Sept 5, 1977; still going): flew past Jupiter and Saturn and made groundbreaking "
                    "discoveries about their moons (it saw Io's volcanoes in 1979). It took the 'Pale Blue Dot' photo and is now "
                    "the farthest human-made object, in interstellar space.\n"
                    "• VOYAGER 2 (launched Aug 20, 1977; still going): flew past Jupiter, Saturn, Uranus and Neptune -- the only "
                    "spacecraft to visit the two ice giants -- and saw eruptions on Triton in 1989. Both Voyagers carry Golden "
                    "Records with sounds and pictures of Earth. (Pioneer 10 and 11 went before them.)\n"
                    "• GALILEO (Oct 18, 1989 - Sept 21, 2003): orbited Jupiter, studying its atmosphere and its moons Io, Europa, "
                    "Ganymede and Callisto; it flew past the asteroids Gaspra and Ida on the way.\n"
                    "• JUNO (launched Aug 5, 2011; until at least 2028): studies Jupiter's core, magnetic field, atmosphere and "
                    "polar regions to learn how Jupiter formed; extended to visit the Galilean moons.\n"
                    "• CASSINI (Oct 15, 1997 - Sept 15, 2017): orbited Saturn, studying its rings, magnetic field and moons -- "
                    "Titan, Enceladus (where it found the geysers), Iapetus, Rhea, Dione, Tethys, Mimas and Pandora. It carried "
                    "ESA's HUYGENS probe, which landed on Titan on January 14, 2005. Cassini ended by diving into Saturn.\n"
                    "• NEW HORIZONS (launched Jan 19, 2006; still going): the first close-up visit to Pluto and its moons "
                    "(Charon, Styx, Nix, Kerberos, Hydra) in July 2015, then the Kuiper Belt object Arrokoth (Jan 1, 2019).\n"
                    "• EUROPA CLIPPER (launched October 2024, arrives 2030) will study Europa's ocean, and DRAGONFLY (launch "
                    "July 2028) will fly a drone on Titan."
                ),
                "infographic": "mission_timeline",
            },
            {
                "heading": "Missions to the inner Solar System and small bodies",
                "body": (
                    "• MERCURY: Mariner 10 and MESSENGER studied it; BEPICOLOMBO (launched Oct 20, 2018; still going), a "
                    "European-Japanese mission, will study Mercury's makeup, magnetic field, thin atmosphere and history, and "
                    "test Einstein's theory of general relativity.\n"
                    "• VENUS: Mariner 2 (1962, first flyby), Venera 7 (1970, first landing that sent data), Pioneer Venus, and "
                    "Magellan (radar map).\n"
                    "• THE MOON: Apollo astronauts walked on it and brought back rocks; the LUNAR RECONNAISSANCE ORBITER (launched "
                    "Jun 28, 2009; still going) is making a detailed, high-resolution atlas of the Moon's surface, environment "
                    "and resources to prepare for future human visits.\n"
                    "• MARS: Viking orbiters and landers; Pathfinder; Mars Global Surveyor; rovers Spirit and Opportunity (2004), "
                    "Curiosity (2012) and Perseverance with the Ingenuity helicopter; the Phoenix lander (2008, polar ice); the "
                    "Mars Reconnaissance Orbiter.\n"
                    "• ASTEROIDS: NEAR-Shoemaker orbited and landed on Eros. HAYABUSA (May 9, 2003 - Jun 13, 2010), from Japan, met "
                    "the near-Earth S-type asteroid Itokawa, collected surface material and returned it to Earth. DAWN (Sept 27, "
                    "2007 - Nov 1, 2018) orbited Vesta and Ceres, the two most massive bodies in the asteroid belt, to learn about "
                    "the early Solar System. Other spacecraft have visited Ryugu and Bennu.\n"
                    "• COMETS: DEEP IMPACT (Jan 12, 2005 - Sept 20, 2013) deliberately crashed an impactor into comet Tempel 1 to "
                    "dig up ancient, untouched material from inside. Rosetta orbited comet 67P and dropped a lander on it."
                ),
            },
            {
                "heading": "Telescopes that watch the sky",
                "body": (
                    "• HUBBLE SPACE TELESCOPE (launched Apr 24, 1990; still going): a general-purpose observatory taking sharp "
                    "pictures of galaxies, stars, star clusters, nebulae and our own Solar System -- including planet-forming "
                    "disks in the Orion Nebula. Telescopes in space avoid the blurring of Earth's air.\n"
                    "• JAMES WEBB SPACE TELESCOPE (JWST; launched Dec 21, 2021 per the wiki -- NASA lists Dec 25; still going): "
                    "sees in infrared to study everything from the early universe to forming stars and planets and exoplanet "
                    "atmospheres. It found organic molecules in planet-forming disks and imaged Fomalhaut's three dust belts.\n"
                    "• ALMA (Atacama Large Millimeter/submillimeter Array; operating since Mar 13, 2013): 66 large radio "
                    "antennas in Chile that capture millimeter and submillimeter light to make extremely detailed images of "
                    "planet and star formation -- like the rings and gaps around HL Tau.\n"
                    "• Planet hunters: CoRoT (2007-2012), Kepler (2009-2018) and TESS (now surveying the whole sky)."
                ),
            },
        ],
        "word_bank": [
            ("Geocentric model", "The old idea that Earth sits at the center with everything orbiting it."),
            ("Heliocentric model", "The Sun-centered model: Earth and the other planets orbit the Sun."),
            ("Tychonic system", "Tycho Brahe's in-between model: planets orbit the Sun, but the Sun and Moon orbit Earth."),
            ("Supernova", "The huge explosion of a massive star. Tycho saw one in 1572."),
            ("Laws of planetary motion", "Kepler's three laws describing how planets orbit the Sun."),
            ("Observatory", "A building or place with telescopes for studying the sky."),
            ("Flyby", "A mission that zooms past a planet or moon without stopping to orbit it."),
            ("Orbiter", "A spacecraft that goes into orbit around a planet, moon or asteroid."),
            ("Lander", "A spacecraft that touches down on a surface."),
            ("Rover", "A robot vehicle that drives around on another world."),
            ("Impactor", "A part of a spacecraft designed to crash into a target on purpose."),
            ("Sample return", "A mission that collects material from another world and brings it back to Earth."),
            ("Interstellar space", "The space between the stars, beyond the Sun's influence."),
            ("Golden Record", "Records on the Voyager spacecraft carrying sounds and pictures from Earth."),
            ("General relativity", "Einstein's theory that describes gravity as a bending of space and time."),
            ("Space telescope", "A telescope in orbit, above Earth's blurry atmosphere."),
        ],
        "key_facts": [
            "Aristarchus: first heliocentric idea. Copernicus (1473-1543): heliocentric model. Tycho (1546-1601): precise data, 1572 supernova, Ven observatory, Tychonic system.",
            "Kepler (1571-1630): Tycho's assistant; laws of planetary motion from Mars' orbit. Galileo (1564-1642): Jupiter's 4 moons (1610), Venus' phases, house arrest.",
            "Huygens: Titan 1655. Halley (1656-1742): first comet orbit; 1705 book; comet returned 1758. Herschel: Uranus March 13, 1781.",
            "Neptune: Sept 23, 1846 (Le Verrier predicted, Galle found). Tombaugh (1906-1997): Pluto 1930 at Lowell Observatory.",
            "Voyager 1: Sept 5, 1977. Voyager 2: Aug 20, 1977 (only visitor to Uranus and Neptune).",
            "Galileo: Oct 18, 1989 - Sept 21, 2003. Juno: Aug 5, 2011 - at least 2028. Cassini: Oct 15, 1997 - Sept 15, 2017 (Huygens on Titan Jan 14, 2005).",
            "New Horizons: Jan 19, 2006 (Pluto July 2015, Arrokoth Jan 1, 2019). Dawn: Sept 27, 2007 - Nov 1, 2018 (Vesta, Ceres).",
            "Hayabusa: May 9, 2003 - Jun 13, 2010 (Itokawa sample). Deep Impact: Jan 12, 2005 - Sept 20, 2013 (Tempel 1).",
            "LRO: Jun 28, 2009. BepiColombo: Oct 20, 2018. Hubble: Apr 24, 1990. JWST: Dec 2021. ALMA: Mar 13, 2013 (66 antennas).",
        ],
        "quick_check": [
            ("Who first suggested a Sun-centered system, and who developed it into a full model?", "Aristarchus first suggested it; Copernicus developed the heliocentric model."),
            ("What two discoveries by Galileo supported the heliocentric model?", "Jupiter's four moons (not everything orbits Earth) and the full phases of Venus (Venus orbits the Sun)."),
            ("How did Kepler discover his laws?", "As Tycho Brahe's assistant he used Tycho's precise data to work out Mars' orbit."),
            ("Which spacecraft is the only one to visit Uranus and Neptune?", "Voyager 2."),
            ("Which mission crashed into a comet on purpose, and why?", "Deep Impact hit comet Tempel 1 to dig up ancient material from inside it."),
            ("Which missions studied Vesta and Ceres, and Itokawa?", "Dawn orbited Vesta and Ceres; Hayabusa returned a sample from Itokawa."),
        ],
        "cards": [
            {
                "term": "Aristarchus & Copernicus",
                "badge": ("SUN", "in the middle", SUN),
                "analogy": "Realizing the class doesn't revolve around you -- everyone revolves around the teacher's desk.",
                "explanation": "Aristarchus (ancient Greece) first proposed a Sun-centered system from eclipse observations. Copernicus (1473-1543) developed the full heliocentric model.",
                "why": "Who-proposed-what questions are common.",
            },
            {
                "term": "Tycho Brahe & Kepler",
                "badge": ("DATA", "+ laws", GOLD),
                "analogy": "Tycho collected the puzzle pieces; Kepler put the puzzle together.",
                "explanation": "Tycho (1546-1601): precise positions of planets and 700+ stars, 1572 supernova, observatory on Ven, Tychonic system. Kepler (1571-1630): his assistant; used Mars' orbit to find the three laws.",
                "why": "Know who did what.",
            },
            {
                "term": "Galileo Galilei",
                "badge": ("1610", "telescope", BLUE),
                "analogy": "The first to really 'zoom in' on the sky -- and it changed everything.",
                "explanation": "Improved the telescope; found Io, Europa, Ganymede and Callisto (1610); saw Venus' full phases; supported heliocentrism; house arrest; 'father of modern observational astronomy'.",
                "why": "Galilean moons + Venus' phases are core facts.",
            },
            {
                "term": "Huygens, Halley & Herschel",
                "badge": ("1781", "Uranus", ICE),
                "analogy": "Each new discovery was another room in a house we thought we knew.",
                "explanation": "Huygens: Titan (1655). Halley: first comet orbit, predicted its 1758 return. Herschel: Uranus (March 13, 1781). Neptune: Sept 23, 1846, predicted by math.",
                "why": "Discovery dates are quick-answer questions.",
            },
            {
                "term": "Tombaugh & Pluto",
                "badge": ("1930", "Pluto", PURPLE),
                "analogy": "A kid with a homemade telescope who ended up finding a whole new world.",
                "explanation": "Clyde Tombaugh (1906-1997) sent his drawings to Lowell Observatory, was hired to hunt 'Planet X', and found Pluto in 1930.",
                "why": "Connects history to dwarf-planet facts.",
            },
            {
                "term": "Voyager 1 & 2",
                "badge": ("1977", "Voyagers", GAS),
                "analogy": "Message-in-a-bottle explorers still sailing out of the Solar System.",
                "explanation": "Voyager 1 (Sept 5, 1977): Jupiter, Saturn, Pale Blue Dot, interstellar space. Voyager 2 (Aug 20, 1977): Jupiter, Saturn, Uranus, Neptune, Triton. Golden Records.",
                "why": "The most famous outer-planet missions.",
            },
            {
                "term": "Galileo, Juno & Cassini",
                "badge": ("ORBIT", "giants", GAS),
                "analogy": "Long-term houseguests studying the giant planets up close.",
                "explanation": "Galileo (1989-2003): Jupiter and moons. Juno (2011-): Jupiter's core and magnetic field. Cassini (1997-2017): Saturn, rings, Titan, Enceladus; Huygens landed on Titan (2005).",
                "why": "Mission-and-target matching is a standard test section.",
            },
            {
                "term": "Small-body missions",
                "badge": ("DAWN", "& more", ROCK),
                "analogy": "Geologists visiting the leftover building blocks of the planets.",
                "explanation": "New Horizons (2006-): Pluto 2015, Arrokoth. Dawn (2007-2018): Vesta, Ceres. Hayabusa (2003-2010): Itokawa sample. Deep Impact (2005-2013): hit comet Tempel 1. NEAR-Shoemaker: Eros. Rosetta: comet 67P.",
                "why": "Small bodies preserve the original ingredients.",
            },
            {
                "term": "Space telescopes & ALMA",
                "badge": ("JWST", "2021", BLUE),
                "analogy": "Going above the clouds of a foggy city to see the stars clearly.",
                "explanation": "Hubble (Apr 24, 1990): general observatory. JWST (Dec 2021): infrared, exoplanet air, disks. ALMA (2013): 66 antennas, millimeter waves, HL Tau. Kepler, CoRoT, TESS: planet hunters.",
                "why": "Central to 'habitability beyond the Solar System'.",
            },
        ],
    },
]
