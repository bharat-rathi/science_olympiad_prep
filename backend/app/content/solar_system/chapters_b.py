"""Solar System learning chapters 8-14: ocean worlds and Titan, planetary
evolution, planet formation around other stars, exoplanet detection and
demographics, habitable zones, and astrobiology -- the core of the 2027
"habitability within and beyond the Solar System" theme.

Source reader sections: OpenStax Astronomy 2e 12.3, 14.4-14.5, 21.3-21.6,
30.1-30.3. Same dict shape and plain-text rules as chapters_a.py.
"""

from app.content.solar_system.svg import BLUE, GAS, GOLD, GREEN, ICE, PURPLE, RED, ROCK, SUN

CHAPTERS_B = [
    # ------------------------------------------------------------------ 8
    {
        "name": "Solar System: Ocean Worlds -- Titan, Enceladus & Triton",
        "description": "Saturn's moon Titan (thick nitrogen air, methane rain and lakes, Huygens landing, Dragonfly), Enceladus' ocean plumes, Neptune's Triton, and why icy moons are prime places to search for life.",
        "source_title": "Source reader: Titan, Triton and life in the outer solar system (OpenStax Astronomy 2e, 12.3, 14.5, 30.3)",
        "infographics": ["ocean_worlds", "titan_cycle"],
        "source_text": (
            "TITAN: Saturn's largest moon (5,150 km, density 1.9, reflectivity 20%). Only moon with a substantial atmosphere: "
            "mostly nitrogen with ~5% methane. Voyager found organic molecules such as hydrogen cyanide (HCN), cyanogen (C2N2) "
            "and cyanoacetylene (HC3N) -> sunlight + nitrogen + methane make a rich organic mix; multiple layers of hydrocarbon "
            "haze and clouds; atmosphere structure has Earth-like features but is much colder. In the upper atmosphere UV breaks "
            "and recombines molecules into complex organics called tholins -> orange haze; heavier particles settle and form "
            "'dunes' cut by flowing liquid hydrocarbons. Cassini orbiter (cameras, spectrometers, radar) made dozens of Titan "
            "flybys 2004-2015. ESA's Huygens probe parachuted down and landed January 14, 2005 -- first (and so far only) "
            "landing on a moon in the outer solar system. 319 kg; landed on a flat, boulder-strewn plain; surface and boulders "
            "of water ice (hard as rock at Titan's temperature); drainage channels suggested the shore of an ancient hydrocarbon "
            "lake; deep orange sky; sunlight 1,000x dimmer than on Earth (but 100x brighter than full moonlight); surface 94 K "
            "(-179 C); heated ice released hydrocarbon gas; worked ~90 minutes before freezing.\n"
            "Radar and infrared: complex, geologically young surface; large methane lakes near the poles interacting with "
            "atmospheric methane like Earth's oceans and water vapor; erosion features -> methane rain flows down valleys to "
            "lakes: a low-temperature version of the water cycle; liquids are methane, ethane and a trace of other hydrocarbons. "
            "Lake 'glint' (sunlight reflecting off a flat liquid surface). Life on Titan? Hydrocarbons are fundamental to large "
            "carbon molecules, but it is far too cold for liquid water and many essential processes; maybe a different "
            "low-temperature carbon-based life with liquid hydrocarbons in water's role -- 'life as we don't know it'. Titan may "
            "also host a liquid water layer deep inside. It must have contained enough ammonia, methane and nitrogen to form "
            "its atmosphere; too cold for CO2 or water vapor, so nitrogen dominates. NASA's Dragonfly (launch 2027) is a drone "
            "that will fly in Titan's atmosphere studying pre-biotic chemistry; proposed balloon and lake 'boat' missions.\n"
            "ENCELADUS: small Saturn moon, ~500 km across. Cassini flyby in 2005 found plumes of gas and icy material venting "
            "from the south polar region at ~250 kg per second. Salts in the icy material -> source is a liquid water ocean "
            "beneath tens of kilometers of ice; local or global, transient or long-lived not yet known; in contact with and has "
            "reacted with a rocky interior (necessary but not sufficient for habitability). Plumes offer ocean samples to any "
            "spacecraft flying through -- could reveal whether it is habitable or even inhabited. Saturn's tides may heat it. "
            "Enceladus may have the most accessible liquid water in the solar system.\n"
            "EUROPA (astrobiology view): ocean tens to perhaps a hundred km deep; Jupiter's tides + friction keep it liquid; six "
            "or more icy moons may harbor oceans; Europa and Enceladus of greatest interest. Life needs energy too: no sunlight "
            "below km of ice, so chemical energy. Ocean likely in contact with rocky mantle; water-rock reactions (especially hot, "
            "like hydrothermal vents) give reducing chemistry (molecules give up electrons) = half a chemical battery; oxidizing "
            "chemistry (molecules accept electrons) completes it. Galileo found Europa's surface rich in oxidizing chemicals; "
            "surface only tens of millions of years old and active, so surface-ocean mixing may occur -- a key objective. On "
            "Earth, reducing vent fluids meeting oxygenated seawater power thriving seafloor communities.\n"
            "TRITON: Neptune's largest moon (don't confuse with Titan): diameter 2,720 km, density 2.1 g/cm3 -> ~75% rock, 25% "
            "water ice. Coldest surface of any world our spacecraft have visited; reflectivity ~80%. Retrograde orbit, thin "
            "atmosphere, active eruptions seen by Voyager 2 in 1989; probably a captured dwarf planet like Pluto. Outer moons "
            "show low-temperature volcanism: water and other ices instead of silicate lava (sulfur on Io)."
        ),
        "story": (
            "FAR FROM THE SUN, BUT NOT DEAD\n\n"
            "For a long time scientists assumed the moons of the outer solar system, getting only a trickle of sunlight, would "
            "be 'geologically dead' balls of frozen ice and rock. Spacecraft proved them wrong. Some of these moons hide oceans, "
            "shoot geysers, or have weather. Six or more icy moons may have liquid water oceans, kept warm by tidal heating -- "
            "the same squeezing that powers Io. That makes them some of the best places to search for life.\n\n"
            "TITAN: A WEIRD COPY OF EARTH\n\n"
            "Titan, Saturn's largest moon (5,150 km across), is the ONLY moon with a thick atmosphere. Its air is mostly nitrogen, "
            "like ours, plus about 5% methane. High up, ultraviolet sunlight breaks these molecules apart and they recombine into "
            "complex carbon-rich (organic) compounds called THOLINS, plus molecules like hydrogen cyanide, cyanogen and "
            "cyanoacetylene. Tholins wrap Titan in an orange haze, and heavier particles drift down and pile into dunes.\n\n"
            "NASA's Cassini spacecraft flew past Titan dozens of times from 2004 to 2015, using radar to see through the haze. It "
            "carried a passenger: Europe's HUYGENS probe. On January 14, 2005, Huygens parachuted down and landed -- the first and "
            "so far only landing on a moon in the outer solar system. It found a flat plain strewn with 'boulders' made of water "
            "ice, which is as hard as rock at Titan's temperature of 94 K (-179 C). The sky was deep orange, and sunlight was "
            "1,000 times dimmer than on Earth (still 100 times brighter than full moonlight). Descent photos showed drainage "
            "channels -- Huygens seemed to sit on the shore of an old lake. It sent data for about 90 minutes before the cold "
            "won.\n\n"
            "Here's the amazing part: Titan has a 'water cycle' -- but with methane. Methane evaporates from big lakes near the "
            "poles, forms clouds, falls as rain, and flows down valleys back into lakes of liquid methane and ethane. Cassini even "
            "caught sunlight glinting off a lake's flat surface. It's weirdly familiar and totally alien at the same time.\n\n"
            "COULD ANYTHING LIVE ON TITAN?\n"
            "Hydrocarbons are the backbone of the big carbon molecules life uses. But Titan is far too cold for liquid water and "
            "for many chemical reactions our kind of life needs. Maybe, though, a completely different kind of carbon-based life "
            "could use liquid methane the way we use water -- 'life as we don't know it'. Finding that would be even more "
            "exciting than finding life like ours on Mars! Titan might also hide liquid water deep inside. NASA's DRAGONFLY, a "
            "drone that will fly through Titan's thick air studying pre-biotic chemistry, is set to launch in 2027. Balloons and "
            "even a boat for Titan's lakes have been proposed.\n\n"
            "Why is Titan's air nitrogen? Titan had enough ammonia, methane and nitrogen to build an atmosphere, and it's too cold "
            "for carbon dioxide or water to stay as gas -- so nitrogen ended up the main ingredient.\n\n"
            "ENCELADUS: THE GEYSER MOON\n\n"
            "Enceladus is tiny -- only about 500 km across. In 2005 Cassini discovered plumes of gas and ice spraying from its "
            "south pole, about 250 kg of material every second. The ice contains SALTS, a strong hint that it comes from a liquid "
            "water ocean under tens of kilometers of ice. The ocean seems to touch and react with a rocky interior, which is "
            "necessary (though not enough by itself) for life. Best of all, the plumes deliver ocean samples into space: a "
            "spacecraft just has to fly through them to test whether Enceladus is habitable -- or even inhabited. It may have the "
            "most accessible liquid water in the solar system.\n\n"
            "EUROPA, LIFE'S BEST BET?\n\n"
            "Europa's hidden ocean may be tens to perhaps a hundred kilometers deep, and it has probably existed for most of "
            "Europa's history. But life needs more than water -- it needs ENERGY. Sunlight can't reach through kilometers of ice, "
            "so the energy would have to be chemical, like a battery:\n"
            "• One side of the battery: water reacting with hot rock on the seafloor (as at Earth's hydrothermal vents) makes "
            "REDUCING chemistry -- molecules that easily give up electrons.\n"
            "• The other side: OXIDIZING chemistry -- molecules that easily accept electrons. The Galileo mission found plenty of "
            "oxidizers on Europa's icy surface.\n"
            "On Earth, when vent fluids meet oxygen-rich seawater, the energy released feeds thriving seafloor communities far "
            "from sunlight. So the big question for Europa is whether surface chemicals can mix down into the ocean through the "
            "ice. Its young (tens of millions of years old), active surface makes that tantalizingly possible.\n\n"
            "TRITON: THE BACKWARD MOON\n\n"
            "Don't mix up Titan with TRITON, Neptune's largest moon. Triton is 2,720 km across with a density of 2.1 g/cm3, so "
            "it's roughly 75% rock and 25% water ice. It reflects about 80% of sunlight and has the coldest surface of any world "
            "our spacecraft have visited. It orbits Neptune backward, has a thin atmosphere, and Voyager 2 saw active eruptions "
            "there in 1989. It may be a dwarf planet like Pluto that Neptune captured.\n\n"
            "ICE VOLCANOES\n"
            "Outer-solar-system worlds show 'low-temperature volcanism': instead of melted rock, they erupt water and other ices "
            "(and sulfur compounds on Io)."
        ),
        "concepts": [
            {
                "term": "Titan's atmosphere",
                "badge": ("N₂", "+5% CH₄", GAS),
                "analogy": "Titan's sky is like a smoggy orange soup -- a chemistry lab running in the sky.",
                "explanation": "Titan (5,150 km, density 1.9) is the only moon with a substantial atmosphere: mostly nitrogen with about 5% methane. Sunlight interacting with nitrogen and methane creates a rich mix of organic molecules -- hydrogen cyanide (HCN), cyanogen (C2N2), cyanoacetylene (HC3N) -- and in the upper atmosphere ultraviolet light builds complex organics called tholins, which shroud Titan in an orange haze with multiple layers of hydrocarbon haze and clouds. Heavier particles settle and form dunes. Titan's atmospheric structure resembles Earth's in some ways but is much colder. Its nitrogen atmosphere formed because it held ammonia, methane and nitrogen, and it is too cold for CO2 or water vapor.",
                "why": "Titan is a natural lab for prebiotic chemistry -- maybe like early Earth's.",
            },
            {
                "term": "Huygens landing on Titan",
                "badge": ("2005", "Jan 14", ICE),
                "analogy": "Huygens was a parachuting robot landing on an icy beach under an orange sky.",
                "explanation": "The NASA Cassini orbiter (cameras, spectrometers, radar) made dozens of close Titan flybys from 2004 to 2015. Its ESA-built Huygens probe (319 kg) descended by parachute and landed on January 14, 2005 -- the first and so far only landing on a moon in the outer solar system. It landed on a flat, boulder-strewn plain where the surface and boulders were water ice, as hard as rock at Titan's 94 K (-179 C). Descent images showed drainage channels, suggesting the shore of an ancient hydrocarbon lake. The sky was deep orange; sunlight was 1,000x dimmer than on Earth (but 100x brighter than full moonlight). The warm probe released hydrocarbon gas from the ice; it returned data for over an hour (~90 minutes) before succumbing to the cold.",
                "why": "Classic mission-fact questions; also evidence of liquid on another world's surface.",
            },
            {
                "term": "Titan's methane cycle",
                "badge": ("CH₄", "rain", GAS),
                "analogy": "Titan has rain, rivers and lakes just like Earth -- but filled with liquid natural gas instead of water.",
                "explanation": "Cassini radar and infrared images revealed a complex, geologically young surface. Large methane lakes near the poles interact with atmospheric methane much as Earth's oceans interact with water vapor. Erosional features show that methane condenses, falls as rain, and flows down valleys to the lakes -- a low-temperature equivalent of the water cycle. The liquids are a combination of methane, ethane and traces of other hydrocarbons. Sunlight 'glint' off a very flat surface confirms liquid lakes. Titan is the only other world known with stable surface liquid.",
                "why": "Shows a non-water 'hydrological cycle' -- important for 'life as we don't know it'.",
            },
            {
                "term": "Life as we don't know it (Titan)",
                "badge": ("???", "alien life", PURPLE),
                "analogy": "Instead of fish swimming in water, imagine microbes 'swimming' in liquid methane.",
                "explanation": "Hydrocarbons are fundamental for the large carbon molecules life on Earth uses, but Titan is far too cold for liquid water or many chemical processes essential to life as we know it. There remains an intriguing possibility of a different form of low-temperature, carbon-based life that uses liquid hydrocarbons in the role of water. Finding such 'life as we don't know it' could be even more exciting than finding life like ours on Mars and would greatly expand our understanding of life and habitable environments. Titan may also host a liquid-water layer deep inside. Titan may be the best place to search for this kind of life.",
                "why": "Habitability isn't only about water -- know the alternative-solvent idea.",
            },
            {
                "term": "Dragonfly mission",
                "badge": ("2027", "launch", BLUE),
                "analogy": "Dragonfly is a nuclear-powered drone that hops between spots on Titan like a giant robotic insect.",
                "explanation": "NASA selected Dragonfly for launch in 2027: a drone that will fly in Titan's thick atmosphere, with emphasis on studying pre-biotic chemistry. Other proposed future missions include a balloon operating in Titan's atmosphere and a 'boat' floating on one of its lakes.",
                "why": "Launches in the 2027 season -- a very likely current-events question.",
            },
            {
                "term": "Enceladus' plumes",
                "badge": ("250", "kg/s", ICE),
                "analogy": "Enceladus is a tiny moon with a cracked ice shell spraying ocean water like a shaken soda bottle.",
                "explanation": "Enceladus is a small (~500 km diameter) moon of Saturn. In 2005 the Cassini mission discovered plumes of gas and icy material venting from its south polar region at a combined ~250 kg per second. Several observations, including salts in the icy material, suggest the source is a liquid water ocean beneath tens of kilometers of ice. Whether it is local or global, transient or long-lived, is not yet known, but it appears to be in contact and to have reacted with a rocky interior -- probably necessary, though not sufficient, for habitability. The plumes provide free ocean samples to any spacecraft flying through, which could reveal whether Enceladus is habitable or even home to life. Saturn's tides may heat it.",
                "why": "Enceladus may have the most accessible liquid water in the solar system.",
            },
            {
                "term": "Ocean worlds",
                "badge": ("6+", "icy moons", BLUE),
                "analogy": "Ocean worlds are like snow globes turned inside out -- liquid water sealed under a shell of ice.",
                "explanation": "Moons of the outer solar system get very little sunlight, so they were long thought to be geologically dead. Instead, tides from their giant planets (like our Moon raising tides on Earth) push and pull them, and the friction generates enough heat to keep water liquid. Scientists now think six or more icy moons may harbor liquid water oceans. Europa (ocean tens to perhaps 100 km deep) and Enceladus are of greatest interest to astrobiologists; Ganymede also shows evidence. Earth and Europa both have large oceans; Mars has subsurface water; Enceladus vents its ocean into space.",
                "why": "Tidal heating extends habitability far beyond the Sun's habitable zone.",
            },
            {
                "term": "Europa's chemical battery",
                "badge": ("+ / −", "energy", GOLD),
                "analogy": "Life in Europa's dark ocean would run like a flashlight battery: it needs both a + end and a − end.",
                "explanation": "Habitability needs energy as well as water. Sunlight can't penetrate Europa's kilometers-thick ice, so energy must be chemical. Europa's ocean is most likely in direct contact with a rocky mantle, and water-rock interaction (especially at high temperature, as in Earth's hydrothermal vents) yields reducing chemistry (molecules readily give up electrons) -- one half of a chemical battery. The other half is oxidizing chemistry (molecules readily accept electrons). Galileo found Europa's surface rich in oxidizing chemicals, so energy for life depends on whether surface and ocean chemistry can mix through the ice. Europa's geologically young (tens of millions of years), active ice makes mixing plausible. On Earth, reducing vent fluids meeting oxygenated seawater feed thriving seafloor communities far from sunlight.",
                "why": "'Water + energy + raw materials' is the full definition of habitable.",
            },
            {
                "term": "Triton",
                "badge": ("2,720", "km", "#9fd6e8"),
                "analogy": "Triton is a runaway that Neptune caught -- it still orbits the 'wrong way'.",
                "explanation": "Neptune's largest moon (don't confuse it with Titan): diameter 2,720 km, density 2.1 g/cm3, so probably ~75% rock and ~25% water ice. Its surface is the coldest of any world our spacecraft have visited, partly because it reflects ~80% of sunlight. It orbits in a retrograde direction (unusual for a large moon), has a very thin atmosphere, and Voyager 2 discovered active eruptions in 1989. Astronomers suggest it began beyond the Neptune system as a dwarf planet like Pluto and was captured.",
                "why": "Classic Titan-vs-Triton mix-up question, and a captured dwarf planet example.",
            },
            {
                "term": "Low-temperature volcanism",
                "badge": ("ICE", "volcanoes", ICE),
                "analogy": "Instead of lava, these worlds erupt slushy water -- volcanoes made of snow cones.",
                "explanation": "The geological evolution of icy moons and Pluto differs from the terrestrial planets: tidal energy sources have been active, and the materials are different. On outer worlds we see low-temperature volcanism: the silicate lava of the inner planets is supplemented by sulfur compounds on Io and replaced by water and other ices on Pluto and outer-planet moons (e.g. Triton's eruptions, Enceladus' plumes). Discoveries of geological activity on Titan and Enceladus, and Pluto's complex surface, were unexpected.",
                "why": "Activity = possible energy and recycling -- key ingredients for habitability.",
            },
        ],
    },
    # ------------------------------------------------------------------ 9
    {
        "name": "Solar System: Planetary Evolution -- Why Worlds Turned Out Different",
        "description": "How size, composition and distance from the Sun shaped geological activity, mountain heights, the shapes of small bodies, and the atmospheres of Venus, Earth, Mars and Titan -- and which worlds could be habitable.",
        "source_title": "Source reader: Planetary Evolution (OpenStax Astronomy 2e, 14.5)",
        "infographics": ["baked_potato", "mountain_heights"],
        "source_text": (
            "After the dust disk dissipated: giant impacts in the first ~100 million years, ending ~4.4 billion years ago; planets "
            "cooled; until ~4 billion years ago they kept acquiring volatiles and heavy cratering; then each terrestrial planet and "
            "outer-planet moon followed its own course set by composition, mass and distance from the Sun.\n"
            "GEOLOGICAL ACTIVITY needs internal energy: primordial heat left from formation or radioactive decay. Larger worlds "
            "retain heat longer and cool more slowly ('baked potato effect'), so larger solid worlds are more likely to show "
            "continuing activity. Exception: Io's heat from Jupiter's tidal flexing; Europa probably heated by jovian tides; "
            "Saturn may do the same to Enceladus. Smaller planets pass through the stages of geological history faster "
            "(Figure 14.18). Moon: internally active until ~3.3 billion years ago when major volcanism ceased; mantle cooled and "
            "solidified; seismic activity near zero; geologically dead. Mercury likely ceased volcanism about the same time. "
            "Mars intermediate: southern crust formed by 4 billion years ago; northern volcanic plains contemporary with lunar "
            "maria; Tharsis bulge later; Tharsis volcanoes active on and off to the present. Earth and Venus largest and most "
            "active: Earth has global plate tectonics driven by mantle convection; most surface <200 million years old. Venus "
            "similar volcanism but no plate tectonics; most surface <=500 million years old; 'blob tectonics' (coronae, pancake "
            "volcanoes). Icy moons and Pluto: tidal energy, different materials; low-temperature volcanism (sulfur on Io; water "
            "and ices on Pluto and outer moons).\n"
            "ELEVATIONS: Moon and Mercury: major mountains are ejecta from large basin-forming impacts. Mars: most large mountains "
            "are volcanoes from repeated eruptions from the same vents (similar but smaller volcanoes on Earth and Venus). "
            "Highest mountains on Earth and Venus: compression and uplift (Earth: continental plates colliding). Max elevation "
            "differences on Earth and Venus ~10 km; Olympus Mons >20 km above surroundings and nearly 30 km above Mars' lowest "
            "areas; nearly 500 km wide; almost 3x Earth's tallest mountain. Reasons: (1) Earth's moving plates create chains like "
            "Hawaii instead of one huge volcano; on Mars (and perhaps Venus) crust stays over the hot spot so a volcano grows for "
            "hundreds of millions of years; (2) gravity: Venus ~ Earth's, Mars ~1/3; a mountain must support its own weight; ~10 "
            "km is the limit on Earth (Mauna Loa slumps when new lava is added) and Venus; Mars supports much more. Figure 14.19: "
            "Mauna Loa and Mt. Everest (Earth), Olympus Mons (Mars), Maxwell Mountains (Venus); 'sea level' only for Earth.\n"
            "SHAPES: gravity pulls large bodies into spheres; rock strength lets small bodies stay irregular. For silicate "
            "bodies the limiting diameter is ~400 km: larger -> approximately spherical; smaller -> almost any shape (asteroid "
            "Ida, ~60 km long, seen by Galileo).\n"
            "ATMOSPHERES: formed by gas escaping from interiors + impacts of volatile-rich debris from the outer solar system. "
            "Terrestrial planets started with similar atmospheres; Mercury too small and hot to keep gas; Moon probably never had "
            "one (volatile-depleted material). Initially hydrogen-containing (reducing) gases -- CO, traces of ammonia (NH3) and "
            "methane (CH4); solar UV split reducing gases, hydrogen escaped, leaving oxidized atmospheres (CO2 dominant). Water's "
            "fate depended on size and distance: early Mars had thick atmosphere and abundant liquid water but lost the CO2 "
            "needed for greenhouse warming, cooled, water froze; Venus had a runaway greenhouse and permanently lost water; only "
            "Earth kept the balance for liquid water. Venus and Mars: ~96% CO2 and a few percent nitrogen. Earth: water then life "
            "removed CO2 into marine sediments; photosynthesis released more oxygen than reactions could remove -> nitrogen most "
            "abundant, the only atmosphere with free oxygen. Titan: only outer moon with a substantial atmosphere, mostly "
            "nitrogen (too cold for CO2 or water vapor).\n"
            "HABITABILITY SURVEY: Mercury, Venus and the Moon unsuitable; most outer moons unsuitable; giant planets (no solid "
            "surfaces) fail. Search focuses on liquid water: Earth and Europa have large oceans (Europa's under thick ice); Mars "
            "had a long history of surface water and has subsurface water, with brief flows today; Enceladus may have the most "
            "accessible water (geysers); Titan too cold for liquid water but with thick air and hydrocarbon lakes may be the best "
            "place for 'life as we don't know it'. Unexpected discoveries: activity on Titan and Enceladus, Pluto's complex "
            "surface. Exoplanets show far more variety than imagined."
        ),
        "story": (
            "SAME START, DIFFERENT ENDINGS\n\n"
            "Earth, Venus and Mars started out as rocky siblings from the same family, probably with similar atmospheres. Today "
            "one is a blue, living world, one is a scorching pressure cooker, and one is a cold desert. What happened? Planetary "
            "evolution -- the way a world changes after it's born -- depends mostly on three things: what it's made of, how big "
            "(massive) it is, and how far it is from the Sun.\n\n"
            "THE EARLY YEARS\n"
            "• The era of giant impacts lasted about the first 100 million years, ending around 4.4 billion years ago.\n"
            "• Until about 4 billion years ago, planets kept collecting volatile materials (water, gases) and got heavily cratered.\n"
            "• After that, outside influences faded and each world followed its own path.\n\n"
            "THE BAKED POTATO EFFECT\n\n"
            "Pull a big baked potato and a tiny one out of the oven. Which stays hot inside longer? The big one! Planets work the "
            "same way. Geological activity (volcanoes, moving crust) needs internal heat -- either leftover heat from formation or "
            "heat from radioactive elements decaying inside. Bigger worlds hold that heat longer, so they stay active longer, and "
            "smaller worlds race through their life stages faster:\n"
            "• THE MOON (smallest): its big volcanoes stopped about 3.3 billion years ago. Its mantle cooled and hardened, and today "
            "even moonquakes are nearly zero. Geologically dead.\n"
            "• MERCURY: probably went quiet around the same time.\n"
            "• MARS (in between): its southern crust formed by 4 billion years ago; its northern volcanic plains are about as old "
            "as the lunar maria; the Tharsis bulge came later, and its giant volcanoes have been active on and off right up to "
            "the present era.\n"
            "• VENUS: very active, with lots of volcanism, but no plate tectonics. Its surface is mostly no more than 500 million "
            "years old, reshaped by 'blob tectonics' -- hot material puckering and bursting through to make coronae and pancake "
            "volcanoes.\n"
            "• EARTH (largest): global plate tectonics, driven by convection in the mantle, constantly recycles the surface. Most "
            "of Earth's surface is less than 200 million years old.\n\n"
            "The big exception is TIDAL HEATING. Little Io is the most volcanic world of all because Jupiter keeps flexing it. "
            "Europa is probably tidally heated too, and Saturn may do the same to Enceladus. On icy moons and Pluto, 'lava' is "
            "replaced by water and other ices.\n\n"
            "WHY MARS HAS THE TALLEST MOUNTAIN\n\n"
            "On the Moon and Mercury, the big mountains are debris thrown up by giant impacts billions of years ago. On Mars, most "
            "big mountains are volcanoes built by eruption after eruption from the same vent. Earth and Venus have volcanoes too, "
            "but their HIGHEST mountains (Everest, the Maxwell Mountains) were squeezed up by compression -- on Earth, by "
            "continents crashing together.\n\n"
            "Mountains on Earth and Venus top out around 10 km above their surroundings. Mars' OLYMPUS MONS towers more than 20 km "
            "high -- nearly 30 km above the lowest parts of Mars -- and is nearly 500 km wide, almost three times taller than "
            "Earth's tallest mountain. Two reasons:\n"
            "1. NO MOVING PLATES. On Earth, a plate slides over a hot spot, so instead of one giant volcano you get a chain, like "
            "the Hawaiian Islands. On Mars (and perhaps Venus) the crust stays put over the hot spot, so one volcano can keep "
            "growing for hundreds of millions of years.\n"
            "2. WEAKER GRAVITY. A mountain must be strong enough to hold up its own weight. Rock strength limits mountains to about "
            "10 km on Earth -- when new lava piles onto Mauna Loa, the mountain slumps. Venus' gravity is almost the same as "
            "Earth's, so the same limit applies. Mars' gravity is only about one third of Earth's, so much taller piles can "
            "stand.\n\n"
            "WHY ARE BIG THINGS ROUND?\n"
            "Gravity pulls everything toward the most 'efficient' shape -- a sphere, where every point on the surface is the same "
            "distance from the center. Rock is strong enough to resist that pull only in small objects. For rocky (silicate) "
            "bodies the cutoff is about 400 km across: bigger ones are always roughly round, while smaller ones can be any shape, "
            "like the potato-shaped asteroid Ida (about 60 km long).\n\n"
            "HOW THE ATMOSPHERES EVOLVED\n\n"
            "Planets got their air from gas escaping their interiors and from impacts of volatile-rich comets and asteroids. The "
            "rocky planets probably started with similar air. Mercury was too small and hot to keep it, and the Moon probably "
            "never had one (it was made of material low in volatiles).\n\n"
            "At first the air likely contained hydrogen-rich ('reducing') gases: carbon monoxide plus traces of ammonia and "
            "methane. Ultraviolet sunlight split these molecules; light hydrogen escaped to space, leaving oxygen-rich ('oxidized') "
            "atmospheres dominated by carbon dioxide.\n\n"
            "Then each planet's WATER took a different path:\n"
            "• MARS: early on it had a thick atmosphere and plenty of liquid water, but it lost the CO2 needed for greenhouse "
            "warming. It cooled, and its water froze.\n"
            "• VENUS: the opposite -- a runaway greenhouse boiled and permanently lost its water.\n"
            "• EARTH: the only one that kept the delicate balance for liquid water to last.\n"
            "With their water gone, Venus and Mars ended up with atmospheres of about 96% CO2 and a few percent nitrogen. On "
            "Earth, water and then LIFE changed everything: CO2 got locked into seafloor sediments, and photosynthesis released "
            "more oxygen than chemistry could remove. So Earth is low in CO2, mostly nitrogen, and has the only planetary "
            "atmosphere with free oxygen -- thanks to life.\n\n"
            "Out in the cold, TITAN is the only moon with a thick atmosphere. It's too cold there for CO2 or water to stay as gas, "
            "so its air ended up mostly nitrogen.\n\n"
            "WHICH WORLDS COULD BE HABITABLE?\n"
            "• NOT suitable: Mercury, Venus, the Moon, most outer moons, and the giant planets (no solid surfaces).\n"
            "• Follow the water: Earth and Europa both have big oceans (Europa's under thick ice). Mars had lots of surface water "
            "long ago, has water underground, and water may still flow briefly today. Enceladus may have the most accessible "
            "water, spraying from geysers.\n"
            "• Wild card: Titan -- too cold for liquid water, but with thick air and hydrocarbon lakes it may be the best place to "
            "look for 'life as we don't know it'.\n\n"
            "Exploring the solar system is one of humanity's greatest adventures -- and with surprises like Titan, Enceladus and "
            "Pluto, it has only just begun."
        ),
        "concepts": [
            {
                "term": "Three controls on a planet's fate",
                "badge": ("C-M-D", "fate", GOLD),
                "analogy": "Like three kids from the same family -- their personality depends on how big they grow and where they move.",
                "explanation": "After the era of giant impacts (the first ~100 million years, ending ~4.4 billion years ago), the planets cooled; until ~4 billion years ago they continued to acquire volatiles and were heavily cratered. As external influences declined, each terrestrial planet and outer-planet moon followed its own evolutionary course, which depended on its composition, its mass (size), and its distance from the Sun.",
                "why": "Use 'composition, mass, distance' to structure any 'why are these planets different' answer.",
            },
            {
                "term": "Baked potato effect",
                "badge": ("BIG=HOT", "longer", ROCK),
                "analogy": "A big baked potato stays hot inside much longer than a tiny one.",
                "explanation": "Internal geological activity needs energy: primordial heat left over from formation or heat from radioactive decay. The larger the planet or moon, the more likely it is to retain internal heat and the more slowly it cools, so larger solid worlds are more likely to show continuing geological activity; smaller worlds pass through the stages of geological history faster. Exceptions are tidally heated moons: Io (Jupiter's tidal flexing), probably Europa, and possibly Saturn's Enceladus.",
                "why": "Internal heat drives volcanism, magnetic fields and outgassing -- all linked to habitability.",
            },
            {
                "term": "Activity ladder: Moon to Earth",
                "badge": ("<200", "Myr Earth", BLUE),
                "analogy": "The smallest worlds 'retired' first; the biggest are still working.",
                "explanation": "Moon: internally active until ~3.3 billion years ago when major volcanism ceased; its mantle cooled and solidified and seismic activity is nearly zero -- geologically dead. Mercury: probably ceased most volcanism about the same time. Mars: intermediate -- southern crust formed by 4 billion years ago, northern volcanic plains as old as the lunar maria, Tharsis bulge later, with Tharsis volcanoes active on and off to the present. Venus: similar volcanism to Earth but no plate tectonics; most of its surface is no more than ~500 million years old, modified by 'blob tectonics' (coronae, pancake volcanoes). Earth: global plate tectonics driven by mantle convection; most surface material less than 200 million years old.",
                "why": "Surface age and activity are frequent compare-and-contrast questions.",
            },
            {
                "term": "Olympus Mons and mountain limits",
                "badge": ("20+", "km high", "#e0603a"),
                "analogy": "On Mars you can stack a sandcastle much higher because the 'sand' weighs less -- and the table never moves.",
                "explanation": "Moon/Mercury mountains are ejecta from huge basin-forming impacts; most large Mars mountains are volcanoes built by repeated eruptions from the same vents; the highest mountains on Earth and Venus come from crustal compression and uplift (on Earth, continental plates colliding). Earth and Venus max elevation differences are ~10 km; Olympus Mons rises more than 20 km above its surroundings (nearly 30 km above Mars' lowest areas), is nearly 500 km wide, and is almost three times as high as Earth's tallest mountain. Reasons: (1) no moving plates on Mars, so one volcano stays over its hot spot for hundreds of millions of years (on Earth a moving plate makes a chain like Hawaii); (2) Mars' surface gravity is only ~1/3 of Earth's, and rock strength limits mountains to ~10 km on Earth and Venus (Mauna Loa slumps under new lava).",
                "why": "A favorite 'explain with two reasons' question.",
            },
            {
                "term": "Why big bodies are round (400 km rule)",
                "badge": ("400", "km", ROCK),
                "analogy": "A small rock can be any lumpy shape, but a giant ball of rock gets squished round by its own weight.",
                "explanation": "Gravity pulls objects into the most efficient shape -- a sphere, where all outside points are equally distant from the center. All planets and larger moons are nearly spherical. Smaller objects can support larger departures from a sphere because rock strength beats their weak gravity. For silicate (rocky) bodies the limiting diameter is about 400 km: larger objects are always approximately spherical; smaller ones can have almost any shape, like asteroid Ida (~60 km long, photographed by the Galileo spacecraft).",
                "why": "Connects to dwarf-planet definitions (round from their own gravity).",
            },
            {
                "term": "Evolution of terrestrial atmospheres",
                "badge": ("CO₂", "96%", RED),
                "analogy": "Three pots of the same soup: one boiled dry (Venus), one froze (Mars), one stayed just right (Earth).",
                "explanation": "Atmospheres formed from gas escaping planetary interiors plus impacts of volatile-rich debris from the outer solar system. The terrestrial planets probably started similar; Mercury was too small and hot to keep gas, and the Moon probably never had an atmosphere (its material was depleted in volatiles). Early air likely held hydrogen-containing (reducing) gases -- carbon monoxide and traces of ammonia and methane; solar UV split these molecules, hydrogen escaped, and oxidized CO2-dominated atmospheres remained. Mars had a thick atmosphere and abundant liquid water early but lost the CO2 needed for greenhouse warming, cooled, and its water froze. Venus had a runaway greenhouse and permanently lost its water. Only Earth maintained liquid water. Venus and Mars ended with ~96% CO2 and a few percent nitrogen.",
                "why": "This is THE story of why only Earth stayed habitable.",
            },
            {
                "term": "Solar System habitability survey",
                "badge": ("H₂O", "follow it", BLUE),
                "analogy": "Like a real-estate search for life: rule out the houses with no water first.",
                "explanation": "Unsuitable: Mercury, Venus and the Moon; most outer-planet moons; and the giant planets (no solid surfaces). The search focuses on liquid water: Earth and Europa both have large oceans (Europa's under a thick ice crust); Mars has a long history of surface water, strong evidence for subsurface water, and brief surface flows today; Enceladus may have the most accessible liquid water, squirting into space through geysers seen by Cassini; Titan is far too cold for liquid water but, with its thick atmosphere and hydrocarbon lakes, may be the best place to search for 'life as we don't know it'. Discoveries of activity on Titan and Enceladus and Pluto's complex surface (New Horizons) were unexpected.",
                "why": "A ready-made ranked list for 'where in the solar system would you look for life?'",
            },
        ],
    },
    # ------------------------------------------------------------------ 10
    {
        "name": "Solar System: Planets Forming Around Other Stars",
        "description": "Protoplanetary and debris disks, how fast planets grow, the 10-Earth-mass gas-capture threshold, HL Tau and Fomalhaut, and molecules JWST finds in disks.",
        "source_title": "Source reader: Evidence that planets form around other stars (OpenStax Astronomy 2e, 14.4, 21.3)",
        "infographics": ["planet_growth"],
        "source_text": (
            "Star formation: dense regions in a molecular cloud collapse (runaway: stronger gravity as it collapses) into a "
            "protostar. About half the time the protostar fragments or binds to others -> binary/multiple stars; otherwise it "
            "collapses alone, like the Sun. Conservation of angular momentum spins up the protostar and flattens surrounding "
            "material into a disk. Hubble, JWST and ground telescopes observe circumstellar disks in star-forming regions (Orion "
            "Nebula, Taurus). Orion disk ~17x the size of our solar system, edge-on; dark areas mean absorption, not absence.\n"
            "Planets are hard to see: they reflect a tiny fraction of starlight and are lost in the glare. Raw material is easier: "
            "dust heated by the protostar radiates in the infrared; disks can be seen in silhouette against bright nebulae "
            "(Hubble images of four Orion disks: 2-8x the orbit of Pluto; central stars <=1 million years old). Infrared is "
            "greatest before dust combines into planets (planets hide dust inside and expose only small surfaces) -> search for "
            "planets begins with infrared from raw material. Nearly all very young protostars have disks, 10 to 1,000 AU across "
            "(Pluto's orbit ~80 AU across; Kuiper belt outer diameter ~100 AU); disk mass typically 1-10% of the Sun's -- more "
            "than all our planets combined. JWST infrared spectra of disks found benzene, ethane, acetic acid (vinegar) and "
            "formaldehyde.\n"
            "Timing: place protostar on H-R diagram to estimate age. Younger than ~1-3 million years: disk extends from near the "
            "star to tens or hundreds of AU. Older: inner regions lose dust -> donut-shaped disk with the star in the hole. "
            "Inner dense parts mostly gone by 10 million years. A forming planet clears a dust-free zone; dust and gas between "
            "star and planet not swept up falls onto the star in ~50,000 years; the planet's gravity keeps outer material from "
            "moving in (like Saturn's shepherd moons). If planets make the holes, planets form in 3-30 million years -- a quick "
            "byproduct of star birth. HD 141943 (~17 Myr) and HD 191089 (~12 Myr) disks imaged with a coronagraph.\n"
            "Growth: dust grains collide and stick (accretion); larger clumps grow faster. At ~10 cm, a perilous stage: unless "
            "they grow beyond ~100 m, gas drag makes orbits decay into the star -> must grow fast to ~1 km = planetesimals. "
            "Survivors accrete smaller planetesimals -> a few large planets. Above ~10 Earth masses, gravity captures hydrogen "
            "gas from the disk -> rapid growth to giant size, but only if the star's strengthening wind hasn't blown the gas away; "
            "disks can be blown away within 10 million years, so giant growth must be fast.\n"
            "Debris disks and shepherd planets: dust is incorporated into planets or ejected; gone after ~30 million years unless "
            "resupplied by colliding comets and asteroids stirred by growing planets. Over several hundred million years collisions "
            "decline; debris disks become undetectable by 400-500 million years (our heavy bombardment ended when the Sun was ~500 "
            "million years old). Some cometary material remains, like our Kuiper belt. Planets concentrate dust into clumps and "
            "arcs (like Saturn's shepherd moons) that are easier to image than the planets. HL Tau: ~1-million-year-old star in "
            "Taurus, ~450 light-years away; ALMA (Atacama Large Millimeter/submillimeter Array) millimeter-wave image (2014) pierces "
            "dust, showing rings and gaps carved by several protoplanets -- forming faster than expected, within the first million "
            "years; protoplanets move faster than disk material, their gravitational reach exceeds their size, sweep up material "
            "and clear gaps; models show lanes and spiral density waves. Fomalhaut (~25 light-years): JWST infrared image shows "
            "three nested belts out to ~150 AU (23 billion km), about twice our Kuiper belt; disk discovered 1983, inner belts "
            "revealed by JWST. Brightness in rings shows dust concentration (more dust, more infrared)."
        ),
        "story": (
            "BABY PICTURES OF PLANETARY SYSTEMS\n\n"
            "We can't watch our own solar system being born -- that was 4.5 billion years ago. But we can watch OTHER systems "
            "being born right now, around young stars in places like the Orion Nebula and the Taurus star-forming region.\n\n"
            "HOW A STAR GETS ITS DISK\n"
            "Stars form when dense pockets of a cold gas-and-dust cloud start collapsing under their own gravity. It's a runaway "
            "process: the more the cloud shrinks, the stronger its gravity gets. About half the time the collapsing protostar "
            "splits or pairs up with others, making a binary or multiple star system. The rest of the time it collapses alone, "
            "like our Sun did. Either way, the spinning material speeds up as it shrinks (conservation of angular momentum -- "
            "like a skater pulling in her arms) and the leftover gas and dust flattens into a disk around the star.\n\n"
            "WHY LOOK FOR DUST INSTEAD OF PLANETS?\n"
            "Planets are tiny and faint, lost in their star's glare. But BEFORE planets form, the same material is spread out "
            "as countless dust grains, each warmed by the young star and glowing in INFRARED light. Spread out, the dust has a "
            "huge glowing surface; once it's packed inside planets, almost all of it is hidden. So the infrared glow is "
            "strongest before planets form -- and the hunt for planets starts with hunting that glow. We can also see disks as "
            "dark silhouettes against bright glowing gas behind them, as Hubble did in the Orion Nebula (those disks are 2 to 8 "
            "times the size of Pluto's orbit, around stars no more than a million years old).\n\n"
            "DISK FACTS\n"
            "• Nearly all very young protostars have disks.\n"
            "• They're 10 to 1,000 AU across. (For scale: Pluto's orbit is about 80 AU across; the Kuiper belt about 100 AU.)\n"
            "• They hold 1-10% of the Sun's mass -- more than all our planets put together. So plenty of stars start out with "
            "enough material to build planets.\n"
            "• The James Webb Space Telescope has found molecules in these disks such as benzene, ethane, acetic acid (the key "
            "ingredient in vinegar) and formaldehyde.\n\n"
            "THE PLANET-BUILDING CLOCK\n"
            "Astronomers can estimate a young star's age (by comparing its temperature and brightness with models) and see how "
            "its disk changes over time:\n"
            "• Younger than about 1-3 million years: the disk stretches from right next to the star out to tens or hundreds of AU.\n"
            "• Older: the inner part has lost its dust, so the disk looks like a DONUT with the star in the hole.\n"
            "• By about 10 million years: the dense inner parts of most disks are gone.\n\n"
            "Calculations show that a forming planet can carve exactly that kind of hole. As the planet grows a few AU from the "
            "star, it clears a dust-free zone around itself. Any gas and dust left between the star and planet falls onto the "
            "star quickly -- in about 50,000 years -- while the planet's gravity keeps material outside its orbit from moving in "
            "(just like Saturn's shepherd moons keep ring edges sharp). If planets really make these holes, then planets form in "
            "only 3 to 30 million years -- a quick side effect of a star being born.\n\n"
            "FROM DUST TO PLANET\n"
            "1. Tiny dust grains collide and stick together (ACCRETION). Bigger clumps grow faster because they grab smaller ones.\n"
            "2. DANGER ZONE: at around 10 cm, clumps feel 'headwind' drag from the disk's gas, and their orbits can quickly decay, "
            "plunging them into the star. They must race past about 100 m in size...\n"
            "3. ...to reach about 1 km, when they become PLANETESIMALS, safe from the drag.\n"
            "4. The biggest planetesimals keep eating smaller ones until a few large planets remain.\n"
            "5. If a planet passes about 10 EARTH MASSES, its gravity can grab hydrogen gas from the disk, and it balloons into a "
            "GIANT planet. But it has to hurry: the young star's growing wind can blow the disk's gas away within about 10 "
            "million years.\n\n"
            "DEBRIS DISKS AND SHEPHERD PLANETS\n"
            "Leftover dust either ends up in planets or gets flung out, and it's gone after about 30 million years -- unless "
            "something refills it. Growing planets stir up comets and asteroids, which smash together at high speeds and make "
            "fresh dust. Over a few hundred million years, the collisions die down. These DEBRIS DISKS fade from view by about "
            "400-500 million years (remember, our solar system's heavy bombardment ended when the Sun was about 500 million years "
            "old). A little cometary material stays behind, like our Kuiper belt. Even when planets are invisible, their gravity "
            "herds dust into rings, clumps and arcs that are much easier to see.\n\n"
            "STAR EXAMPLES\n"
            "• HL TAU: a 'newborn' star about 1 million years old, ~450 light-years away in Taurus. In 2014 the ALMA radio telescope "
            "array used millimeter waves (which pierce the dust cocoon) to reveal a disk of bright rings and dark gaps carved by "
            "several young planets. As a protoplanet grows, it moves faster than the disk gas and dust and its gravity reaches "
            "farther than its own size, so it sweeps up material and clears a lane. HL Tau showed planets can form faster than we "
            "thought -- within the first million years.\n"
            "• FOMALHAUT: a hot young star about 25 light-years away. JWST's infrared image revealed THREE nested dust belts "
            "stretching to about 150 AU (23 billion km), roughly twice the size of our Kuiper belt. The outer disk was found in "
            "1983, but the inner belts were first seen by JWST."
        ),
        "concepts": [
            {
                "term": "How a star gets a disk",
                "badge": ("SPIN", "+ flatten", PURPLE),
                "analogy": "A spinning figure skater pulls in her arms and spins faster; a collapsing cloud does the same and flattens like pizza dough.",
                "explanation": "Stars like the Sun form when dense regions in a molecular cloud (gas and dust) collapse under gravity -- a runaway process, since gravity strengthens as the cloud shrinks, concentrating material into a protostar. Roughly half the time the protostar fragments or is bound to other protostars, forming a binary or multiple star system; otherwise (as for the Sun) it collapses alone. Conservation of angular momentum spins up the protostar and flattens surrounding material into a disk. Hubble, JWST and big ground telescopes image these circumstellar (protoplanetary) disks in star-forming regions such as the Orion Nebula and Taurus -- flattened, spinning clouds of gas and dust that are modern versions of our own solar nebula. Because nearly all very young stars have one, disks and stars must form together, and planets are probably forming in them right now.",
                "why": "Disks are where every planet -- habitable or not -- is born.",
            },
            {
                "term": "Hunting disks in infrared",
                "badge": ("IR", "glow", RED),
                "analogy": "It's easier to spot a whole field of glowing embers than the few logs they later become.",
                "explanation": "Planets are hard to detect: they reflect a tiny fraction of their star's light and are lost in its glare. Raw material is easier: each dust grain is heated by the young protostar and radiates in the infrared. Once dust is gathered into planets, nearly all of it is hidden inside, and only the small outer surfaces radiate, so infrared emission is greatest BEFORE planets form. Disks can also be seen in silhouette against bright gas (Hubble images of Orion Nebula disks 2-8 times Pluto's orbit around stars under 1 million years old). JWST infrared spectra have found benzene, ethane, acetic acid and formaldehyde in disks.",
                "why": "Explains why infrared telescopes (JWST) are key planet-formation tools.",
            },
            {
                "term": "Disk sizes and masses",
                "badge": ("10-1000", "AU", ICE),
                "analogy": "A young star's disk can be like our whole solar system's footprint -- or many times bigger.",
                "explanation": "Observations show nearly all very young protostars have disks, ranging from 10 to 1,000 AU across. For comparison, the average diameter of Pluto's orbit (a rough size for our planetary system) is 80 AU, and the Kuiper belt's outer diameter is about 100 AU. Disk masses are typically 1-10% of the Sun's mass -- more than all the planets in our solar system combined -- so a large fraction of stars begin with enough material in the right place to form planets.",
                "why": "Numbers like these are typical short-answer facts.",
            },
            {
                "term": "Donut disks and planet timing",
                "badge": ("3-30", "Myr", GOLD),
                "analogy": "A planet acts like a snowplow, clearing a lane through the dusty disk.",
                "explanation": "By placing a protostar on an H-R diagram we estimate its age and watch disks change. Younger than ~1-3 million years: the disk extends from near the star to tens or hundreds of AU. Older: the inner region loses its dust, leaving a donut with the star in the hole; dense inner parts are mostly gone by 10 million years. A planet forming a few AU out clears a dust-free region; dust and gas inside its orbit not swept up falls onto the star in ~50,000 years, while the planet's gravity keeps outer material from moving inward (like Saturn's shepherd moons). If planets make these holes, planets form in 3 to 30 million years -- short compared with stellar lifetimes.",
                "why": "Planet formation is fast -- a key timeline fact.",
            },
            {
                "term": "Accretion and the 10 cm danger zone",
                "badge": ("10 cm", "danger!", RED),
                "analogy": "Like a snowball rolling downhill -- but if it stays small too long, the wind blows it into a fire.",
                "explanation": "Accretion drives rapid growth: dust grains collide and stick, and larger clumps grow faster by capturing smaller ones. At about 10 cm, clumps enter a perilous stage: unless they grow larger than about 100 m, drag from friction with the disk gas makes their orbits decay rapidly, plunging them into the star. So they must quickly grow to nearly 1 km, when they are considered planetesimals. Survivors keep accreting smaller planetesimals, ultimately leaving a few large planets.",
                "why": "Shows why planet building is a race against time.",
            },
            {
                "term": "Gas giants: the 10 Earth-mass threshold",
                "badge": ("10 M⊕", "grab gas", GAS),
                "analogy": "Once a planet is heavy enough, it becomes a 'gas vacuum cleaner' and balloons into a giant.",
                "explanation": "If a growing planet exceeds about 10 times Earth's mass, its gravity is strong enough to capture and hold the hydrogen gas remaining in the disk, so it grows rapidly in mass and radius to giant-planet size. This requires that the rapidly evolving star hasn't yet driven the disk's gas away with its increasingly vigorous wind. Disks can be blown away within 10 million years, so giant-planet growth must also be very fast. In the traditional model, giant cores form beyond the frost line (~5-10 AU) where solid ice is plentiful.",
                "why": "Explains why giant planets formed far out -- and why hot Jupiters needed to migrate.",
            },
            {
                "term": "Debris disks",
                "badge": ("400-500", "Myr fade", ROCK),
                "analogy": "A debris disk is the dusty cloud from planet-building 'construction', kept dusty by fender-benders between comets.",
                "explanation": "Dust around newly formed stars is either incorporated into planets or ejected by gravitational interactions; it disappears after about 30 million years unless resupplied. Comets and asteroids, stirred up by growing planets, collide at high speeds and shatter into silicate dust and ice, keeping the disk supplied. Over several hundred million years their numbers and collisions decline; dusty debris disks become largely undetectable by 400-500 million years (our heavy bombardment ended when the Sun was ~500 million years old). Some cometary material likely remains, like our Kuiper belt.",
                "why": "Debris disks signal hidden planets and ongoing collisions in young systems.",
            },
            {
                "term": "Shepherd planets",
                "badge": ("ARCS", "& gaps", PURPLE),
                "analogy": "An invisible sheepdog (the planet) herds dust 'sheep' into neat rings you can see from far away.",
                "explanation": "In a young planetary system, even if we can't see the planets, they can concentrate dust particles into clumps and arcs much larger than the planets themselves and much easier to image -- just as Saturn's tiny moons shepherd ring particles into arcs and sharp edges. Debris disks with such clumps, arcs, gaps, and rings whose brightness varies with position have been found around many stars. The brightness traces dust concentration, since we see infrared from the dust: more dust, more radiation.",
                "why": "Indirect evidence of planets -- the same 'see the effect, not the planet' logic as exoplanet detection.",
            },
            {
                "term": "HL Tau (ALMA image)",
                "badge": ("HL Tau", "1 Myr", GOLD),
                "analogy": "HL Tau's disk looks like a bullseye of rings -- grooves carved by baby planets.",
                "explanation": "HL Tau is a ~1-million-year-old 'newborn' star in the Taurus star-forming region, about 450 light-years away, wrapped in dust that hides it in visible light. In 2014, ALMA (the Atacama Large Millimeter/submillimeter Array) imaged it at millimeter wavelengths (1.3 mm), which pierce the dust, revealing multiple rings and gaps carved by several newly formed protoplanets. As protoplanets grow, they orbit faster than the disk gas and dust and their gravitational reach exceeds their cross-section, so they sweep up material and clear gaps (models also show spiral density waves). HL Tau shows planets can form faster than once thought -- within the first million years.",
                "why": "The most famous image of planet formation in action.",
            },
            {
                "term": "Fomalhaut's nested belts (JWST)",
                "badge": ("3", "belts", ICE),
                "analogy": "Fomalhaut wears three dusty hula hoops, one inside the other.",
                "explanation": "Fomalhaut is a hot, young star about 25 light-years away. JWST's infrared image revealed three nested belts in its debris disk, extending to about 150 AU (23 billion km) -- roughly twice the size of our Kuiper belt. The disk was discovered in 1983, but the inner belts were revealed for the first time by JWST.",
                "why": "A recent JWST result -- good current-events material.",
            },
        ],
    },
    # ------------------------------------------------------------------ 11
    {
        "name": "Solar System: Finding Exoplanets",
        "description": "Center of mass, astrometry, the Doppler (radial velocity) method, 51 Pegasi b, selection effects, transits and transit depth, Kepler, CoRoT and TESS, and direct imaging (HR 8799).",
        "source_title": "Source reader: Planets beyond the Solar System -- search and discovery (OpenStax Astronomy 2e, 14.4, 21.4)",
        "infographics": ["doppler_method", "transit_method", "detection_compare"],
        "source_text": (
            "Exoplanet = planet orbiting a star other than the Sun. Direct observation is hard (mosquito near a giant spotlight "
            "seen from an airplane). First exoplanet around a main-sequence star found in 1995; most stars form with planets. "
            "Most detections observe the planet's effect on its star: a wobble, or dimming when it crosses in front.\n"
            "Center of mass: star and planet both orbit their common center of mass; smaller mass -> larger orbit. A Jupiter-like "
            "planet ~1/1000 the star's mass -> star's orbit 1/1000 the planet's. From Alpha Centauri (~4.25 light-years), "
            "Jupiter's orbit spans 10 arcsec, the Sun's 0.010 arcsec (1 arcsec = 1/3600 deg) with a 12-year period. Astrometry "
            "(measuring position changes) is extremely difficult -- no confirmed detections yet.\n"
            "Doppler / radial velocity: star moving toward us -> spectral lines blueshifted; away -> redshifted. The Sun's radial "
            "velocity changes ~13 m/s (~30 mph) with a 12-year period due to Jupiter. Change in speed doesn't depend on distance; "
            "works if the star is bright enough for high-quality spectra and a large telescope is available. Gives planet's "
            "orbital period and MINIMUM mass (orbit tilt usually unknown); multiple planets can be disentangled; most sensitive to "
            "large planets close to the star; used to find hundreds of planets including one around Proxima Centauri (nearest "
            "star). First success 1995: Michel Mayor and Didier Queloz (Geneva Observatory) found a planet around Sun-like 51 "
            "Pegasi, ~40 light-years away near the Great Square of Pegasus; orbit 4.2 days (Mercury takes 88 days); ~7 million km "
            "from the star; a few thousand degrees C; at least half Jupiter's mass; 2019 Nobel Prize in physics. Almost a thousand "
            "giant planets found by Doppler; many close-in 'hot Jupiters'. Selection effect: technique favors massive, close-in "
            "planets (largest wobbles, shortest orbits to monitor); analogy: only meeting people at events that need a student ID.\n"
            "Transits: when we see the orbit edge-on, the planet crosses the star once per orbit, dimming it slightly. Light curve "
            "stages: out of transit, ingress, full transit. Transit depth = (R planet / R star)^2 (area of planet disk / area of "
            "star disk). Jupiter (71,400 km) / Sun (695,700 km): ~0.01 = 1%. Earth (6,371 km) / star half the Sun's size: ~0.0003 "
            "= 0.03%. Interval between transits = planet's year -> distance via Kepler's laws; depth -> size (if star size known). "
            "Giant planets easier, even from the ground; from space down to Mars-size. Doppler mass + transit size -> density. "
            "1999: first transiting planet, HD 209458 b: transits ~3 hours every 3.5 days; ~70% of Jupiter's mass, radius ~35% "
            "larger -> gas/liquid world; atmosphere absorbs starlight at sodium lines -> sodium detected.\n"
            "CoRoT (CNES/ESA, 2007): 32 transiting exoplanets, including the first with Earth-like size and density; computer "
            "failure 2012. Kepler (NASA, 2009): stared at >150,000 stars near Cygnus, just above the Milky Way's plane; needed 3 "
            "reaction wheels (launched with 4); two failed by May 2013 -- exactly 4 years and 1 day after observing began (design "
            "life 4 years); observed 2 more years in other directions (short-period transits); closed 2018 (out of fuel). Goal: "
            "frequency of exoplanets of different sizes around different stars. TESS: transit survey of nearer, brighter stars all "
            "over the sky; by end of 2024 almost 600 planets and ~7,400 candidates.\n"
            "Discovery rules: single transit = slight dip lasting hours; need a second of similar depth, and a THIRD with the same "
            "depth and spacing to claim discovery. Citizen scientists found transits computers missed. Best confirmation: "
            "ground-based Doppler with the same period (generally impossible for Earth-size planets); or finding more planets "
            "around the same star. Kepler biases: large and short-period planets easier; 3 transits needed -> periods < 1/3 of the "
            "observing span; Earth-like 1-year orbits only found in its fourth year.\n"
            "Direct imaging: Earth reflects less than a billionth of the Sun's light; star glare and imperfect optics. Works best "
            "for young gas giants emitting infrared (stored formation heat) far from their stars. HR 8799 (Pegasus): three planets "
            "imaged in 2008, a fourth (closer) in 2010 (Keck). Challenge: planet vs brown dwarf (failed star). Brightness at "
            "different wavelengths -> temperature (HR 8799 planet 1: thick clouds); spectra -> hydrogen-rich atmosphere (planet "
            "1), methane (planet 4). Infrared best: planets brighten, Sun-like stars dim; optics suppress starlight; Earth-size "
            "imaging still hard even from space."
        ),
        "story": (
            "THE MOSQUITO AND THE SPOTLIGHT\n\n"
            "Imagine a mosquito buzzing around a giant spotlight at a store's grand opening. Up close, you could spot it. Now "
            "imagine looking from an airplane: the spotlight is easy to see, but the mosquito? Hopeless. That's what trying to "
            "photograph a planet around another star is like. So for years astronomers have used clever INDIRECT methods: instead "
            "of seeing the planet, they watch what the planet does to its star. An EXOPLANET is any planet orbiting a star other "
            "than our Sun. The first one around a normal (main-sequence) star was found in 1995; today we know most stars form "
            "with planets.\n\n"
            "EVERYBODY WOBBLES\n\n"
            "Gravity pulls both ways. A star doesn't sit perfectly still while a planet circles it -- both orbit their shared "
            "CENTER OF MASS, like two kids of different weights on a spinning seesaw. The lighter one swings in a big circle; the "
            "heavier one barely moves. A Jupiter-like planet with 1/1000 of its star's mass makes the star swing in an orbit "
            "1/1000 as big as the planet's.\n\n"
            "METHOD 1: WATCHING THE WIGGLE (ASTROMETRY)\n"
            "Alien astronomers at Alpha Centauri (about 4.25 light-years away) could try to see our Sun shift position in the sky. "
            "Jupiter's orbit would span 10 arcseconds, but the Sun's little loop only 0.010 arcseconds (1 arcsecond = 1/3600 of a "
            "degree), repeating every 12 years. Measuring positions that precisely is so hard that no planets have been confirmed "
            "this way yet.\n\n"
            "METHOD 2: THE DOPPLER (RADIAL VELOCITY) METHOD\n"
            "Remember how an ambulance siren sounds higher coming toward you and lower going away? Light does something similar. "
            "When a wobbling star moves toward us, the lines in its spectrum shift slightly toward blue (BLUESHIFT); moving away, "
            "toward red (REDSHIFT). Measuring these shifts gives the star's RADIAL VELOCITY -- its speed toward or away from us.\n"
            "• Jupiter makes our Sun's speed change by about 13 m/s (about 30 mph -- city driving speed!) every 12 years.\n"
            "• The size of the speed change doesn't depend on how far away the star is -- just on getting a bright, sharp spectrum "
            "with a big telescope.\n"
            "• One full wiggle = one orbit, giving the planet's year (and, by Kepler's laws, its distance). The size of the wiggle "
            "gives the planet's MINIMUM mass -- minimum because we usually can't tell how tilted the orbit is.\n"
            "• Several planets can be untangled from one star's wiggles.\n\n"
            "THE FIRST ONE: 51 PEGASI b (1995)\n"
            "Michel Mayor and Didier Queloz of the Geneva Observatory used the Doppler method to find a planet around 51 Pegasi, a "
            "Sun-like star about 40 light-years away near the Great Square of Pegasus. Shock: the planet orbits in just 4.2 days "
            "(Mercury takes 88), only about 7 million km from its star, heated to a few thousand degrees, with at least half "
            "Jupiter's mass. They won the 2019 Nobel Prize in physics. Since then, almost a thousand giant planets have been "
            "found this way, many of them close-in HOT JUPITERS. The method has even found a planet around Proxima Centauri, the "
            "nearest star.\n\n"
            "BEWARE THE SELECTION EFFECT\n"
            "Why so many hot Jupiters at first? Big planets close to their stars make the biggest, fastest wobbles, and their "
            "short orbits can be confirmed quickly. So the method 'selects' them as easy finds. It's like looking for friends only "
            "at events that need a student ID -- you'll only meet students! As we watch longer and measure smaller shifts, we find "
            "smaller and more distant planets too.\n\n"
            "METHOD 3: TRANSITS (THE SHADOW METHOD)\n"
            "If we happen to see a planet's orbit edge-on, the planet crosses in front of its star once per orbit -- a TRANSIT -- "
            "blocking a tiny bit of light. A graph of the star's brightness (a LIGHT CURVE) shows a dip: (1) out of transit, (2) the "
            "planet starts crossing, (3) the full drop.\n"
            "• TRANSIT DEPTH = (radius of planet / radius of star) squared, because the planet's disk blocks the star's disk "
            "(circle area = pi x R^2).\n"
            "  Jupiter (71,400 km) in front of the Sun (695,700 km): (71,400/695,700)^2 = about 0.01, or 1% -- easy for Kepler.\n"
            "  Earth (6,371 km) in front of a star half the Sun's size: about 0.0003, or 0.03% -- much harder.\n"
            "• The time between dips = the planet's year -> its distance (Kepler's laws).\n"
            "• The depth -> the planet's SIZE (if we know the star's size).\n"
            "• Combine Doppler MASS with transit SIZE and you get DENSITY -- what the planet is made of!\n"
            "In 1999 the first transiting planet was found around HD 209458: it passes in front for about 3 hours every 3.5 days. "
            "It has about 70% of Jupiter's mass but a radius 35% larger, so it must be a gas-and-liquid world. During transit, "
            "atoms in its atmosphere absorb some starlight -- revealing SODIUM in its air.\n\n"
            "SPACE TELESCOPES ON THE HUNT\n"
            "• CoRoT (French and European space agencies, 2007): found 32 transiting planets, including the first with Earth-like "
            "size and density; a computer failure ended it in 2012.\n"
            "• KEPLER (NASA, 2009): stared at more than 150,000 stars in one patch of sky near the constellation Cygnus. It needed "
            "three spinning reaction wheels to point steadily (it carried four). By May 2013 two had failed -- ironically exactly "
            "4 years and 1 day after it started its 4-year mission. It kept working two more years in other directions, then ran "
            "out of fuel in 2018. It found thousands of planets.\n"
            "• TESS (Transiting Exoplanet Survey Satellite): now surveying nearer, brighter stars all over the sky -- almost 600 "
            "planets and about 7,400 candidates by the end of 2024.\n\n"
            "WHEN DOES A DIP COUNT AS A DISCOVERY?\n"
            "One dip could be a glitch. A second dip of the same depth might be a different planet. Only a THIRD dip with the same "
            "depth and the same spacing counts as a discovery. That's why Kepler, which needed three transits, could only find "
            "planets with years shorter than a third of its observing time -- Earth-like 1-year orbits only showed up in its "
            "fourth year. Even then, astronomers like extra proof: a matching Doppler wobble (usually impossible for Earth-size "
            "planets) or more planets around the same star. Citizen scientists even spotted transits that computers missed!\n\n"
            "METHOD 4: DIRECT IMAGING\n"
            "Seeing is believing -- but Earth reflects less than a billionth of the Sun's light, and even the best telescope "
            "optics smear a star's glare. Direct imaging works best for YOUNG GIANT planets far from their stars, which still glow "
            "in infrared with heat left from forming. In 2008 three planets were photographed around the star HR 8799 in Pegasus; "
            "a fourth, closer one appeared in 2010. Their colors reveal temperatures (planet 1 seems to have thick clouds) and "
            "their spectra reveal gases: hydrogen in planet 1's atmosphere, methane in planet 4's. A tricky part: making sure the "
            "dot is a planet and not a BROWN DWARF (a failed star). Infrared is the best light to use, because planets get "
            "brighter in infrared while Sun-like stars get dimmer, and special optics can block the starlight. Still, imaging an "
            "Earth-size planet will be very hard, even from space."
        ),
        "concepts": [
            {
                "term": "Exoplanet",
                "badge": ("EXO", "planet", GOLD),
                "analogy": "An exoplanet is a planet with a different 'home sun' than ours.",
                "explanation": "A planet orbiting a star other than the Sun. Imaging one directly is like spotting a mosquito next to a giant spotlight from an airplane: planets are faint and lost in the glare. In 1995, after decades of effort, the first exoplanet orbiting a main-sequence star was found; today we know most stars form with planets. Most detections observe the planet's effect on its host star -- a gravitational wobble, or a periodic dimming when the planet crosses in front.",
                "why": "Every 'beyond the Solar System' habitability question starts here.",
            },
            {
                "term": "Center of mass and astrometry",
                "badge": ("0.010", "arcsec", PURPLE),
                "analogy": "A grown-up and a toddler swinging each other around: the toddler zooms in a circle, the grown-up just shuffles.",
                "explanation": "A star and planet both revolve around their common center of mass; the smaller the mass, the larger the orbit. A Jupiter-like planet with 1/1000 of its star's mass makes the star's orbit 1/1000 the size of the planet's. Seen from Alpha Centauri (~4.25 light-years), Jupiter's apparent orbit is 10 arcseconds across and the Sun's only 0.010 arcseconds (1 arcsecond = 1/3600 degree), with a 12-year period. Astrometry -- measuring a star's changing position -- could then give the planet's mass and distance with Kepler's laws, but it is so difficult that no confirmed detections have been made this way yet.",
                "why": "Know why astrometry is the 'hard' method and what 'center of mass' means.",
            },
            {
                "term": "Doppler (radial velocity) method",
                "badge": ("RV", "wobble", BLUE),
                "analogy": "Like hearing an ambulance siren's pitch rise and fall -- the star's light 'pitch' shifts as it wobbles.",
                "explanation": "As a star moves around the center of mass, part of its motion is toward or away from us. Its spectral lines shift: blueshift when moving toward us, redshift when moving away. The Sun's radial velocity changes by ~13 m/s (~30 mph) with a 12-year period due to Jupiter. The speed change doesn't depend on the star's distance -- it works at any distance if the star is bright enough for high-quality spectra on a large telescope. It gives the planet's orbital period (and distance via Kepler's laws) and its minimum mass (the orbit's tilt is usually unknown); several planets' signals can be disentangled. Most sensitive to large planets close to their stars; it found hundreds of planets, including one around Proxima Centauri.",
                "why": "The most-tested detection method -- know what it measures and its bias.",
            },
            {
                "term": "51 Pegasi b",
                "badge": ("1995", "first!", SUN),
                "analogy": "Finding 51 Peg b was like discovering a gas giant 'racing' around its star in under a week.",
                "explanation": "In 1995 Michel Mayor and Didier Queloz (Geneva Observatory) used the Doppler method to find a planet around 51 Pegasi, a Sun-like star about 40 light-years away near the Great Square of Pegasus. It orbits in only 4.2 days (Mercury takes 88), about 7 million km from its star, so it is heated to a few thousand degrees C, and it has at least half Jupiter's mass -- clearly a jovian planet, the first 'hot Jupiter'. Mayor and Queloz received the 2019 Nobel Prize in physics. Almost a thousand giant planets have since been found with the Doppler technique.",
                "why": "Classic history question: first exoplanet around a Sun-like star.",
            },
            {
                "term": "Selection effect (observational bias)",
                "badge": ("BIAS", "easy finds", RED),
                "analogy": "If you only fish with a big net, you'll think the lake only has big fish.",
                "explanation": "A selection effect is when the discovery technique selects certain kinds of objects as easy finds. Doppler favors massive planets close to their stars (biggest, fastest wobbles; short orbits completed quickly), so early discoveries were mostly hot Jupiters. Transits likewise favor large planets with short periods. Analogy from the text: if you only attend events that require a student ID, you'll only meet students. Correcting for these biases shows small planets are actually more common than giant ones. Watching longer and measuring smaller shifts reveals more distant, less massive planets.",
                "why": "Explains why the exoplanet 'census' doesn't match reality at first glance.",
            },
            {
                "term": "Transit method",
                "badge": ("DIP", "transit", GOLD),
                "analogy": "Like a moth flying in front of a porch light -- you can't see the moth, but the light flickers.",
                "explanation": "When a planet's orbit is seen nearly edge-on, the planet crosses in front of its star once per orbit (a transit), dimming it slightly. The light curve shows (1) out of transit, (2) ingress, (3) the full drop in brightness. The interval between transits is the planet's year, which gives its distance via Kepler's laws; the depth gives the planet's size if the star's size is known. Larger planets block more light, so giant-planet transits can be detected even from the ground; from space (above atmospheric distortion) transits as small as Mars-size have been detected. Transits favor large planets and short periods.",
                "why": "The method behind most known exoplanets -- and atmosphere studies.",
            },
            {
                "term": "Transit depth formula",
                "badge": ("(Rp/Rs)²", "depth", GOLD),
                "analogy": "A coin held in front of a flashlight blocks light in proportion to the coin's area compared with the light's area.",
                "explanation": "The planet's circular disk blocks the star's circular disk; circle area = pi R^2, so transit depth = (pi Rp^2)/(pi Rs^2) = (Rp / Rs)^2. Example: Jupiter (radius 71,400 km) and the Sun (695,700 km): (71,400 / 695,700)^2 = 0.0105, about 1%, easily detected by Kepler. Check: Earth (6,371 km) in front of a star half the Sun's size (347,850 km): (6,371 / 347,850)^2 = 0.000335, about 0.03% -- far less than 1%. Smaller stars make small planets easier to detect.",
                "why": "A guaranteed calculation type -- practice it with your calculator.",
            },
            {
                "term": "Mass + size = density (HD 209458 b)",
                "badge": ("1999", "HD 209458", GAS),
                "analogy": "Knowing both how heavy and how big a ball is tells you if it's a bowling ball or a beach ball.",
                "explanation": "Doppler gives mass; transit gives size; together they give average density (mass/volume) and so composition. In 1999 the first transiting planet was found (from the ground) around HD 209458: it transits for ~3 hours every 3.5 days. Doppler showed ~70% of Jupiter's mass, but its radius is ~35% larger than Jupiter's, so it must be a gas and liquid world like Jupiter or Saturn -- the first exoplanet whose makeup we could determine. During transit, atoms in its atmosphere absorb starlight; absorption at yellow sodium lines showed sodium in its atmosphere, and other elements can now be measured.",
                "why": "Transit spectroscopy is how we'll read exoplanet atmospheres for biomarkers.",
            },
            {
                "term": "Kepler, CoRoT and TESS",
                "badge": ("150K", "stars", BLUE),
                "analogy": "Kepler was a space telescope that stared at one patch of sky like a lifeguard watching one pool for years.",
                "explanation": "CoRoT (CNES/ESA, launched 2007) found 32 transiting exoplanets, including the first transiting planet with Earth-like size and density; a computer failure ended it in 2012. NASA's Kepler (launched 2009) continuously monitored more than 150,000 stars in a small patch near Cygnus, just above the Milky Way's plane, to measure how often planets of different sizes occur around different stars. It needed three reaction wheels to point (launched with four); two failed by May 2013 -- exactly 4 years and 1 day after observing began (designed for 4 years). It then observed other fields for two more years and closed in 2018 when out of fuel. TESS (Transiting Exoplanet Survey Satellite) now surveys nearer, brighter stars all over the sky: almost 600 planets and ~7,400 candidates by end of 2024.",
                "why": "Mission names, dates and goals are common quick-answer questions.",
            },
            {
                "term": "Rules for a transit 'discovery'",
                "badge": ("3", "transits", GREEN),
                "analogy": "One knock could be the wind, two could be a coincidence -- three evenly spaced knocks means someone's at the door.",
                "explanation": "A single transit is a slight dip lasting hours that could be a false signal near the telescope's precision limit. A second dip of similar depth might be another planet. A discovery requires a third transit with similar depth and the same spacing. Strongest confirmation: a ground-based Doppler shift with the same period (generally impossible for Earth-size planets) or finding more planets orbiting the same star. Citizen scientists have found transits computer searches missed. Because 3 transits are needed, Kepler could only find planets with periods under a third of its observing span -- Earth-like 1-year orbits only in its fourth year.",
                "why": "Explains why long-period (Earth-like) planets are under-discovered.",
            },
            {
                "term": "Direct imaging (HR 8799)",
                "badge": ("HR 8799", "4 planets", PURPLE),
                "analogy": "Taking a photo of a firefly next to a lighthouse -- you need to block the lighthouse first.",
                "explanation": "Earth reflects less than one billionth of the Sun's light, and imperfect optics smear a star's glare. Direct imaging works best for young gas giants that emit infrared (heat stored from formation) at large distances from their stars, using techniques to subtract starlight. In 2008 three planets were imaged around HR 8799 (in Pegasus); a fourth, closer one was found in 2010 (Keck). Brightness at different wavelengths gives atmospheric temperature (planet 1's color suggests thick clouds); spectra show a hydrogen-rich atmosphere for planet 1 and methane for planet 4. A challenge is telling planets from brown dwarfs (failed stars). Infrared is optimal because planets brighten and Sun-like stars dim there; Earth-size imaging remains very hard even from space.",
                "why": "Future habitable-planet searches will rely on direct imaging + spectra.",
            },
        ],
    },
    # ------------------------------------------------------------------ 12
    {
        "name": "Solar System: Exoplanets Everywhere & New Ideas on Planet Formation",
        "description": "What Kepler taught us: super-Earths and mini-Neptunes, how common planets are, mass-radius relations, inflated hot Jupiters, multi-planet systems like Kepler-62, hot Jupiter migration, and how our own planets may have moved.",
        "source_title": "Source reader: Exoplanets everywhere and new perspectives on planet formation (OpenStax Astronomy 2e, 14.4, 21.5, 21.6)",
        "infographics": ["exoplanet_zoo", "hot_jupiter_migration"],
        "source_text": (
            "Before exoplanets, astronomers expected systems like ours (circular orbits, giants several AU out). Such systems "
            "exist, but many are very different, and some planet classes don't exist here: masses between Earth and Neptune, and "
            "planets several times more massive than Jupiter. First planet around a solar-type star announced 1995; within two "
            "decades thousands known. Most found so far are larger/more massive than Earth -- an observational bias (small "
            "planets harder to detect). Corrected: small planets more common than giants; 'super-Earths' (2-10 Earth masses) "
            "common though absent here. Kepler suggests about half (or more) of stars have planets -> at least 100 billion planets "
            "in the Galaxy. Most planets in transit statistics are sizes between Earth and Neptune. Early discoveries were "
            "Jupiter-mass; later, Neptune- and Earth-size. Kepler 'discovery space': periods < ~400 days, sizes > Mars. Many "
            "exoplanets in multiplanet systems; whether they're coplanar measured by astrometry (difficult).\n"
            "Mass-radius (Figure 21.25): theoretical lines for pure iron, rock, water, hydrogen planets; Jupiter = ~320 Earths. "
            "More mass -> larger radius at low masses, but above ~1,000 Earth masses radius stops increasing and more massive "
            "planets are smaller (gravity compresses material). Real planets layered (Earth: solid iron core, liquid outer core, "
            "rocky mantle and crust, thin atmosphere); models use 2-3 layers -- narrowing possibilities first. Venus and Earth fall "
            "between pure iron and pure rock lines. Many gas giants >100 Earth masses are less dense than pure hydrogen should be "
            "-- inflated: close-in planets absorb lots of starlight trapped deep in the atmosphere; slightly eccentric close orbits "
            "get tidal dissipation that also inflates. Cooler 'cold Jupiters' in wider orbits shouldn't be inflated unless young "
            "-- no data yet.\n"
            "Systems: first multi-planet system Upsilon Andromedae (1999, Doppler). Transits need coplanar systems seen edge-on; "
            "Kepler sensitive to periods < ~4 years -> compact systems. By end of 2025, >1,000 systems; many with 2 known planets, "
            "some 5, one with 8; mostly very compact, planets closer than Mercury. Kepler-62: all but one planet larger than Earth "
            "(super-Earths); 62d mini-Neptune size (likely gaseous); smallest about Mars-size; three inner planets very close; only "
            "outer two have orbits larger than Mercury's; habitable zone smaller than the Sun's because the star is fainter. "
            "Closely spaced planets tug each other -> transits a few minutes early/late (transit timing) -> masses. Planets orbiting "
            "close double stars (two suns, like Tatooine); planets around one star of a wide binary.\n"
            "Comparison with theory (14.4): nothing contradicts formation in disks, but hot Jupiters (jovian mass closer than "
            "Mercury's orbit) are the biggest problem -- giants need water ice to condense, which isn't stable near a star. So "
            "giants formed several AU out and migrated: disk interactions (planet moves faster than gas/dust, feels a 'headwind', "
            "loses energy, spirals in; some plunge into the star, some stop) or gravitational encounters scattering a planet "
            "inward. Large orbital eccentricities also point to scattering. A few percent of systems have hot Jupiters. New data "
            "contradicting theories drive science forward.\n"
            "21.6: traditional model works only for giants forming at ~5-10 AU; can't explain hot Jupiters (no solids close in) or "
            "elliptical orbits (disk interactions circularize orbits). Migration options: lose angular momentum to the gas disk "
            "and spiral inward; or gravitational interactions make the orbit elliptical, carrying it inward, then friction-like "
            "forces circularize it close to the star. Transit + Doppler can test alignment: early cases aligned with star spin; "
            "later giant planets found orbiting at right angles or opposite to the star's spin -> planet-planet kicks or a passing "
            "star. Galaxy's early stars lacked heavy elements; Kepler-444: 5 planets (Mercury- to Venus-size), all orbiting faster "
            "than Mercury, around a star >11 billion years old formed when the Milky Way was ~2 billion years old -> rocky planet "
            "formation began early. Close-in rocky planets common elsewhere but missing here -> perhaps Jupiter migrated inward and "
            "knocked such planets into the Sun. Uranus and Neptune likely formed nearer Jupiter and Saturn and were scattered "
            "outward (disk too thin beyond Saturn to build them before disks vanish in a few million years). Lesson: dangerous to "
            "generalize from one example. Polite skaters vs roller derby."
        ),
        "story": (
            "WE WERE WRONG -- AND THAT'S GREAT!\n\n"
            "Before 1995, astronomers knew just one planetary system: ours. Logically enough, they assumed others would be similar "
            "-- rocky planets close in, giants a few AU out, everyone on neat circular orbits. Then the discoveries poured in, "
            "and nature had surprises. Systems like ours do exist in large numbers, but many are wildly different, and there are "
            "whole kinds of planets we don't have at all. In science, those 'that's not what we expected' moments are often the "
            "most exciting, because they force new and deeper ideas.\n\n"
            "PLANETS ARE EVERYWHERE\n"
            "• Kepler's data suggest about HALF of all stars (or more) have planets. That means at least 100 BILLION planets in "
            "our Galaxy alone.\n"
            "• Early on, most planets found were bigger than Earth. That was a SELECTION EFFECT: small planets are harder to "
            "detect. After correcting for it, small, Earth-like planets turn out to be MORE common than giants.\n"
            "• The most common sizes Kepler found are ones we don't have: between Earth and Neptune. SUPER-EARTHS have 2 to 10 "
            "times Earth's mass; MINI-NEPTUNES are a bit bigger and probably mostly gas.\n"
            "• Kepler's 'discovery space' was planets with orbits shorter than about 400 days and sizes bigger than Mars (because "
            "of its 4-year mission and the difficulty of seeing tiny dips).\n\n"
            "WHAT ARE THEY MADE OF? MASS vs. SIZE\n"
            "When a planet has both a measured mass and radius, we can compare it with model planets made of pure iron, pure rock, "
            "pure water or pure hydrogen. (Jupiter has enough mass to make about 320 Earths.)\n"
            "• Like adding clay to a clay ball, adding mass usually makes a planet bigger.\n"
            "• But above about 1,000 Earth masses, extra mass makes a planet SMALLER! Its stronger gravity squeezes even rock and "
            "gas tighter.\n"
            "• Real planets are layered (Earth has a solid iron inner core, liquid outer core, rocky mantle and crust, and a thin "
            "atmosphere). Modelers start with simple 2-3 layer models -- narrowing down possibilities is a good first step in "
            "science. Venus and Earth plot between the pure-iron and pure-rock lines, just as we'd expect.\n"
            "• PUFFY HOT JUPITERS: some giant planets are less dense than even pure hydrogen should be! Many orbit very close to "
            "their stars and absorb huge amounts of energy, which can get trapped deep inside and puff them up. Slightly oval "
            "close-in orbits also let the star raise tides in the planet, and that tidal energy can inflate it too. COLD JUPITERS "
            "in wide orbits shouldn't be puffed up (unless very young) -- but we don't have that data yet.\n\n"
            "FAMILIES OF PLANETS\n"
            "The first multi-planet system around another star, Upsilon Andromedae, was found in 1999 with the Doppler method. To "
            "see several transiting planets, their orbits must line up in nearly the same plane facing us, and Kepler could only "
            "catch orbits shorter than about 4 years -- so it found flat, compact systems. By the end of 2025, more than 1,000 "
            "multi-planet systems were known. Many have two known planets, some have five, and one has EIGHT, like ours. Most are "
            "very compact, with planets closer to their star than Mercury is to the Sun.\n\n"
            "KEPLER-62 is a good example: all but one of its planets are bigger than Earth (super-Earths), one (62d) is mini-Neptune "
            "size and probably gassy, and the smallest is about Mars' size. Three planets hug the star; only the outer two orbit "
            "farther than Mercury does from the Sun. Its HABITABLE ZONE (where liquid water could exist) is smaller and closer in "
            "than the Sun's, because the star is fainter.\n\n"
            "In tightly packed systems, planets tug on each other, so transits arrive a few minutes early or late. Measuring those "
            "timing shifts lets scientists calculate the planets' masses. Kepler also found planets circling CLOSE DOUBLE STARS -- "
            "a sky with two suns, like Tatooine in Star Wars -- and planets orbiting one star of a wide double-star pair.\n\n"
            "THE HOT JUPITER PUZZLE\n"
            "Hot Jupiters -- giant planets closer to their stars than Mercury is to the Sun -- were the biggest headache. As far "
            "as we know, a giant planet can't form without water ice to build its core, and ice can't survive that close to a "
            "star. The traditional model only builds giants about 5-10 AU out, where the disk is cold enough to have lots of solid "
            "material. It also can't explain oval orbits, because interactions with the disk quickly make a young planet's orbit "
            "circular. (Only a few percent of systems have hot Jupiters, but each needs explaining.)\n\n"
            "The answer: giants form far out and then MIGRATE inward. Two ways:\n"
            "1. DISK DRAG: while gas remains in the disk, the planet moves faster than the gas and dust, feels a kind of "
            "'headwind', loses energy (angular momentum) to the disk, and spirals inward. Many protoplanets probably plunge into "
            "their star; somehow some stop in time and survive as hot Jupiters.\n"
            "2. SCATTERING: in a chaotic young system, gravitational encounters between sibling planets can fling a giant onto a "
            "stretched, oval orbit that dips close to the star; then friction-like forces circularize it close in.\n"
            "Many exoplanets have very oval (eccentric) orbits, which also points to planets shoving each other around. By "
            "combining transits and Doppler, astronomers found some giants orbiting at RIGHT ANGLES to their star's spin, or even "
            "BACKWARD -- probably from planet-planet kicks or a passing star.\n\n"
            "WHEN DID ROCKY PLANETS START FORMING?\n"
            "The earliest stars had few heavy elements (like iron) to build rocky cores. The star KEPLER-444 helps answer this: it "
            "has five tightly packed planets, from Mercury-size to Venus-size, all orbiting faster than Mercury does -- and the star "
            "is more than 11 billion years old, born when the Milky Way was only about 2 billion years old. So rocky planets were "
            "being made soon after our Galaxy formed.\n\n"
            "MAYBE WE'RE THE ODD ONES\n"
            "Close-in rocky planets are common around other stars but missing in our system. Maybe Jupiter once migrated inward "
            "and knocked such planets into the Sun. Astronomers also think Uranus and Neptune formed closer in, near where Jupiter "
            "and Saturn are now, and were thrown outward by gravitational interactions -- because beyond Saturn the disk was so "
            "thin it would have taken billions of years to build them, yet disks only last a few million years. Lesson: it's "
            "dangerous to draw big conclusions from just one example!\n\n"
            "THE NEW PICTURE\n"
            "The old view was a skating rink full of polite skaters all going the same way in neat circles. The new view is a "
            "ROLLER DERBY: planets crash, change direction, and sometimes get thrown out of the rink entirely."
        ),
        "concepts": [
            {
                "term": "How common are planets?",
                "badge": ("100B+", "in Galaxy", GOLD),
                "analogy": "Planets turned out to be as common as stars -- like finding that almost every house on the street has a backyard.",
                "explanation": "The first planet circling a solar-type star was announced in 1995; twenty years later thousands were known. Kepler data suggest perhaps half of all stars (or more) have exoplanets, implying at least 100 billion planets in our Galaxy alone. Most planets found so far are larger or more massive than Earth, but that's an observational bias; corrected, small (terrestrial-type) planets are actually more common than giant planets.",
                "why": "Abundant planets raise the odds of habitable worlds -- key to life-beyond-Earth questions.",
            },
            {
                "term": "Super-Earths and mini-Neptunes",
                "badge": ("2-10", "Earth masses", "#6fb07a"),
                "analogy": "They're the 'medium' size planets on a menu where our solar system only ordered small and extra-large.",
                "explanation": "Super-Earths have 2 to 10 times Earth's mass; mini-Neptunes are slightly larger and likely largely gaseous (e.g. Kepler-62d). We have none in our solar system, yet nature makes them easily: the largest numbers of transiting planets found are in sizes between Earth and Neptune. Another class we lack: planets several times more massive than Jupiter. In early years most detected planets were Jupiter-mass (easiest); improved technology later found Neptune-size and near-Earth-size worlds. Kepler's discovery space: periods under ~400 days and sizes larger than Mars.",
                "why": "Many 'habitable zone' candidates are super-Earths -- know the term.",
            },
            {
                "term": "Mass-radius diagram",
                "badge": ("M vs R", "makeup", PURPLE),
                "analogy": "Adding clay makes a clay ball bigger -- until the ball is so heavy it squishes itself smaller.",
                "explanation": "Exoplanets with measured mass and radius are compared with model lines for pure iron, rock, water and hydrogen planets (Jupiter holds about 320 Earth masses). At low masses, radius grows with mass. Above ~1,000 Earth masses the radius stops increasing and more massive planets are actually smaller, because stronger gravity compresses even 'incompressible' materials. Real planets are layered (Earth: solid iron inner core, liquid iron outer core, rocky mantle and crust, thin atmosphere); modelers simplify to two or three layers -- narrowing possibilities first, a good example of how science works. Venus and Earth plot between the pure-iron and pure-rock lines, consistent with their mixed composition.",
                "why": "How we decide if an exoplanet is rocky (possibly habitable) or gaseous.",
            },
            {
                "term": "Hot Jupiters and cold Jupiters",
                "badge": ("HOT", "Jupiters", "#ff7a3d"),
                "analogy": "A hot Jupiter is like a marshmallow held right next to a campfire -- scorching and puffed up.",
                "explanation": "HOT JUPITERS are gas-giant exoplanets in extremely close orbits around their stars -- often just a few days long and closer than Mercury is to the Sun -- with temperatures over 1,000 K. A commonly tested fact: their masses range from about 0.36 to 13.6 Jupiter masses. They were the first and easiest exoplanets to find with the Doppler (wobble) method because big, close planets make the biggest, fastest wobbles (51 Pegasi b, 1995). Many are probably tidally locked, with a permanent day side. Many are puffier than even pure hydrogen should be: they soak up so much starlight, and get so much tidal heating on slightly oval orbits, that their atmospheres inflate. COLD JUPITERS are gas giants like Jupiter that orbit beyond the frost (snow) line, where it is cold enough for water, ammonia and methane to freeze into ice; they shouldn't be inflated unless very young. Only a few percent of planetary systems have hot Jupiters.",
                "why": "Hot vs. cold Jupiter definitions and the mass range are favorite exoplanet questions.",
            },
            {
                "term": "Hot Neptunes",
                "badge": ("HOT", "Neptunes", "#7fb8d8"),
                "analogy": "A hot Neptune is a hot Jupiter's smaller cousin that got its puffy outer layers blown away.",
                "explanation": "Hot Neptunes are exoplanets similar to hot Jupiters but smaller: they have less atmosphere and denser cores, because their star's radiation has stripped much of their gas away. They are more like ice giants (containing water, ammonia and methane) than the mostly hydrogen-and-helium hot Jupiters, and they often orbit within about 1 AU of their stars. Planets between Earth and Neptune in size -- super-Earths and mini-Neptunes -- turn out to be the most common kinds Kepler found, even though our solar system has none.",
                "why": "Exoplanet-type classification questions often list hot Neptunes.",
            },
            {
                "term": "Multi-planet systems",
                "badge": ("1000+", "systems", ICE),
                "analogy": "Most stars that have one planet have brothers and sisters for it too.",
                "explanation": "Our system has 8 major planets, half a dozen dwarf planets and millions of smaller objects; disks naturally form multiple planets. The first multi-planet exosystem, Upsilon Andromedae, was found by Doppler in 1999. Multiple transiting planets are only seen if their orbits are nearly coplanar and edge-on to us, and Kepler was sensitive only to periods under ~4 years -- so it found compact, coplanar systems. By the end of 2025, more than 1,000 such systems were known: many with two known planets, some with five, one with eight. Most are very compact, with planets closer to their star than Mercury is to the Sun. Kepler also found planets orbiting close double stars (two suns, like Tatooine) and planets around one star of a wide binary.",
                "why": "Shows our solar system's layout is just one of many possibilities.",
            },
            {
                "term": "Kepler-62",
                "badge": ("K-62", "5 planets", GREEN),
                "analogy": "Kepler-62 is a crowded little neighborhood around a dim star, with its 'just right' zone pulled in close.",
                "explanation": "One of the largest known exoplanet systems. All but one planet are larger than Earth (super-Earths); 62d is in the mini-Neptune size range and likely largely gaseous; the smallest is about the size of Mars. The three inner planets orbit very close to their star, and only the outer two have orbits larger than Mercury's. Its habitable zone (green in Figure 21.26) is much smaller than the Sun's because the star is intrinsically fainter. (Planet drawings are artistic -- we have no detailed images of exoplanets.)",
                "why": "A worked example of a habitable zone around a fainter star.",
            },
            {
                "term": "Transit timing variations",
                "badge": ("±min", "timing", BLUE),
                "analogy": "Like runners on neighboring lanes bumping elbows -- each arrives a little early or late.",
                "explanation": "In closely spaced systems, planets interact gravitationally, so observed transits occur a few minutes earlier or later than simple orbits predict. Measuring these timing variations lets Kepler scientists calculate the planets' masses -- another way to learn about exoplanets, especially valuable when Doppler measurements are impossible (e.g. for Earth-size planets). Finding multiple planets around one star is also one of the most convincing confirmations that a dip is really a planet.",
                "why": "An alternative way to get mass -- and thus density -- of small planets.",
            },
            {
                "term": "Hot Jupiter migration",
                "badge": ("INWARD", "migration", "#ff7a3d"),
                "analogy": "A hot Jupiter is like a kid who was born in the backyard and later moved into the kitchen right next to the stove.",
                "explanation": "Hot Jupiters (jovian mass, closer than Mercury's orbit) pose the biggest problem for formation theory: giant planets need condensed water ice, which isn't stable near a star, and the traditional model builds giants only at ~5-10 AU. It also can't explain eccentric orbits (disk interactions circularize young orbits). Most research supports migration: (1) while gas remains in the disk, the planet transfers orbital angular momentum to the disk -- it moves faster than the gas and dust, feels a 'headwind' like friction, loses energy and spirals inward (many may plunge into the star; some stop); (2) gravitational interactions between planets make a giant's orbit elliptical, carrying it into the hot region, where friction-like forces circularize it close to the star. A few percent of systems have hot Jupiters.",
                "why": "The standard explanation tested whenever hot Jupiters come up.",
            },
            {
                "term": "Eccentric and misaligned orbits",
                "badge": ("TILTED", "orbits", PURPLE),
                "analogy": "Planets playing bumper cars can end up driving sideways or backward around the track.",
                "explanation": "Many exoplanets have large orbital eccentricities (non-circular orbits), which weren't expected for planets forming in a disk -- support for planets scattering each other through gravitational interactions. Combining transits and Doppler measurements shows whether planets orbit in their star's equatorial plane and spin direction. Early cases matched (like our solar system), but some gas giants orbit at right angles to, or opposite to, their star's spin -- likely from close planet-planet encounters kicking one into an unusual orbit, or a passing star disturbing the young system.",
                "why": "Evidence that planetary systems evolve violently -- the 'roller derby' model.",
            },
            {
                "term": "Kepler-444 and early rocky planets",
                "badge": ("11+", "Gyr old", ROCK),
                "analogy": "Kepler-444's planets are like ancient ruins proving builders were at work very early in history.",
                "explanation": "The young Milky Way's stars had few heavy elements like iron; several generations of stars had to enrich the gas. Since planets form 'inside out' from rocky cores, when did planet formation 'turn on'? Kepler-444 hosts a tightly packed system of five planets, from Mercury-size to Venus-size, all orbiting faster than Mercury orbits the Sun. The star is more than 11 billion years old and formed when the Milky Way was only ~2 billion years old -- so heavy elements for rocky planets were available relatively soon after the Galaxy formed.",
                "why": "Older rocky planets = more time for life to arise elsewhere (Fermi paradox link).",
            },
            {
                "term": "Did our planets move? (the Nice Model)",
                "badge": ("Nice", "model", GAS),
                "analogy": "Our solar system's furniture may have been rearranged after the house was built.",
                "explanation": "Close-in rocky planets are common around other stars (like Kepler-444) but missing in our system, so maybe more rocky planets once existed close to the Sun. Evidence from outer solar system motions suggests Jupiter may have migrated inward long ago, and its gravity could have knocked close-in rocky planets into the Sun. Astronomers also think Uranus and Neptune formed closer to where Jupiter and Saturn are now and were kicked outward by gravitational interactions, because the disk beyond Saturn was too thin to build them in the few million years disks survive (it would take billions of years). Models in which the giant planets' orbits shifted after they formed are often called the 'Nice Model'; such a shuffle in the first few hundred million years may also have flung asteroids inward, causing the heavy bombardment. Lesson: it's dangerous to draw conclusions from a single example.",
                "why": "Ties exoplanet lessons back to our own solar system's history.",
            },
            {
                "term": "Polite skaters vs. roller derby",
                "badge": ("DERBY", "new model", RED),
                "analogy": "Old idea: planets are polite ice skaters. New idea: planets play roller derby.",
                "explanation": "Exoplanets have produced a much more chaotic picture of planetary system formation. The original model (based only on our solar system) imagined planets like polite skaters obeying the rink's rules, all moving the same direction on roughly circular paths. The new picture is a roller derby: planets crash into one another, change directions, and sometimes are thrown entirely out of the rink. Nothing contradicts the basic idea that planets form by clumping in circumstellar disks -- but migration and scattering are now part of the story. New data contradicting expectations is how science makes progress.",
                "why": "A memorable summary for essay-style 'how did our view change?' questions.",
            },
        ],
    },
    # ------------------------------------------------------------------ 13
    {
        "name": "Solar System: Habitability & the Habitable Zone",
        "description": "What makes an environment habitable, the habitable zone and inverse-square law, greenhouse warming on Venus, Earth and Mars, M-dwarf and Proxima Centauri planets, the continuously habitable zone, and Earth-like exoplanet candidates.",
        "source_title": "Source reader: Habitable environments and habitable planets (OpenStax Astronomy 2e, 21.6, 30.2, 30.3)",
        "infographics": ["habitable_zone", "greenhouse_numbers", "life_recipe"],
        "source_text": (
            "Habitable environment = an environment capable of hosting life; discussed for life chemically similar to Earth's "
            "(life 'as we don't know it' is speculative). Requirements: a solvent for building biomolecules and their "
            "interactions -- for us, liquid water (abundant in the universe but must be liquid, only in a certain range of "
            "temperature AND pressure). 'Follow the water' drives exploration in and beyond the solar system. Biochemistry uses "
            "carbon, hydrogen, nitrogen, oxygen, phosphorus, sulfur (CHNOPS); carbon at the core of organic chemistry -- forms "
            "four bonds with itself and other elements -> vast numbers of molecules. Life also needs energy (sunlight or "
            "chemical) and raw materials ('habitable' on Mars = water + energy + elemental raw materials).\n"
            "Habitable zone (HZ): region around a star where liquid water could exist on a planet's surface. In our system Venus "
            "is far above water's boiling point, Mars almost always below freezing, Earth 'just right'. Surface temperature "
            "depends on the radiation budget: how much starlight is absorbed and retained, and how winds and ocean circulation "
            "distribute it. Starlight received depends on the star's output (amount and type) and distance, how much the planet "
            "reflects, and greenhouse retention. Inverse-square law: illumination per square meter falls with distance squared: "
            "2x distance -> 1/4 (2^2); 10x -> 1/100. Venus (0.72 of Earth's distance) receives 1/(0.72)^2 = 1.92 (~2x) and Mars "
            "(1.52) 1/(1.52)^2 = 0.43 (~half) the light per square meter. But Venus' clouds reflect ~2x as much as Earth; Mars "
            "reflects ~half as much -> all three absorb comparable sunlight energy. The difference: greenhouse gases trap the "
            "infrared that planets radiate: Earth's natural greenhouse (mostly water vapor and CO2) raises the average ~33 C; Mars' "
            "thin air ~2 C; Venus' massive CO2 atmosphere ~510 C. These worlds are much colder/hotter than Earth would be in their "
            "orbits -> habitability depends on atmosphere AND distance.\n"
            "Stars vary: hotter/bluer and dimmer/redder; HZ distance varies. M-dwarf HZ is 3-30x closer than for G-type (Sun-like) "
            "stars; M dwarfs are by far the most numerous and long-lived stars, with some downsides for life. Sun-like stars "
            "brighten over their main-sequence lives -> HZ migrates outward; the Sun's output rose at least 30% over 4 billion "
            "years: Venus was once in the HZ, and early Earth received too little energy to stay unfrozen with today's atmosphere, "
            "yet geology shows liquid water billions of years ago. Continuously habitable zone = orbits that stay in the HZ for "
            "the star's whole lifetime -- much narrower. Proxima Centauri (nearest star, M type, 4.2 light-years): planet of at "
            "least 1.3 Earth masses (reported 2016), orbit ~11 days at 0.05 AU, maybe in the HZ; habitability debated. Being in "
            "the HZ is no guarantee: Venus today has virtually no water. Nearly 300 confirmed/candidate exoplanets orbit in HZs and "
            ">10% of those are roughly Earth-size; >40% of stars may have at least one Earth-size HZ planet. Several dozen possibly "
            "habitable exoplanets; most Sun-like stars host at least one planet; multi-planet systems not unusual.\n"
            "21.6: only a few candidates resemble Earth; unclear what defines 'another Earth' -- exact size probably unimportant "
            "(life could have arisen on a slightly smaller or larger Earth). Habitability depends on distance AND atmosphere "
            "(greenhouse, as with Venus and increasingly Earth). Questions: must an Earth twin orbit a Sun-like star or could K- "
            "and M-class stars work? HZ location consistent with surface liquid water is probably the most important "
            "characteristic of an Earth analog. New instruments may look for signs of life (atmospheric gases); space telescopes "
            "take years to plan, build and launch."
        ),
        "story": (
            "WHAT DOES 'HABITABLE' MEAN?\n\n"
            "A HABITABLE environment is one that could host life. We focus on life chemically like ours, since alien chemistries "
            "('life as we don't know it') are still pure guesswork. So what does our kind of life need?\n\n"
            "INGREDIENT 1: LIQUID WATER\n"
            "Life needs a SOLVENT -- a liquid where chemicals dissolve, meet and react to build the molecules of life. For us, "
            "that's water. Water is common in the universe, but it has to be LIQUID, which only happens within a certain range of "
            "temperatures AND pressures (too hot or too cold, too high or too low pressure, and it becomes ice or vapor -- think "
            "of Mars, where low pressure turns ice straight into gas). That's why the motto of exploration is 'FOLLOW THE WATER'.\n\n"
            "INGREDIENT 2: THE RIGHT ELEMENTS\n"
            "Our biochemistry is built mainly from six elements: carbon, hydrogen, nitrogen, oxygen, phosphorus and sulfur "
            "(remember 'CHNOPS'). Carbon is the superstar: it can form four bonds, both with itself and with the others, so it "
            "can build an almost endless variety of big molecules.\n\n"
            "INGREDIENT 3: ENERGY\n"
            "Life needs a power source: sunlight (photosynthesis) or chemical energy (like the vent communities on Earth's dark "
            "seafloor, or maybe Europa's ocean). When Curiosity proved ancient Mars was 'habitable', it meant water AND energy "
            "AND raw materials were all there.\n\n"
            "THE HABITABLE ZONE\n\n"
            "The HABITABLE ZONE is the range of distances from a star where a planet's surface could hold liquid water. In our "
            "solar system, Venus is far too hot (way above boiling), Mars is almost always below freezing, and Earth is 'just "
            "right' -- the Goldilocks planet.\n\n"
            "But distance isn't the whole story. A planet's temperature depends on its RADIATION BUDGET:\n"
            "• how much and what kind of light its star gives off,\n"
            "• how far it is from the star,\n"
            "• how much light it reflects back to space,\n"
            "• how well its atmosphere traps heat (the greenhouse effect),\n"
            "• and how winds and oceans spread heat around.\n\n"
            "THE INVERSE-SQUARE LAW\n"
            "Starlight spreads out as it travels, so the light hitting each square meter drops with the SQUARE of the distance. "
            "Twice as far gets 1/4 the light (2 squared = 4); ten times as far gets 1/100. Venus, at 0.72 of Earth's distance, gets "
            "1/(0.72)^2 = 1.92 -- about twice our sunlight per square meter. Mars, at 1.52, gets 1/(1.52)^2 = 0.43 -- about half.\n\n"
            "Here's a twist: Venus' bright clouds reflect about twice as much light as Earth does, and Mars reflects only about "
            "half as much. So all three planets actually ABSORB about the same amount of solar energy! Then why are they so "
            "different? Their atmospheres:\n"
            "• EARTH: water vapor and CO2 give about 33 C of greenhouse warming -- enough to keep the oceans liquid.\n"
            "• MARS: thin air, only about 2 C of warming.\n"
            "• VENUS: a massive CO2 atmosphere, about 510 C of warming!\n"
            "So Mars is much colder, and Venus much hotter, than Earth would be in their orbits. To judge habitability you need to "
            "know the atmosphere AND the distance.\n\n"
            "DIFFERENT STARS, DIFFERENT ZONES\n"
            "Stars vary a lot. Hot, bright, bluish stars have habitable zones far out; dim, cool, reddish stars have them close "
            "in. Around RED DWARFS (M-dwarf stars), the habitable zone is 3 to 30 times closer than around Sun-like (G-type) stars. "
            "Red dwarfs are by far the most common and longest-lived stars in the Galaxy, so their planets matter -- though they "
            "have some downsides for life.\n\n"
            "Example: PROXIMA CENTAURI, the nearest star (an M dwarf 4.2 light-years away), has a planet with at least 1.3 Earth "
            "masses (announced in 2016). It orbits in about 11 days at just 0.05 AU, which may put it in its star's habitable "
            "zone -- but whether it's actually friendly to life is hotly debated.\n\n"
            "ZONES ON THE MOVE\n"
            "Stars like the Sun slowly brighten during their lives, so their habitable zones creep outward. The Sun is at least 30% "
            "brighter than 4 billion years ago. That means Venus was once inside the habitable zone, and young Earth got too little "
            "sunlight to stay unfrozen with today's atmosphere -- yet rocks prove Earth had liquid water billions of years ago (a "
            "thicker greenhouse blanket probably helped). The CONTINUOUSLY HABITABLE ZONE is the range of orbits that stay in the "
            "habitable zone for the star's whole life -- much narrower than the zone at any one time.\n\n"
            "IN THE ZONE ISN'T ENOUGH\n"
            "Being in the habitable zone is no guarantee. Venus today has almost no water, so even if we moved it to a 'just right' "
            "orbit, it still couldn't support life like ours.\n\n"
            "HOW MANY 'EARTHS' ARE OUT THERE?\n"
            "• Nearly 300 known planets and candidates orbit in their stars' habitable zones, and more than 10% of those are roughly "
            "Earth-size.\n"
            "• More than 40% of stars may have at least one Earth-size planet in their habitable zone.\n"
            "• Most Sun-like stars host at least one planet, and multi-planet systems are common.\n"
            "Still, only a few candidates truly resemble Earth. Does an Earth twin need exactly Earth's size? Probably not -- life "
            "could likely have started on a slightly bigger or smaller Earth. Does it need a Sun-like star, or could K- and M-type "
            "stars work? We don't know yet. Most astronomers think the single most important feature of an 'Earth analog' is "
            "orbiting in the habitable zone where surface liquid water is possible. New telescopes may soon examine these planets' "
            "atmospheres for gases made by life -- though space telescopes take years to plan, build and launch."
        ),
        "concepts": [
            {
                "term": "Habitable environment",
                "badge": ("W+E+R", "needs", GREEN),
                "analogy": "A habitable place is like a working kitchen: you need water, ingredients, and a way to turn on the stove.",
                "explanation": "A habitable environment is one capable of hosting life. Scientists focus on life chemically similar to Earth's, since alternative biochemistries ('life as we don't know it') are completely speculative. Requirements: a liquid solvent (water) in which biomolecules form and interact; the elements of life (CHNOPS, with carbon at the core); and energy (sunlight or chemical). On Mars, Curiosity showed 'habitable' meant not only liquid water but that life's needs for energy and elemental raw materials could have been met. Understanding habitability tells us how widespread life might be and where to search.",
                "why": "The core definition for the entire 2027 habitability theme.",
            },
            {
                "term": "Liquid water as the solvent",
                "badge": ("H₂O", "liquid!", BLUE),
                "analogy": "Water is life's mixing bowl -- ingredients can only react if they can swim around and meet.",
                "explanation": "Life requires a solvent (a liquid in which chemicals dissolve) that enables building biomolecules and the interactions between them. For life as we know it, that solvent is water, whose properties are critical to our biochemistry. Water is abundant in the universe, but it must be liquid (not ice or gas), which happens only within a certain range of temperatures and pressures -- too high or too low in either and water becomes solid or gas. Identifying environments with water in the right temperature and pressure range is the first step; 'follow the water' drives exploration of planets in and beyond the solar system.",
                "why": "Temperature AND pressure both matter -- e.g. Mars' 0.006 bar limit.",
            },
            {
                "term": "CHNOPS and carbon",
                "badge": ("CHNOPS", "elements", GREEN),
                "analogy": "Carbon is the LEGO brick with four connectors, so it can build almost anything.",
                "explanation": "Our biochemistry is based on molecules made of carbon, hydrogen, nitrogen, oxygen, phosphorus and sulfur. Carbon is at the core of organic chemistry: it can form four bonds, both with itself and with the other elements of life, allowing an enormous number of possible molecules. Organic molecules contain carbon; hydrocarbons (only hydrogen and carbon) are the basis of biochemistry. Amino acids (building blocks of proteins) and sugars have been found in meteorites.",
                "why": "Know the six elements and why carbon is special.",
            },
            {
                "term": "Habitable zone",
                "badge": ("HZ", "Goldilocks", GREEN),
                "analogy": "Sitting around a campfire: too close you roast, too far you freeze, in between is just right.",
                "explanation": "A habitable zone is the range of distances from a star in which water could be present in liquid form on a planet's surface. In our solar system Venus' surface is far above water's boiling point and Mars' is almost always below freezing; Earth, between them, is 'just right'. Whether a surface can keep liquid water depends on the radiation budget -- how much starlight a planet absorbs and retains -- and how winds and ocean circulation distribute it. Starlight received depends on how much and what sort of light the star emits and on distance; also important are how much the planet reflects and how well its atmosphere retains heat (greenhouse effect). Kepler-62's HZ is smaller and closer because its star is fainter.",
                "why": "THE most important concept for 'habitability beyond the Solar System'.",
            },
            {
                "term": "Inverse-square law",
                "badge": ("1/d²", "light", GOLD),
                "analogy": "Spray paint from twice as far spreads over 4 times the area, so each spot gets 1/4 the paint.",
                "explanation": "The starlight received per unit area of a planet's surface decreases with the square of the distance from the star: double the distance and illumination drops by 4 (2^2); ten times the distance and it drops by 100 (10^2). Venus and Mars orbit at about 72% and 152% of Earth's distance, so Venus receives 1/(0.72)^2 = 1.92 (about twice) and Mars 1/(1.52)^2 = 0.43 (about half) as much light per square meter as Earth.",
                "why": "A go-to calculation: practice computing relative sunlight at any distance.",
            },
            {
                "term": "Same sunlight, different worlds",
                "badge": ("2/33/510", "°C", RED),
                "analogy": "Three people get the same paycheck, but one saves almost nothing (Mars), one saves sensibly (Earth), and one hoards it all (Venus).",
                "explanation": "Venus receives ~2x Earth's sunlight but its clouds reflect ~2x as much; Mars receives ~half but reflects ~half as much. So all three absorb comparable amounts of solar energy. The difference is the greenhouse effect: some atmospheric gases trap the infrared that planets radiate. Earth's natural greenhouse (mostly water vapor and CO2) raises the average surface temperature by ~33 C; Mars' thin atmosphere gives ~2 C; Venus' massive CO2 atmosphere gives ~510 C. These worlds are much colder and hotter than Earth would be in their orbits, so evaluating habitability requires knowing the atmosphere as well as the distance.",
                "why": "Explains why HZ edges are fuzzy and depend on atmospheres.",
            },
            {
                "term": "Habitable zones around different stars",
                "badge": ("M", "3-30x closer", "#ff6b4a"),
                "analogy": "A small candle's warm circle is tiny; a bonfire's warm circle is huge.",
                "explanation": "Stars vary widely in intensity and spectrum: some are brighter and hotter (bluer), others dimmer and cooler (redder), and the HZ distance varies accordingly. The habitable zone around M-dwarf stars is 3 to 30 times closer in than for G-type (Sun-like) stars. M dwarfs are by far the most numerous and long-lived stars in our Galaxy, so there is great interest in whether their planets could be habitable, although they have some potential downsides for supporting life. Open question: must an Earth twin orbit a Sun-like star, or are K- and M-class stars' planets candidates too?",
                "why": "Most nearby 'habitable zone' planets orbit red dwarfs -- expect questions on them.",
            },
            {
                "term": "Proxima Centauri's planet",
                "badge": ("4.2", "light-yrs", "#ff6b4a"),
                "analogy": "Our nearest neighbor star has a planet huddled close to it like someone warming hands on a tiny heater.",
                "explanation": "Proxima Centauri, the nearest star to the Sun (spectral type M, 4.2 light-years away), has a planet of at least 1.3 Earth masses, reported in summer 2016 (found with the Doppler method). It orbits in about 11 days at about 0.05 AU, which may place it in its star's habitable zone, but whether conditions on such a planet near such a star are hospitable to life is a matter of great scientific debate.",
                "why": "The nearest potentially habitable exoplanet -- a classic test fact.",
            },
            {
                "term": "Migrating and continuously habitable zones",
                "badge": ("+30%", "brighter Sun", SUN),
                "analogy": "As a campfire grows over the evening, the comfy spot keeps moving farther away.",
                "explanation": "Stars like the Sun increase in luminosity over their main-sequence lifetimes, so the habitable zone migrates outward as a system ages. The Sun's power output has increased by at least 30% over the past 4 billion years: Venus was once within the habitable zone, and early Earth received too little solar energy to keep the modern Earth (with today's atmosphere) from freezing -- yet geology shows liquid water was present billions of years ago. The continuously habitable zone is the range of orbits that stay within the habitable zone during the star's entire lifetime; it is much narrower than the habitable zone at any one time.",
                "why": "Explains the 'faint young Sun' puzzle and long-term habitability.",
            },
            {
                "term": "In the zone isn't a guarantee",
                "badge": ("HZ ≠", "habitable", RED),
                "analogy": "Owning a house in a nice neighborhood doesn't help if the house has no plumbing.",
                "explanation": "Even when planets orbit within their star's habitable zone, they aren't guaranteed to be habitable. Venus today has virtually no water, so even if suddenly moved to a 'just right' orbit, a critical requirement for life would still be missing. Habitability depends on distance AND the nature of the atmosphere (greenhouse effect), and on actually having water. Scientists study all factors defining the HZ and the habitability of planets within it, because this guides which exoplanets to search for life.",
                "why": "A common trick question: HZ means 'could have liquid water', not 'has life'.",
            },
            {
                "term": "Tidal locking and habitability",
                "badge": ("DAY", "/ night", ICE),
                "analogy": "A tidally locked planet is like a marshmallow on a stick that never gets turned -- one side toasts, the other stays cold.",
                "explanation": "Planets in close orbits -- like those in the habitable zones of dim M-dwarf stars, which are 3-30 times closer than the Sun's -- are often tidally locked: one side always faces the star. That gives a permanent day side and a permanent night side, which strongly affects climate and where liquid water could last. A thick atmosphere and oceans that carry heat around the planet (winds and currents redistribute energy) could keep such a world habitable, maybe in a ring of 'twilight' between day and night. This is one of the open questions about planets like the one around Proxima Centauri (11-day orbit at 0.05 AU).",
                "why": "Most nearby habitable-zone candidates orbit red dwarfs -- tidal locking is a key debate.",
            },
            {
                "term": "Earth-like exoplanet statistics",
                "badge": ("~300", "in HZ", GREEN),
                "analogy": "We've found hundreds of 'apartments' in the right neighborhood -- now we need to check if anyone lives there.",
                "explanation": "Of confirmed or candidate exoplanets known at the time of writing, nearly 300 are considered to orbit within their star's habitable zone, and more than 10% of those are roughly Earth-size. Current estimates suggest more than 40% of stars have at least one Earth-size planet in the habitable zone. The majority of Sun-like stars appear to host at least one planet, and several dozen possibly habitable exoplanets are known. Still, only a few candidates closely resemble Earth. Exact Earth size may not matter for habitability; orbiting in the HZ where surface liquid water is possible is probably the most important characteristic of an Earth analog.",
                "why": "Numbers that show habitable worlds are likely common.",
            },
        ],
    },
    # ------------------------------------------------------------------ 14
    {
        "name": "Solar System: Astrobiology -- Searching for Life",
        "description": "Chemical evolution and the Copernican principle, the Fermi paradox, life's building blocks in space, Miller-Urey and hydrothermal vents, the RNA world, photosynthesis and oxygen, and biomarkers for spotting life on exoplanets.",
        "source_title": "Source reader: Life in the Universe (OpenStax Astronomy 2e, 30.1-30.3)",
        "infographics": ["biomarkers"],
        "source_text": (
            "Cosmic context: Big Bang ~14 billion years ago; first atoms hydrogen and helium (tiny lithium); stars made other "
            "elements (iron, silicon, magnesium, oxygen; carbon, oxygen, nitrogen for life) -> compounds in space. Life on Earth "
            "is based on organic molecules (contain carbon), especially hydrocarbons (only H and C) -> biochemistry; 'chemical "
            "evolution of the universe'. ~5 billion years ago a gas and dust cloud collapsed into the Sun, planets, comets; the "
            "third planet cooled and gathered liquid water. Comets (e.g. Hyakutake, 1996) can deliver water and organic chemicals. "
            "Molecules that copy themselves (reproduce) are essential for beginning life. Evolution was punctuated by impacts "
            "(dinosaur extinction 65 million years ago). Humans are made of atoms forged in earlier stars -- 'the universe "
            "becomes aware of itself'; atoms are on loan from the 'lending library' of the cosmos.\n"
            "Copernican principle: nothing special about our place (Galileo: Earth not the center; Sun an ordinary star halfway "
            "through its main-sequence life; nothing special about our place in the Galaxy). Planet formation is a natural "
            "consequence of star formation; thousands of exoplanets; likely billions of 'exo-Earths' in the Milky Way. Most "
            "scientists would be surprised if life were limited to Earth. Real question: is organic biochemistry likely or "
            "unlikely in the universe? Finding even 'unrelated to us' life on a world like Europa would help answer it.\n"
            "Fermi paradox (Enrico Fermi): if life and intelligence are common and could spread, where are they? Proposed "
            "solutions: life common but intelligence/technology rare; network hasn't developed yet; we can't detect their "
            "signals; advanced species don't interfere with young civilizations; civilizations self-destruct.\n"
            "Astrobiology (also exobiology, bioastronomy): multidisciplinary study of origin, evolution, distribution and fate of "
            "life in the universe (astronomers, planetary scientists, chemists, geologists, biologists). Building blocks: no "
            "unambiguous evidence of life beyond Earth yet, but meteorites contain extraterrestrial amino acids (building blocks "
            "of proteins, which provide structure/function and do the cell's work) and sugars; comets' gas and dust contain "
            "organic molecules; radio astronomy found >100 molecules in interstellar clouds (formaldehyde, alcohol...), most in "
            "dusty regions where stars and planets form (e.g. cloud in Scorpius eaten by the Scorpius OB Association).\n"
            "Miller-Urey experiments (Stanley Miller and Harold Urey, University of Chicago, early 1950s onward): simulated early "
            "Earth and produced building blocks of proteins and nucleic acids. Problem: best results need reducing gases (ammonia, "
            "methane), but early atmosphere was probably CO2-dominated. Hydrothermal vents (seawater superheated and circulated "
            "through crustal/mantle rock) could supply organics without a reducing atmosphere. Both Earth and space sources may "
            "have contributed (more direct evidence for space). Life might even have been seeded from elsewhere (doesn't solve "
            "origin).\n"
            "Origin: genes contain millions of units in precise sequence; even primitive life needs a way to extract energy and "
            "to encode and replicate information. Little direct evidence of earliest Earth (plate tectonics resurfacing). Heavy "
            "bombardment 3.8-4.1 billion years ago could heat-sterilize the surface. Fossil microbes in 3.5-billion-year-old rocks; "
            "possible (debated) life at 3.8 billion years. Proteins do the chemical work; DNA (deoxyribonucleic acid) stores "
            "information -- a 'chicken and egg problem' since each needs the other; RNA (ribonucleic acid) might do both -> 'RNA "
            "world' increasingly accepted.\n"
            "Photosynthesis: most important innovation after life's origin -- sunlight makes energy-storing products "
            "(carbohydrates), releasing oxygen; supports a larger biosphere. Oxygen rose ~2.4 billion years ago, so oxygenic "
            "photosynthesis was globally important by then (likely earlier). Stromatolites ~3.5 billion years (earliest 3.47, "
            "Western Australia; modern Lake Thetis); simpler non-oxygen photosynthesis probably came first; photosynthesis at least "
            "3.4 billion years ago. Oxygen -> ozone layer -> UV protection -> life on land. Oxygen was deadly to some microbes "
            "(reactive, damages biomolecules) but a boon to others: combining oxygen with organic matter releases lots of energy "
            "(like a burning log). Evolution by natural selection explains diversity but not life's beginning. Hypothesis that "
            "life arises whenever conditions allow = another form of the Copernican principle; finding a second example nearby "
            "would imply the universe is filled with biology.\n"
            "Biomarkers (30.3): need robust biospheres able to make planet-scale change detectable by telescopes. Earth is the "
            "only solar-system body where atmosphere composition and reflected light differ from no-life expectations; subsurface "
            "life (Mars, icy moons) unlikely to be telescopically detectable. Earth's photosynthetic biosphere needs surface liquid "
            "water and sunlight -- hence the HZ focus on surface water. Plants make Earth look greener in visible light and "
            "reflect more near-infrared; photosynthesis made >20% of our atmosphere oxygen -- very hard to explain without life. "
            "Nitrous oxide and methane found together with oxygen also suggested as signs of life; detectable through effects on "
            "a planet's spectrum (atmosphere spectra of some exoplanets now measurable). Search should focus on roughly Earth-size "
            "HZ planets with gases or colors hard to explain without biology -- many challenges. Pale Blue Dot: Voyager 1 image "
            "of Earth from 4 billion miles (~6 billion km), less than a pixel."
        ),
        "story": (
            "WE ARE MADE OF STAR STUFF\n\n"
            "The universe began with the Big Bang about 14 billion years ago. When it cooled enough for atoms, there was only "
            "hydrogen and helium (plus a pinch of lithium). Every other element -- the iron, silicon, magnesium and oxygen in "
            "Earth, and the carbon, nitrogen and oxygen in YOU -- was forged later inside stars. These elements combined in space "
            "into many compounds, including ORGANIC MOLECULES (molecules with carbon), and especially HYDROCARBONS (only hydrogen "
            "and carbon), the basis of our biochemistry. This long process is called the CHEMICAL EVOLUTION of the universe.\n\n"
            "About 5 billion years ago a cloud collapsed into the Sun, its planets and comets. The third planet cooled enough to "
            "collect liquid water. Comets like Hyakutake (seen in 1996) can deliver water and organic chemicals. Eventually "
            "molecules formed that could COPY THEMSELVES -- the essential first step for life. Billions of years of evolution "
            "followed, sometimes reset by big impacts (like the one that ended the dinosaurs 65 million years ago), producing a "
            "creature that can wonder about its own origins. Your atoms are 'on loan' from the universe's lending library: they "
            "were made in earlier generations of stars, and through you, the universe becomes aware of itself.\n\n"
            "THE COPERNICAN PRINCIPLE\n"
            "Every time humans claimed Earth was special, we turned out to be wrong. Galileo showed Earth isn't the center of the "
            "solar system. The Sun is an ordinary star, halfway through its life like billions of others. Our spot in the Milky "
            "Way isn't special either. Planets form naturally whenever stars form, and there are probably billions of Earth-size "
            "'exo-Earths' in our Galaxy. The idea that there's nothing special about our place is called the COPERNICAN "
            "PRINCIPLE. Applied to life, it suggests life probably exists elsewhere -- most scientists would be surprised if it "
            "didn't. The real open question: is organic biochemistry a lucky rarity, or a normal part of the universe's chemistry? "
            "Finding even one example of life unrelated to us -- say, on Europa -- would help answer it.\n\n"
            "THE FERMI PARADOX: 'WHERE IS EVERYBODY?'\n"
            "If life and intelligence are common, older civilizations around older stars may have had a billion-year head start "
            "and could have spread probes or messages across the Galaxy. Physicist Enrico Fermi asked: then where are they? "
            "Possible answers: life is common but intelligence (or technology) is rare; a galactic network hasn't had time to "
            "form yet; their signals are all around us but we can't detect them; advanced species deliberately leave young "
            "civilizations like ours alone; or civilizations tend to destroy themselves. Nobody knows!\n\n"
            "ASTROBIOLOGY\n"
            "ASTROBIOLOGY (also called exobiology or bioastronomy) is the science of life's origin, evolution, distribution and "
            "future in the universe. Astronomers, planetary scientists, chemists, geologists and biologists work on it together.\n\n"
            "LIFE'S INGREDIENTS ARE EVERYWHERE\n"
            "We haven't found clear evidence of life beyond Earth yet, but its building blocks are all over space:\n"
            "• METEORITES contain AMINO ACIDS (the building blocks of proteins, which build our tissues and do the cell's work) "
            "and SUGARS that clearly came from space.\n"
            "• COMETS' gas and dust contain organic molecules.\n"
            "• Radio astronomers have found more than 100 kinds of molecules in giant gas-and-dust clouds between stars -- including "
            "formaldehyde and alcohol -- mostly in the dusty regions where new stars and planets form.\n\n"
            "MAKING LIFE'S BUILDING BLOCKS IN A LAB\n"
            "Starting in the early 1950s, STANLEY MILLER and HAROLD UREY at the University of Chicago zapped mixtures of gases "
            "meant to imitate early Earth and produced building blocks of proteins and nucleic acids. The catch: their best "
            "results needed hydrogen-rich ('reducing') gases like ammonia and methane, but early Earth's air was probably mostly "
            "CO2, like Venus and Mars today. Another candidate kitchen: HYDROTHERMAL VENTS, where seawater gets superheated as it "
            "circulates through hot rock on the seafloor -- they could make organic compounds without needing a special "
            "atmosphere. Probably both Earth and space contributed organics (we have more direct evidence for space). Life might "
            "even have been seeded from elsewhere -- but that just moves the question of how it started.\n\n"
            "FROM CHEMISTRY TO BIOLOGY\n"
            "Even the simplest life needs two abilities: a way to get ENERGY from its surroundings, and a way to STORE "
            "INFORMATION and copy itself. In modern cells, PROTEINS do the chemical work and DNA stores the instructions. But "
            "proteins are needed to build DNA, and DNA is needed to build proteins -- a chicken-and-egg problem! One solution: "
            "RNA, a molecule that can both store information and do some chemical work. Many scientists now favor an early 'RNA "
            "WORLD'.\n\n"
            "Earth's earliest days left few clues because plate tectonics recycled the oldest rocks. During the heavy bombardment "
            "(3.8-4.1 billion years ago), giant impacts could have sterilized the surface. Once things calmed down, there's fossil "
            "evidence of microbes in 3.5-billion-year-old rocks, and possible (debated) signs back to 3.8 billion years.\n\n"
            "PHOTOSYNTHESIS CHANGES EVERYTHING\n"
            "Besides the origin of life itself, the biggest innovation in biology was PHOTOSYNTHESIS: using sunlight to make "
            "energy-storing products like carbohydrates, releasing oxygen as a by-product. Sunlight is a huge energy supply, so "
            "it supported a much bigger biosphere. Stromatolites -- layered rocks built by microbe mats reaching for sunlight -- "
            "date back almost 3.5 billion years (the oldest, 3.47 billion years, is in Western Australia; living ones still grow "
            "in Lake Thetis). A simpler kind of photosynthesis that doesn't make oxygen probably came first, and one kind or the "
            "other was working by at least 3.4 billion years ago. Oxygen began piling up in the air about 2.4 billion years ago, "
            "which built the OZONE LAYER and let life move onto land. Oxygen was poison to some microbes (it damages delicate "
            "molecules) but a jackpot for others: combining oxygen with food releases tons of energy, like a burning log. Evolution "
            "by natural selection then built life's amazing variety.\n\n"
            "If life arises whenever conditions are right (the Copernican principle again), then finding a second example nearby "
            "would mean the universe is probably full of life.\n\n"
            "HOW COULD WE SPOT LIFE LIGHT-YEARS AWAY? BIOMARKERS\n"
            "We can't send probes to other stars, so we must read the LIGHT from distant planets. From 6 billion km away, Voyager 1 "
            "saw Earth as the 'PALE BLUE DOT' -- less than one pixel. Could that speck reveal life?\n"
            "• We need a BIOSPHERE big enough to change a whole planet. Earth is the only world in our solar system where life "
            "changes the atmosphere and reflected light in telescope-visible ways. Life hidden under Mars' surface or under icy "
            "moons' crusts probably couldn't be seen from far away.\n"
            "• Earth's photosynthetic life needs SURFACE water and sunlight -- that's why the habitable-zone search focuses on "
            "surface liquid water.\n"
            "• OXYGEN: more than 20% of our air is oxygen made by photosynthesis -- very hard to explain without life.\n"
            "• GAS COMBINATIONS: methane or nitrous oxide found TOGETHER with oxygen are strong hints of biology.\n"
            "• COLOR: plants make Earth look greener in visible light and reflect extra near-infrared light.\n"
            "• We can now measure the atmospheric spectra of some exoplanets (for example during transits).\n"
            "So the plan: find roughly Earth-size planets in habitable zones and look for gases or colors that are hard to explain "
            "without life. Simple? Not at all -- but it's one of the greatest searches humans have ever attempted."
        ),
        "concepts": [
            {
                "term": "Chemical evolution of the universe",
                "badge": ("STARS", "made us", SUN),
                "analogy": "Stars are cosmic kitchens that cooked up every ingredient in your body except hydrogen.",
                "explanation": "After the Big Bang (~14 billion years ago), matter was hydrogen and helium with a tiny bit of lithium. Processes inside stars created other elements -- those making up Earth (iron, silicon, magnesium, oxygen) and those required for life (carbon, oxygen, nitrogen). These combined in space into many compounds. Life on Earth is based on organic molecules (containing carbon), especially hydrocarbons (only hydrogen and carbon), the basis of biochemistry. The sequence of events leading to creatures like us is the chemical evolution of the universe. Our atoms were forged in earlier generations of stars and are 'on loan' from the cosmos.",
                "why": "Explains where life's ingredients came from.",
            },
            {
                "term": "Copernican principle",
                "badge": ("NOT", "special", BLUE),
                "analogy": "Like realizing your town is one of millions of towns -- so other towns probably have kids like you too.",
                "explanation": "We have always been wrong when claiming Earth is unique: Galileo showed Earth is not the center of the solar system; the Sun is an undistinguished star halfway through its main-sequence life; nothing is special about our position in the Galaxy. Planet formation is a natural consequence of star formation, and earthlike planets seem frequent enough for many billions of 'exo-Earths' in the Milky Way. The idea that there's nothing special about our place in the universe is the Copernican principle; applied to life, most scientists would be surprised if life were limited to Earth. The real unknown: is organic biochemistry likely or rare? Even one example of life 'unrelated to us' (e.g. on Europa) would help answer it.",
                "why": "Frequently asked in astrobiology essay questions.",
            },
            {
                "term": "Fermi paradox",
                "badge": ("WHERE?", "are they", PURPLE),
                "analogy": "If the Galaxy is a huge party with lots of guests, why is our corner so quiet?",
                "explanation": "If the Copernican principle applies to life, intelligent life might be common, and civilizations around older stars could have had a billion-year head start to develop technology like sending information, probes or even life between stars. Physicist Enrico Fermi asked: where are they? Proposed solutions: life is common but intelligence (or technological civilization) is rare; a galactic network will come about but hasn't had time yet; streams of data flow past us that we can't detect; advanced species don't interfere with immature civilizations; or civilizations self-destruct after reaching a certain technology level. We don't yet know.",
                "why": "A classic 'list possible explanations' question.",
            },
            {
                "term": "Astrobiology",
                "badge": ("ASTRO", "+ BIO", GREEN),
                "analogy": "Astrobiology is a team sport where astronomers, chemists, geologists and biologists all play together.",
                "explanation": "The multidisciplinary study of the origin, evolution, distribution and ultimate fate of life in the universe; also called exobiology or bioastronomy. It brings together astronomers, planetary scientists, chemists, geologists and biologists. Astrobiologists study the conditions under which life arose on Earth, why life on Earth is so adaptable, which worlds beyond Earth are habitable, and how to look for life there in practice.",
                "why": "The field the 2027 habitability theme belongs to.",
            },
            {
                "term": "Building blocks in space",
                "badge": ("100+", "molecules", ICE),
                "analogy": "Space is like a giant pantry already stocked with life's basic ingredients.",
                "explanation": "No unambiguous evidence of life beyond Earth has been found, but life's chemical building blocks have been detected widely. Meteorites contain amino acids (molecular building blocks of proteins, which provide the structure and function of tissues and do the cell's work) and sugars whose structures mark them as extraterrestrial. Gas and dust around comets contain organic molecules. Radio astronomy has identified more than 100 molecules in giant interstellar gas-and-dust clouds, including formaldehyde and alcohol, found most readily where dust is abundant -- exactly where stars and planets form (e.g. the Scorpius cloud shaped by the Scorpius OB Association).",
                "why": "Organics are common -- so the ingredients for life are likely everywhere.",
            },
            {
                "term": "Miller-Urey experiments",
                "badge": ("1950s", "lab life", GOLD),
                "analogy": "Miller and Urey tried to make 'primordial soup' in a jar with lightning sparks.",
                "explanation": "Since the early 1950s, experiments pioneered by Stanley Miller and Harold Urey at the University of Chicago simulated early-Earth conditions and produced fundamental building blocks of life, including those of proteins and of nucleic acids. Problem: the most interesting chemistry uses hydrogen-rich (reducing) gases like ammonia and methane, but Earth's early atmosphere was probably dominated by CO2 (like Venus and Mars today) and may not have had enough reducing gases. Sagan also simulated early-Earth 'primordial soup' chemistry.",
                "why": "A famous experiment -- know its result AND its limitation.",
            },
            {
                "term": "Hydrothermal vents",
                "badge": ("VENTS", "deep sea", RED),
                "analogy": "Underwater hot springs are like natural pressure cookers making life's chemicals.",
                "explanation": "Hydrothermal vents are seafloor systems where ocean water is superheated and circulated through crustal or mantle rocks before re-emerging into the ocean. They are suggested as contributors of organic compounds on early Earth and would not require a reducing early atmosphere. Today, entire ecosystems cluster around deep-ocean hot springs, deriving energy from mineral-laden water independent of sunlight -- a model for possible life in Europa's or Enceladus' oceans. Both earthly and extraterrestrial sources probably contributed organics (more direct evidence exists for extraterrestrial); life might even have been seeded from elsewhere, which doesn't solve how it began.",
                "why": "Connects Earth's origin of life to ocean-world habitability.",
            },
            {
                "term": "DNA, proteins and the RNA world",
                "badge": ("RNA", "first?", PURPLE),
                "analogy": "Chicken or egg? Proteins build DNA, DNA codes proteins -- RNA may be the 'egg' that does both jobs.",
                "explanation": "Even the simplest genes contain millions of molecular units in precise sequence. Primitive life needed two capabilities: a means of extracting energy from its environment and a means of encoding and replicating information to copy itself. Modern life uses proteins (the functional molecules doing the cell's chemical work) and DNA (deoxyribonucleic acid, storing information). Neither works without the other -- a 'chicken and egg problem'. RNA (ribonucleic acid), which helps genetic information flow from DNA to proteins, can both store information and do chemical work, so an early 'RNA world' has become increasingly accepted, though much remains unknown.",
                "why": "Explains a key open question in the origin of life.",
            },
            {
                "term": "Biomarkers (biosignatures)",
                "badge": ("O₂+CH₄", "signs", GREEN),
                "analogy": "Like smelling cookies from outside a house -- you can't see the baker, but you know someone's baking.",
                "explanation": "With no way to send probes, we must detect life from light. We need robust biospheres able to create planet-scale changes that are telescopically observable and clearly biological. Earth is the only solar-system body where life does this; subsurface life on Mars or icy moons is very unlikely to be detectable from afar. Earth's photosynthetic biosphere (requiring surface liquid water and sunlight) makes our planet greener in visible light and more reflective in near-infrared, and has made more than 20% of our atmosphere oxygen -- very difficult to explain without life. Nitrous oxide and methane found simultaneously with oxygen are also suggested indicators. Sufficiently abundant gases change a planet's spectrum, which can now be measured for some exoplanets.",
                "why": "How we'll actually search for life beyond the Solar System -- a must-know for 2027.",
            },
            {
                "term": "Pale Blue Dot and the search strategy",
                "badge": ("1 px", "Earth", BLUE),
                "analogy": "Finding life on an exoplanet is like reading a whole book from a single glowing dot.",
                "explanation": "Voyager 1 imaged Earth from about 4 billion miles (~6 billion km) away as a 'pale blue dot' -- less than a pixel of light. Searching for exoplanet life depends on extracting information from such faint light. Astronomers conclude the initial search should focus on exoplanets as Earth-like as possible -- roughly Earth-size planets in the habitable zone -- and look for atmospheric gases or visible colors hard to explain without biology. In reality this poses many challenges, and suitable space telescopes take years to plan, build and launch.",
                "why": "Summarizes the whole plan for finding life beyond our solar system.",
            },
        ],
    },
]
