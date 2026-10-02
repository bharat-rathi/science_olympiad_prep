"""Unit 1 -- Space Basics: the tools for everything else (distances, orbits,
the Sun and stars, and how the Solar System formed).

Lesson chapter format (shared by every lessons_unit*.py file, consumed by
seed.py):
  unit           -> unit number (see UNITS in plan.py)
  name           -> the chapter's sub-topic name
  description    -> one-line summary shown on the chapter card
  goals          -> "By the end of this chapter you can..." bullets
  sections       -> the in-depth explanation, in reading order. Each is
                    {"heading", "body", "infographic"?}; body is plain text
                    (blank line = new paragraph, "• " = bullet) and an
                    infographic key (infographics.INFOGRAPHICS) is shown
                    right under the section it explains.
  word_bank      -> (word, kid-friendly meaning) for every jargon word the
                    chapter uses; the student page highlights them in the
                    text and lists them in a Word bank tab.
  key_facts      -> short note-sheet lines (numbers and names to memorize)
  quick_check    -> (question, answer) self-test pairs
  cards          -> review flashcards {term, badge (label, sub, color),
                    analogy, explanation, why}

Written for 11-12 year olds with little science background: every idea
starts from something familiar, every number is explained, and nothing
from the source reader (OpenStax Astronomy 2e) or the scioly.org Solar
System wiki is left out -- each fact lives in exactly one chapter.
"""

from app.content.solar_system.svg import BLUE, GOLD, ICE, PURPLE, RED, ROCK, SUN

