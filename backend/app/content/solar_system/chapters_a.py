"""Solar System learning chapters 1-7: our planetary system, its origin,
Earth, Venus, Mars, and the moons and rings of the giant planets.

Written for Division B students (roughly grades 6-9): every concept has a
kid-friendly analogy up front, but the explanation keeps every number and
idea from the source reader (OpenStax Astronomy 2e, sections 7.1, 7.4,
8.1, 8.3-8.5, 10.1-10.3, 10.5, 12.1-12.2). Text is plain (no Markdown)
because the student page renders it with white-space: pre-wrap.

Each chapter dict is consumed by seed.py:
  name / description  -> the chapter's sub-topic row
  source_title / source_text -> a fact-sheet Resource for the chapter
  story -> Topic.story_md (the long-form "read it like a story" view)
  infographics -> keys into infographics.INFOGRAPHICS (stored as Diagrams)
  concepts -> approved ConceptTerm flashcards; `badge` is (label, sub, color)
"""

from app.content.solar_system.svg import BLUE, GAS, GOLD, GREEN, ICE, PURPLE, RED, ROCK, SUN

CHAPTERS_A = [
    # ------------------------------------------------------------------ 1
    {
        "name": "Solar System: Meet Our Planetary System",
        "description": "A tour of everything that orbits the Sun -- planets, dwarf planets, moons, rings, asteroids, comets and dust -- with the key numbers for each planet.",
        "source_title": "Source reader: Overview of Our Planetary System (OpenStax Astronomy 2e, 7.1)",
        "infographics": ["mass_budget", "planet_lineup", "sun_layers", "small_bodies"],
        "source_text": (
            "The solar system = the Sun + planets, their moons and rings, asteroids, comets and dust. Most formed together "
            "with the Sun ~4.5 billion years ago from a huge cloud of gas and dust. 'Planetary system' is the general term; "
            "ours is the 'solar system' because the Sun is called Sol. Spacecraft (Voyager, Pioneer, Curiosity, Pathfinder) "
            "have flown past, orbited or landed on every planet; studied 2 dwarf planets, hundreds of moons, 4 ring systems, "
            "a dozen asteroids, several comets. Probes entered Jupiter's atmosphere and landed on Venus, Mars, the Moon, "
            "Titan, asteroids Eros, Itokawa, Ryugu, Bennu and comet 67P (Churyumov-Gerasimenko). Humans walked on the Moon "
            "(Apollo); a helicopter drone flew on Mars.\n"
            "MASS (Table 7.1): Sun 99.80%; Jupiter 0.10%; comets 0.0005-0.03% (est.); all other planets and dwarf planets "
            "0.04%; moons and rings 0.00005%; asteroids 0.000002% (est.); cosmic dust 0.0000001% (est.). The Sun is brighter "
            "than ~80% of stars in the Galaxy, ~1.4 million km across, interior millions of degrees. Jupiter is more massive "
            "than all other planets combined; ~1,300 Earths fit inside it. Planet masses were found with Kepler's laws + "
            "Newton's gravity, now refined by tracking spacecraft.\n"
            "PLANETS (Table 7.2: distance AU / year y / diameter km / mass 10^23 kg / density g/cm3): Mercury 0.39/0.24/4,878/"
            "3.3/5.4; Venus 0.72/0.62/12,120/48.7/5.2; Earth 1.00/1.00/12,756/59.8/5.5; Mars 1.52/1.88/6,787/6.4/3.9; Jupiter "
            "5.20/11.86/142,984/18,991/1.3; Saturn 9.54/29.46/120,536/5,686/0.7; Uranus 19.18/84.07/51,118/866/1.3; Neptune "
            "30.06/164.82/49,660/1,030/1.6. 1 AU = Earth-Sun distance. Water = 1 g/cm3 = 1000 kg/m3.\n"
            "Five planets known to the ancients (Mercury, Venus, Mars, Jupiter, Saturn); Uranus and Neptune found with "
            "telescopes. All 8 revolve in the same direction, in nearly the same plane, in nearly circular orbits. Most spin "
            "the same way they orbit; exceptions: Venus spins backward (retrograde) very slowly; Uranus and Pluto spin tipped "
            "nearly on their sides. Spin of Eris, Haumea, Makemake unknown.\n"
            "Terrestrial (inner) planets Mercury-Mars (+ often the Moon): small, rock and metal, solid surfaces with craters, "
            "mountains, volcanoes. Jovian (giant) planets Jupiter-Neptune: mostly light ices, liquids, gases; no solid "
            "surface; like spherical oceans with small dense cores.\n"
            "TNOs (trans-Neptunian objects): Pluto first (1930); Eris about Pluto's size with at least one moon; Pluto has 5 "
            "moons; >3,900 TNOs known; Arrokoth visited by New Horizons. Largest TNOs and Ceres (largest asteroid) are dwarf "
            "planets. Five known dwarf planets: Eris, Haumea, Pluto, Ceres, Makemake; Pluto's orbit is tilted out of the "
            "planets' plane. New Horizons flew past Pluto July 2015 (Sputnik Plain).\n"
            "DENSITY: density = mass / volume, sphere volume V = (4/3) pi R^3. Mimas (Saturn moon, ~400 km across) has density "
            "~1.2 g/cm3 -> mostly ice. Earth ~5.5 g/cm3, 4-5x Mimas; Earth is the densest planet.\n"
            "SMALL MEMBERS: ~430 known moons orbit planets/dwarf planets; only Mercury and Venus have none. Biggest moons: our "
            "Moon, Jupiter's 4 Galilean moons, Saturn's Titan, Neptune's Triton. All 4 giants have rings (countless bodies "
            "from mountain-size to dust, orbiting the equator), shaped by moons; Saturn's are brightest. Asteroids: rocky, "
            "mostly between Mars and Jupiter, some cross Earth's orbit (Eros, visited by NEAR-Shoemaker); remnants from before "
            "the planets formed; Mars' small moons likely captured asteroids. Comets: mostly ice (frozen water, CO2, CO), "
            "remnants stored in a cold 'deep freeze' far out (e.g. 67P seen by Rosetta). Cosmic dust: burns up as meteors "
            "('shooting stars', millions per day); pieces that reach the ground are meteorites.\n"
            "CARL SAGAN (1934-1996): showed Venus' thick air acts like a giant greenhouse; showed Mars' seasonal changes were "
            "wind-blown dust, not plants; got plaques on Pioneer and records on Voyager; co-founded The Planetary Society; "
            "simulated early-Earth chemistry; nuclear winter models; books Cosmos, Pale Blue Dot, The Demon-Haunted World, "
            "Contact; TV series Cosmos seen by ~500 million people in 60 countries; inspired Neil deGrasse Tyson."
        ),
        "story": (
            "WELCOME TO THE SUN'S FAMILY\n\n"
            "Imagine a giant, flat racetrack in space. In the middle sits a blazing star -- the Sun. Racing around it, each in "
            "its own lane, are eight planets, all going the same direction. That racetrack is our solar system: the Sun plus "
            "everything that orbits it -- planets, their moons and rings, and leftover 'debris' like asteroids, comets and dust.\n\n"
            "Fun word fact: any star with planets has a planetary system. Ours is called the SOLAR system because an old name "
            "for the Sun is Sol. So, strictly speaking, there is only one solar system!\n\n"
            "Almost everything in the family was born at the same time, about 4.5 billion years ago, from one enormous cloud "
            "of gas and dust. The middle of the cloud became the Sun; a tiny bit of the outer material became everything else.\n\n"
            "THE SUN IS THE BOSS\n\n"
            "If you put the whole solar system on a scale, the Sun would be 99.8% of the weight. Jupiter has 0.1%, and every "
            "other planet, dwarf planet, moon, comet, asteroid and speck of dust shares what is left. The Sun is about "
            "1.4 million kilometers across, brighter than about 80% of the stars in our Galaxy, and millions of degrees inside. "
            "Jupiter is the second boss: it is more massive than all the other planets put together, and about 1,300 Earths "
            "could fit inside it. How do we weigh planets? Centuries ago astronomers used Kepler's laws and Newton's law of "
            "gravity to see how planets tug on each other and on their moons. Today we track how they bend the paths of "
            "passing spacecraft.\n\n"
            "TWO KINDS OF PLANETS\n\n"
            "The four inner planets -- Mercury, Venus, Earth and Mars -- are the TERRESTRIAL planets (the Moon is often included "
            "too). They are small, made of rock and metal, and have solid surfaces covered in craters, mountains and volcanoes "
            "that record their history.\n\n"
            "The four outer planets -- Jupiter, Saturn, Uranus and Neptune -- are the JOVIAN or GIANT planets ('Jove' is another "
            "name for Jupiter). They are huge and made mostly of light gases, liquids and ices. There is nowhere to land: they "
            "are like giant spherical oceans with small, dense cores in the middle.\n\n"
            "You can see the difference in their densities. Density is mass divided by volume (for a sphere, volume = 4/3 x pi x "
            "radius cubed). Water has a density of 1 g/cm3 (that is 1,000 kg/m3). The terrestrial planets are 3.9 to 5.5 -- "
            "Earth, at 5.5, is the densest planet of all. The giants are only 0.7 to 1.6. Saturn, at 0.7, is less dense than "
            "water! Saturn's little moon Mimas has a density of about 1.2, so it must be made mostly of ice, not rock.\n\n"
            "THE PLANET NUMBERS (distance in AU / year / diameter / density)\n"
            "• Mercury: 0.39 AU / 0.24 y / 4,878 km / 5.4\n"
            "• Venus: 0.72 AU / 0.62 y / 12,120 km / 5.2\n"
            "• Earth: 1.00 AU / 1.00 y / 12,756 km / 5.5\n"
            "• Mars: 1.52 AU / 1.88 y / 6,787 km / 3.9\n"
            "• Jupiter: 5.20 AU / 11.86 y / 142,984 km / 1.3\n"
            "• Saturn: 9.54 AU / 29.46 y / 120,536 km / 0.7\n"
            "• Uranus: 19.18 AU / 84.07 y / 51,118 km / 1.3\n"
            "• Neptune: 30.06 AU / 164.82 y / 49,660 km / 1.6\n"
            "(1 AU, an astronomical unit, is the distance from Earth to the Sun.) Notice the pattern: the farther out a planet "
            "is, the longer its year.\n\n"
            "Ancient people knew five planets besides Earth (Mercury, Venus, Mars, Jupiter, Saturn). Uranus and Neptune were "
            "only found after the telescope was invented.\n\n"
            "SPINNING RULE-BREAKERS\n\n"
            "Every planet spins on an axis, and most spin in the same direction they orbit. The rule-breakers: Venus spins "
            "backward (retrograde), and very slowly. Uranus and Pluto are tipped nearly on their sides. We don't yet know how "
            "Eris, Haumea and Makemake spin.\n\n"
            "BEYOND NEPTUNE: DWARF PLANETS AND TNOs\n\n"
            "Past Neptune is a realm of icy worlds called trans-Neptunian objects (TNOs). Pluto was the first one found, in 1930. "
            "More than 3,900 are known now. Eris is about Pluto's size and has at least one moon; Pluto has five. The biggest "
            "TNOs are called dwarf planets, and so is Ceres, the largest asteroid. The five known dwarf planets are Eris, "
            "Haumea, Pluto, Ceres and Makemake. Pluto's orbit is tilted out of the planets' flat plane. NASA's New Horizons "
            "flew past Pluto in July 2015 (photographing the bright Sputnik Plain) and later visited the TNO Arrokoth.\n\n"
            "THE SUN UP CLOSE\n"
            "The Sun is 1,392,000 km across (about 109 Earths side by side), weighs 1.989 x 10^30 kg, and is about 74% hydrogen and "
            "25% helium. Deep in its core, at about 15,000,000 C, hydrogen is squeezed into helium by nuclear fusion, releasing the "
            "energy that lights the solar system (3.846 x 10^26 watts!). That energy creeps outward through the RADIATIVE ZONE, then "
            "gets carried up by boiling gas in the CONVECTION ZONE, and finally shines from the visible surface, the PHOTOSPHERE "
            "(about 6,000 C). Above that are the CHROMOSPHERE, a thin TRANSITION REGION and the wispy CORONA -- which is strangely "
            "hotter than the surface, about 1,000,000 C. The Sun is an ordinary star about halfway through its life.\n\n"
            "THE SMALLER MEMBERS\n"
            "• Moons: about 430 known, orbiting planets and dwarf planets. Only Mercury and Venus have none. The biggest -- our "
            "Moon, Jupiter's four Galilean moons, Saturn's Titan and Neptune's Triton -- are as big and interesting as small planets.\n"
            "• Rings: all four giant planets have rings made of countless pieces, from mountain-sized chunks to dust, circling "
            "the planet's equator. Saturn's are the brightest; moons shape all of them.\n"
            "• Asteroids: rocky, airless leftovers, mostly in the main belt between Mars and Jupiter, where Jupiter's gravity kept "
            "them from building a planet. They come in types: dark carbon-rich C-types (most common), stony S-types and metal-rich "
            "M-types. Some, like Eros, cross Earth's orbit; Mars' small moons are probably captured asteroids.\n"
            "• Comets: 'dirty snowballs' of frozen water, carbon dioxide and carbon monoxide. Near the Sun the ice of the solid "
            "NUCLEUS turns to gas, making a fuzzy COMA and long TAILS. Periodic comets come back within about 200 years (like "
            "Halley's); long-period comets take thousands to millions of years. They live in two deep freezers: the KUIPER BELT "
            "(about 30-50 AU out, just past Neptune) and the far more distant OORT CLOUD (a huge shell with about 40 Earths' worth "
            "of icy bodies).\n"
            "• Dwarf planets: round from their own gravity, but they haven't cleared their orbits. The five known: Ceres, Pluto, "
            "Eris, Haumea and Makemake. The ones beyond Neptune are called PLUTOIDS (Pluto, Haumea, Makemake, Eris); Sedna is a "
            "candidate with an 11,518-year orbit!\n"
            "• Cosmic dust: bits of broken rock. When they hit our air (millions a day!) they burn up as METEORS, or 'shooting "
            "stars'. A piece that survives and lands is a METEORITE.\n\n"
            "HOW WE EXPLORED IT\n\n"
            "Planetary astronomy is the one part of astronomy where we can actually visit what we study: robot explorers have flown "
            "past, orbited or landed on every planet. The people and spacecraft behind these discoveries have their own chapter: "
            "'Astronomers & Space Missions'."
        ),
        "concepts": [
            {
                "term": "Solar system vs. planetary system",
                "badge": ("Sol", "our star", SUN),
                "analogy": "Every family has a last name -- 'planetary system' is the general word, and 'solar system' is the special name for OUR star's family.",
                "explanation": "The solar system is the Sun plus everything that orbits it: planets, their moons and rings, asteroids, comets and dust. A group of planets and bodies circling any star is a planetary system; ours is the 'solar' system because the Sun is sometimes called Sol. Strictly speaking, there is only one solar system. Most of its members formed together with the Sun about 4.5 billion years ago from one huge cloud of gas and dust: the center became the Sun and a small fraction of the outer material became everything else.",
                "why": "Tests love vocabulary precision: an exoplanet orbits a star in a different PLANETARY system, not 'another solar system'.",
            },
            {
                "term": "The Sun holds 99.8% of the mass",
                "badge": ("99.8%", "the Sun", SUN),
                "analogy": "If the solar system were a 1,000-pound pile, the Sun would be 998 pounds and everything else would share the last 2 pounds.",
                "explanation": "Table 7.1: Sun 99.80%; Jupiter 0.10%; comets 0.0005-0.03% (estimate); all other planets and dwarf planets 0.04%; moons and rings 0.00005%; asteroids 0.000002% (estimate); cosmic dust 0.0000001% (estimate). The Sun is about 1.4 million km across, brighter than about 80% of the Galaxy's stars, and millions of degrees inside. Jupiter is more massive than all other planets combined, and about 1,300 Earths could fit inside it. Planet masses were first found using Kepler's laws and Newton's gravity (tugs on each other and on moons) and are now measured precisely by tracking spacecraft that fly past.",
                "why": "Ranking questions ('which holds most of the mass after the Sun?') -- the answer is Jupiter, not 'all the planets'.",
            },
            {
                "term": "The Sun up close",
                "badge": ("15M°C", "core", SUN),
                "analogy": "The Sun is a giant nuclear furnace: in its core, hydrogen is squeezed into helium and the leftover energy shines out as light.",
                "explanation": "Diameter 1,392,000 km (about 109 Earths across); mass 1.989 x 10^30 kg; luminosity 3.846 x 10^26 watts (3.846 x 10^33 erg/s); about 74% hydrogen and 25% helium. It makes energy by nuclear fusion of hydrogen into helium in its core. Its layers, from the center out: CORE (about 15,000,000 C) -> RADIATIVE ZONE (energy creeps out as light, ~2,000,000 C) -> CONVECTION ZONE (hot gas rises and sinks like boiling water) -> PHOTOSPHERE (the visible surface, ~6,000 C) -> CHROMOSPHERE -> TRANSITION REGION -> CORONA (the thin outer atmosphere, strangely about 1,000,000 C). The Sun is an ordinary star about halfway through its life, and it slowly brightens over time -- it is at least 30% brighter than 4 billion years ago.",
                "why": "Sun facts and layer order are classic short-answer questions, and the Sun's brightening moves the habitable zone.",
            },
            {
                "term": "Terrestrial planets",
                "badge": ("ROCK", "inner 4", ROCK),
                "analogy": "Terrestrial planets are like rocky marbles: small, heavy for their size, and you could stand on them.",
                "explanation": "Mercury, Venus, Earth and Mars (and the Moon is often grouped with them, making five terrestrial objects). They are relatively small, made mostly of rock and metal, and all have solid surfaces that record their history as craters, mountains and volcanoes. They are dense: from 3.9 g/cm3 (Mars) to 5.5 g/cm3 (Earth, the densest planet). Their heavy-element makeup (iron, silicon) shows the light gases and ices were lost in the hot inner part of the young solar system.",
                "why": "Habitability starts here: only solid-surfaced worlds can hold surface oceans like Earth's.",
            },
            {
                "term": "Jovian (giant) planets",
                "badge": ("GAS", "outer 4", GAS),
                "analogy": "A giant planet is like a huge ball of soda with a small pebble in the middle -- no ground to stand on.",
                "explanation": "Jupiter, Saturn, Uranus and Neptune, named after 'Jove' (Jupiter). They are much larger and made mostly of light ices, liquids and gases, with no solid surface -- more like vast spherical oceans around much smaller dense cores. Densities are low: Jupiter 1.3, Saturn 0.7 (less than water!), Uranus 1.3, Neptune 1.6 g/cm3. All four have ring systems and many moons. They formed in the cold outer disk where ice was available to build big cores.",
                "why": "Giant planets themselves fail the habitability test (no surface), but their icy moons are top targets for life.",
            },
            {
                "term": "Planet data table (Table 7.2)",
                "badge": ("AU", "the numbers", BLUE),
                "analogy": "Like a baseball card for each planet -- distance, year, day, size, weight and density.",
                "explanation": "Distance (AU) / year / day (one spin) / diameter (km) / mass (10^23 kg) / density (g/cm3): Mercury 0.39 AU / 0.24 y (87.97 days) / 58.6 days / 4,878 / 3.3 / 5.4. Venus 0.72 / 0.62 y (224.7 days) / 243 days, backward / 12,120 / 48.7 / 5.2. Earth 1.00 / 1.00 y / 1 day / 12,756 / 59.8 / 5.5. Mars 1.52 / 1.88 y / 1.03 days / 6,787 / 6.4 / 3.9. Jupiter 5.20 / 11.86 y / 0.41 days (~10 hours, the shortest day) / 142,984 / 18,991 / 1.3. Saturn 9.54 / 29.46 y / 0.42 days / 120,536 / 5,686 / 0.7. Uranus 19.18 / 84.07 y / 0.72 days / 51,118 / 866 / 1.3 (discovered 1781). Neptune 30.06 / 164.82 y / 0.67 days / 49,660 / 1,030 / 1.6 (discovered 1846). An AU (astronomical unit) is the Earth-Sun distance. Five planets were known to the ancients; Uranus and Neptune were found with telescopes. Notice: farther out = longer year (Kepler's third law), and Venus' day is longer than its year!",
                "why": "Put this table on your note sheet -- it powers Kepler's third law, density and comparison questions.",
            },
            {
                "term": "Density = mass / volume",
                "badge": ("ρ=m/V", "density", PURPLE),
                "analogy": "A bowling ball and a beach ball can be the same size, but one is packed with stuff -- that's density.",
                "explanation": "Density tells what a world is made of. Volume of a sphere: V = (4/3) x pi x R^3. Water has density 1 g/cm3 = 1,000 kg/m3 (multiply g/cm3 by 1,000 to get kg/m3). Saturn's moon Mimas (about 400 km across, radius 200 km) works out to roughly 1.2 g/cm3, so it is mainly ice, not rock. Earth works out to about 5.5 g/cm3, four to five times Mimas -- Earth is the densest planet. Rock is ~3 g/cm3, so a density above that means a metal core.",
                "why": "Exoplanet questions combine transit size + Doppler mass into density to decide 'rocky, watery or gassy'.",
            },
            {
                "term": "Orbits and spins (and the rule-breakers)",
                "badge": ("SAME", "direction", GOLD),
                "analogy": "Like cars on a giant flat racetrack, each planet stays in its own lane and drives the same direction.",
                "explanation": "All eight planets revolve around the Sun in the same direction, in nearly the same plane, on nearly circular orbits, obeying the laws found by Galileo, Kepler and Newton. Each planet also rotates (spins) on an axis, usually in the same direction it revolves. Exceptions: Venus rotates backward (retrograde) and very slowly; Uranus and Pluto spin with their axes tipped nearly on their sides. The spins of Eris, Haumea and Makemake are not yet known. These exceptions are probably scars of giant collisions during formation.",
                "why": "The shared direction and plane are the #1 clue that everything formed from one spinning disk.",
            },
            {
                "term": "Dwarf planets, Plutoids and TNOs",
                "badge": ("TNO", "past Neptune", ICE),
                "analogy": "Dwarf planets are like kids who are big enough to be round but haven't cleaned up their room (their orbit) yet.",
                "explanation": "A DWARF PLANET is round because of its own gravity, orbits the Sun, has NOT cleared its orbital neighborhood of other objects, and is not a moon. The five currently known dwarf planets are Ceres (the largest asteroid, in the main belt), Pluto, Eris, Haumea and Makemake. A PLUTOID is a dwarf planet that orbits beyond Neptune -- the four official Plutoids are Pluto, Haumea, Makemake and Eris. Sedna is a Plutoid candidate (not official yet) with an extremely stretched orbit lasting about 11,518 years. Objects beyond Neptune are called trans-Neptunian objects (TNOs): Pluto was the first found (1930); more than 3,900 are now known. Eris is about Pluto's size and has at least one moon; Pluto has five (Charon is the biggest). Pluto's orbit is tilted out of the planets' plane. New Horizons flew past Pluto in July 2015 (photographing the bright Sputnik Plain) and later visited the TNO Arrokoth.",
                "why": "Definitions of dwarf planet vs. Plutoid vs. TNO are favorite test questions.",
            },
            {
                "term": "Moons and rings",
                "badge": ("~430", "known moons", "#a39e93"),
                "analogy": "Moons are a planet's pets that follow it everywhere; rings are a swarm of glittering pebbles circling its waist.",
                "explanation": "About 430 moons are known around planets and dwarf planets, and many small ones surely remain undiscovered. Only Mercury and Venus have no moons. The largest moons -- our Moon, Jupiter's four Galilean moons, Saturn's Titan and Neptune's Triton -- are as big and interesting as small planets. All four giant planets have rings: countless small bodies, from mountain-size to dust grains, orbiting the planet's equator. Saturn's bright rings are by far the easiest to see; all four ring systems have complicated shapes influenced by the pull of the moons.",
                "why": "Moons (not planets) are where most of the solar system's possible extra-terrestrial habitats are.",
            },
            {
                "term": "Asteroids and their types",
                "badge": ("C-S-M", "asteroids", ROCK),
                "analogy": "Asteroids are the crumbs left on the table after the planets were 'baked' -- and they still tell us the recipe.",
                "explanation": "Asteroids are small, rocky, airless bodies that orbit the Sun like miniature planets, mostly in the MAIN BELT between Mars and Jupiter. They are leftover planetesimals that never built a full planet, because Jupiter's strong gravity stirred them up and stopped them from clumping. Ongoing collisions have broken them into many sizes. Their makeup depends on how hot it was where they formed: C-type (dark, carbon-rich -- the most common), S-type (stony silicate rock, brighter) and M-type (metal-rich, like iron-nickel), plus several rarer classes. Some asteroids cross Earth's orbit, like Eros (orbited and landed on by NEAR-Shoemaker); others share Jupiter's orbit as Trojans. Objects smaller than about 400 km can be lumpy, like 60-km-long Ida; Mars' tiny moons are probably captured asteroids.",
                "why": "Asteroids preserve the solar system's original ingredients -- and can deliver water and organics.",
            },
            {
                "term": "Comets, the Kuiper Belt and the Oort Cloud",
                "badge": ("ICE", "comets", ICE),
                "analogy": "Comets are dirty snowballs stored in the solar system's deep freezer, which sprout glowing tails when they visit the Sun.",
                "explanation": "Comets are icy bodies -- frozen water, carbon dioxide and carbon monoxide mixed with dust -- formed in the cold outer solar system. A comet has a solid NUCLEUS; near the Sun its ices turn to gas, making a fuzzy COMA and long TAILS pointing away from the Sun (e.g. comet 67P, visited by Rosetta, with gas jets). PERIODIC (short-period) comets return in less than about 200 years (like Halley's Comet); NON-PERIODIC (long-period) comets take thousands to millions of years. They come from two reservoirs of leftover building blocks: the KUIPER BELT, a flat disk of icy objects about 30-50 AU from the Sun just beyond Neptune (home of Pluto and many dwarf planets), and the OORT CLOUD, a vast, distant, spherical shell of icy bodies (estimated mass about 40 Earths) thought to supply many comets. Dust left along a comet's path causes meteor showers when Earth passes through it.",
                "why": "Comets may have delivered water and organic molecules to young Earth.",
            },
            {
                "term": "Meteors and meteorites",
                "badge": ("ZOOM", "shooting star", GOLD),
                "analogy": "A meteor is a grain of space dust burning up like a spark; a meteorite is a piece tough enough to land.",
                "explanation": "Countless grains of broken rock, called cosmic dust, float through the solar system. When they enter Earth's atmosphere -- millions every day -- they burn up as a brief streak of light called a METEOR ('shooting star'). Many meteors seeming to come from one point in the sky (the radiant) form a METEOR SHOWER, made when Earth crosses a comet's dust trail. A piece that survives the trip and hits the ground is a METEORITE: irons (iron-nickel), stony-irons, and stones. The most primitive stones, carbonaceous meteorites like Murchison and Allende, date to the solar system's birth 4.5 billion years ago and contain organic molecules, including amino acids and sugars from space.",
                "why": "Meteorites are physical samples of the early solar system and of life's building blocks.",
            },
        ],
    },
    # ------------------------------------------------------------------ 2
    {
        "name": "Solar System: How the Solar System Was Born",
        "description": "The solar nebula model: the motion and chemistry clues, why the inner planets are rocky, planetesimals, giant impacts and differentiation.",
        "source_title": "Source reader: Origin of the Solar System (OpenStax Astronomy 2e, 7.4, 14.3, 14.5)",
        "infographics": ["nebula_steps", "star_lifecycle"],
        "source_text": (
            "Patterns among planets reveal the origin. All planets lie in nearly the same plane and revolve the same direction; "
            "the Sun spins the same way -> Sun and planets formed together from a spinning cloud of gas and dust, the SOLAR "
            "NEBULA. Composition (by spectroscopy): Sun has the same hydrogen-dominated composition as Jupiter and Saturn (same "
            "reservoir). Terrestrial planets and Moon are deficient in light gases and ices (from O, C, N); mostly heavy elements "
            "like iron and silicon -> lighter materials escaped from the inner region. Reason: the inner disk was hotter -- not "
            "mainly because of sunlight (it couldn't penetrate the dense disk) but because inner material moved faster (Kepler's "
            "laws) -> more friction -> too warm for water to condense as ice. So inner planets rocky; icy worlds farther out.\n"
            "Evidence from far away: many young stars have circumstellar disks (flattened spinning clouds of gas and dust), e.g. "
            "in the Orion Nebula seen by Hubble -- modern analogs of our solar nebula. Disks and stars form together.\n"
            "Building planets: material first forms planetesimals (precursors of planets), probably no larger than ~100 km. "
            "Computers simulate millions of them gathering under mutual gravity. The process was violent: collisions, sometimes "
            "disrupting growing planets. Impacts + radioactive heat melted planets -> differentiated (layers). Random giant "
            "collisions may explain exceptions: Uranus and Pluto spinning on their sides, Venus spinning slowly backward, the Moon "
            "resembling Earth yet different. Today, ~4.5 billion years later, things are calmer, but leftover fragments still "
            "roam and can hit Earth.\n"
            "Exoplanet systems differ: superearths (between terrestrial and giant sizes) are common; some have giant planets close "
            "to the star (reverse of ours).\n"
            "Summary (14.3): a viable theory must satisfy motion, chemical and age constraints. Meteorites, comets and asteroids "
            "are survivors of the solar nebula, which came from a collapsing interstellar cloud that conserved angular momentum, "
            "forming the Sun and a thin spinning disk. Condensation -> planetesimals -> planets. Accretion heated planets -> "
            "differentiation. Giant planets also captured gas from the nebula. After a few million years of violent impacts, "
            "most debris was swept up or ejected; stable leftovers remain in the asteroid belt (Mars-Jupiter) and Kuiper belt "
            "(beyond Neptune) as asteroids, comets and TNOs. Orbital shifts of Jupiter and Saturn in the first few hundred "
            "million years may have scattered asteroids inward, causing the 'heavy bombardment' seen in the oldest lunar craters.\n"
            "Planetary evolution (14.5): giant impacts mostly within the first 100 million years, ending ~4.4 billion years ago; "
            "planets kept gaining volatiles and heavy cratering until ~4 billion years ago; then each followed its own course set "
            "by composition, mass and distance from the Sun."
        ),
        "story": (
            "A CLOUD THAT BECAME A FAMILY\n\n"
            "Astronomers are a bit like detectives. Nobody was around 4.5 billion years ago to watch the solar system form, so we "
            "look for clues -- patterns the planets still carry today.\n\n"
            "CLUE 1: EVERYTHING MOVES THE SAME WAY\n\n"
            "All the planets orbit in nearly the same flat plane and in the same direction, and the Sun spins in that same "
            "direction too. That's not a coincidence. It tells us the Sun and planets were born together from one spinning cloud "
            "of gas and dust. We call that cloud the SOLAR NEBULA. As it collapsed, it spun faster (like a figure skater pulling "
            "in her arms -- conservation of angular momentum) and flattened into a disk.\n\n"
            "CLUE 2: THE CHEMISTRY\n\n"
            "Using spectroscopy (reading the light from objects), we find the Sun has the same hydrogen-rich recipe as Jupiter "
            "and Saturn -- they came from the same reservoir. But Earth, its rocky neighbors and the Moon are short on the light "
            "gases and on ices made from oxygen, carbon and nitrogen. Instead they're mostly heavier, rarer elements like iron "
            "and silicon. The light stuff must have escaped from the inner solar system, leaving the heavy stuff behind.\n\n"
            "WHY WAS THE INNER DISK SO HOT?\n\n"
            "You might guess 'because it was close to the Sun'. Surprise: the dense disk blocked most sunlight. The real reason "
            "is speed. By Kepler's laws, material closer in orbits faster, so particles rubbed and bumped more -- more friction, "
            "more heat. Near the Sun it was too warm for water to freeze into ice. So the inner planets were built of rock and "
            "metal, and the icy worlds formed farther out. (The boundary where ice can survive is often called the frost line.)\n\n"
            "CLUE 3: WE CAN SEE OTHER 'SOLAR NEBULAS' TODAY\n\n"
            "We can't rewind time, but many stars are much younger than the Sun. Around them the Hubble Space Telescope sees "
            "circumstellar disks -- flattened, spinning clouds of gas and dust -- for example in the Orion Nebula, a nearby "
            "star-forming region. These disks are modern-day versions of our own solar nebula, places where planets are "
            "probably forming right now. Since young stars almost always have disks, disks and stars must form together.\n\n"
            "BUILDING PLANETS: A ROUGH CONSTRUCTION SITE\n\n"
            "As a disk cools, its dust clumps into small solid bodies called PLANETESIMALS -- the building blocks of planets, "
            "probably no bigger than about 100 km. Computer models follow millions of them pulling together by gravity. It was "
            "violent: planetesimals smashed into each other and sometimes even broke apart growing planets. Those impacts, plus "
            "heat from radioactive elements, melted the young planets so that heavy metal sank and lighter rock floated up. "
            "That separation into layers is called DIFFERENTIATION, and it explains the layered insides of planets today.\n\n"
            "Random giant collisions might also explain the solar system's oddballs: why Uranus and Pluto spin on their sides, "
            "why Venus spins slowly backward, and why the Moon is like Earth in many ways but different in others.\n\n"
            "The giant planets did one extra thing: their big cores grabbed and held gas straight from the nebula.\n\n"
            "CLEANING UP\n\n"
            "After a few million years of crashes, most debris had been swept up by planets or flung out of the system. Only in "
            "two places could leftover planetesimals orbit safely: the ASTEROID BELT between Mars and Jupiter and the KUIPER BELT "
            "beyond Neptune. Their survivors are today's asteroids, comets and trans-Neptunian objects -- and their meteorite "
            "fragments are free samples of the early solar system.\n\n"
            "Newer studies suggest Jupiter and Saturn shifted their orbits during the first few hundred million years. Because "
            "their gravity controls the asteroids, that may have flung asteroids inward, causing the 'heavy bombardment' "
            "recorded in the Moon's oldest craters.\n\n"
            "TIMELINE OF THE EARLY DAYS\n"
            "• ~4.5 billion years ago: the solar nebula collapses; the Sun and disk form.\n"
            "• First ~100 million years: the era of giant impacts, ending by about 4.4 billion years ago.\n"
            "• Until ~4 billion years ago: planets keep collecting volatile materials and get heavily cratered.\n"
            "• After that: each world follows its own path, set by its composition, mass and distance from the Sun.\n\n"
            "A HUMBLE NOTE\n\n"
            "Thousands of planets found around other stars show that many planetary systems look nothing like ours. Many have "
            "'super-Earths' (between Earth and Neptune in size), and some have giant planets hugging their stars -- the reverse "
            "of our order. A good theory must explain them too (see the exoplanet chapters).\n\n"
            "THE LIFE OF A STAR\n"
            "Our Sun is just one star, and stars have life stories. A star is born when a cold, dense clump of a nebula collapses "
            "into a PROTOSTAR, heating up as it shrinks. Once its core is hot enough to fuse hydrogen, it becomes a MAIN-SEQUENCE "
            "star and shines steadily for most of its life. A Sun-like star later swells into a RED GIANT, puffs off its outer "
            "layers, and leaves a small, hot WHITE DWARF. A much heavier star becomes a RED SUPERGIANT and explodes as a SUPERNOVA, "
            "leaving a NEUTRON STAR or a BLACK HOLE. Supernovas spread heavy elements through space -- the iron, oxygen and carbon "
            "that later build planets and people.\n\n"
            "A GOOD THEORY MUST PASS THREE TESTS\n"
            "• Motion: same plane, same direction, Sun's spin.\n"
            "• Chemistry: rocky inside, icy and gassy outside.\n"
            "• Age: meteorites, comets and asteroids date back to ~4.5 billion years."
        ),
        "concepts": [
            {
                "term": "Solar nebula",
                "badge": ("NEB", "the cloud", PURPLE),
                "analogy": "Like pizza dough tossed in the air: as it spins it flattens into a disk, with a thick lump (the Sun) in the middle.",
                "explanation": "The solar nebula is the spinning cloud of gas and dust from which the Sun and all planets formed about 4.5 billion years ago. An interstellar cloud collapsed; conserving angular momentum it spun faster and flattened into a thin disk around the newborn Sun. Evidence: all planets lie in nearly the same plane and revolve the same direction, and the Sun spins the same way. The solar nebula model explains many of the solar system's regularities.",
                "why": "This is the starting point for every planet-formation and habitability question.",
            },
            {
                "term": "The chemistry clue",
                "badge": ("Fe Si", "vs H", GOLD),
                "analogy": "Like a beach where waves washed away the light sand and left the heavy pebbles near the water.",
                "explanation": "Spectroscopy shows the Sun has the same hydrogen-dominated composition as Jupiter and Saturn, so they formed from the same reservoir. The terrestrial planets and the Moon are deficient in light gases and in ices made from oxygen, carbon and nitrogen; they are made mostly of rarer heavy elements such as iron and silicon. So the processes that built the inner planets must have excluded the lighter materials, which escaped and left a heavy residue.",
                "why": "Explains why habitable rocky planets form near stars while water-rich bodies form farther out.",
            },
            {
                "term": "Why the inner disk was hot",
                "badge": ("HOT", "friction", RED),
                "analogy": "Inner racers on a track move fastest and bump the most -- all that rubbing makes heat.",
                "explanation": "The inner disk was hotter, but NOT mainly from sunlight -- the Sun's rays had trouble penetrating the dense disk. Material closer to the center moved faster (Kepler's laws), causing more friction among particles, which heated the inner disk to high temperatures. It was too warm for water to condense as ice, so the inner planets became rocky and icy worlds formed farther from the Sun. The same pattern appears in Jupiter's moons: rocky Io and Europa close in, icy Ganymede and Callisto farther out.",
                "why": "A classic 'gotcha' question: the answer is orbital speed/friction, not sunlight.",
            },
            {
                "term": "Frost line (snow line)",
                "badge": ("ICE", "line", ICE),
                "analogy": "Like the line on a mountain above which snow stays frozen all year.",
                "explanation": "The distance from a young star beyond which it is cold enough for water (and other volatiles like ammonia and methane) to freeze into solid ice grains. Inside it, only rock and metal can condense, giving rocky terrestrial planets; outside it, ice is plentiful, so solid cores can grow big enough to capture gas and become giant planets. Giant planets cannot form without condensing water ice -- which is why hot Jupiters must have formed beyond the frost line and migrated inward.",
                "why": "Frost line + migration is the key to explaining hot and cold Jupiters on exoplanet questions.",
            },
            {
                "term": "Planetesimals",
                "badge": ("100", "km max", ROCK),
                "analogy": "Planetesimals are the LEGO bricks of planets -- millions of small pieces snapping together.",
                "explanation": "As a disk cools, material first coalesces into smaller solid objects called planetesimals, the precursors of planets -- probably no larger than about 100 km across. Fast computers simulate millions of planetesimals gathering under their mutual gravity to build the planets. The process was violent: planetesimals crashed into each other and sometimes disrupted the growing planets themselves. Survivors in stable zones became asteroids, comets and TNOs.",
                "why": "Planetesimal collisions explain heavy cratering and delivery of water/organics.",
            },
            {
                "term": "Differentiation",
                "badge": ("LAYERS", "melt & sort", GOLD),
                "analogy": "Like a salad dressing left to sit: heavy stuff sinks, light stuff floats into layers.",
                "explanation": "Violent impacts plus heat from radioactive elements heated young planets until they were liquid and gas, so they differentiated: dense metal sank to form cores while lighter rock rose to form mantles and crusts. This explains the planets' present internal structures. Not every body finished: Jupiter's moon Callisto froze before differentiation was complete.",
                "why": "Layering (cores, magnetic fields, oceans) is tied to whether a world can protect and support life.",
            },
            {
                "term": "Giant collisions explain the oddballs",
                "badge": ("BOOM", "impacts", RED),
                "analogy": "Like bumper cars: a big hit can leave a car spinning backward or tipped on its side.",
                "explanation": "Random collisions of massive planetesimals may explain exceptions to the solar system's 'rules': why Uranus and Pluto spin on their sides, why Venus spins slowly and backward, and why the Moon resembles Earth in many ways yet has substantial differences. The era of giant impacts was probably confined to the first 100 million years, ending about 4.4 billion years ago.",
                "why": "Shows formation was messy -- the same lesson exoplanets teach ('roller derby').",
            },
            {
                "term": "Asteroid belt and Kuiper belt survivors",
                "badge": ("BELTS", "safe zones", ROCK),
                "analogy": "After the party, a few guests are still hanging out in the two quiet corners of the room.",
                "explanation": "After a few million years of violent impacts, most debris was swept up by planets or ejected. Stable orbits were possible in two regions: the asteroid belt between Mars and Jupiter and the Kuiper belt beyond Neptune. The planetesimals (and fragments) surviving there are today's asteroids, comets and trans-Neptunian objects. Meteorites, comets and asteroids are survivors of the solar nebula -- samples of what the planets were made from.",
                "why": "These leftovers are time capsules of the original ingredients, including water and organics.",
            },
            {
                "term": "Heavy bombardment",
                "badge": ("4.1-3.8", "bya", RED),
                "analogy": "A cosmic hailstorm of space rocks pounding the young planets.",
                "explanation": "Studies of planet and asteroid orbits suggest violent events soon after formation, perhaps substantial changes in Jupiter's and Saturn's orbits during the first few hundred million years. Because those giants control the asteroids' distribution, asteroids may have been scattered into the inner solar system, causing the 'heavy bombardment' recorded in the oldest lunar craters (about 4.1 to 3.8 billion years ago). Planets kept being heavily cratered and gaining volatiles until about 4 billion years ago. It ended when the Sun was about 500 million years old.",
                "why": "Big impacts could have sterilized early Earth's surface -- a key date for when life could start.",
            },
            {
                "term": "Three tests for a formation theory",
                "badge": ("3", "constraints", BLUE),
                "analogy": "Like a detective's story that must match the fingerprints, the alibi AND the timeline.",
                "explanation": "A viable theory of solar system formation must satisfy (1) motion constraints -- planets in one plane, same direction, Sun spinning the same way; (2) chemical constraints -- rock and metal inside, ice and gas outside; and (3) age constraints -- the oldest materials (meteorites) date to about 4.5 billion years. The solar nebula model passes all three, while random giant impacts explain the exceptions.",
                "why": "Good framework for any 'explain the evidence' free-response question.",
            },
            {
                "term": "The life cycle of a star",
                "badge": ("STAR", "life cycle", SUN),
                "analogy": "Stars have life stories like people: born in a cloud, a long adulthood, and an ending that depends on how big they are.",
                "explanation": "Stars form in cold, dense regions of a nebula that collapse under their own gravity into a PROTOSTAR, which heats up as it shrinks. When its core gets hot and dense enough, hydrogen fusion starts and it becomes a MAIN-SEQUENCE star -- where it spends most of its life (the Sun is about halfway through). Low- to medium-mass stars like the Sun later swell into RED GIANTS, puff off their outer layers, and leave behind a hot, dense WHITE DWARF. High-mass stars become RED SUPERGIANTS and explode as a SUPERNOVA, leaving a NEUTRON STAR or a BLACK HOLE. Supernovas scatter heavy elements (like iron, carbon and oxygen) into space, where they become part of new stars, planets -- and people.",
                "why": "Star evolution is the background for planet formation and for 'we are made of star stuff'.",
            },
        ],
    },
    # ------------------------------------------------------------------ 3
    {
        "name": "Solar System: Earth as a Planet",
        "description": "Earth's properties, interior layers, magnetic shielding, atmosphere layers and composition, where our air came from, weather, the greenhouse effect and climate change.",
        "source_title": "Source reader: Earth as a Planet (OpenStax Astronomy 2e, 8.1, 8.3, 8.4)",
        "infographics": ["earth_interior", "atmosphere_layers", "greenhouse"],
        "source_text": (
            "Earth: medium-size, diameter ~12,760 km (12,756 km), terrestrial, mostly heavy elements iron, silicon, oxygen (unlike "
            "the Sun's hydrogen and helium). Nearly circular orbit; only planet 'just right' for liquid surface water. Table 8.1: "
            "semimajor axis 1.00 AU; period 1.00 year; diameter 12,756 km; radius 6,378 km; escape velocity 11.2 km/s; rotation "
            "23 h 56 m 4 s; density 5.514 g/cm3; atmospheric pressure 1.00 bar. 'Blue Marble' photo by Apollo 17.\n"
            "INTERIOR: studied indirectly; we know the top few km of crust best -- we know less about 5 km beneath our feet than "
            "the surfaces of Venus and Mars. Metal + silicate rock, mostly solid, some molten. Seismic waves from earthquakes or "
            "explosions travel like sound in a struck bell; they bend (refract) between layers so some stations are in "
            "'shadows'; a network of seismographs builds a model of liquid and solid layers (like ultrasound). Layers: crust, "
            "mantle, liquid outer core, solid inner core. Oceanic crust: 55% of surface, ~6 km thick, basalt (silicon, oxygen, "
            "iron, aluminum, magnesium). Continental crust: 45%, 20-70 km thick, mostly granite. Crust density ~3 g/cm3 (water "
            "1); crust only ~0.3% of Earth's mass. Mantle: from base of crust to 2,900 km depth, more or less solid.\n"
            "ATMOSPHERE: ozone (O3) layer near top of stratosphere absorbs UV, protecting life; its breakup heats the "
            "stratosphere, reversing the troposphere's decreasing-temperature trend. CFCs destroyed ozone (clear by 1980s); "
            "phased out by international agreement; ozone loss stopped and the Antarctic 'ozone hole' is shrinking. Above 100 km "
            "the air is so thin satellites pass with little friction; many atoms ionized (ionosphere); atoms can escape, "
            "especially light ones (hydrogen, helium leak away). Mars' thin air came from leakage; Venus' dry air because nearby "
            "Sun vaporized and broke apart its water, gases lost to space.\n"
            "COMPOSITION at surface: 78% N2, 21% O2, 1% Ar, traces of H2O, CO2 and others, plus dust and droplets. Volatiles "
            "evaporate at low temperatures. If heated above 100 C (373 K) the oceans would boil: water to cover Earth ~300 m "
            "deep, 10 m of water = ~1 bar, so ~300 bars of water vapor. Carbonate rocks would release ~70 bars of CO2 (vs "
            "today's 0.0005 bar). A warm Earth: ~400 bars of water vapor + CO2. Volcanoes release CO2, H2O, SO2 (but burning "
            "fossil fuels releases far more CO2 than volcanoes; much volcanic gas is recycled by plate tectonics). Origin of air "
            "and oceans: (1) formed with Earth from debris, (2) released from interior by volcanism, (3) delivered by comet and "
            "asteroid impacts; evidence favors interior + impacts.\n"
            "WEATHER = circulation of the atmosphere, powered mainly by sunlight heating the surface; rotation and seasons vary "
            "sunlight; air and oceans move heat from warm to cool areas.\n"
            "GREENHOUSE EFFECT: sunlight passes through air, heats ground, ground re-emits infrared; CO2, methane and water vapor "
            "absorb infrared, trapping heat like a blanket; surface warms until energy radiated to space equals energy received. "
            "More CO2 -> higher balance temperature. Like a greenhouse or a car with windows up. Current greenhouse effect raises "
            "Earth's surface ~23 C (chapter 8; chapter 30 says ~33 C); without it Earth would be below freezing in a global ice "
            "age. Fossil fuels: CO2 up ~30% in the past century, rising >0.5%/year, predicted to double pre-industrial level "
            "before 2100; deforestation worsens it; isotopes show added CO2 is from fossil fuels. Climate change: records broken, "
            "all but one hottest years since 2000, glaciers retreating, Arctic ice thinner, sea level rising (melting + warm water "
            "expanding); highest temperatures in >50 million years. Fossil-fuel CO2 is 100x volcanic. Human impacts: early "
            "hunters killed megafauna (diprotodon, zygomaturus, 10-ft kangaroos, mammoths, saber-tooth cats, mastodons, giant "
            "sloths, camels), farmers cut forests, Polynesian expansion doomed large birds. Proposed epoch name: anthropocene."
        ),
        "story": (
            "OUR HOME, VIEWED AS A PLANET\n\n"
            "To understand other worlds, start with the one we know best. From space, Earth is a medium-size rocky planet about "
            "12,760 km across -- the famous 'Blue Marble' photo was taken by the Apollo 17 astronauts. Unlike the Sun (mostly "
            "hydrogen and helium), Earth is made mostly of heavy elements: iron, silicon and oxygen. Its orbit is nearly a "
            "circle, and it is the only planet in our solar system that is neither too hot nor too cold, but 'just right' for "
            "liquid water on its surface.\n\n"
            "EARTH'S STATS\n"
            "• Distance from Sun (semimajor axis): 1.00 AU; year: 1.00\n"
            "• Diameter 12,756 km; radius 6,378 km\n"
            "• Density 5.514 g/cm3 (the densest planet)\n"
            "• Escape velocity 11.2 km/s\n"
            "• Rotation: 23 h 56 m 4 s\n"
            "• Air pressure at the surface: 1.00 bar\n\n"
            "A JOURNEY TO THE CENTER OF THE EARTH\n\n"
            "Here is a surprising fact: we know less about the rock 5 km under our feet than about the surfaces of Venus and "
            "Mars! We can only touch the top few kilometers of crust. So how do we know what's inside? We listen.\n\n"
            "Earthquakes (and explosions) send SEISMIC WAVES through the planet, the way a struck bell rings. A bell's sound "
            "depends on what it's made of; a planet's 'ring' depends on its layers. Some waves travel along the surface and "
            "others go straight through. When they cross from one material to another, they bend (refract), just like light in "
            "a telescope lens. That leaves some seismograph stations in 'shadows' where waves never arrive. Comparing many "
            "stations lets scientists map which layers are liquid and which are solid -- a bit like an ultrasound scan of the "
            "planet.\n\n"
            "The layers, from outside in:\n"
            "• CRUST -- the thin outer skin. Oceanic crust covers 55% of Earth, is about 6 km thick and made of dark volcanic "
            "basalt (silicon, oxygen, iron, aluminum, magnesium). Continental crust covers 45%, is 20 to 70 km thick and made "
            "mostly of granite. Both have densities of about 3 g/cm3. The crust is only about 0.3% of Earth's mass!\n"
            "• MANTLE -- the biggest part of the solid Earth, from the base of the crust down to 2,900 km. It's more or less solid.\n"
            "• OUTER CORE -- liquid metal.\n"
            "• INNER CORE -- solid metal at the very center, 6,378 km down.\n\n"
            "OUR BLANKET OF AIR\n\n"
            "Near the ground, air is 78% nitrogen, 21% oxygen and 1% argon, with traces of water vapor, carbon dioxide and other "
            "gases, plus dust and water droplets.\n\n"
            "The atmosphere comes in layers. We live in the TROPOSPHERE, where weather happens and it gets colder as you climb. "
            "Above it is the STRATOSPHERE, with the precious OZONE LAYER near the top. Ozone (O3) is oxygen with three atoms "
            "instead of two. It absorbs much of the Sun's dangerous ultraviolet light -- that's what makes life on land "
            "possible -- and the energy it absorbs warms the stratosphere, flipping the temperature trend. In the 1980s we "
            "learned that chemicals called CFCs were destroying ozone. Countries agreed to phase them out, ozone loss stopped, "
            "and the Antarctic 'ozone hole' is slowly shrinking -- proof that teamwork can protect a planet's habitability.\n\n"
            "Higher still, above 100 km, the air is so thin that satellites glide through. Ultraviolet light knocks electrons off "
            "atoms, so this region is called the IONOSPHERE. Up here, some atoms -- especially light, fast ones like hydrogen and "
            "helium -- escape into space. Earth slowly leaks its atmosphere. Leakage is also why Mars has thin air, and why Venus "
            "is dry: sunlight broke apart its water and the pieces were lost to space.\n\n"
            "WHAT IF EARTH GOT HOTTER?\n\n"
            "'Volatile' materials evaporate at fairly low temperatures. If Earth were heated past 100 C (373 K), the oceans would "
            "boil. There is enough water to cover the whole Earth about 300 m deep, and every 10 m of water presses like 1 bar, so "
            "the boiled oceans would make a 300-bar atmosphere of steam! Heat the carbonate rocks too and they'd release about "
            "70 bars of carbon dioxide (today we have only 0.0005 bar). A hot Earth would have a crushing ~400-bar atmosphere of "
            "water vapor and CO2 -- remember that when you meet Venus.\n\n"
            "WHERE DID OUR AIR AND OCEANS COME FROM?\n"
            "Three ideas: (1) they came with the debris that built Earth, (2) volcanoes released them from the interior later, "
            "or (3) comets and asteroids from the outer solar system delivered them. The evidence favors a mix of the interior "
            "and impacts. Volcanoes still release CO2, water and sulfur dioxide -- though much of it is recycled by plate "
            "tectonics, and today burning fossil fuels releases far more CO2 than volcanoes (about 100 times more).\n\n"
            "WEATHER\n"
            "Any planet with an atmosphere has weather: the circulation of its air. The energy comes mostly from sunlight "
            "heating the surface. Earth's spin and the seasons change how much sunlight hits each place, and the air and oceans "
            "carry heat from warm areas to cool ones.\n\n"
            "THE GREENHOUSE EFFECT\n\n"
            "Sunlight passes through the air and warms the ground. The warm ground gives off invisible infrared (heat) radiation. "
            "Gases like carbon dioxide, methane and water vapor let sunlight in but absorb infrared, so they act like a blanket. "
            "The surface has to warm up until the heat escaping to space balances the sunlight coming in. More CO2 means a "
            "warmer balance point. It's like a car parked in the sun with the windows up: glass lets sunlight in but slows the "
            "heat escaping.\n\n"
            "The good news: Earth's natural greenhouse effect keeps us comfortable. Without it, Earth would be well below freezing, "
            "locked in a global ice age. (One chapter of the source says it adds about 23 C; another says about 33 C -- know both.)\n\n"
            "The bad news: burning coal and oil -- energy stored by plants millions of years ago -- releases CO2, and cutting "
            "tropical forests removes the plants that soak it up. CO2 rose about 30% in the past century, keeps rising more than "
            "0.5% per year, and should double its pre-industrial level before 2100. The fingerprints (isotopes) of the extra CO2 "
            "show it comes from fossil fuels. Records keep breaking: all but one of the hottest years on record came after 2000, "
            "glaciers are shrinking, Arctic sea ice is thinner, and seas are rising from melting ice and warming water that "
            "expands. We're heading toward the highest temperatures in more than 50 million years.\n\n"
            "HUMANS AS A PLANETARY FORCE\n"
            "This isn't the first time people reshaped Earth. Early hunters wiped out giant animals -- diprotodons and 10-foot "
            "kangaroos in Australia; mammoths, mastodons, saber-tooth cats, giant sloths and camels in North America and Asia. "
            "Early farmers cut most forests in Europe and China, and the Polynesian expansion doomed large Pacific birds. "
            "Scientists have proposed calling our time the ANTHROPOCENE, the age when humans became the dominant influence on "
            "the planet."
        ),
        "concepts": [
            {
                "term": "Earth's vital statistics",
                "badge": ("1 AU", "home", BLUE),
                "analogy": "Earth is the 'just right' bowl of porridge -- not too hot, not too cold for liquid water.",
                "explanation": "Table 8.1: semimajor axis 1.00 AU, period 1.00 year, diameter 12,756 km, radius 6,378 km, escape velocity 11.2 km/s, rotation 23 h 56 m 4 s, density 5.514 g/cm3, surface pressure 1.00 bar. Earth is a medium-size terrestrial planet made mostly of iron, silicon and oxygen, very different from the Sun's hydrogen and helium. Its orbit is nearly circular and it is the only planet in our solar system with liquid water on its surface -- 'just right' for life as we know it.",
                "why": "Earth is the benchmark: exoplanet and habitability questions compare everything to Earth = 1.",
            },
            {
                "term": "Seismic waves",
                "badge": ("WAVES", "seismic", PURPLE),
                "analogy": "Tapping a watermelon to tell if it's ripe -- the sound reveals what's inside without cutting it.",
                "explanation": "Earth's interior is studied indirectly by measuring seismic waves from earthquakes or explosions. They travel through the planet like sound through a struck bell; a planet's response depends on its composition and structure. Some waves travel along the surface, others through the interior. Crossing between materials they bend (refract), so some seismic stations receive waves and others are in 'shadows'. A network of seismographs reveals liquid and solid layers, similar to medical ultrasound. We know less about rock 5 km down than about the surfaces of Venus and Mars.",
                "why": "Same logic lets missions infer hidden oceans from gravity and magnetic data on icy moons.",
            },
            {
                "term": "Earth's layers",
                "badge": ("4", "layers", GOLD),
                "analogy": "Earth is like a peach: thin skin (crust), thick fruit (mantle), and a hard pit (core).",
                "explanation": "Crust: oceanic crust covers 55% of the surface, about 6 km thick, volcanic basalt (silicon, oxygen, iron, aluminum, magnesium); continental crust covers 45%, 20-70 km thick, mostly granite (silicates); both about 3 g/cm3; the crust is only ~0.3% of Earth's mass. Mantle: largest part of the solid Earth, from the base of the crust to 2,900 km deep, more or less solid. Outer core: liquid metal. Inner core: solid metal. Earth is composed largely of metal and silicate rock.",
                "why": "A molten metal core makes a magnetic field; layering is compared across planets and moons.",
            },
            {
                "term": "Ozone layer",
                "badge": ("O₃", "UV shield", ICE),
                "analogy": "Ozone is Earth's sunscreen -- a layer of SPF high in the sky.",
                "explanation": "Near the top of the stratosphere is a layer of ozone (O3: three oxygen atoms instead of the usual two). Ozone absorbs ultraviolet light, protecting the surface from dangerous UV and making life possible on land. Its breakup heats the stratosphere, reversing the troposphere's falling temperature. In the 1980s it became clear that human-made chlorofluorocarbons (CFCs) were destroying ozone; international agreement phased them out, ozone loss stopped, and the Antarctic ozone hole is gradually shrinking. Ozone only formed after oxygen built up from photosynthesis.",
                "why": "Ozone/oxygen are biomarkers and shields -- both central to habitability.",
            },
            {
                "term": "Ionosphere and atmospheric escape",
                "badge": ("H↑", "leaks away", PURPLE),
                "analogy": "Light gas atoms are like the fastest kids at recess -- some run right off the playground.",
                "explanation": "Above 100 km the atmosphere is so thin that satellites orbit with little friction. Many atoms are ionized (lose an electron to solar UV) -- the ionosphere. There, atoms can occasionally escape Earth's gravity. Light atoms move faster than heavy ones, so hydrogen and helium leak away to space continuously. Leakage created Mars' thin atmosphere. Venus' dry atmosphere evolved because closeness to the Sun vaporized and split its water, and the pieces were lost to space.",
                "why": "Whether a planet can keep its air and water decides if it stays habitable.",
            },
            {
                "term": "Atmosphere composition",
                "badge": ("78/21", "N₂ / O₂", BLUE),
                "analogy": "Breathe in: about 4 out of every 5 molecules you inhale are nitrogen, 1 is oxygen.",
                "explanation": "At the surface: 78% nitrogen (N2), 21% oxygen (O2), 1% argon (Ar), with traces of water vapor (H2O), carbon dioxide (CO2) and other gases, plus variable dust and water droplets. Today's CO2 is only about 0.0005 bar. Earth is the only planet with free oxygen in its air -- a result of life. Without life, Earth's air would probably be dominated by CO2 like Venus and Mars.",
                "why": "An oxygen-rich atmosphere is the strongest known sign of a living planet.",
            },
            {
                "term": "Volatiles and a 'hot Earth'",
                "badge": ("400", "bars", RED),
                "analogy": "Heat a pot of soup and the water turns into steam -- heat a planet and its oceans become sky.",
                "explanation": "Volatile materials evaporate at relatively low temperatures. If Earth were heated above 100 C (373 K), the oceans would boil: there is enough water to cover Earth ~300 m deep, and 10 m of water exerts about 1 bar, so the vapor would add about 300 bars. Heating the carbonate rocks of the crust would release about 70 bars of CO2. A warm Earth would have an atmosphere dominated by water vapor and CO2 with a surface pressure near 400 bars.",
                "why": "This thought experiment is exactly what happened to Venus (runaway greenhouse).",
            },
            {
                "term": "Origin of the atmosphere and oceans",
                "badge": ("3", "sources", GREEN),
                "analogy": "Like filling a pool from three hoses: one built in, one from below (volcanoes), one from deliveries (comets).",
                "explanation": "Three possible sources: (1) formed with Earth from debris left over from the Sun's formation; (2) released from the interior by volcanic activity after Earth formed; (3) delivered by impacts of comets and asteroids from the outer solar system. Current evidence favors a combination of interior and impact sources. Today volcanoes release CO2, H2O and SO2, much of it recycled through plate tectonics; burning fossil fuels releases far more CO2 than volcanoes (about 100 times more).",
                "why": "Water delivery by comets/asteroids links small bodies to habitability.",
            },
            {
                "term": "Weather",
                "badge": ("WIND", "circulation", BLUE),
                "analogy": "Weather is the atmosphere stirring itself, like a pot of soup with hot spots and cool spots.",
                "explanation": "All planets with atmospheres have weather: the circulation of the atmosphere. The energy comes primarily from sunlight heating the surface. The planet's rotation and slower seasonal changes vary the sunlight on different parts of the planet, and the atmosphere and oceans redistribute heat from warmer to cooler areas. Weather on any planet is its atmosphere's response to changing energy from the Sun.",
                "why": "Heat redistribution affects whether a whole planet (e.g. a tidally locked one) can stay habitable.",
            },
            {
                "term": "Greenhouse effect",
                "badge": ("CO₂", "heat blanket", RED),
                "analogy": "A car in the sun with its windows up: light gets in, heat can't easily get out.",
                "explanation": "Sunlight penetrates the atmosphere, is absorbed by the ground and heats it; the surface re-emits the energy as infrared (heat). Air lets visible light through but CO2, methane and water vapor absorb infrared, trapping heat like a blanket. To keep energy balanced, the surface and lower air warm until the energy radiated to space equals the energy received. More CO2 means a higher balance temperature. Earth's natural greenhouse effect raises the surface temperature by about 23 C (chapter 8) -- chapter 30 gives about 33 C. Without it Earth would be well below freezing, in a global ice age.",
                "why": "The greenhouse effect sets the inner and outer edges of the habitable zone.",
            },
            {
                "term": "Global warming and climate change",
                "badge": ("+30%", "CO₂", RED),
                "analogy": "Adding CO2 is like adding extra blankets on a warm night -- the planet can't cool off.",
                "explanation": "Burning fossil fuels (energy-rich material made by photosynthesis tens of millions of years ago) releases CO2; destroying tropical forests removes CO2 absorbers. In the past century CO2 rose about 30% and keeps rising more than 0.5% per year; it is predicted to double the pre-industrial level before 2100. Isotopes show the added CO2 is mostly from fossil fuels. Effects: records broken, all but one of the hottest years since 2000, retreating glaciers, thinner Arctic ice, rising seas (melting ice + expanding warm water); temperatures heading for the highest in more than 50 million years. Climate change is called the greatest known threat (barring nuclear war) to civilization and ecology.",
                "why": "Earth's warming connects directly to Venus' runaway greenhouse and to habitability limits.",
            },
            {
                "term": "Anthropocene",
                "badge": ("HUMAN", "age", ROCK),
                "analogy": "Humans have become like a giant geological force, the way glaciers or volcanoes are.",
                "explanation": "Humans have altered the environment before: early hunters killed many large mammals and marsupials (e.g. elephant-sized diprotodon and zygomaturus and 10-foot kangaroos in Australia; mammoths, saber-tooth cats, mastodons, giant sloths and camels in North America and Asia), early farmers cut down most forests, and the Polynesian expansion doomed large Pacific birds. A greater mass extinction is now underway due to rapid climate change. Scientists have proposed (not officially approved) naming the current epoch the anthropocene, when human activity has a significant global impact.",
                "why": "Reminds us that habitability can be changed by the life on a planet -- for better or worse.",
            },
        ],
    },
    # ------------------------------------------------------------------ 4
    {
        "name": "Solar System: Life on Early Earth & Cosmic Impacts",
        "description": "When and how life began on Earth, how life changed our atmosphere (oxygen, ozone, CO2), the tree of life, and how impacts like Tunguska shape a planet.",
        "source_title": "Source reader: Life, Chemical Evolution and Cosmic Influences (OpenStax Astronomy 2e, 8.4, 8.5)",
        "infographics": ["earth_life_timeline"],
        "source_text": (
            "Origin of life: oldest surviving rocks ~3.9 billion years old; chemical evidence shows life already existed. By 3.5 "
            "billion years ago life built large colonies called stromatolites (still grow today, layered domes of sediment "
            "trapped by photosynthesizing blue-green bacteria; colonies date back >3 billion years). Abundant fossils only for "
            "the last 600 million years (<15% of Earth's history). Early atmosphere: abundant CO2, some methane, NO oxygen gas; "
            "without oxygen many complex reactions can make amino acids, proteins and other building blocks. For tens of "
            "millions of years life (perhaps little more than large molecules like viruses) lived in warm nutrient-rich seas off "
            "accumulated organic chemicals; when food ran low, evolution diversified life, which began changing the atmosphere.\n"
            "Genetics/genomics: your genome is 99.9% identical to Julius Caesar's or Marie Curie's; human and chimp genomes 99% "
            "the same; all life descends from a common ancestor. Tree of life (based on an RNA sequence shared by all species): "
            "three domains -- bacteria, archaea, eukarya; plants, animals, fungi are short branches; most diversity is microbial; "
            "more microbes in a bucket of soil than stars in the Galaxy; likely 'aliens' are microbes. Earliest surviving life "
            "forms were adapted to high temperatures -- life may have begun in very hot places; or possibly on Mars (cooled "
            "sooner) and been seeded to Earth by meteorites (no Mars rock has shown this so far).\n"
            "Evolution of the atmosphere: blue-green algae take in CO2 and release oxygen (photosynthesis), giving rise to plants. "
            "Free oxygen lacking until ~2 billion years ago because reactions with the crust removed it; growing plant life plus "
            "erosion burying plant carbon let oxygen accumulate from ~2 billion years ago (chapter 30: ~2.4 billion). Oxygen -> "
            "ozone layer -> UV protection -> life colonized land; animals proliferated, breathing oxygen (plants' waste product). "
            "Life plus geology stripped most CO2 from our air; without life Earth would have a CO2 atmosphere like Mars or Venus.\n"
            "Cosmic influences (8.5): the Moon shows craters; Earth must have been hit as heavily, but plate tectonics and erosion "
            "erase craters; atmosphere burns small debris (meteors) but gives no shield against large impacts (craters several km "
            "across). Ouarkziz crater, Algeria, 4 km, Cretaceous. Tunguska, Siberia, June 30, 1908: explosion ~8 km above the "
            "surface flattened >1,000 square km of forest, killed reindeer, knocked a man 80 km away from his chair; pressure "
            "wave recorded around the world; 5-megaton blast from a stony object ~50 m across (size of a small office building). "
            "Impacts influenced life's evolution: the impact 65 million years ago led to extinction of the dinosaurs (and most "
            "living things), letting mammals dominate."
        ),
        "story": (
            "HOW LONG HAS LIFE BEEN HERE?\n\n"
            "Earth's restless crust has erased most of its baby pictures, but a few clues survive. The oldest surviving rocks are "
            "about 3.9 billion years old, and their chemistry shows that life ALREADY existed then. By 3.5 billion years ago, "
            "tiny microbes were building big colonies called STROMATOLITES: layered domes made when mats of blue-green bacteria "
            "trapped sediment in shallow water, climbed on top, trapped more, and so on. Stromatolites are so successful that "
            "they still grow today (for example in Western Australia, where the oldest known one, 3.47 billion years old, was "
            "also found). Abundant fossils, though, only cover the last 600 million years -- less than 15% of Earth's history.\n\n"
            "HOW DID LIFE START?\n\n"
            "We have little direct evidence, but we know the early atmosphere had lots of carbon dioxide, some methane and NO "
            "oxygen gas. Without oxygen, many complex chemical reactions can happen that make amino acids, proteins and other "
            "building blocks of life. So these ingredients were probably around very early, ready to combine into living things. "
            "For tens of millions of years, early life (maybe little more than big molecules, a bit like today's viruses) "
            "probably lived in warm seas, feeding on organic chemicals that had built up. When that easy food ran low, life "
            "began the long evolutionary road to the huge variety we see today -- and started changing the air.\n\n"
            "Genes give another clue. Studies show the earliest surviving life forms were adapted to high temperatures, so life "
            "may have begun in very hot places. Another wild idea: life could have started on Mars (which cooled sooner) and been "
            "carried to Earth inside meteorites. Mars rocks still land on Earth, but none has shown signs of carrying microbes.\n\n"
            "THE TREE OF LIFE\n\n"
            "Your genome (the complete map of your DNA) is 99.9% identical to Julius Caesar's or Marie Curie's, and 99% the same as "
            "a chimpanzee's. Comparing genes shows all life on Earth descends from a common ancestor. Using one RNA sequence that "
            "every species shares, scientists built the 'tree of life', with three big domains: BACTERIA, ARCHAEA and EUKARYA. "
            "Plants, animals and fungi are just short twigs at the end! Most of life's diversity is microscopic -- there are more "
            "microbes in a bucket of soil than stars in our Galaxy. So if we find aliens, they'll most likely be microbes.\n\n"
            "HOW LIFE REBUILT THE ATMOSPHERE\n\n"
            "A key moment was the rise of blue-green algae, which take in carbon dioxide and release oxygen as waste. Using "
            "sunlight's energy to make food is PHOTOSYNTHESIS, and these microbes gave rise to all plants. At first the oxygen "
            "didn't stay in the air: chemical reactions with the crust grabbed it as fast as it formed. Slowly, more plants made "
            "more oxygen, and erosion buried plant carbon before it could recombine with oxygen. Free oxygen began piling up "
            "about 2 billion years ago (another chapter says about 2.4 billion).\n\n"
            "Oxygen made the OZONE LAYER, which blocks deadly ultraviolet light. Before that, life had to stay in the protective "
            "oceans and the continents were barren. With an ozone shield, life moved onto land and animals spread, eventually "
            "learning to breathe oxygen directly. Funny thought: we evolved to breathe the waste product of plants!\n\n"
            "Life also pulled most CO2 out of our air (with help from geology). Without life, Earth would probably have a CO2 "
            "atmosphere like Mars or Venus.\n\n"
            "WHERE ARE EARTH'S CRATERS?\n\n"
            "The Moon is covered in craters, and it's practically next door, so Earth must have been hit just as much. Our air "
            "burns up small pieces (meteors) but is no shield against big impacts that blast craters several kilometers wide. "
            "The difference: Earth's active geology -- plate tectonics constantly renewing the crust, plus erosion -- erases "
            "craters before they pile up. Only recently have geologists found the worn-down remains of many, like the 4-km "
            "Ouarkziz crater in Algeria, photographed from the International Space Station.\n\n"
            "TUNGUSKA, 1908\n\n"
            "On June 30, 1908, near the Tunguska River in Siberia, something exploded about 8 km above the ground. The blast "
            "flattened more than 1,000 square kilometers of forest, killed reindeer herds, and knocked a man 80 km away out of "
            "his chair. Instruments around the world recorded the pressure wave. It was a 5-megaton explosion from a stony "
            "object only about 50 m across -- the size of a small office building.\n\n"
            "IMPACTS AND EVOLUTION\n"
            "Big impacts have steered the story of life. About 65 million years ago a massive impact led to the extinction of the "
            "dinosaurs (and most other living things), clearing the way for mammals -- and eventually us."
        ),
        "concepts": [
            {
                "term": "Earliest evidence of life",
                "badge": ("3.9", "bya rocks", GREEN),
                "analogy": "Like finding footprints in the oldest pages of a diary -- someone was already there.",
                "explanation": "The record of life's birth was lost to the restless crust, but by the time the oldest surviving rocks formed (~3.9 billion years ago) chemical evidence shows life already existed. By 3.5 billion years ago life built large colonies called stromatolites. Possible (debated) evidence goes back to 3.8 billion years. Few rocks survive from then, and abundant fossils exist only for the past 600 million years -- less than 15% of Earth's history.",
                "why": "Life started fast once Earth was calm -- a hopeful hint for other habitable worlds.",
            },
            {
                "term": "Stromatolites",
                "badge": ("3.47", "bya", GREEN),
                "analogy": "Stromatolites are like layer cakes baked by microbes, one sticky layer at a time.",
                "explanation": "Layered, dome-like structures made by mats of photosynthesizing blue-green bacteria that trap sediment in shallow water; the microbes climb on top of each layer and trap more. Colonies date back more than 3 billion years; the earliest known stromatolite is 3.47 billion years old (Western Australia), and they still grow today (e.g. Lake Thetis, Western Australia). They are among the earliest physical evidence of life and of photosynthesis.",
                "why": "A model biosignature: life leaving structures in rock that we can look for on Mars.",
            },
            {
                "term": "Building blocks in an oxygen-free world",
                "badge": ("no O₂", "early air", PURPLE),
                "analogy": "Oxygen is like a bully that breaks fragile molecules -- without it, delicate chemistry can build up.",
                "explanation": "Early Earth's atmosphere contained abundant CO2 and some methane, but no oxygen gas. Without oxygen, many complex chemical reactions can produce amino acids, proteins and other chemical building blocks of life. These were probably available very early and combined to make living organisms. For tens of millions of years, early life (perhaps little more than large molecules like viruses) lived in warm, nutrient-rich seas on accumulated organic chemicals; when that food ran out, evolution took off.",
                "why": "Explains why prebiotic chemistry experiments (Miller-Urey) and Titan's oxygen-free chemistry matter.",
            },
            {
                "term": "Tree of life",
                "badge": ("3", "domains", GREEN),
                "analogy": "Plants and animals are just a couple of twigs on a giant tree that's mostly microbes.",
                "explanation": "Genetic studies (one RNA sequence all species share) build the tree of life with three domains: bacteria, archaea and eukarya. Plant, animal and fungi kingdoms are short branches at the far end; most diversity and most evolution happened at the microbial level -- more microbes in a bucket of soil than stars in the Galaxy. Your genome matches Julius Caesar's or Marie Curie's at the 99.9% level; humans and chimps match at 99%. All life descends from a common ancestor. The 'aliens' most likely out there are microbes.",
                "why": "Searches for extraterrestrial life target microbial life first.",
            },
            {
                "term": "Hot start or Mars start?",
                "badge": ("HOT", "origin?", RED),
                "analogy": "Like tracing a family back to a great-grandparent who lived in a very hot place.",
                "explanation": "Genetic studies suggest the earliest surviving life forms were adapted to high temperatures, so life might have begun in extremely hot locations. Another possibility: life began on Mars (which cooled sooner) and was 'seeded' onto Earth by meteorites from Mars. Mars rocks still reach Earth, but none has shown evidence of carrying microorganisms.",
                "why": "Links Earth's origin of life to hydrothermal vents and to life on Mars questions.",
            },
            {
                "term": "Photosynthesis and the oxygen revolution",
                "badge": ("O₂", "~2.4 bya", GREEN),
                "analogy": "Photosynthesis plugged life into the Sun's giant power outlet -- and the 'exhaust' was the oxygen we breathe.",
                "explanation": "Photosynthesis uses sunlight to turn carbon dioxide and water into energy-storing food (carbohydrates), releasing oxygen as a by-product. Blue-green algae (cyanobacteria) did it first and gave rise to all plants. Besides the origin of life itself, it may be biology's most important invention: sunlight is a huge energy supply, so it supported a much larger biosphere. A simpler kind that makes no oxygen probably came first; one kind or the other was working at least 3.4 billion years ago, and stromatolites suggest oxygen-makers almost 3.5 billion years ago. At first, chemical reactions with the crust grabbed the oxygen as fast as it formed. As plant life grew and erosion buried plant carbon, free oxygen began piling up in the air about 2.4 billion years ago (another chapter of the source says about 2 billion). Oxygen formed the OZONE LAYER, which blocks deadly ultraviolet light, so life could finally leave the oceans and colonize the land. Oxygen poisoned some microbes (it damages delicate molecules) but was a jackpot for others: combining oxygen with food releases lots of energy, like a burning log, so animals evolved to breathe it -- we breathe plants' waste product!",
                "why": "Abundant oxygen is both a life-changer and the strongest biomarker for exoplanets.",
            },
            {
                "term": "How life rebuilt Earth's air",
                "badge": ("−CO₂", "+O₂", BLUE),
                "analogy": "Earth's living things were like gardeners who completely remade the planet's sky.",
                "explanation": "Earth, Venus and Mars probably started with similar CO2-rich atmospheres. On Earth, liquid water and then life changed everything: CO2 dissolved in the oceans and got locked into marine sediments and carbonate rocks, and photosynthesis released more oxygen than natural chemical reactions could remove. Living things, together with Earth's active geology, stripped the air of most of its CO2. The result: Earth's air is low in CO2, mostly nitrogen (78%), and it is the ONLY planetary atmosphere with free oxygen (21%). Without life, Earth would probably have a CO2-dominated atmosphere like Venus and Mars (each about 96% CO2). An atmosphere can be changed by the life on a planet -- which is exactly why astronomers look at exoplanet atmospheres for signs of life.",
                "why": "Free oxygen + low CO2 = the signature of a living planet.",
            },
            {
                "term": "Why Earth has few craters",
                "badge": ("ERASED", "craters", ROCK),
                "analogy": "Like a beach where the tide keeps smoothing away footprints.",
                "explanation": "Earth must have been hit as heavily as the Moon -- it's practically next door. The atmosphere burns up small debris (meteors) but gives no shield against large impacts that make craters several km across. The difference is that Earth's active geology -- plate tectonics constantly renewing the crust, plus erosion -- destroys craters before they accumulate. Geologists have only recently identified eroded remnants of many, like the 4-km Ouarkziz crater in Algeria (Cretaceous period).",
                "why": "Crater counting dates surfaces on every world -- few craters = young, active surface.",
            },
            {
                "term": "Tunguska event (1908)",
                "badge": ("1908", "Siberia", RED),
                "analogy": "A space rock the size of an office building exploded in the sky with the force of a huge bomb.",
                "explanation": "On June 30, 1908, near the Tunguska River in Siberia, an explosion about 8 km above the surface flattened more than 1,000 square km of forest, killed herds of reindeer, and knocked a man 80 km away from his chair, unconscious. The pressure wave was recorded around the world. It was a 5-megaton blast from a stony projectile about 50 m across (the size of a small office building).",
                "why": "Shows small bodies remain a hazard -- and why we search for objects that could hit Earth.",
            },
            {
                "term": "Impacts and extinction",
                "badge": ("65", "Mya", RED),
                "analogy": "One unlucky space rock reshuffled the deck of life on Earth.",
                "explanation": "Impacts have influenced the evolution of life. About 65 million years ago a massive impact led to the extinction of the dinosaurs along with the majority of other living things, and mammals may owe their domination of Earth's surface to it. Earlier, during the heavy bombardment (3.8-4.1 billion years ago), large impacts could have heat-sterilized Earth's surface layers.",
                "why": "Habitability isn't permanent -- impacts can reset a biosphere.",
            },
        ],
    },
    # ------------------------------------------------------------------ 5
    {
        "name": "Solar System: Venus -- Earth's Scorching Twin",
        "description": "Venus vs. Earth vs. Mars, Venus' backward rotation, radar-mapped geology, volcanoes and coronae, crater ages, and the runaway greenhouse effect.",
        "source_title": "Source reader: Venus (OpenStax Astronomy 2e, 10.1-10.3)",
        "infographics": ["three_planets", "venus_geology", "runaway_greenhouse"],
        "source_text": (
            "Moon and Mercury are geologically dead; Earth, Venus, Mars more active. Venus: 108 million km from the Sun (0.72 AU), "
            "nearly circular orbit; 'evening star'/'morning star' like Mercury; comes closest to Earth of any planet, 40 million "
            "km (Mars' closest ~56 million km). Very bright; Galileo saw Venus' full range of phases -> Venus circles the Sun, "
            "not Earth. Clouds reflect ~70% of sunlight; surface hidden even from orbit (Pioneer Venus UV image).\n"
            "Rotation found by bouncing radar: 243 days, backward (retrograde, east to west). Year 225 Earth days -> day longer "
            "than year; Sun returns to the same place in the sky every 117 Earth days. Likely cause: solar tides on Venus and its "
            "thick atmosphere (tidal friction slows rotation); or powerful collisions during formation.\n"
            "Table 10.1 (Earth/Venus/Mars): semimajor axis 1.00/0.72/1.52 AU; period 1.00/0.61/1.88 yr; mass 1.00/0.82/0.11 "
            "Earth; diameter 12,756/12,102/6,790 km; density 5.5/5.3/3.9 g/cm3; surface gravity 1.00/0.91/0.38; escape velocity "
            "11.2/10.4/5.0 km/s; rotation 23.9 h/243 d/24.6 h; surface area 1.00/0.90/0.28; pressure 1.00/90/0.007 bar. Venus "
            "is Earth's twin (0.82 mass, almost identical density, high geological activity) but surface pressure ~100x (90 bar) "
            "and surface 730 K (over 850 F), hotter than an oven's self-clean cycle.\n"
            "Geology: no plate tectonics; little erosion. ~50 spacecraft launched, about half successful; Mariner 2 (1962) first "
            "flyby; Soviet Union launched most later missions; Venera 7 (1970) first to land and send data from the surface. "
            "Magellan radar mapping. ~75% lowland lava plains (like lunar maria, eruptions without crustal spreading); no "
            "subduction zones. Two continents: Aphrodite (size of Africa, along the equator, 1/3 around the planet) and Ishtar "
            "(size of Australia, north) with the Maxwell Mountains, 11 km high (only feature named after a man, James Clerk "
            "Maxwell, whose electromagnetism theory led to radar; others named for women).\n"
            "Craters: age of a surface (not the planet) from crater counts. Largest crater Mead, 275 km (slightly larger than "
            "Chicxulub, much smaller than lunar basins). Very few craters <10 km: projectiles smaller than ~1 km stopped by the "
            "atmosphere; 10-30 km craters often distorted/multiple from projectiles breaking up (Stein crater, triple, projectile "
            "1-2 km). Using craters >=30 km, average surface age 300-600 million years -- between Earth's ocean basins (younger) "
            "and continents (older). Craters look fresh -> very low erosion; planet-wide volcanic resurfacing 300-600 million "
            "years ago.\n"
            "Volcanoes: lowland eruptions renew surface; hot spots (mantle convection). Sif Mons ~500 km across, 3 km high "
            "(broader but lower than Mauna Loa), caldera ~40 km, lava flows up to 500 km. Thousands of small volcanoes. Pancake "
            "domes ~25 km across, ~2 km tall, from viscous lava. Coronae: circular/oval bulges from upwelling lava that doesn't "
            "reach the surface (like granite ranges such as the Sierra Nevada on Earth); Fotla Corona ('Miss Piggy'). Tectonic "
            "features: mantle convection pushes/stretches crust -> ridges, cracks, rift valleys (Lakshmi Plains grid); Ishtar and "
            "Maxwell resemble the Tibetan Plateau and Himalayas (compression).\n"
            "Atmosphere: surface above 700 K due to greenhouse effect; almost a million times more CO2 than Earth. Runaway "
            "greenhouse: Venus may once have been Earthlike (moderate temperatures, oceans, CO2 dissolved or in rocks); extra "
            "heat (e.g. Sun's gradual brightening) -> more evaporation + gas from rocks -> more CO2 and H2O -> stronger greenhouse "
            "-> hotter. It is an evolutionary process, not just a big greenhouse; new hotter equilibrium. Irreversible: oceans "
            "evaporated (removing the CO2 'safety valve'); UV split water, hydrogen escaped, oxygen combined with rock. Unknown "
            "whether Earth could run away; Venus shows a planet can't heat indefinitely without major change."
        ),
        "story": (
            "MEET EARTH'S 'TWIN'\n\n"
            "Venus is the closest planet to Earth -- at its nearest, just 40 million km away (Mars never gets closer than about "
            "56 million km). It orbits the Sun at 0.72 AU (108 million km) on an almost perfect circle, and it shines so brightly "
            "that, like Mercury, it appears as the 'evening star' or 'morning star'. Galileo saw that Venus shows a full set of "
            "phases like the Moon, which proved Venus goes around the Sun, not Earth.\n\n"
            "On paper Venus looks like Earth's twin: 0.82 times Earth's mass, almost the same density (5.3 vs 5.5), surface "
            "gravity 0.91, escape velocity 10.4 km/s, and lots of geological activity. But step outside and you'd be crushed and "
            "cooked: the air is about 90 times thicker than Earth's (90 bars) and the surface is 730 K -- over 850 F, hotter than "
            "the self-cleaning cycle of an oven. The big mystery: how did twins turn out so different?\n\n"
            "A HIDDEN SURFACE\n\n"
            "Thick clouds reflect about 70% of sunlight, so even cameras in orbit can't see the ground. Scientists mapped Venus "
            "with RADAR, which passes through clouds. Radar also revealed its spin: Venus rotates once every 243 days, and "
            "BACKWARD (east to west, retrograde). Its year is only 225 days, so a Venus 'day' is longer than its year! Measured "
            "from one noon to the next, the Sun takes 117 Earth days to return to the same spot in the sky. ('See you tomorrow' "
            "on Venus means a long wait.) The most likely cause of this slow, backward spin is tides raised by the Sun in Venus "
            "and its thick atmosphere (tidal friction slows spins). Another idea is one or more big collisions during formation.\n\n"
            "EXPLORING VENUS\n"
            "Nearly 50 spacecraft have been launched to Venus, but only about half succeeded. Mariner 2 (USA, 1962) made the first "
            "flyby; the Soviet Union launched most of the later missions, and Venera 7 (1970) was the first probe to land and send "
            "data from the surface. NASA's Magellan orbiter made detailed radar maps.\n\n"
            "THE LANDSCAPE\n\n"
            "About 75% of Venus is low, flat LAVA PLAINS. They look a bit like Earth's ocean floors, but there are no subduction "
            "zones, so Venus never had plate tectonics. The plains formed more like the Moon's maria: huge floods of lava without "
            "plates spreading apart.\n\n"
            "Two 'continents' rise above the plains. APHRODITE, about the size of Africa, stretches a third of the way around the "
            "equator. ISHTAR, in the north, is about the size of Australia and holds the MAXWELL MOUNTAINS, 11 km high -- the "
            "highest place on Venus. They're named for James Clerk Maxwell, whose theory of electromagnetism led to radar; they are "
            "the only feature on Venus named after a man. Everything else is named for women from history or mythology.\n\n"
            "CRATERS TELL TIME\n\n"
            "The more craters a surface has, the older it is (that's the age of the SURFACE, not the planet). Venus' thick air "
            "protects it from small rocks: there are very few craters smaller than 10 km, because projectiles under about 1 km "
            "get stopped. Craters 10-30 km across are often lumpy or doubled because the rock broke apart in the air (like the "
            "triple Stein crater). Counting only big craters (30 km and up), the plains are just 300 to 600 million years old. "
            "The largest crater, Mead, is 275 km across -- a bit bigger than Earth's Chicxulub. And nearly every crater looks "
            "fresh, so there's almost no erosion. It seems Venus had a mysterious, planet-wide volcanic makeover 300 to 600 "
            "million years ago, unlike anything in Earth's history.\n\n"
            "VOLCANOES, PANCAKES AND MISS PIGGY\n"
            "• Lava floods renew the plains and bury old craters. Hot spots, where the mantle carries heat upward, build younger volcanoes.\n"
            "• SIF MONS, the largest volcano, is ~500 km across but only 3 km high (broader but lower than Hawaii's Mauna Loa), with a 40-km summit caldera and lava flows up to 500 km long.\n"
            "• Thousands of smaller volcanoes dot the surface, down to the size of a parking lot.\n"
            "• PANCAKE DOMES: flat round volcanoes ~25 km across and ~2 km tall, made by thick, sludgy (viscous) lava spreading evenly.\n"
            "• CORONAE: big round or oval bulges where hot lava pushed up the crust without breaking through. One, Fotla Corona, looks like Miss Piggy!\n\n"
            "TECTONIC FORCES\n"
            "Convection in the mantle pushes and stretches the crust, cracking the lava plains into grids of ridges and cracks "
            "(like the Lakshmi Plains) and even tearing open rift valleys. Ishtar and the Maxwell Mountains were squeezed up by "
            "compression, like Earth's Tibetan Plateau and Himalayas.\n\n"
            "WHY IS VENUS SO HOT? THE RUNAWAY GREENHOUSE\n\n"
            "Venus is a bit closer to the Sun, but that only explains a little of its heat. The real culprit is the greenhouse "
            "effect: Venus has almost a MILLION times more carbon dioxide than Earth. That thick CO2 blanket traps infrared heat, "
            "and the ground must get extremely hot before it can radiate away as much energy as it receives.\n\n"
            "Was Venus always like this? Maybe not. Scientists imagine a young Venus with mild temperatures, oceans, and its CO2 "
            "dissolved in water or locked in rocks -- like Earth. Then add a little extra heat (the Sun slowly brightens over "
            "time). More water evaporates and more gas escapes from rocks. More CO2 and water vapor make the greenhouse stronger, "
            "which makes it hotter, which releases even more gas... This loop is the RUNAWAY GREENHOUSE EFFECT. It's not just a "
            "big greenhouse -- it's a process that evolves a planet from Earthlike to a new, much hotter balance.\n\n"
            "And it's a one-way trip. On Earth, oceans and rocks hold most CO2 -- a safety valve. When Venus' oceans boiled away, "
            "the valve was gone. Ultraviolet sunlight then split the water vapor; the light hydrogen escaped to space and the "
            "oxygen combined with surface rocks. Once water is lost this way, it can't come back. There's evidence this really "
            "happened to Venus.\n\n"
            "Could Earth run away too? Nobody knows exactly where the tipping point is. But Venus proves a planet can't keep "
            "heating forever without a dramatic change to its oceans and atmosphere -- something worth remembering as Earth's CO2 "
            "rises."
        ),
        "concepts": [
            {
                "term": "Venus at a glance",
                "badge": ("0.72", "AU", "#e8c27a"),
                "analogy": "Venus is Earth's twin who moved somewhere much too hot and wrapped up in a thick wool coat.",
                "explanation": "Orbit 0.72 AU (108 million km), very nearly circular; year 0.61 Earth years (225 days). Closest approach to Earth 40 million km -- nearer than any other planet (Mars: ~56 million km). Mass 0.82 Earth, diameter 12,102 km, density 5.3 g/cm3, surface gravity 0.91, escape velocity 10.4 km/s, surface area 0.90 Earth. Surface pressure 90 bars (nearly 100x Earth) and temperature 730 K (over 850 F). Appears as the 'evening star' or 'morning star'. Galileo observed its full range of phases, proving it orbits the Sun.",
                "why": "Venus is the textbook example of a planet that lost its habitability.",
            },
            {
                "term": "Venus' backward, slow rotation",
                "badge": ("243 d", "retrograde", "#e8c27a"),
                "analogy": "On Venus your birthday (one year) comes before the end of a single day!",
                "explanation": "Because clouds hide the surface, Venus' rotation was found by bouncing radar off the planet (first in the early 1960s, then by tracking radar-visible surface features). It rotates once every 243 days, in a backward (retrograde, east-to-west) direction. Its year is 225 days, so its day (one spin) is longer than its year; the Sun returns to the same place in Venus' sky every 117 Earth days. Likely cause: tides from the Sun acting on Venus and its thick atmosphere (tidal friction slows rotation); alternatively, powerful collisions during formation slowed and reversed it.",
                "why": "Slow rotation and tidal effects are part of the tidal-locking story for exoplanets.",
            },
            {
                "term": "Exploring Venus",
                "badge": ("Venera", "7 (1970)", ROCK),
                "analogy": "Landing on Venus is like parking a robot inside a pressure cooker on full blast.",
                "explanation": "Nearly 50 spacecraft have been launched to Venus, about half successful. The US Mariner 2 flyby (1962) was first; the Soviet Union launched most later missions. Venera 7 (1970) was the first probe to land and broadcast data from Venus' surface. Clouds reflect about 70% of sunlight and hide the surface even from orbit, so radar (e.g. NASA's Magellan) was used to map it; Pioneer Venus imaged the cloud tops in ultraviolet.",
                "why": "Mission history and radar mapping are common test details.",
            },
            {
                "term": "Venus' lava plains and continents",
                "badge": ("75%", "lava plains", ROCK),
                "analogy": "Venus is mostly flat lava 'oceans' with two big rocky 'continents' poking up.",
                "explanation": "About 75% of Venus is lowland lava plains, which resemble Earth's basaltic ocean basins but formed like the lunar maria -- widespread eruptions without plate spreading. There are no subduction zones: Venus never had plate tectonics (mantle convection stressed the crust but didn't start plates moving). Two continents: Aphrodite (about the size of Africa, along the equator for a third of the way around) and Ishtar (about the size of Australia, in the north), which holds the Maxwell Mountains, 11 km high -- the only feature named after a man (James Clerk Maxwell); all others are named for women.",
                "why": "Plate tectonics (or lack of it) matters for recycling CO2 and long-term climate stability.",
            },
            {
                "term": "Crater ages on Venus",
                "badge": ("300-600", "Myr", BLUE),
                "analogy": "Counting craters is like counting dents in a car to guess how long it's been on the road.",
                "explanation": "Crater counts give the age of a surface (not of the planet); more craters = older. Venus has very few craters smaller than 10 km because its atmosphere stops projectiles smaller than ~1 km; 10-30 km craters are often distorted or multiple because the projectile broke up (e.g. the triple Stein crater, projectile 1-2 km). Using craters 30 km and larger, the plains average only 300-600 million years old -- between Earth's younger ocean basins and older continents. The largest crater, Mead, is 275 km (slightly bigger than Earth's Chicxulub, far smaller than lunar basins). Fresh-looking craters mean very low erosion; Venus apparently had a planet-wide volcanic resurfacing 300-600 million years ago.",
                "why": "Crater-counting logic appears for Venus, Ganymede, Europa and Mars questions.",
            },
            {
                "term": "Venus' volcanoes",
                "badge": ("Sif", "Mons", RED),
                "analogy": "Venus' pancake domes look like giant pancakes poured from a batter of thick, sludgy lava.",
                "explanation": "Volcanic eruptions are the main way Venus' plains are renewed, with fluid lava destroying old craters; younger volcanic mountains sit over hot spots where mantle convection brings heat up. Sif Mons, the largest volcano, is about 500 km across and 3 km high -- broader but lower than Mauna Loa -- with a ~40 km caldera and lava flows up to 500 km long. Thousands of smaller volcanoes exist, down to parking-lot size. 'Pancake domes' are ~25 km across and ~2 km tall, formed by highly viscous (sludgy) lava spreading evenly.",
                "why": "Volcanic outgassing builds atmospheres -- including Venus' massive CO2 one.",
            },
            {
                "term": "Coronae and tectonic features",
                "badge": ("BLOBS", "coronae", PURPLE),
                "analogy": "A corona is like a blister on the crust, pushed up by hot lava that never broke through.",
                "explanation": "Upwelling lava that doesn't reach the surface collects and bulges the crust (as with Earth granite ranges like the Sierra Nevada). On Venus these make large circular or oval features called coronae, surrounded by tectonic ridges and cracks (e.g. Fotla Corona, the 'Miss Piggy' corona, with pancake volcanoes). Tectonic forces from mantle convection crack the plains into ridge-and-crack grids (Lakshmi Plains), tear rift valleys, and compress the crust into Ishtar and the Maxwell Mountains, like the Tibetan Plateau and Himalayas. Planetary scientists call this 'blob tectonics'.",
                "why": "Shows how a planet can be geologically active without Earth-style plate tectonics.",
            },
            {
                "term": "Runaway greenhouse effect",
                "badge": ("LOOP", "runaway", RED),
                "analogy": "Like a snowball rolling downhill getting bigger and faster -- each bit of heat makes more heat.",
                "explanation": "Venus has almost a million times more CO2 than Earth, so its greenhouse effect is far stronger, heating the surface above 700 K. Venus may once have been Earthlike, with oceans and its CO2 dissolved in water or bound in rocks. Modest extra heating (e.g. the Sun's gradual brightening) increases evaporation and releases gas from rocks; more CO2 and H2O strengthen the greenhouse, causing more heating and more release. Unless something intervenes, temperature keeps rising. The runaway greenhouse is an evolutionary process, not just a large greenhouse effect: the planet settles into a new, much hotter equilibrium.",
                "why": "This sets the INNER edge of the habitable zone -- a top 2027 habitability concept.",
            },
            {
                "term": "Irreversible water loss",
                "badge": ("H₂O→H↑", "lost forever", ICE),
                "analogy": "Once you pour water on hot sand and it disappears into the air, you can't scoop it back.",
                "explanation": "On Earth, most CO2 is bound in crustal rocks or dissolved in the oceans -- a safety valve. As Venus heated, its oceans evaporated, removing that valve. Water vapor doesn't last under solar ultraviolet light: UV splits it, the light hydrogen escapes to space, and the oxygen combines chemically with surface rock. Loss of water is therefore irreversible -- once gone, it cannot be restored -- and there is evidence this happened to Venus. We don't know where Earth's tipping point is, but Venus shows a planet can't keep heating without major changes to its oceans and atmosphere.",
                "why": "Explains why Venus, even if moved into the habitable zone today, would still lack water.",
            },
        ],
    },
    # ------------------------------------------------------------------ 6
    {
        "name": "Solar System: Mars -- Following the Water",
        "description": "Mars' properties and seasons, the 'canals' myth, thin CO2 air, polar caps, runoff and outflow channels, gullies and salty streaks, rover discoveries, buried ice, and the search for life.",
        "source_title": "Source reader: Mars, Water and Life (OpenStax Astronomy 2e, 10.1, 10.5, 30.3)",
        "infographics": ["mars_water", "mars_ice"],
        "source_text": (
            "Mars: 227 million km (1.52 AU); closest to Earth ~56 million km. Red from iron oxides in its soil (associated with "
            "war/blood). Best Earth telescope resolution ~100 km (like the Moon to the naked eye): polar caps and changing dark "
            "markings, no topography. Canals: Schiaparelli (1835-1910) in 1877 reported 'canale' (channels), mistranslated "
            "'canals'. Percival Lowell (1855-1916) built an observatory in Flagstaff, Arizona (1894) and promoted intelligent "
            "Martians (books Mars 1895, Mars and Its Canals 1906); inspired H. G. Wells' War of the Worlds (1897) and the 1938 "
            "radio panic. Larger telescopes failed to confirm canals -- an optical illusion (mind connecting dim dots into lines). "
            "Pluto found at Lowell Observatory in 1930 (name starts with P.L.); first measurements of galaxies' speeds there.\n"
            "Rotation: sidereal day 24 h 37 min 23 s (precise from 200+ years of observations). Axis tilt ~25 deg -> seasons like "
            "Earth's, each ~6 months long (year almost 2 Earth years). Mass 0.11 Earth; larger than Moon and Mercury; keeps a thin "
            "atmosphere; long ago probably thick atmosphere and seas; maybe life persists underground.\n"
            "Atmosphere: average surface pressure 0.007 bar (<1% Earth's; like 30 km above Earth); 95% CO2, ~3% N2, ~2% Ar. "
            "Winds fast but weak; loft fine dust -> planet-wide dust storms; dust gives red color; wind erosion (yardangs); dust "
            "devils (may clean rover solar panels). (The Martian movie's storm too strong.) Liquid water not stable: cold + low "
            "pressure; below 0.006 bar boiling point <= freezing point, so ice sublimates like dry ice. Salts lower freezing point "
            "-> salty water can sometimes be liquid. Clouds: dust; water-ice (around mountains); CO2 dry-ice hazes (need ~150 K, "
            "-125 C; never on Earth).\n"
            "Polar caps: seasonal caps of frozen CO2 condense below ~150 K, extend to ~50 deg latitude by spring. Southern "
            "permanent cap 350 km, CO2 + lots of water ice, stays at 150 K all summer. Northern permanent cap >=1000 km, water "
            "ice, ~3 km thick, ~10 million km3 (like Mediterranean Sea), in a basin the size of the Arctic Ocean basin (maybe an "
            "old shallow sea; possible shorelines). Layered terrain above 80 deg latitude: layers 10 to tens of meters, light and "
            "dark bands, wind-blown dust + ice, cycles of tens of thousands of years (like ice ages), caused by planets' pull "
            "changing Mars' orbit and tilt. Phoenix (2008) landed near the north cap; trench revealed white water ice that "
            "sublimated over days.\n"
            "Example: Earth's ocean = 3 km layer over Earth -> ~1.5x10^21 kg; one Mars polar cap (2 km thick, radius 400 km) ~1x10^18 "
            "kg, ~0.1% of Earth's oceans; Greenland ice sheet 2.85x10^15 m3 ~2.85x Mars caps (same order of magnitude).\n"
            "Channels: runoff channels (highland plains; few m deep, tens of m wide, 10-20 km long; look like rain runoff; ~4 "
            "billion years old -- more cratered than lunar maria, less than lunar highlands). Outflow channels (10+ km wide, "
            "hundreds of km long, drain into Chryse basin where Pathfinder landed; carved by catastrophic floods from melted "
            "permafrost, maybe heated with volcanic plains). Neither visible from Earth nor straight -> not Lowell's canals. "
            "Gullies (Mars Global Surveyor, resolution a few meters): on steep high-latitude valley/crater walls, very young (no "
            "craters, cut dunes), change with seasons; dark streaks = recurring slope lineae (RSL), 2015 spectra showed hydrated "
            "salts -> salty water may flow 100+ m; source unknown (Horowitz crater, Garni crater).\n"
            "Rovers: Spirit (2004-2010, Gusev crater lake bed covered by lava; drove 7.73 km, 20x longer than planned); "
            "Opportunity (layered sedimentary rock, evaporation evidence -> shallow salty lake; hematite spheres 'blueberries' "
            "form only in water); Curiosity (2012, Gale crater; mudstones from ancient lakebed; cross-bedded sandstone; confirmed "
            "an ancient HABITABLE environment -- water + energy + raw materials); Perseverance (Jezero crater, 45 km, lake bed and "
            "river delta, collecting samples for return). Glaciers covered by dust at mid-latitudes; ice bands 100 m tall in "
            "cliffs; formed in warm periods; useful for future human exploration.\n"
            "Mars history (30.3): early warmer, wetter epochs; lost much atmosphere; water dried up, got saltier and more acidic; "
            "surface bathed in radiation, uninhabitable; underground ice and liquid water may persist; salty water may flow "
            "briefly today; life, if present, hidden in the crust. 'Face on Mars' (Viking, Cydonia mesa) -- pareidolia, higher "
            "resolution showed an ordinary mesa."
        ),
        "story": (
            "THE RED PLANET THROUGH A TELESCOPE\n\n"
            "Mars orbits at 227 million km from the Sun (1.52 AU) and comes as close as about 56 million km to Earth. It's "
            "distinctly red because its soil contains iron oxides -- rust! That blood-red color may be why ancient cultures linked "
            "it to war. Even the best telescopes on the ground only see details about 100 km across (like looking at the Moon "
            "with just your eyes), so no mountains or craters show up -- just bright polar caps and dusky markings that change "
            "with the seasons.\n\n"
            "THE CANAL CRAZE\n\n"
            "In 1877 the Italian astronomer Giovanni Schiaparelli reported long, faint, straight lines he called 'canale' -- "
            "Italian for channels. In English it was mistranslated as 'canals', which sounds like something built. Percival "
            "Lowell, from a wealthy Boston family, built an observatory in Flagstaff, Arizona in 1894 and drew maps covered with "
            "canals, oases and reservoirs. He wrote books (Mars, 1895; Mars and Its Canals, 1906) claiming a dying Martian "
            "civilization was piping water from the polar caps. His ideas inspired H. G. Wells' novel The War of the Worlds "
            "(1897), and a 1938 radio version scared listeners into thinking Martians were invading New Jersey.\n\n"
            "But bigger telescopes couldn't find the canals. They were an OPTICAL ILLUSION: when our eyes glimpse dim, random dots "
            "at the edge of what they can see, our brains connect them into straight lines. (Fun fact: Pluto was discovered at "
            "Lowell Observatory in 1930, and its name starts with Percival Lowell's initials.) The 'Face on Mars', a mesa in a "
            "Viking photo, is another trick of our face-loving brains -- sharper images show an ordinary hill.\n\n"
            "MARS BY THE NUMBERS\n"
            "• Day: 24 h 37 min 23 s (measured to hundredths of a second by watching thousands of rotations over 200+ years)\n"
            "• Axis tilt: about 25 degrees -- so Mars has seasons like ours, each about 6 months long because its year is nearly 2 Earth years (1.88)\n"
            "• Mass 0.11 Earth; diameter 6,790 km; density 3.9; gravity 0.38; escape velocity 5.0 km/s; surface area 0.28 Earth\n"
            "• Bigger than the Moon and Mercury, so it kept a thin atmosphere and was geologically active long ago\n\n"
            "THIN, DUSTY AIR\n\n"
            "Mars' air presses down with only 0.007 bar, less than 1% of Earth's -- like the air 30 km above Earth. It's 95% carbon "
            "dioxide, about 3% nitrogen and 2% argon (similar proportions to Venus, but far less of it). Winds can be fast, but "
            "thin air pushes weakly (so the giant storm in the movie The Martian couldn't really happen). Still, wind lifts fine "
            "red dust into planet-wide dust storms, whirls up dust devils, piles up dunes and carves long ridges called yardangs.\n\n"
            "WHY NO PUDDLES?\n\n"
            "Mars is cold, but there's a bigger problem: pressure. Below about 0.006 bar, water's boiling point is as low as its "
            "freezing point, so ice turns straight into vapor without ever melting -- just like dry ice on Earth. Salt helps: it "
            "lowers the freezing point (that's why we salt icy roads), so salty water can sometimes stay liquid briefly on Mars.\n\n"
            "Mars has three kinds of clouds: dust clouds, water-ice clouds (often around mountains, like on Earth), and hazes of "
            "frozen CO2 -- dry-ice crystals that need about 150 K (-125 C), colder than Earth ever gets.\n\n"
            "THE POLAR CAPS\n"
            "• SEASONAL CAPS are thin frost of frozen CO2 that condenses from the air each winter when it drops below ~150 K, "
            "reaching down to about 50 degrees latitude by spring.\n"
            "• The SOUTH PERMANENT CAP is 350 km across: frozen CO2 plus lots of water ice, staying at 150 K through summer.\n"
            "• The NORTH PERMANENT CAP is water ice, never smaller than 1,000 km across, about 3 km thick, with a volume of about "
            "10 million km3 (like the Mediterranean Sea). It sits in a basin as big as Earth's Arctic Ocean basin -- maybe once a "
            "shallow sea.\n"
            "• Around both poles (above 80 degrees) are stacks of light and dark layers, each 10 to tens of meters thick, made of "
            "dust and ice. They record climate cycles every tens of thousands of years -- Martian 'ice ages' caused by other "
            "planets tugging on Mars' orbit and tilt.\n"
            "• In 2008 the Phoenix lander dug a trench near the north pole and found bright white ice that slowly vanished "
            "(sublimated) over a few days -- frozen water!\n\n"
            "HOW MUCH WATER? (a classic calculation)\n"
            "Volume of a layer = area x thickness. Earth's oceans equal a 3-km layer over the whole planet: 4 x pi x (6.4 x 10^6 m)^2 "
            "x 3,000 m = about 1.5 x 10^18 m3, or 1.5 x 10^21 kg of water. One Mars polar cap, if 2 km thick with a 400 km radius: "
            "pi x (4 x 10^5 m)^2 x 2,000 m = about 1 x 10^15 m3, or 1 x 10^18 kg -- about 0.1% of Earth's oceans. Earth's "
            "Greenland ice sheet (2.85 x 10^15 m3) holds about 2.85 times as much, the same order of magnitude.\n\n"
            "FOLLOW THE WATER\n\n"
            "All life on Earth needs liquid water, so the rule for finding life on Mars is 'follow the water'. And Mars is "
            "covered in clues that water once flowed:\n"
            "• RUNOFF CHANNELS: small twisting valleys in the old highlands, a few meters deep, tens of meters wide and 10-20 km long, "
            "like runoff from ancient rainstorms. Crater counts make them about 4 billion years old.\n"
            "• OUTFLOW CHANNELS: giants, 10 km or more wide and hundreds of km long (the biggest drain into the Chryse basin, where "
            "Pathfinder landed). They were carved by catastrophic floods when frozen ground (permafrost) was suddenly melted, "
            "perhaps by volcanic heat.\n"
            "• GULLIES: discovered by Mars Global Surveyor (sharp enough to see a bus). They're on steep crater walls at high "
            "latitudes and are very young -- no craters on them, and some cut across recent dunes. Dark streaks called RECURRING "
            "SLOPE LINEAE grow downhill each season. In 2015, spectra found hydrated salts in them: salty water may flow 100 m "
            "or more before evaporating or soaking in. We still don't know where that water comes from.\n"
            "None of these are Lowell's canals: they're too small to see from Earth and not straight.\n\n"
            "ROBOT GEOLOGISTS\n"
            "• SPIRIT (2004-2010) drove 7.73 km and lasted 20 times longer than planned. It aimed for an old lake bed in Gusev "
            "crater -- but lava had covered it.\n"
            "• OPPORTUNITY found layered sedimentary rock with chemical signs of evaporation (an old salty lake) and tiny spheres "
            "of hematite, a mineral that forms only in water -- nicknamed 'blueberries'.\n"
            "• CURIOSITY (2012) explored Gale crater: cracked mudstones from an ancient lake and cross-bedded sandstone from flowing "
            "water. It proved Mars once had a HABITABLE environment -- not just water, but energy and raw materials for life.\n"
            "• PERSEVERANCE is exploring Jezero crater (45 km wide), an old lake bed and river delta, collecting rock samples to "
            "bring to Earth one day.\n"
            "• From orbit we also see dust-covered glaciers at mid-latitudes and 100-m-tall bands of ice in cliffs -- frozen water "
            "just below the surface that future astronauts could use.\n\n"
            "THE STORY OF MARS\n"
            "Early Mars had warmer, wetter times that could have supported life at the surface. Then it lost much of its "
            "atmosphere. Its shrinking lakes became saltier and more acidic until the surface dried out and was bathed in harsh "
            "radiation. The surface became uninhabitable -- but underground, ice and even liquid water may survive, and briny "
            "water may still trickle on the surface sometimes. If life ever took hold, its traces are hidden in the crust, "
            "waiting for us to read them."
        ),
        "concepts": [
            {
                "term": "Mars at a glance",
                "badge": ("1.52", "AU", "#e0603a"),
                "analogy": "Mars is Earth's smaller, colder, rusty little sibling.",
                "explanation": "Average distance 227 million km (1.52 AU); closest approach to Earth ~56 million km. Year 1.88 Earth years; sidereal day 24 h 37 min 23 s; axis tilt ~25 deg, so it has seasons like Earth's, each about six Earth months long. Mass 0.11 Earth, diameter 6,790 km, density 3.9 g/cm3, surface gravity 0.38, escape velocity 5.0 km/s, surface area 0.28 Earth, pressure 0.007 bar. Red from iron oxides in its soil. Larger than the Moon and Mercury, so it kept a thin atmosphere and had considerable geological activity; it probably once had a thick atmosphere and seas.",
                "why": "Mars is the most promising place in the solar system to look for past (or present) life.",
            },
            {
                "term": "The Martian 'canals' (and the Face on Mars)",
                "badge": ("canali", "illusion", RED),
                "analogy": "Like connecting random dots in the dark into shapes that aren't really there.",
                "explanation": "In 1877 Giovanni Schiaparelli (1835-1910) reported straight lines he called 'canale' (channels), mistranslated as 'canals'. Percival Lowell (1855-1916) built his Flagstaff, Arizona observatory in 1894 and argued for intelligent Martians irrigating a dying planet (books Mars, 1895; Mars and Its Canals, 1906), inspiring H. G. Wells' The War of the Worlds (1897) and the 1938 radio panic. Larger telescopes failed to confirm them: they were an optical illusion -- the mind connects dim dots into lines. Pluto was found at Lowell Observatory in 1930. The 'Face on Mars' (a Viking-imaged mesa in Cydonia) is likewise our tendency to see faces.",
                "why": "A great example of how science tests claims -- and that real water channels are a different thing.",
            },
            {
                "term": "Mars' atmosphere",
                "badge": ("0.007", "bar", "#e0603a"),
                "analogy": "Standing on Mars is like being 30 km above Earth -- the air is super thin.",
                "explanation": "Average surface pressure 0.007 bar, less than 1% of Earth's (as thin as Earth's air ~30 km up). Composition: 95% CO2, ~3% nitrogen, ~2% argon -- similar proportions to Venus but far less gas. Winds can be fast but exert little force; they still lift fine dust into planet-wide storms, giving Mars its red color, carving yardangs, and making dust devils (which may clean rovers' solar panels). Mars has very little greenhouse warming (~2 C). Atmospheric leakage created its thin atmosphere.",
                "why": "Too little air = too little greenhouse warming and no stable liquid water: Mars sits at the cold edge.",
            },
            {
                "term": "Why liquid water can't last on Mars",
                "badge": ("0.006", "bar limit", ICE),
                "analogy": "On Mars, ice acts like dry ice -- it skips the puddle stage and turns straight into gas.",
                "explanation": "Liquid water is not stable on Mars' surface. Low temperature is part of it, but even on a summer day above freezing, the low pressure prevents liquid except at the lowest elevations. At pressures below ~0.006 bar the boiling point is as low as or lower than the freezing point, so water goes directly from solid to vapor (sublimation), like dry ice on Earth. Dissolved salts lower water's freezing point, so salty water can sometimes exist as liquid on the surface under the right conditions.",
                "why": "Habitability needs the right temperature AND pressure for liquid water.",
            },
            {
                "term": "Clouds on Mars",
                "badge": ("3", "cloud types", ICE),
                "analogy": "Mars has three cloud 'flavors': dust, water ice, and dry ice.",
                "explanation": "Three types: (1) dust clouds raised by wind; (2) water-ice clouds similar to Earth's, often forming around mountains; (3) hazes of dry-ice (CO2) crystals at high altitude. The CO2 clouds have no counterpart on Earth because our temperatures never drop low enough (~150 K, about -125 C) for CO2 to condense. Mars' air also contains small amounts of water vapor.",
                "why": "Water-ice clouds show water still cycles through Mars' atmosphere today.",
            },
            {
                "term": "Mars' polar caps",
                "badge": ("CAPS", "CO₂ + H₂O", ICE),
                "analogy": "Mars wears a permanent ice hat, plus a seasonal frosty scarf of dry ice each winter.",
                "explanation": "Seasonal caps are thin frozen CO2 (dry ice) that condenses from the atmosphere below ~150 K, extending to ~50 deg latitude by spring. Permanent (residual) caps: the southern one is 350 km across, frozen CO2 plus much water ice, staying at 150 K all summer; the northern one is water ice, never smaller than 1,000 km, ~3 km thick, ~10 million km3 (like the Mediterranean Sea), sitting in a basin the size of Earth's Arctic Ocean basin -- possibly an ancient shallow sea. Above 80 deg latitude, layered deposits (10 to tens of meters each, light/dark bands of dust and ice) record climate cycles of tens of thousands of years, caused by other planets' pull changing Mars' orbit and tilt. Phoenix (2008) exposed white ice in a trench that sublimated in days -- water ice.",
                "why": "The caps are Mars' biggest known water reservoir -- habitability and future human use.",
            },
            {
                "term": "Mars vs. Earth water (calculation)",
                "badge": ("0.1%", "of oceans", BLUE),
                "analogy": "All the ice in one Mars polar cap is like a spoonful compared to Earth's ocean bowl.",
                "explanation": "Volume of a layer = area x thickness. Earth's oceans equal a 3 km layer over the sphere: 4 pi R^2 x 3,000 m with R = 6.4 x 10^6 m gives ~1.5 x 10^18 m3, or ~1.5 x 10^21 kg (water: 1,000 kg/m3). One Mars polar cap, 2 km thick with radius 400 km: pi r^2 x h = pi x (4 x 10^5 m)^2 x 2,000 m ~ 1 x 10^15 m3, ~1 x 10^18 kg -- about 0.1% of Earth's oceans. Greenland's ice sheet (~2.85 x 10^15 m3) holds ~2.85 times as much -- the same to the nearest power of 10.",
                "why": "Typical calculation question: practice unit conversions (km to m) and powers of 10.",
            },
            {
                "term": "Runoff and outflow channels",
                "badge": ("RIVERS", "long ago", BLUE),
                "analogy": "Runoff channels are like little creeks after a storm; outflow channels are like a dam bursting.",
                "explanation": "Runoff channels: in the highland equatorial plains, small sinuous channels a few m deep, tens of m wide, 10-20 km long, like surface runoff from ancient rainstorms; crater counts (more than the lunar maria, fewer than the lunar highlands) make them ~4 billion years old -- evidence of a very different early climate. Outflow channels: much larger, 10+ km wide and hundreds of km long (the largest drain into the Chryse basin where Pathfinder landed), carved by huge volumes of water released catastrophically from permafrost, perhaps heated by the volcanism that made Mars' volcanic plains. Neither is visible from Earth or straight -- not Lowell's canals.",
                "why": "Core evidence that Mars once had flowing surface water.",
            },
            {
                "term": "Gullies and recurring slope lineae",
                "badge": ("RSL", "salty flows", GREEN),
                "analogy": "Seasonal dark streaks are like trickles of salty water drawing lines down a hill.",
                "explanation": "Mars Global Surveyor (resolution a few meters -- truck-size) found gullies on steep valley and crater walls at high latitudes. They are very young: no superimposed craters, and some cut across recent dunes. Dark streaks (recurring slope lineae) elongate within days and change with the seasons, suggesting something flows downhill. In 2015 spectra showed hydrated salts from evaporating salty water; salty water could flow 100 m or more before evaporating or soaking in (e.g. Horowitz crater; Garni crater). The ultimate water source (atmosphere or underground aquifers) is still unknown.",
                "why": "Hints that liquid water may exist on Mars even today -- big for present-day habitability.",
            },
            {
                "term": "Mars rovers and what they found",
                "badge": ("4", "rovers", ROCK),
                "analogy": "Rovers are robot geologists with wheels, hunting for old lake beds.",
                "explanation": "Spirit (2004-2010) targeted an ancient lake bed in Gusev crater but found it covered by lava; it drove 7.73 km and lasted 20x longer than planned. Opportunity found layered sedimentary rock with chemical signs of evaporation (a shallow salty lake) and hematite-rich spheres ('blueberries') that form only in water. Curiosity (2012, Gale crater) found mudstones from an ancient lakebed and cross-bedded sandstone from flowing water, confirming an ancient habitable environment. Perseverance explores Jezero crater (45 km), a former lake bed and river delta, collecting samples for return to Earth.",
                "why": "Curiosity's 'habitable' finding is a key fact for the 2027 habitability theme.",
            },
            {
                "term": "Buried ice and glaciers",
                "badge": ("ICE", "underground", ICE),
                "analogy": "Mars hides its water like a freezer buried under a dusty blanket.",
                "explanation": "There is evidence of large quantities of ice just below Mars' surface. At mid-latitudes, orbiters see glaciers covered with dirt and dust; in some cliffs ice is seen directly as bands about 100 m tall, buried just a few meters down (Mars Reconnaissance Orbiter). These glaciers likely formed in warm periods when the atmosphere was thicker and snow and ice could fall. This readily available frozen water could support future human exploration.",
                "why": "Water resources matter for both past habitability and future human habitats.",
            },
            {
                "term": "Mars' habitability history",
                "badge": ("past?", "life", GREEN),
                "analogy": "Mars is like a house whose lights went out long ago -- but maybe someone is still in the basement.",
                "explanation": "Early Mars had warmer, wetter epochs conducive to surface life. Mars then lost much of its early atmosphere (the CO2 needed for greenhouse warming), the temperature dropped and surface water dried up; shrinking reservoirs became saltier and more acidic until no significant surface liquid remained and the surface was bathed in harsh radiation -- uninhabitable. Underground, ice and liquid (probably very salty) water could still exist where pressure and temperature allow, and briny water may briefly flow even today. If life ever took hold, its evidence is hidden in the crust. Guiding principle: 'follow the water'.",
                "why": "The exact storyline 2027 habitability questions expect you to explain.",
            },
        ],
    },
    # ------------------------------------------------------------------ 7
    {
        "name": "Solar System: Moons & Rings of the Giant Planets",
        "description": "Regular vs. irregular moons, the moon and ring systems of Jupiter, Saturn, Uranus and Neptune, and Jupiter's four Galilean moons -- Callisto, Ganymede, Europa and Io -- plus tidal heating.",
        "source_title": "Source reader: Ring and Moon Systems and the Galilean Moons (OpenStax Astronomy 2e, 12.1-12.2)",
        "infographics": ["galilean_moons", "tidal_heating"],
        "source_text": (
            "Outer-solar-system rings and moons formed where it was cold, so lots of water ice; many contain dark organic "
            "compounds -> many objects icy AND dark. Regular (direct) moons: about a quarter; revolve west-to-east in the plane "
            "of the planet's equator. Irregular moons (majority): retrograde (east-to-west), or highly eccentric or inclined "
            "orbits; mostly far from the planet; probably captured.\n"
            "Jupiter: 97 known moons and a faint ring. Galilean moons Callisto, Ganymede, Europa, Io discovered by Galileo in "
            "1610; Europa and Io about our Moon's size; Ganymede and Callisto about Mercury's size. Most other moons small, "
            "retrograde, >20 million km out -- captured asteroids.\n"
            "Saturn: at least 274 known moons (128 small ones announced early 2025) + magnificent rings. Titan almost as big as "
            "Ganymede; only moon with a substantial atmosphere and lakes/seas of liquid hydrocarbons (methane, ethane). Six other "
            "large regular moons 400-1600 km; small moons in/near rings; captured strays. Enceladus has active water geysers. "
            "Rings: broad, flat, major and minor gaps; not solid -- icy fragments (mostly water ice) the size of ping-pong balls, "
            "tennis balls and basketballs, orbiting the equator.\n"
            "Uranus: system tilted 98 deg like the planet; 11 rings and 29 moons; five largest moons 500-1600 km; rings "
            "discovered 1977 -- narrow ribbons of dark material with broad gaps, confined by small (unseen) moons.\n"
            "Neptune: 16 known moons; Triton relatively large in a retrograde orbit, thin atmosphere, active eruptions found by "
            "Voyager (1989); may be a captured dwarf planet like Pluto. Rings narrow, faint, dark.\n"
            "Galileo spacecraft (1996-1999) made repeated close encounters; Juno has viewed Ganymede and Europa. Table 12.1 "
            "(diameter km / mass Moon=1 / density g/cm3 / reflectivity %): Moon 3476/1.0/3.3/12; Callisto 4820/1.5/1.8/20; "
            "Ganymede 5270/2.0/1.9/40; Europa 3130/0.7/3.0/70; Io 3640/1.2/3.5/60; Titan 5150/1.9/1.9/20.\n"
            "Callisto: ~2 million km from Jupiter, 17-day orbit, tidally locked (day = month = 17 days); noon 130 K, ice stable. "
            "Diameter nearly Mercury's but 1/3 the mass -> 1/3 density -> icy interior. Not fully differentiated (no dense core, "
            "from gravity pull on Galileo) -- froze before differentiation finished. Heavily cratered like lunar highlands; no "
            "interior activity; geologically dead >4 billion years ('stillborn'). Cold ice is hard as rock and doesn't flow. Icy "
            "spires 80-100 m tall erode, dark dust slides into lows.\n"
            "Ganymede: largest moon in the solar system. ~1/4 of surface old and cratered like Callisto; rest younger (sparser, "
            "fresher craters), perhaps 2-3 billion years, some as young as Venus' surface (few hundred million). Differentiated: "
            "rock core about our Moon's size, ice mantle and crust; magnetic field (Galileo) -> partially molten interior; very "
            "likely liquid water inside; intermittent activity. Young terrain from tectonic and volcanic forces: cracked crust "
            "flooded craters with water; compression made long ridges and parallel valleys a few km apart; craters split and "
            "pulled apart (Nicholson Regio); hints of plate-tectonic-like motion. Darker = older, lighter = younger (reverse of "
            "the Moon). Why different from Callisto: maybe size/internal heat, more likely Jupiter's tides heating it "
            "episodically.\n"
            "Tidal force = unequal gravitational pull on two sides of a body; moons flexed by Jupiter and each other -> tidal "
            "heating, more important closer to Jupiter.\n"
            "Europa: with Io, mostly rocky (density/size like our Moon). Rocky-inside/icy-outside pattern mirrors planets: inner "
            "parts of Jupiter's disk warmer (faster, more friction). Ice-covered surface (spectra); very few craters -> surface no "
            "more than a few million years old; more geologically active than Earth at erasing craters. Smooth ice crisscrossed by "
            "cracks and ridges thousands of km long, mostly double/multiple ('freeway'); Conamara Chaos ice blocks like icebergs. "
            "Lines are real (unlike Mars canals): cracks in ice floating on liquid water. Ice crust ~1 to 20 km; Juno 2024 data: "
            "maybe twice as thick. Induced magnetic field signature = liquid salty ocean. Maybe the only other place with large "
            "liquid water amounts (Ganymede and Enceladus also show ocean evidence). Warmed by tidal heating; possible warm "
            "springs; Earth's deep-sea hot-spring ecosystems live without sunlight. Europa Clipper launched Oct 2024, arrives "
            "2030; flybys (radiation would destroy an orbiter).\n"
            "Io: innermost Galilean moon, near twin of our Moon in size and density, but highest volcanism in the solar system. "
            "Voyager 1 (March 1979) saw 8 volcanoes erupting, 6 still active 4 months later for Voyager 2; Galileo found >50 "
            "eruptions in 1997; plumes hundreds of km high (one 140 km; Prometheus 75 km); >100 recently active volcanoes; flows "
            "cover ~25% of surface. Mostly hot silicate lava; meeting frozen sulfur and SO2 gives huge plumes; sulfur 'snow' up "
            "to 1,000 km from vents; orange = sulfur, white = SO2; colors are a thin sulfur veneer (Sagan: needs penicillin). "
            "Pillan Patera eruption, 400-km dark deposit, Pele red material (1997-1999). Tvashtar Catena lava fountains. Radiation "
            "near Io intense. Tidal heating: Io about as far from Jupiter as the Moon from Earth; Jupiter >300x Earth's mass -> "
            "several-km bulge; orbit kept eccentric by Europa and Ganymede -> twisting and flexing, like a bent coat hanger; "
            "drove out water and CO2; sulfur compounds now most volatile; interior entirely melted; crust recycled. From Callisto "
            "inward to Io: more activity and heating -- distance from a giant planet shapes moons like distance from the Sun "
            "shapes planets."
        ),
        "story": (
            "MINI SOLAR SYSTEMS\n\n"
            "Each giant planet is like the center of its own little solar system, with dozens of moons and a set of rings. "
            "These formed out where it's cold, so they're made with lots of water ice -- often mixed with dark, carbon-rich "
            "(organic) compounds. Don't be surprised that many moons are both icy AND dark!\n\n"
            "Moons come in two kinds:\n"
            "• REGULAR moons (about a quarter) orbit 'politely': west to east, in the plane of the planet's equator.\n"
            "• IRREGULAR moons (the majority) go backward (retrograde), or on very stretched (eccentric) or tilted (inclined) "
            "orbits. They're mostly far from their planet and were probably captured.\n\n"
            "THE FOUR FAMILIES\n"
            "• JUPITER: 97 known moons and a faint ring. Most are small, backward-orbiting captured asteroids more than 20 million "
            "km away. The stars are the four GALILEAN moons, discovered by Galileo in 1610.\n"
            "• SATURN: at least 274 known moons (128 tiny ones announced in early 2025!). TITAN, almost as big as Ganymede, is the "
            "only moon with a thick atmosphere and lakes of liquid methane and ethane. Six other big regular moons are 400-1,600 km "
            "across, and little ENCELADUS shoots geysers of water into space. Saturn's famous rings are broad and flat, with gaps, "
            "and made of countless icy pieces the size of ping-pong balls, tennis balls and basketballs, swirling in a traffic "
            "jam around the equator.\n"
            "• URANUS: tipped 98 degrees, and its whole ring-and-moon system is tipped too. 11 narrow, dark rings (found in 1977) "
            "with wide gaps, held in place by small moons we mostly haven't seen yet, and 29 known moons (the five largest are "
            "500-1,600 km).\n"
            "• NEPTUNE: 16 known moons and faint, dark, narrow rings. TRITON is large but orbits BACKWARD, has a thin atmosphere and "
            "active eruptions (seen by Voyager in 1989). It may be a captured dwarf planet like Pluto.\n\n"
            "THE GALILEAN MOONS\n"
            "(Explored by the Galileo spacecraft 1996-1999 and lately by Juno.)\n"
            "• Moon (for comparison): 3,476 km, density 3.3, reflects 12%\n"
            "• Io: 3,640 km, density 3.5, reflects 60%\n"
            "• Europa: 3,130 km, density 3.0, reflects 70%\n"
            "• Ganymede: 5,270 km, density 1.9, reflects 40%\n"
            "• Callisto: 4,820 km, density 1.8, reflects 20%\n"
            "• Titan (Saturn, for comparison): 5,150 km, density 1.9, reflects 20%\n"
            "Io and Europa are about the size of our Moon; Ganymede and Callisto are about the size of Mercury.\n\n"
            "CALLISTO: THE FROZEN TIME CAPSULE\n"
            "Callisto is the outermost, about 2 million km from Jupiter, orbiting in 17 days. Like our Moon it always shows the "
            "same face to its planet (its day equals its month). At noon it's only 130 K, so ice never evaporates. It's almost "
            "Mercury's size but only a third of its mass, so it must be icy through much of its inside. Surprisingly, Callisto "
            "never fully separated into layers -- it froze before it could finish. Its surface is crowded with craters, like the "
            "Moon's highlands, and it has been geologically dead for more than 4 billion years. Out there, ice is as hard as rock "
            "and doesn't flow like glaciers. Close-ups show 80-100 m icy spires slowly eroding as dark dust slides downhill.\n\n"
            "GANYMEDE: THE GIANT\n"
            "Ganymede is the largest moon in the whole solar system. About a quarter of its surface is old and cratered; the rest "
            "is younger (maybe 2-3 billion years, some bits only a few hundred million). Unlike Callisto, Ganymede IS layered: a "
            "rocky core about the size of our Moon with an icy mantle and crust on top. It even has a magnetic field, a sign of a "
            "partly molten interior, and very likely liquid water deep inside. Its crust cracked and flooded craters with water, "
            "got squeezed into long ridges and valleys, and even split craters apart -- maybe like Earth's plate tectonics. On "
            "Ganymede, darker means older and lighter means younger (the reverse of our Moon). Why so different from Callisto? "
            "Probably Jupiter's tides, which flex and heat moons closer to the planet.\n\n"
            "WHAT IS TIDAL HEATING?\n"
            "A TIDAL FORCE comes from gravity pulling harder on the near side of a body than the far side. Jupiter's big moons are "
            "caught in a 'dance' with Jupiter and each other that keeps flexing and kneading their insides -- and flexing makes "
            "heat. The closer a moon is to Jupiter, the stronger the effect.\n\n"
            "EUROPA: THE OCEAN MOON\n"
            "Europa and Io are mostly rock, like our Moon. That matches the solar system's pattern: the inner part of Jupiter's "
            "disk was warmer (faster-moving material, more friction), so rocky moons formed close in and icy ones farther out.\n\n"
            "Yet Europa is covered in ice, and that ice has very few craters -- the surface is at most a few million years old. "
            "Europa erases craters faster than Earth does! The ice is smooth but crisscrossed by cracks and ridges thousands of km "
            "long, mostly double or triple, like a giant freeway system. In Conamara Chaos, ice blocks look like icebergs that "
            "drifted, rotated and refroze. Unlike Lowell's fake Martian lines, Europa's lines are real -- the kind of cracks that "
            "form when an ice shell floats on liquid water.\n\n"
            "More evidence: Europa makes a small magnetic field when it moves through Jupiter's magnetic environment, and its "
            "'signature' matches a salty liquid ocean, not ice or rock. The ice shell might be 1 to 20 km thick (Juno data from "
            "2024 suggest maybe twice that). Tidal heating keeps the ocean liquid, and there could be warm springs on the seafloor. "
            "On Earth, whole ecosystems thrive around deep-sea hot springs with no sunlight at all -- could that happen on Europa? "
            "Many scientists think Europa is the most likely place beyond Earth to find life. NASA's EUROPA CLIPPER launched in "
            "October 2024 and arrives in 2030; it will swoop past in flybys, because Jupiter's radiation would fry an orbiter's "
            "electronics. (Ganymede and Saturn's Enceladus also show signs of hidden oceans.)\n\n"
            "IO: THE VOLCANO MOON\n"
            "Io is our Moon's near-twin in size and density, but it has the most volcanic activity in the solar system -- far more "
            "than Earth. Voyager 1 saw 8 volcanoes erupting in March 1979; 6 were still going when Voyager 2 passed four months "
            "later. Galileo found more than 50 eruptions in 1997 alone, plumes hundreds of km high (one about 140 km; the "
            "Prometheus plume about 75 km), and more than 100 recently active volcanoes whose lava covers about 25% of the moon. "
            "The lava is hot silicate rock like Earth's, but when it hits frozen sulfur and sulfur dioxide, giant plumes shoot up "
            "and colorful sulfur 'snow' falls up to 1,000 km away. Io's yellow-orange-white colors are just a thin coat of sulfur "
            "compounds. (Carl Sagan joked Io looks like it needs a shot of penicillin.) New features appeared between Galileo's "
            "orbits -- like the 400-km dark deposit from Pillan Patera, soon partly covered by red material from the volcano Pele.\n\n"
            "HOW DOES A SMALL MOON STAY SO HOT?\n"
            "Io is about as far from Jupiter as our Moon is from Earth, but Jupiter is more than 300 times as massive as Earth. "
            "Its gravity stretches Io into a slightly egg shape with a bulge several km high. If Io's orbit were a perfect circle, "
            "the bulge would just sit there. But Europa and Ganymede keep tugging Io's orbit into a slight oval, so Io moves nearer "
            "and farther and twists back and forth. Its insides get flexed like a wire coat hanger bent back and forth -- and they "
            "heat up. Over billions of years this melted Io's interior and drove away its water and CO2; now sulfur is the most "
            "volatile stuff left, and volcanoes constantly recycle the crust.\n\n"
            "THE BIG PATTERN\n"
            "Going inward from Callisto to Io, the moons get rockier, hotter and more active. Just as a planet's character depends "
            "on its distance from the Sun, a moon's character depends on its distance from its giant planet -- thanks largely to "
            "tidal heating."
        ),
        "concepts": [
            {
                "term": "Regular vs. irregular moons",
                "badge": ("2 KINDS", "of moons", "#a39e93"),
                "analogy": "Regular moons are kids walking in line with the class; irregular moons are kids who wandered in from another school.",
                "explanation": "Roughly a quarter of outer-solar-system moons are regular (direct): they revolve west-to-east in the plane of the planet's equator. The majority are irregular: retrograde (east-to-west) orbits, or high eccentricity (more elliptical) or high inclination (in and out of the equatorial plane). Irregular moons are mostly far from their planet and were probably formed elsewhere and captured. Outer moons and rings are icy (formed where it was cold) and often dark from organic compounds.",
                "why": "Captured moons like Triton show how bodies can move between systems.",
            },
            {
                "term": "Jupiter's and Saturn's systems",
                "badge": ("97/274", "moons", GAS),
                "analogy": "Saturn's rings are like a giant highway jammed with ice cubes from ping-pong ball to basketball size.",
                "explanation": "JUPITER: 97 known moons and a faint ring. Its four large Galilean moons -- Io, Europa, Ganymede and Callisto -- were discovered by Galileo in 1610; most of the others are small moons in backward (retrograde) orbits more than 20 million km out, probably captured asteroids. SATURN: at least 274 known moons (128 small ones announced in early 2025) plus its magnificent rings. Its largest moon, TITAN, was discovered by Christiaan Huygens in 1655; it is almost as big as Ganymede and is the only moon with a thick atmosphere and lakes of liquid methane and ethane. Six other large regular moons are 400-1,600 km across, and little Enceladus shoots geysers of water. Saturn's rings are broad and flat with gaps, made of countless icy pieces the size of ping-pong balls to basketballs, kept in line partly by shepherd moons like Pan and Prometheus. Note: older references list 'Jupiter 79+ moons, Saturn 60+' -- moon counts keep rising as telescopes find more tiny ones, so use the newest numbers.",
                "why": "Moon counts, discoverers and Titan facts are common test questions.",
            },
            {
                "term": "Uranus' and Neptune's systems",
                "badge": ("98°", "tilt", ICE),
                "analogy": "Uranus is a planet rolling on its side, and its moons and rings roll along with it.",
                "explanation": "URANUS (discovered 1781): its ring and moon system is tilted 98 degrees, like the planet. It has 11 rings and 29 known moons; the five major moons are Miranda, Ariel, Umbriel, Titania and Oberon (500-1,600 km across). Its rings, discovered in 1977, are narrow ribbons of dark material with wide gaps, probably held in place by small, mostly unseen shepherd moons. NEPTUNE (discovered 1846): 16 known moons and narrow, faint, dark rings. Its largest moon, TRITON, orbits backward (retrograde) -- unusual for a big moon -- has a thin atmosphere, and showed active eruptions to Voyager 2 in 1989; it may be a captured dwarf planet like Pluto. Neptune and Pluto are in a 3:2 orbital resonance.",
                "why": "Uranus' moon names and Triton's retrograde orbit are classic test facts.",
            },
            {
                "term": "Moons of the rocky planets and Pluto",
                "badge": ("1+2", "inner moons", "#bdbdbd"),
                "analogy": "The inner planets travel light: Mercury and Venus have no moons at all, Earth has one, and Mars has two little potatoes.",
                "explanation": "Mercury and Venus have no moons. EARTH has one, the Moon (3,476 km across, density 3.3), which is tidally locked so we always see the same face; it has been geologically dead since major volcanism stopped about 3.3 billion years ago. MARS has two tiny, lumpy moons, PHOBOS and DEIMOS, discovered in 1877 -- probably captured asteroids. Out past Neptune, the dwarf planet PLUTO has five known moons; the largest, CHARON, is so big compared to Pluto that the two are mutually tidally locked, each always showing the other the same face. In all, about 430 moons are known around the planets and dwarf planets.",
                "why": "Completes the moon roster tests ask about, not just the giant planets'.",
            },
            {
                "term": "Galilean moons data (Table 12.1)",
                "badge": ("I-E-G-C", "in order", GOLD),
                "analogy": "From Jupiter outward remember 'I Eat Green Carrots': Io, Europa, Ganymede, Callisto.",
                "explanation": "Diameter (km) / mass (Moon = 1) / density (g/cm3) / reflectivity: Moon 3,476 / 1.0 / 3.3 / 12%. Io 3,640 / 1.2 / 3.5 / 60%. Europa 3,130 / 0.7 / 3.0 / 70%. Ganymede 5,270 / 2.0 / 1.9 / 40%. Callisto 4,820 / 1.5 / 1.8 / 20%. Titan (Saturn) 5,150 / 1.9 / 1.9 / 20%. Io and Europa are about our Moon's size and rocky; Ganymede and Callisto are about Mercury's size and icy. Rocky-inside, icy-outside mirrors the solar system: Jupiter's inner disk was warmer from faster motion and friction. Explored by the Galileo orbiter (1996-1999) and Juno.",
                "why": "Density and order questions on the Galilean moons are very common.",
            },
            {
                "term": "Callisto",
                "badge": ("dead", "4 Gyr", "#6d6459"),
                "analogy": "Callisto is a frozen time capsule -- nothing has changed there for over 4 billion years.",
                "explanation": "Outermost Galilean moon, ~2 million km from Jupiter, 17-day orbit, tidally locked (its day equals its 17-day month). Noon temperature 130 K, so surface ice never evaporates. Diameter 4,820 km, almost Mercury's, but only one-third the mass, so one-third the density: an icy interior. Gravity measurements by Galileo show no dense core -- Callisto is not fully differentiated; it froze before differentiation finished. Its surface is covered in impact craters (like the lunar highlands), showing no interior forces at work: geologically dead for over 4 billion years. Ice this cold is nearly as hard as rock and doesn't flow; icy spires 80-100 m tall erode as dark dust slides down.",
                "why": "The 'baseline' moon: weakest tidal heating = no activity, low habitability potential.",
            },
            {
                "term": "Ganymede",
                "badge": ("5,270", "km", "#a39e93"),
                "analogy": "Ganymede is the king of moons -- bigger than Mercury and with its own magnetic shield.",
                "explanation": "The largest moon in the solar system. About a quarter of its surface is old and heavily cratered like Callisto's; the rest is younger (sparser, fresher craters), perhaps 2-3 billion years, with some features as young as Venus' surface (a few hundred million years). It is differentiated: a rocky core about the size of our Moon with an ice mantle and crust. Galileo found a magnetic field -- the signature of a partially molten interior -- and there is very likely liquid water inside. Young terrain came from tectonic and volcanic forces: cracked crust flooding craters with water, compression making long ridges with valleys a few km apart, craters split apart (Nicholson Regio), hints of plate-tectonic-like motion. Darker areas are older, lighter younger (opposite of the Moon). Its activity is probably driven by episodic tidal heating from Jupiter.",
                "why": "Ganymede is one of the 'ocean worlds' with possible subsurface liquid water.",
            },
            {
                "term": "Tidal force and tidal heating",
                "badge": ("FLEX", "= heat", RED),
                "analogy": "Bend a paper clip back and forth fast and it gets warm -- that's tidal heating for moons.",
                "explanation": "A tidal force results from the unequal gravitational pull on two sides of a body. Jupiter's large moons are caught in the varying gravity of the giant planet and of each other, which flexes and kneads their interiors and heats them -- tidal heating. It matters more for moons closer to Jupiter: from Callisto inward to Io there is more and more geological activity and internal heating. Tidal heating likely keeps Europa's ocean liquid and may affect Saturn's Enceladus. Tidal friction can also slow rotations (e.g. Venus' slow spin, tidally locked moons).",
                "why": "Tidal heating lets oceans exist far outside the Sun's habitable zone -- huge for 2027.",
            },
            {
                "term": "Europa's ocean",
                "badge": ("OCEAN", "under ice", "#e8e2d0"),
                "analogy": "Europa is like a frozen pond with a thick ice lid -- but the 'pond' is a whole global ocean.",
                "explanation": "Europa is mostly rocky (density 3.0) but ice-covered. Very few craters mean its surface is no more than a few million years old -- more active than Earth at erasing craters. The smooth ice is crisscrossed by cracks and ridges thousands of km long, mostly double or multiple; in Conamara Chaos ice blocks slid and rotated like icebergs and refroze. These real straight lines form when an ice crust floats almost frictionlessly on liquid water; water or slush seeps up through cracks. The crust may be ~1 to 20 km thick (Juno 2024 data: possibly twice that). Its induced magnetic field (from Jupiter's magnetosphere) has the signature of a liquid salty ocean. The ocean is warmed by tidal heating; warm springs could exist, like Earth's deep-sea hot-spring ecosystems that live without sunlight.",
                "why": "Many scientists consider Europa the most likely place beyond Earth to find life.",
            },
            {
                "term": "Europa Clipper",
                "badge": ("2030", "arrival", BLUE),
                "analogy": "Clipper dips in and out of danger like a swimmer diving into an ice-cold pool and climbing back out.",
                "explanation": "NASA's Europa Clipper mission will characterize Europa's liquid ocean and ice crust and find places where interior material has risen to the surface -- material that might reveal direct evidence of microbial life. It will not orbit Europa, because the intense energetic particles of Jupiter's magnetosphere would quickly destroy its electronics; instead it makes brief close flybys. It launched successfully in October 2024 and is scheduled to arrive in the Jupiter system in 2030.",
                "why": "Current missions targeting habitability are fair game on 2027 tests.",
            },
            {
                "term": "Io, the volcanic moon",
                "badge": ("100+", "volcanoes", "#f4d35e"),
                "analogy": "Io is a pizza-colored moon that never stops bubbling -- the most volcanic place in the solar system.",
                "explanation": "Io is nearly our Moon's twin in size and density but has the highest level of volcanism in the solar system, exceeding Earth's. Voyager 1 (March 1979) saw 8 volcanoes erupting; 6 were still active when Voyager 2 passed four months later. Galileo found more than 50 eruptions in 1997 alone, plumes hundreds of km high (one ~140 km, Prometheus ~75 km), and more than 100 recently active volcanoes whose flows cover ~25% of the surface. The lava is hot silicate (like Earth's); when it hits frozen sulfur and SO2, huge plumes form and sulfur 'snow' falls up to 1,000 km from vents. Orange deposits are sulfur, white is SO2 -- only a thin veneer. Features changed between orbits (Pillan Patera's 400-km dark deposit, later partly covered by red material from Pele). Radiation near Io's orbit is the most intense.",
                "why": "Io shows tidal heating at its most extreme -- a model for tidally heated exoplanets.",
            },
            {
                "term": "Why Io is so hot",
                "badge": ("300×", "Earth mass", RED),
                "analogy": "Io's orbit is like a squeeze toy being pressed and released over and over.",
                "explanation": "Io is about as far from Jupiter as our Moon is from Earth, but Jupiter is more than 300 times as massive as Earth, so it pulls Io into an elongated shape with a bulge several km high toward Jupiter. If Io kept exactly the same face toward Jupiter on a circular orbit, the bulge wouldn't generate heat. But tugs from Europa and Ganymede keep Io's orbit slightly eccentric, so Io moves nearer and farther and twists back and forth each orbit, flexing its interior like a bent wire coat hanger. Over billions of years this drove away water, CO2 and other gases (sulfur compounds are now the most volatile materials left), melted its interior entirely, and keeps recycling the crust.",
                "why": "Explains the distance-from-planet pattern: Io (hottest) to Callisto (coldest).",
            },
        ],
    },
]