UNIT1 = [
    # ------------------------------------------------------------------ 1
    {
        "unit": 1,
        "name": "Solar System: Space Basics -- Distances, Orbits & Measuring",
        "description": "The toolkit for the whole event: what the Solar System is, how big space is (km, AU, light-years), orbits vs. spins, days, years and seasons, density, and the planet data table.",
        "goals": [
            "Say what the Solar System is and name everything in it.",
            "Use astronomical units (AU) and light-years, and read big numbers in scientific notation.",
            "Explain the difference between rotation (a day) and revolution (a year), and what causes seasons.",
            "Use density to tell whether a world is made of rock, ice or gas.",
            "Read the planet data table that many test questions are built on.",
        ],
        "sections": [
            {
                "heading": "What is the Solar System?",
                "body": (
                    "The Solar System is the Sun plus everything that travels around it: eight planets, their moons and "
                    "rings, dwarf planets like Pluto, and millions of smaller leftovers -- asteroids, comets and specks of "
                    "dust. Almost all of it was born together, about 4.5 billion years ago, from one giant spinning cloud of "
                    "gas and dust.\n\n"
                    "Any star that has planets has a PLANETARY SYSTEM. Ours gets the special name 'solar system' because an "
                    "old Latin name for the Sun is Sol. So when you read about a planet around another star, the correct "
                    "phrase is 'another planetary system', not 'another solar system' -- tests like to check that!\n\n"
                    "Picture a huge, flat racetrack. The Sun sits in the middle. The planets race around it in their own "
                    "lanes, all going the same direction. The inner lanes hold four small rocky planets (Mercury, Venus, "
                    "Earth, Mars). The outer lanes hold four giant planets (Jupiter, Saturn, Uranus, Neptune). Between the "
                    "two groups is the asteroid belt, and far beyond Neptune are the icy Kuiper Belt and the distant Oort "
                    "Cloud.\n\n"
                    "The Solar System is also the one part of the universe we can actually visit. Robot spacecraft have "
                    "flown past, orbited or landed on every planet, and people have walked on the Moon."
                ),
            },
            {
                "heading": "How far is far? Kilometers, AU and light-years",
                "body": (
                    "Space is so big that kilometers quickly become silly. Earth is about 150,000,000 km (150 million km) "
                    "from the Sun. Writing all those zeros gets tiring, so astronomers use bigger rulers:\n\n"
                    "• The ASTRONOMICAL UNIT (AU) is the average distance from Earth to the Sun: about 150 million km. Earth "
                    "is at 1 AU. Mars is at 1.52 AU (one and a half times as far). Jupiter is at 5.2 AU and Neptune at about "
                    "30 AU.\n"
                    "• A LIGHT-YEAR is how far light travels in one year: about 9.46 trillion km, or about 63,000 AU. It is "
                    "a distance, not a time! The nearest star after the Sun, Proxima Centauri, is about 4.2 light-years away.\n\n"
                    "Light is the fastest thing there is (300,000 km every second), yet sunlight still needs about 8 minutes "
                    "to reach Earth, about 43 minutes to reach Jupiter, and more than 4 hours to reach Neptune. When you look "
                    "at the Sun's light, you are seeing light that left it 8 minutes ago.\n\n"
                    "SCIENTIFIC NOTATION is a shortcut for huge or tiny numbers. Instead of 150,000,000 we write 1.5 x 10^8: "
                    "the little 8 (the EXPONENT) tells you to move the decimal point 8 places to the right. The Sun's mass, "
                    "1.989 x 10^30 kg, would need 30 places! A negative exponent moves the point to the left: 10^-3 = 0.001."
                ),
                "infographic": "scale_ruler",
            },
            {
                "heading": "Orbits and spins: days, years and seasons",
                "body": (
                    "Planets do two kinds of moving at the same time, like a spinning top that also circles a table.\n\n"
                    "• ROTATION means spinning on an imaginary pole through the planet, called its AXIS. One full spin is "
                    "one DAY. Earth rotates once in about 24 hours (more exactly, 23 h 56 min).\n"
                    "• REVOLUTION means traveling all the way around the Sun. That path is an ORBIT, and one trip is one "
                    "YEAR. Earth takes 365.25 days.\n\n"
                    "All eight planets revolve in the same direction and in almost the same flat plane, on orbits that are "
                    "nearly circles (really slightly squashed circles called ellipses -- see the Kepler chapter). Most "
                    "planets also spin in that same direction. The rule-breakers are clues to violent collisions long ago: "
                    "Venus spins backward (this is called RETROGRADE) and very slowly, and Uranus and Pluto are tipped over "
                    "and spin on their sides. Funny fact: Venus takes 243 Earth days to spin once but only 225 days to orbit, "
                    "so its day is longer than its year!\n\n"
                    "WHY DO WE HAVE SEASONS? Not because Earth gets closer to the Sun -- Earth's orbit is almost a circle. "
                    "Seasons happen because Earth's axis is TILTED (by about 23.5 degrees). For half the year the Northern "
                    "Hemisphere leans toward the Sun: sunlight hits it more directly and days are longer, so it is summer. "
                    "Half a year later it leans away, and it is winter. Mars is tilted about 25 degrees, so it has seasons "
                    "too -- each one about six months long, because a Mars year is almost two Earth years."
                ),
                "infographic": "orbit_vs_spin",
            },
            {
                "heading": "Mass, weight and density -- what is a world made of?",
                "body": (
                    "MASS is how much stuff (matter) something contains, measured in kilograms. WEIGHT is how hard gravity "
                    "pulls on that stuff. On the Moon you would weigh less, but your mass would be exactly the same.\n\n"
                    "DENSITY tells you how tightly the stuff is packed: density = mass / volume. A bowling ball and a beach "
                    "ball are the same size, but the bowling ball is packed with much more matter, so it is far denser. For "
                    "planets, density is a superpower: it tells us what a world is made of without visiting it.\n\n"
                    "We measure density in grams per cubic centimeter (g/cm3). Water is 1 g/cm3 (that is the same as 1,000 "
                    "kg/m3 -- multiply by 1,000). Ice is a bit less than 1, rock is about 3, and iron is about 8. So:\n"
                    "• about 1 = mostly ice or gas\n"
                    "• about 3 = mostly rock\n"
                    "• more than 3 = rock plus a heavy metal core\n\n"
                    "The rocky planets have densities from 3.9 (Mars) to 5.5 g/cm3 (Earth -- the densest planet of all). "
                    "The giant planets are only 0.7 to 1.6. Saturn, at 0.7, is less dense than water: in a big enough "
                    "bathtub it would float! Saturn's little moon Mimas comes out at about 1.2, so it must be mostly ice.\n\n"
                    "To find a planet's volume we use the formula for a ball (a SPHERE): V = (4/3) x pi x R^3, where R is "
                    "the radius (the distance from the center to the surface) and pi is about 3.14."
                ),
            },
            {
                "heading": "Who has all the mass?",
                "body": (
                    "If you could put the whole Solar System on a giant scale, the Sun would make up 99.8% of the total. "
                    "Jupiter has about 0.1%. Everything else -- the other seven planets, the dwarf planets, all the moons, "
                    "comets, asteroids and dust -- shares the tiny bit left over.\n\n"
                    "Jupiter is the 'second boss': it has more mass than all the other planets put together, and about "
                    "1,300 Earths could fit inside it.\n\n"
                    "How do you weigh a planet you can't put on a scale? You watch how hard it pulls on things. Long ago, "
                    "astronomers used Kepler's and Newton's laws to measure how a planet tugs on its moons. Today we also "
                    "track how a planet bends the path of a spacecraft flying past it."
                ),
                "infographic": "mass_budget",
            },
            {
                "heading": "Two families of planets and the planet data table",
                "body": (
                    "The inner four planets -- Mercury, Venus, Earth and Mars -- are the TERRESTRIAL planets (from the Latin "
                    "word for Earth). They are small, made of rock and metal, dense, and have solid surfaces covered in "
                    "craters, mountains and volcanoes. The Moon is often counted with them.\n\n"
                    "The outer four -- Jupiter, Saturn, Uranus and Neptune -- are the JOVIAN or giant planets ('Jove' is "
                    "another name for Jupiter). They are huge, made mostly of light gases, liquids and ices, and have no "
                    "solid ground to stand on: think of a giant ball of soda with a small pebble (a dense core) in the "
                    "middle. All four have rings and many moons.\n\n"
                    "The infographic below is the planet 'baseball card' table. Notice the patterns:\n"
                    "• Farther from the Sun = longer year (Mercury 88 days, Neptune 165 years).\n"
                    "• The giants spin fastest: Jupiter's day is only about 10 hours.\n"
                    "• Rocky planets are dense; giants are not.\n"
                    "Five planets were known to ancient people because you can see them without a telescope (Mercury, Venus, "
                    "Mars, Jupiter, Saturn). Uranus (found March 13, 1781) and Neptune (found September 23, 1846) needed "
                    "telescopes.\n\n"
                    "The scioly.org wiki gives each planet's RADIUS and MASS too: Mercury 2,439.7 km and 3.302 x 10^23 kg; "
                    "Venus 6,051.9 km and 4.869 x 10^24 kg; Earth 6,371 km and 5.9742 x 10^24 kg; Mars 3,389.5 km and "
                    "6.4191 x 10^23 kg; Jupiter about 71,500 km and 1.8987 x 10^27 kg; Saturn 60,268 km and 5.6851 x 10^26 "
                    "kg; Uranus 25,559 km and 8.6849 x 10^25 kg; Neptune 24,764 km and 1.0244 x 10^26 kg."
                ),
                "infographic": "planet_lineup",
            },
        ],
        "word_bank": [
            ("Solar System", "The Sun and everything that orbits it: planets, moons, dwarf planets, asteroids, comets and dust."),
            ("Planetary system", "Any star together with the planets that orbit it. Ours is the only one called the 'solar' system."),
            ("Planet", "A big, round world that orbits a star and has cleared its path of other objects (there are 8 in our Solar System)."),
            ("Astronomical unit (AU)", "The average Earth-Sun distance, about 150 million km. Handy for measuring distances inside the Solar System."),
            ("Light-year", "The distance light travels in one year: about 9.46 trillion km. It measures distance, not time."),
            ("Scientific notation", "A short way to write huge or tiny numbers, like 1.5 x 10^8 instead of 150,000,000."),
            ("Exponent", "The small number in 10^8 that tells you how many places to move the decimal point."),
            ("Axis", "An imaginary pole through a planet's center that it spins around."),
            ("Rotation", "Spinning around your own axis. One rotation of a planet is one day."),
            ("Revolution", "Traveling all the way around another object. One revolution around the Sun is one year."),
            ("Orbit", "The path one object follows as it travels around another, held by gravity."),
            ("Retrograde", "Moving or spinning backward compared with almost everything else in the Solar System."),
            ("Axial tilt", "How far a planet's axis leans over. Earth's tilt (about 23.5 degrees) causes the seasons."),
            ("Mass", "How much matter (stuff) something contains, measured in kilograms. It doesn't change from planet to planet."),
            ("Weight", "How hard gravity pulls on your mass. You would weigh less on the Moon."),
            ("Density", "How tightly packed something is: mass divided by volume. Water is 1 g/cm3, rock about 3, iron about 8."),
            ("Volume", "How much space something takes up."),
            ("Sphere", "A perfectly round ball shape. Its volume is (4/3) x pi x radius^3."),
            ("Radius", "The distance from the center of a circle or ball to its edge. Half the diameter."),
            ("Diameter", "The distance straight across a circle or ball through its center."),
            ("Terrestrial planet", "A small, rocky, dense planet with a solid surface: Mercury, Venus, Earth, Mars."),
            ("Jovian planet", "A giant planet made mostly of gas, liquid and ice with no solid surface: Jupiter, Saturn, Uranus, Neptune."),
        ],
        "key_facts": [
            "1 AU = about 150 million km (1.5 x 10^8 km) = the Earth-Sun distance.",
            "1 light-year = about 9.46 trillion km = about 63,000 AU. Proxima Centauri: 4.2 light-years.",
            "Sunlight takes about 8.3 minutes to reach Earth.",
            "The Sun has 99.8% of the Solar System's mass; Jupiter has most of the rest (0.1%).",
            "Water = 1 g/cm3; Earth = 5.5 g/cm3 (densest planet); Saturn = 0.7 g/cm3 (would float).",
            "Seasons come from axial tilt (Earth about 23.5 degrees), NOT from distance to the Sun.",
            "Venus spins backward (retrograde); Uranus and Pluto spin on their sides.",
            "Uranus discovered March 13, 1781; Neptune discovered September 23, 1846.",
        ],
        "quick_check": [
            ("What is the difference between a solar system and a planetary system?", "A planetary system is any star with planets. 'The Solar System' is the name of ours, because the Sun is called Sol."),
            ("Mars is 1.52 AU from the Sun. About how many km is that?", "1.52 x 150 million km = about 228 million km (the reader says 227 million km)."),
            ("Is a light-year a unit of time or distance?", "Distance -- the distance light travels in one year, about 9.46 trillion km."),
            ("What causes Earth's seasons?", "The tilt of Earth's axis. The hemisphere leaning toward the Sun gets more direct sunlight and longer days."),
            ("A moon has a density of 1.2 g/cm3. What is it mostly made of?", "Mostly ice (water is 1 and rock about 3), like Saturn's moon Mimas."),
            ("Which planet would float in water, and why?", "Saturn, because its density (0.7 g/cm3) is less than water's (1 g/cm3)."),
        ],
        "cards": [
            {
                "term": "Astronomical unit (AU)",
                "badge": ("1 AU", "150M km", BLUE),
                "analogy": "The AU is a 'Solar System ruler' -- one tick is the trip from the Sun to Earth.",
                "explanation": "1 AU is the average Earth-Sun distance, about 150 million km. Mars is at 1.52 AU, Jupiter 5.2 AU, Neptune about 30 AU. Sunlight crosses 1 AU in about 8.3 minutes.",
                "why": "Kepler's third law (p^2 = a^3) and many distance questions use AU.",
            },
            {
                "term": "Light-year",
                "badge": ("ly", "distance!", PURPLE),
                "analogy": "A light-year is like saying 'my school is a 10-minute walk away' -- a time word used to mean a distance.",
                "explanation": "A light-year is the distance light travels in a year: about 9.46 trillion km, or 63,000 AU. The nearest star after the Sun, Proxima Centauri, is 4.2 light-years away.",
                "why": "Exoplanet distances are always given in light-years.",
            },
            {
                "term": "Rotation vs. revolution",
                "badge": ("DAY", "vs YEAR", GOLD),
                "analogy": "A spinning top (rotation) that also circles the table (revolution).",
                "explanation": "Rotation = spinning on your axis; one rotation is a day. Revolution = going around the Sun; one revolution is a year. All planets revolve the same direction in nearly the same plane; Venus rotates backward and Uranus is tipped on its side.",
                "why": "Mixing up 'day' and 'year' is the most common mistake on planet-data questions.",
            },
            {
                "term": "Why we have seasons",
                "badge": ("23.5°", "tilt", SUN),
                "analogy": "Tilt a flashlight's beam onto a table: a slanted beam spreads out and feels weaker.",
                "explanation": "Earth's axis is tilted about 23.5 degrees. The hemisphere leaning toward the Sun gets more direct light and longer days (summer); the other gets slanted light and short days (winter). Distance has almost nothing to do with it.",
                "why": "Tilt changes how much starlight a planet's surface gets -- important for habitability.",
            },
            {
                "term": "Density",
                "badge": ("m/V", "density", ROCK),
                "analogy": "A bowling ball and a beach ball are the same size, but one is packed with much more stuff.",
                "explanation": "Density = mass / volume. Water 1, rock about 3, iron about 8 g/cm3. Rocky planets are 3.9-5.5 (Earth 5.5 is densest), giants 0.7-1.6 (Saturn 0.7 would float). A sphere's volume is (4/3) x pi x R^3.",
                "why": "Density tells you if a planet or exoplanet is rocky, icy or gassy.",
            },
            {
                "term": "The Sun's 99.8%",
                "badge": ("99.8%", "the Sun", SUN),
                "analogy": "If the Solar System weighed 1,000 kg, the Sun would be 998 kg and everything else would share 2 kg.",
                "explanation": "The Sun holds 99.8% of the mass; Jupiter has about 0.1% -- more than all other planets combined, and about 1,300 Earths would fit inside it.",
                "why": "'Which body has the most mass after the Sun?' -- Jupiter.",
            },
            {
                "term": "Terrestrial vs. Jovian planets",
                "badge": ("4 + 4", "planets", ICE),
                "analogy": "Rocky marbles close to the Sun; giant soda balls with a pebble inside far away.",
                "explanation": "Terrestrial: Mercury, Venus, Earth, Mars -- small, rocky, dense, solid surfaces. Jovian: Jupiter, Saturn, Uranus, Neptune -- huge, gas/liquid/ice, no solid surface, all with rings and many moons.",
                "why": "Only solid-surfaced worlds can hold surface oceans like Earth's.",
            },
            {
                "term": "Scientific notation",
                "badge": ("10^8", "shortcut", RED),
                "analogy": "Like writing 'a dozen dozen' instead of counting 144 eggs one by one.",
                "explanation": "1.5 x 10^8 means 1.5 with the decimal point moved 8 places right: 150,000,000. A negative exponent moves it left: 6.67 x 10^-11 = 0.0000000000667.",
                "why": "Every gravity, escape-velocity and mass calculation uses it.",
            },
        ],
    },
    # ------------------------------------------------------------------ 2
    {
        "unit": 1,
        "name": "Solar System: The Sun & the Lives of Stars",
        "description": "Our star up close -- its size, layers, temperatures, how fusion makes its light, why it slowly brightens -- and the life story of stars from cloud to white dwarf, supernova, neutron star or black hole.",
        "goals": [
            "Give the Sun's key numbers and name its layers from the core outward.",
            "Explain nuclear fusion in simple words and how the Sun's energy reaches us.",
            "Describe how a star is born and how Sun-like and massive stars end their lives.",
            "Explain why we are 'made of star stuff'.",
        ],
        "sections": [
            {
                "heading": "Our star by the numbers",
                "body": (
                    "The Sun is a STAR: a giant ball of hot, glowing gas that makes its own light. It is the biggest thing in "
                    "the Solar System.\n\n"
                    "• Diameter: 1,392,000 km -- about 109 Earths lined up side by side.\n"
                    "• Mass: 1.989 x 10^30 kg -- 99.8% of the whole Solar System.\n"
                    "• Made of: about 74% hydrogen and 25% helium, with a sprinkle of other elements.\n"
                    "• LUMINOSITY (the total energy it gives off every second): 3.846 x 10^26 watts, which the wiki writes as "
                    "3.846 x 10^33 erg/s (an erg is a tiny energy unit). That is like trillions of trillions of light bulbs.\n"
                    "• Age: about 4.6 billion years -- roughly halfway through its life.\n\n"
                    "The Sun is brighter than about 80% of the stars in our Galaxy, but it is still an ordinary, middle-aged "
                    "star. Because it is a ball of gas, not a solid ball, different parts spin at different speeds: the "
                    "equator turns once in about 25 days, but the regions near the poles take about 35 days."
                ),
            },
            {
                "heading": "The Sun's power plant: nuclear fusion",
                "body": (
                    "Deep in the Sun's CORE the temperature is about 15,000,000 degrees C and the pressure is enormous. "
                    "There, the centers of hydrogen atoms (their NUCLEI) smash together so hard that they stick and become "
                    "helium. This is NUCLEAR FUSION. Each time it happens, a little bit of mass turns into a lot of energy. "
                    "Fusion is what makes the Sun -- and every star -- shine.\n\n"
                    "Gravity is always trying to squeeze the Sun smaller, and the energy from fusion pushes outward. The two "
                    "are balanced, which is why the Sun stays the same size for billions of years.\n\n"
                    "The Sun slowly gets brighter as it ages: it is at least 30% brighter today than it was 4 billion years "
                    "ago. That small change matters a lot for which planets can hold liquid water (see the Habitability "
                    "chapter)."
                ),
            },
            {
                "heading": "A trip from the core to the corona",
                "body": (
                    "The Sun is built in layers, like an onion. Starting at the center and moving out (temperatures from the "
                    "scioly.org wiki):\n\n"
                    "• CORE (about 15,000,000 C): where fusion makes the energy.\n"
                    "• RADIATIVE ZONE (about 2,000,000 C): energy creeps outward as light, bouncing around for a very long "
                    "time.\n"
                    "• CONVECTION ZONE: hot gas rises, cools and sinks again, like boiling soup, carrying the heat up. "
                    "(Moving heat by moving hot material is called CONVECTION.)\n"
                    "• PHOTOSPHERE (about 6,000 C): the visible 'surface' -- the part we see shining.\n"
                    "• CHROMOSPHERE: a thin, reddish layer above the surface.\n"
                    "• TRANSITION REGION: a thin zone where the temperature shoots up.\n"
                    "• CORONA (about 1,000,000 C): the Sun's wispy outer atmosphere, seen as a glowing crown during a total "
                    "solar eclipse. Strangely, it is far hotter than the surface below it!\n\n"
                    "From the photosphere and corona, the energy flies out into space as light and heat -- the rays that warm "
                    "every planet. A memory trick from the center out: 'Cows Run Cautiously, Peacefully Chewing The Corn' "
                    "(Core, Radiative, Convection, Photosphere, Chromosphere, Transition region, Corona)."
                ),
                "infographic": "sun_layers",
            },
            {
                "heading": "How a star is born",
                "body": (
                    "Space between stars is not totally empty. It contains huge, cold clouds of gas and dust called NEBULAE "
                    "(one is a NEBULA). Inside a nebula, a cold, dense clump can start to collapse under its own gravity. As "
                    "it shrinks, it gets hotter and starts to glow: this baby star is a PROTOSTAR.\n\n"
                    "When the protostar's core finally gets hot and dense enough to start hydrogen fusion, the star 'switches "
                    "on'. It is now a MAIN-SEQUENCE star -- the long, steady adult stage where a star spends most of its "
                    "life, with fusion pushing out and gravity pulling in, perfectly balanced. Our Sun is a main-sequence "
                    "star today.\n\n"
                    "Leftover gas and dust swirling around a newborn star flattens into a disk, and that disk is where "
                    "planets form (see the next chapter and 'Planets Forming Around Other Stars')."
                ),
            },
            {
                "heading": "How stars die -- it depends on their mass",
                "body": (
                    "A star's MASS decides its whole future.\n\n"
                    "LOW- AND MEDIUM-MASS STARS (like the Sun):\n"
                    "• When the hydrogen in the core runs low, the star swells into a huge, cooler RED GIANT.\n"
                    "• It gently puffs its outer layers into space, making a glowing shell called a PLANETARY NEBULA (nothing "
                    "to do with planets -- it just looked round like a planet in old telescopes).\n"
                    "• The leftover core is a WHITE DWARF: about Earth-sized, incredibly dense and hot. Over a very long time "
                    "it cools into a dark BLACK DWARF.\n\n"
                    "HIGH-MASS STARS (many times the Sun's mass):\n"
                    "• They swell into enormous RED SUPERGIANTS.\n"
                    "• Then they explode in a SUPERNOVA, one of the brightest events in the universe.\n"
                    "• What is left is either a NEUTRON STAR (a city-sized ball so dense a teaspoon would weigh billions of "
                    "tons) or a BLACK HOLE (gravity so strong that not even light escapes).\n\n"
                    "Bigger stars burn their fuel much faster, so they live short, dramatic lives; small stars live calmly for "
                    "a very long time."
                ),
                "infographic": "star_lifecycle",
            },
            {
                "heading": "We are made of star stuff",
                "body": (
                    "Right after the Big Bang, about 14 billion years ago, the universe had almost only hydrogen and helium "
                    "(plus a pinch of lithium). Every other element -- the carbon in your cells, the oxygen you breathe, the "
                    "iron in your blood, the silicon in rocks -- was made later inside stars by fusion. Supernova explosions "
                    "blasted those elements into space, where they mixed into new clouds, which formed new stars, planets "
                    "and eventually people.\n\n"
                    "So the atoms in your body were cooked in earlier generations of stars. Astronomers like to say your atoms "
                    "are 'on loan' from the universe's lending library."
                ),
            },
        ],
        "word_bank": [
            ("Star", "A huge ball of hot gas that makes its own light and heat by nuclear fusion."),
            ("Luminosity", "The total amount of energy a star gives off every second -- its true brightness."),
            ("Erg", "A very small unit of energy used by astronomers. 10 million ergs = 1 joule."),
            ("Nucleus", "The tiny, heavy center of an atom (plural: nuclei)."),
            ("Nuclear fusion", "Squeezing small atomic nuclei together so they join into a bigger one, releasing huge energy. It powers stars."),
            ("Core", "The very center of a star or planet."),
            ("Radiative zone", "The Sun layer where energy slowly moves outward as light."),
            ("Convection", "Moving heat by moving the hot material itself -- hot stuff rises, cool stuff sinks, like boiling soup."),
            ("Convection zone", "The Sun layer where boiling, rising gas carries heat toward the surface."),
            ("Photosphere", "The Sun's visible surface, about 6,000 C."),
            ("Chromosphere", "A thin reddish layer of the Sun's atmosphere just above the photosphere."),
            ("Transition region", "A thin layer between the chromosphere and corona where the temperature jumps upward."),
            ("Corona", "The Sun's thin, super-hot outer atmosphere (about 1,000,000 C), seen during total solar eclipses."),
            ("Nebula", "A giant cloud of gas and dust in space where stars can be born (plural: nebulae)."),
            ("Protostar", "A baby star still collapsing and heating up, before fusion starts."),
            ("Main sequence", "The long, steady adult stage of a star's life when it fuses hydrogen in its core. The Sun is here now."),
            ("Red giant", "A swollen, cooler, very large star near the end of a Sun-like star's life."),
            ("Planetary nebula", "The glowing shell of gas a dying Sun-like star puffs off (not related to planets)."),
            ("White dwarf", "The small, hot, super-dense leftover core of a Sun-like star."),
            ("Black dwarf", "A white dwarf that has cooled down and stopped glowing."),
            ("Red supergiant", "An enormous swollen star that will later explode as a supernova."),
            ("Supernova", "The gigantic explosion of a massive star at the end of its life."),
            ("Neutron star", "The city-sized, unbelievably dense core left after some supernovas."),
            ("Black hole", "An object with gravity so strong that not even light can escape."),
        ],
        "key_facts": [
            "Sun: diameter 1,392,000 km (109 Earths); mass 1.989 x 10^30 kg; 74% H, 25% He.",
            "Luminosity 3.846 x 10^26 W = 3.846 x 10^33 erg/s. Age about 4.6 billion years (halfway through life).",
            "Rotation: about 25 days at the equator, about 35 days near the poles.",
            "Layers (in to out): core 15,000,000 C, radiative zone 2,000,000 C, convection zone, photosphere 6,000 C, chromosphere, transition region, corona 1,000,000 C.",
            "The Sun is at least 30% brighter than 4 billion years ago.",
            "Sun-like star: nebula -> protostar -> main sequence -> red giant -> planetary nebula + white dwarf -> black dwarf.",
            "Massive star: ... -> red supergiant -> supernova -> neutron star or black hole.",
        ],
        "quick_check": [
            ("What process makes the Sun shine?", "Nuclear fusion of hydrogen into helium in its core."),
            ("Which is hotter, the photosphere or the corona?", "The corona (about 1,000,000 C) is far hotter than the photosphere (about 6,000 C)."),
            ("Why does the Sun's equator rotate faster than its poles?", "The Sun is a ball of gas, not a solid, so different parts can spin at different speeds (about 25 vs 35 days)."),
            ("What will be left when the Sun dies?", "A white dwarf (after a red giant stage and a planetary nebula), which slowly cools into a black dwarf."),
            ("What decides whether a star becomes a white dwarf or a black hole?", "Its mass: Sun-like stars become white dwarfs; very massive stars explode as supernovas and leave neutron stars or black holes."),
        ],
        "cards": [
            {
                "term": "Nuclear fusion",
                "badge": ("H→He", "fusion", SUN),
                "analogy": "Like squeezing two balls of clay so hard they merge -- and a burst of energy pops out.",
                "explanation": "In the Sun's core (15,000,000 C), hydrogen nuclei fuse into helium and a little mass becomes a lot of energy. Fusion's outward push balances gravity's squeeze, keeping the Sun stable.",
                "why": "Fusion powers every star and sets how long it shines.",
            },
            {
                "term": "Layers of the Sun",
                "badge": ("7", "layers", SUN),
                "analogy": "Like an onion with a nuclear furnace in the middle.",
                "explanation": "Core (15M C) -> radiative zone (2M C) -> convection zone -> photosphere (6,000 C, the visible surface) -> chromosphere -> transition region -> corona (1M C, hotter than the surface!).",
                "why": "Layer order and temperatures are classic short-answer questions.",
            },
            {
                "term": "The Sun's vital statistics",
                "badge": ("109×", "Earth wide", GOLD),
                "analogy": "If Earth were a pea, the Sun would be a beach ball.",
                "explanation": "Diameter 1,392,000 km; mass 1.989 x 10^30 kg; 74% hydrogen, 25% helium; luminosity 3.846 x 10^33 erg/s; 4.6 billion years old; equator spins in 25 days, poles in 35.",
                "why": "Put these numbers on your note sheet.",
            },
            {
                "term": "Birth of a star",
                "badge": ("NEB", "to star", PURPLE),
                "analogy": "A snowball rolling together from loose snow until it's so packed it starts to glow.",
                "explanation": "A cold, dense clump of a nebula collapses under gravity into a protostar, heating as it shrinks. When its core is hot enough to fuse hydrogen, it becomes a main-sequence star.",
                "why": "Star birth and planet birth happen together in the same cloud.",
            },
            {
                "term": "Death of a Sun-like star",
                "badge": ("WD", "white dwarf", ICE),
                "analogy": "A campfire that flares up big, then shrinks to glowing embers that slowly go dark.",
                "explanation": "Red giant -> puffs off a planetary nebula -> leaves a hot, Earth-sized white dwarf -> cools into a black dwarf.",
                "why": "The Sun's future -- and why its habitable zone keeps moving.",
            },
            {
                "term": "Death of a massive star",
                "badge": ("BOOM", "supernova", RED),
                "analogy": "A huge firework that ends in one giant bang, leaving a tiny super-heavy cinder.",
                "explanation": "Massive stars become red supergiants, explode as supernovas, and leave a neutron star or a black hole. Supernovas spread the heavy elements that build planets and people.",
                "why": "No supernovas = no iron, oxygen or carbon for rocky, living planets.",
            },
        ],
    },
    # ------------------------------------------------------------------ 3
    {
        "unit": 1,
        "name": "Solar System: How the Solar System Formed",
        "description": "The solar nebula story: a spinning cloud flattens into a disk, the frost line splits rocky from icy worlds, dust grows into planetesimals and planets, giant impacts, layers inside planets, the asteroid and Kuiper belts, the heavy bombardment and the Nice Model.",
        "goals": [
            "Tell the solar nebula story in order, from cloud to planets.",
            "Explain the clues (motion, chemistry, age) that support it.",
            "Explain why the inner planets are rocky and the outer planets are giants, using the frost line.",
            "Describe accretion, planetesimals, differentiation and giant impacts.",
        ],
        "sections": [
            {
                "heading": "Being a space detective",
                "body": (
                    "Nobody was around 4.57 billion years ago to watch the Solar System form. So astronomers act like "
                    "detectives: they look for clues the planets still carry today. A good theory has to pass three tests:\n\n"
                    "• MOTION: All the planets orbit in nearly the same flat plane and the same direction, and the Sun spins "
                    "that same way too.\n"
                    "• CHEMISTRY: The rocky planets are near the Sun and the gassy, icy giants are far away.\n"
                    "• AGE: The oldest materials we can test -- certain meteorites -- are all about 4.5 billion years old.\n\n"
                    "The SOLAR NEBULA THEORY passes all three. It says the Sun and planets were born together from one "
                    "spinning cloud of gas and dust called the solar nebula."
                ),
            },
            {
                "heading": "Step 1: a cloud collapses, spins up and flattens",
                "body": (
                    "About 4.57 billion years ago, a cold cloud of gas and dust started to collapse under its own gravity. "
                    "(Something may have given it a nudge -- possibly a nearby exploding star.) As it shrank, it spun faster "
                    "and faster. Ice skaters do the same: when they pull their arms in, they spin faster. Scientists call "
                    "this CONSERVATION OF ANGULAR MOMENTUM -- a spinning thing that gets smaller must spin faster.\n\n"
                    "The spinning cloud flattened into a disk, like pizza dough tossed in the air. Most of the material fell "
                    "to the center and became the PROTOSUN (the baby Sun). The rest stayed in the flat, spinning disk "
                    "around it -- and that disk built the planets. This is why everything still orbits in one plane and one "
                    "direction!\n\n"
                    "We can see this happening today: the Hubble and James Webb space telescopes have photographed flat "
                    "disks of gas and dust around young stars, for example in the Orion Nebula. These are modern copies of "
                    "our own solar nebula."
                ),
                "infographic": "nebula_steps",
            },
            {
                "heading": "Step 2: the frost line sorts rock from ice",
                "body": (
                    "The young disk was hot near the middle and cold far out. You might think the heat came from the young "
                    "Sun -- but the disk was so thick and dusty that sunlight could barely get through. The real reason is "
                    "speed: material closer to the center orbited faster (Kepler's laws), so particles rubbed and bumped "
                    "against each other more. More FRICTION means more heat.\n\n"
                    "Somewhere in the disk there was a dividing line called the FROST LINE (or SNOW LINE). Closer than the "
                    "frost line, it was too warm for water, ammonia or methane to freeze, so only rock and metal could become "
                    "solid. Farther out, those VOLATILES (substances that turn to gas easily) froze into ice grains.\n\n"
                    "• Inside the frost line: small rocky planets (Mercury, Venus, Earth, Mars).\n"
                    "• Outside the frost line: lots of extra solid ice, so planet cores grew big -- big enough to grab gas "
                    "and become giants (Jupiter, Saturn, Uranus, Neptune).\n\n"
                    "The chemistry clue fits perfectly: the Sun, Jupiter and Saturn are mostly hydrogen and helium (they "
                    "come from the same supply), while Earth and its rocky neighbors are short on light gases and ices and "
                    "made mostly of heavy elements like iron and silicon. The light stuff escaped from the inner disk and the "
                    "heavy stuff was left behind. Jupiter's moons show the same pattern in miniature: rocky Io and Europa "
                    "close in, icy Ganymede and Callisto farther out."
                ),
            },
            {
                "heading": "Step 3: from dust to planets",
                "body": (
                    "Planets were built from the bottom up, like LEGO:\n\n"
                    "• Tiny dust grains bumped into each other and stuck together. Growing by sticking is called ACCRETION.\n"
                    "• The clumps grew into PLANETESIMALS -- the building blocks of planets, from about 1 km up to maybe 100 km "
                    "across.\n"
                    "• Planetesimals pulled on each other with gravity, crashed and merged into PROTOPLANETS (baby planets).\n"
                    "• The biggest protoplanets swept up the rest and became the planets.\n"
                    "• Out past the frost line, once a solid core reached about 10 times Earth's mass, its gravity could hold "
                    "on to hydrogen and helium gas from the disk, and it ballooned into a giant planet.\n\n"
                    "It was a rough construction site! Computer models follow millions of planetesimals pulling and crashing "
                    "into each other; some crashes even broke growing planets apart."
                ),
            },
            {
                "heading": "Step 4: melting, layering and giant crashes",
                "body": (
                    "All that crashing, plus heat from RADIOACTIVE elements (atoms that slowly break apart and give off "
                    "heat), melted the young planets. In a melted planet, heavy iron sinks to the middle and lighter rock "
                    "floats to the top -- like salad dressing separating into layers. This sorting into layers is called "
                    "DIFFERENTIATION, and it is why Earth has a metal core, a rocky mantle and a thin crust.\n\n"
                    "Giant collisions also explain the Solar System's oddballs:\n"
                    "• Uranus and Pluto spin on their sides.\n"
                    "• Venus spins slowly backward.\n"
                    "• Our Moon is a lot like Earth's rocky outer layers, but different in some ways -- most scientists think "
                    "it formed from debris thrown out when a Mars-sized body slammed into the young Earth.\n\n"
                    "This era of giant impacts lasted roughly the first 100 million years and ended about 4.4 billion years "
                    "ago."
                ),
            },
            {
                "heading": "Step 5: cleaning up -- belts, bombardment and moving giants",
                "body": (
                    "After a few million years of crashes, most of the leftover pieces had been swept up by the planets or "
                    "flung out of the Solar System. Leftovers survived in safe parking spots:\n\n"
                    "• The ASTEROID BELT, between Mars and Jupiter: Jupiter's strong gravity kept stirring these "
                    "planetesimals up, so they never managed to build a planet.\n"
                    "• The KUIPER BELT (pronounced 'KAI-per'), beyond Neptune, and the even more distant OORT CLOUD: icy "
                    "leftovers at the cold edges. They are the source of many comets and of dwarf planets like Pluto, Eris, "
                    "Haumea and Makemake (Ceres is a dwarf planet in the asteroid belt).\n\n"
                    "These leftovers -- asteroids, comets and the meteorites that fall from them -- are free samples of the "
                    "original ingredients of the planets.\n\n"
                    "THE PLANETS MAY HAVE MOVED. Models such as the NICE MODEL (named after the city of Nice in France) say "
                    "the giant planets' orbits shifted after they formed, through gravity tugs on each other and on the "
                    "leftover planetesimals. Uranus and Neptune probably formed closer in and were pushed outward. This "
                    "shuffle may have flung asteroids and comets inward, causing the HEAVY BOMBARDMENT -- a storm of impacts "
                    "about 4.1 to 3.8 billion years ago recorded in the Moon's oldest craters. Planets kept getting heavily "
                    "cratered, and kept collecting water and gases, until about 4 billion years ago. After that, each world "
                    "followed its own path."
                ),
            },
        ],
        "word_bank": [
            ("Solar nebula", "The spinning cloud of gas and dust that the Sun and planets formed from."),
            ("Solar nebula theory", "The scientific explanation that the Sun and planets formed together from one collapsing, spinning cloud."),
            ("Conservation of angular momentum", "The rule that a spinning object spins faster when it gets smaller, like a skater pulling in her arms."),
            ("Protosun", "The baby Sun in the center of the solar nebula, before fusion started."),
            ("Friction", "The rubbing between things that slows them and makes heat."),
            ("Frost line", "The distance from a young star beyond which it is cold enough for water, ammonia and methane to freeze into ice. Also called the snow line."),
            ("Snow line", "Another name for the frost line."),
            ("Volatiles", "Substances that turn into gas at fairly low temperatures, like water, carbon dioxide, ammonia and methane."),
            ("Accretion", "Growing bigger by collecting and sticking together smaller pieces."),
            ("Planetesimal", "A small solid building block of a planet, about 1 to 100 km across."),
            ("Protoplanet", "A baby planet that is still growing by sweeping up planetesimals."),
            ("Radioactive", "Describes atoms that slowly break apart on their own and give off heat and energy."),
            ("Differentiation", "When a melted planet sorts itself into layers: heavy metal sinks to the core, lighter rock rises."),
            ("Asteroid belt", "The region between Mars and Jupiter full of rocky leftovers from planet building."),
            ("Kuiper Belt", "A flat ring of icy leftovers beyond Neptune, about 30-50 AU from the Sun (say 'KAI-per')."),
            ("Oort Cloud", "A huge, distant shell of icy objects surrounding the Solar System, where many comets come from."),
            ("Nice Model", "A model in which the giant planets moved to new orbits after they formed (named after Nice, France)."),
            ("Heavy bombardment", "A period about 4.1 to 3.8 billion years ago when many asteroids and comets hit the planets and the Moon."),
            ("Meteorite", "A piece of space rock that survives falling through the air and lands on the ground."),
        ],
        "key_facts": [
            "The Solar System formed about 4.57 billion years ago from the solar nebula.",
            "Three tests: motion (one plane, one direction), chemistry (rock inside, ice/gas outside), age (meteorites about 4.5 billion years).",
            "Inner disk hot mainly because faster-moving material had more friction -- not mainly from sunlight.",
            "Frost line: beyond it, water/ammonia/methane freeze -> giant planet cores.",
            "Dust -> (accretion) -> planetesimals (1-100 km) -> protoplanets -> planets; about 10 Earth masses -> grabs gas -> giant.",
            "Giant impact era: first ~100 million years, ended ~4.4 billion years ago. Heavy bombardment ~4.1-3.8 billion years ago.",
            "Leftovers: asteroid belt (Mars-Jupiter), Kuiper Belt (30-50 AU) and Oort Cloud.",
        ],
        "quick_check": [
            ("Why do all the planets orbit in the same direction and plane?", "They formed from one spinning disk of gas and dust (the solar nebula), which all turned the same way."),
            ("Why was the inner part of the solar nebula hotter?", "Material close in moved faster, so there was more friction and heat. Sunlight barely got through the thick disk."),
            ("What is the frost line and why does it matter?", "The distance beyond which water, ammonia and methane freeze into ice. Extra ice let cores grow big enough to become giant planets."),
            ("What is differentiation?", "When a melted planet separates into layers: heavy metal sinks to make a core and lighter rock rises to make the mantle and crust."),
            ("Why is there an asteroid belt instead of a planet between Mars and Jupiter?", "Jupiter's strong gravity kept stirring up the planetesimals there, so they never clumped into one planet."),
            ("Give two oddballs that giant collisions may explain.", "Uranus (and Pluto) spinning on their sides, Venus spinning slowly backward, and the Moon forming from a giant impact on Earth."),
        ],
        "cards": [
            {
                "term": "Solar nebula",
                "badge": ("NEB", "the cloud", PURPLE),
                "analogy": "Pizza dough tossed in the air: as it spins it flattens, with a thick lump (the Sun) in the middle.",
                "explanation": "A collapsing cloud of gas and dust spun faster (conservation of angular momentum) and flattened into a disk. The center became the Sun; the disk built the planets about 4.57 billion years ago.",
                "why": "The starting point for every formation and habitability question.",
            },
            {
                "term": "Frost (snow) line",
                "badge": ("ICE", "line", ICE),
                "analogy": "Like the line on a mountain above which snow never melts.",
                "explanation": "Beyond the frost line, water, ammonia and methane freeze into ice grains. Inside it only rock and metal are solid (rocky planets); outside, extra ice builds big cores that grab gas (giant planets).",
                "why": "Explains our planet layout -- and why hot Jupiters must have moved inward.",
            },
            {
                "term": "Why the inner disk was hot",
                "badge": ("HOT", "friction", RED),
                "analogy": "Racers on the inside lane go fastest and bump the most.",
                "explanation": "Not mainly sunlight (the dusty disk blocked it): inner material orbited faster, so it rubbed and collided more, heating up. Too warm for ice to form.",
                "why": "A classic trick question -- the answer is speed/friction.",
            },
            {
                "term": "Accretion & planetesimals",
                "badge": ("1-100", "km", ROCK),
                "analogy": "Planets were built like LEGO -- tiny bricks snapping into bigger and bigger pieces.",
                "explanation": "Dust stuck together (accretion) into planetesimals (1-100 km), which merged into protoplanets and planets. A core of about 10 Earth masses can grab gas and become a giant.",
                "why": "The same process happens in disks around other stars today.",
            },
            {
                "term": "Differentiation",
                "badge": ("LAYERS", "sort", GOLD),
                "analogy": "Salad dressing left to sit: heavy stuff sinks, light stuff floats.",
                "explanation": "Impacts and radioactive heat melted young planets, so iron sank to form cores and lighter rock rose into mantles and crusts.",
                "why": "A molten metal core can make a magnetic field that protects a planet's air.",
            },
            {
                "term": "Giant impacts",
                "badge": ("BOOM", "oddballs", RED),
                "analogy": "Bumper cars: one big hit can leave a car spinning backward or tipped over.",
                "explanation": "Giant collisions (first ~100 million years, ending ~4.4 billion years ago) may explain Uranus and Pluto on their sides, Venus spinning backward, and the Moon's birth.",
                "why": "Shows planet formation was messy, not neat.",
            },
            {
                "term": "Heavy bombardment & the Nice Model",
                "badge": ("4.1-3.8", "bya", GOLD),
                "analogy": "Rearranging big furniture in a room knocks loose everything on the shelves.",
                "explanation": "The giant planets' orbits likely shifted after they formed (Nice Model), flinging asteroids inward and causing the heavy bombardment about 4.1-3.8 billion years ago, seen in the Moon's oldest craters.",
                "why": "Big impacts could have sterilized early Earth -- important for when life began.",
            },
            {
                "term": "The leftovers",
                "badge": ("BELTS", "+ cloud", ROCK),
                "analogy": "After a party, a few guests are still hanging out in quiet corners.",
                "explanation": "Leftover planetesimals survive in the asteroid belt (Mars-Jupiter), the Kuiper Belt (beyond Neptune) and the Oort Cloud: today's asteroids, comets and dwarf planets.",
                "why": "They are time capsules of the planets' original ingredients, including water.",
            },
        ],
    },
]
