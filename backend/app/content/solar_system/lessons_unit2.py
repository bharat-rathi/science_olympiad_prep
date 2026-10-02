"""Unit 2 -- Rocky Worlds: Earth inside and out, life on early Earth and
impacts, how the rocky worlds evolved (with Mercury and the Moon), Venus and
Mars. Same lesson-chapter format as lessons_unit1.py.
"""

from app.content.solar_system.svg import BLUE, GOLD, GREEN, ICE, PURPLE, RED, ROCK

VENUS = "#e8c27a"
MARS = "#e0603a"

UNIT2 = [
    # ------------------------------------------------------------------ 4
    {
        "unit": 2,
        "name": "Solar System: Earth -- Inside and Out",
        "description": "Earth as a planet: its numbers, how earthquake waves reveal its layers, the atmosphere's layers and ozone shield, where our air and oceans came from, weather, the greenhouse effect and climate change.",
        "goals": [
            "Give Earth's key numbers and explain why it is the 'just right' planet.",
            "Name Earth's layers and explain how seismic waves let us 'see' inside.",
            "Name the atmosphere's layers and what our air is made of.",
            "Explain the greenhouse effect -- the good news and the bad news.",
        ],
        "sections": [
            {
                "heading": "Earth, the benchmark planet",
                "body": (
                    "To understand other worlds, start with the one we know best. From space, Earth is a medium-size rocky "
                    "planet -- the famous 'Blue Marble' photo was taken by the Apollo 17 astronauts. Unlike the Sun (mostly "
                    "hydrogen and helium), Earth is made mostly of heavy elements: iron, silicon and oxygen.\n\n"
                    "• Distance from the Sun: 1.00 AU, on an orbit that is almost a perfect circle. Year: 1.00 (365.25 days).\n"
                    "• Diameter 12,756 km (radius 6,378 km).\n"
                    "• Density 5.514 g/cm3 -- the densest planet.\n"
                    "• ESCAPE VELOCITY (the speed needed to fly away from Earth for good): 11.2 km/s.\n"
                    "• Rotation: 23 hours 56 minutes 4 seconds.\n"
                    "• Air pressure at the surface: 1.00 BAR (a bar is a unit for how hard the air presses down).\n\n"
                    "Earth is the only planet in our Solar System that is neither too hot nor too cold but 'just right' for "
                    "liquid water on its surface. Astronomers compare every other world to Earth = 1."
                ),
            },
            {
                "heading": "Listening to the inside of Earth",
                "body": (
                    "Here is a surprise: we know less about the rock 5 km under our feet than about the surfaces of Venus "
                    "and Mars! We can only drill into the top few kilometers. So how do we know what's inside? We listen.\n\n"
                    "Earthquakes (and big explosions) send SEISMIC WAVES through the planet, the way a struck bell rings. "
                    "Some waves travel along the surface; others go straight through. When the waves cross from one material "
                    "into another, they bend (REFRACT), just like light bending in water. That leaves some measuring "
                    "stations in 'shadow zones' where certain waves never arrive. By comparing a whole network of SEISMOGRAPHS "
                    "(machines that record shaking), scientists map which layers are solid and which are liquid -- a bit like "
                    "an ultrasound scan of the planet."
                ),
            },
            {
                "heading": "Earth's layers",
                "body": (
                    "Earth is like a peach: thin skin, thick fruit, and a hard pit.\n\n"
                    "• CRUST -- the thin outer skin. OCEANIC CRUST covers 55% of Earth's surface, is only about 6 km thick and "
                    "is made of dark volcanic rock called BASALT (silicon, oxygen, iron, aluminum, magnesium). CONTINENTAL "
                    "CRUST covers 45%, is 20 to 70 km thick and is mostly GRANITE. Both have a density of about 3 g/cm3. The "
                    "whole crust is only about 0.3% of Earth's mass!\n"
                    "• MANTLE -- the biggest layer, from the bottom of the crust down to 2,900 km. It is mostly solid but very "
                    "slowly churns, like extremely thick, hot putty. That slow churning (convection) moves the crust's "
                    "PLATES around -- this is PLATE TECTONICS.\n"
                    "• OUTER CORE -- liquid metal (mostly iron and nickel). Its swirling makes Earth's MAGNETIC FIELD, an "
                    "invisible shield that helps protect our air from the solar wind.\n"
                    "• INNER CORE -- solid metal at the very center, about 6,378 km down."
                ),
                "infographic": "earth_interior",
            },
            {
                "heading": "Our blanket of air",
                "body": (
                    "Near the ground, air is 78% nitrogen (N2), 21% oxygen (O2) and 1% argon (Ar), with traces of water vapor, "
                    "carbon dioxide (CO2) and other gases, plus dust and water droplets. Earth is the only planet with lots "
                    "of free oxygen in its air -- made by living things (see the next chapter).\n\n"
                    "The ATMOSPHERE comes in layers:\n"
                    "• TROPOSPHERE -- the bottom layer where we live and where weather happens. It gets colder as you climb.\n"
                    "• STRATOSPHERE -- above it, home of the OZONE LAYER near its top. OZONE (O3) is oxygen with three atoms "
                    "instead of two. It soaks up most of the Sun's harmful ULTRAVIOLET (UV) light -- Earth's sunscreen -- which "
                    "makes life on land possible. The energy ozone absorbs warms the stratosphere.\n"
                    "• Above 100 km the air is so thin that satellites glide through. UV light knocks electrons off atoms "
                    "there, so it is called the IONOSPHERE. Light, fast atoms like hydrogen and helium can escape into space "
                    "from up here: Earth slowly leaks.\n\n"
                    "In the 1980s scientists found that chemicals called CFCs (once used in spray cans and fridges) were "
                    "destroying ozone. Countries agreed to ban them, ozone loss stopped, and the 'ozone hole' over Antarctica "
                    "is slowly shrinking -- proof that people can work together to protect a planet."
                ),
                "infographic": "atmosphere_layers",
            },
            {
                "heading": "Where did our air and oceans come from?",
                "body": (
                    "Scientists have three ideas, and the evidence says the answer is a mix of the second and third:\n"
                    "1. The gases came with the rocky pieces that built Earth.\n"
                    "2. VOLCANOES released them from inside Earth after it formed (volcanoes still puff out carbon dioxide, "
                    "water vapor and sulfur dioxide).\n"
                    "3. Comets and asteroids from the cold outer Solar System crashed in and delivered water and gases.\n\n"
                    "A THOUGHT EXPERIMENT: what if Earth got really hot? VOLATILE materials evaporate at fairly low "
                    "temperatures. Heat Earth above 100 C and the oceans would boil. There is enough water to cover the whole "
                    "Earth about 300 m deep, and every 10 m of water presses down like 1 bar of air -- so the steam would make "
                    "a 300-bar atmosphere! Heating carbonate rocks would add about 70 bars of CO2 (today Earth has only "
                    "0.0005 bar of CO2). A hot Earth would have a crushing ~400-bar atmosphere of steam and CO2. Keep this in "
                    "mind when you meet Venus.\n\n"
                    "WEATHER is simply the circulation (movement) of a planet's air. It is powered mostly by sunlight heating "
                    "the ground. Earth's spin and the seasons change how much sunlight each place gets, and the air and oceans "
                    "carry heat from warm places to cool places."
                ),
            },
            {
                "heading": "The greenhouse effect: good news and bad news",
                "body": (
                    "Sunlight passes through the air and warms the ground. The warm ground then gives off invisible INFRARED "
                    "light (heat). Some gases -- carbon dioxide, methane and water vapor, called GREENHOUSE GASES -- let "
                    "sunlight in but absorb that outgoing infrared, like a blanket. The planet has to warm up until the heat "
                    "escaping to space balances the sunlight coming in. More greenhouse gas = a warmer balance point. It's "
                    "like a car parked in the sun with the windows up.\n\n"
                    "THE GOOD NEWS: Earth's natural greenhouse effect keeps us comfortable. Without it, Earth would be stuck "
                    "below freezing in a global ice age. (One chapter of the reader says it warms Earth by about 23 C, another "
                    "by about 33 C -- the 33 C value is the one usually used.)\n\n"
                    "THE BAD NEWS: burning FOSSIL FUELS (coal, oil and gas -- the remains of plants and animals from millions "
                    "of years ago) releases CO2, and cutting down forests removes the trees that soak it up. CO2 rose about 30% "
                    "in the past century, keeps rising more than 0.5% a year, and is expected to double its pre-industrial "
                    "level before 2100. Burning fossil fuels releases about 100 times more CO2 than all volcanoes. The results "
                    "of this CLIMATE CHANGE: record heat (nearly all of the hottest years on record came after 2000), "
                    "shrinking glaciers, thinner Arctic ice and rising seas.\n\n"
                    "People have changed Earth before: early hunters wiped out giant animals (mammoths, mastodons, giant "
                    "sloths, 10-foot kangaroos), and farmers cut down forests. Scientists have suggested naming our time the "
                    "ANTHROPOCENE -- the age when humans became a planet-changing force."
                ),
                "infographic": "greenhouse",
            },
        ],
        "word_bank": [
            ("Escape velocity", "The speed something must reach to fly away from a planet and never fall back. Earth's is 11.2 km/s."),
            ("Bar", "A unit of pressure. Earth's air pushes down with about 1 bar at sea level."),
            ("Seismic waves", "Vibrations from earthquakes or explosions that travel through a planet."),
            ("Refract", "To bend when passing from one material into another."),
            ("Seismograph", "An instrument that records the shaking of the ground."),
            ("Crust", "A planet's thin, solid outer layer."),
            ("Basalt", "A dark rock made from cooled lava. It makes up the ocean floors."),
            ("Granite", "A light-colored rock that makes up much of the continents."),
            ("Mantle", "The thick layer of hot rock between a planet's crust and core."),
            ("Plate tectonics", "The slow movement of giant pieces (plates) of Earth's crust, driven by the churning mantle."),
            ("Magnetic field", "An invisible region of magnetic force around a planet that helps shield it from the solar wind."),
            ("Atmosphere", "The layer of gases surrounding a planet."),
            ("Troposphere", "The lowest layer of the atmosphere, where we live and weather happens."),
            ("Stratosphere", "The atmosphere layer above the troposphere, where the ozone layer is."),
            ("Ozone", "A form of oxygen with three atoms (O3) that blocks the Sun's harmful UV light."),
            ("Ultraviolet (UV)", "Invisible, high-energy light from the Sun that can damage living things (it causes sunburn)."),
            ("Ionosphere", "The very thin upper atmosphere, above about 100 km, where atoms lose electrons."),
            ("CFCs", "Human-made chemicals that destroyed ozone; they are now banned."),
            ("Volatile", "A substance that turns into gas easily at low temperatures (like water or CO2)."),
            ("Weather", "The movement (circulation) of a planet's air, powered by sunlight."),
            ("Infrared", "Invisible light that we feel as heat."),
            ("Greenhouse effect", "When gases in the air trap infrared heat, warming a planet's surface."),
            ("Greenhouse gas", "A gas that traps infrared heat, such as carbon dioxide, methane and water vapor."),
            ("Fossil fuels", "Coal, oil and natural gas, made from the remains of ancient living things. Burning them releases CO2."),
            ("Climate change", "Long-term change in a planet's typical temperatures and weather -- on Earth today, mainly warming caused by extra CO2."),
            ("Anthropocene", "A suggested name for our time, when humans have become a major force changing the planet."),
        ],
        "key_facts": [
            "Earth: 1.00 AU; diameter 12,756 km; radius 6,378 km; density 5.514 g/cm3; escape velocity 11.2 km/s; rotation 23 h 56 m 4 s; 1.00 bar.",
            "Oceanic crust: 55% of surface, ~6 km, basalt. Continental crust: 45%, 20-70 km, granite. Crust = 0.3% of Earth's mass.",
            "Mantle to 2,900 km; liquid outer core; solid inner core.",
            "Air: 78% N2, 21% O2, 1% Ar, traces of H2O and CO2 (0.0005 bar of CO2).",
            "Ozone (O3) in the stratosphere blocks UV; CFCs banned; Antarctic ozone hole shrinking.",
            "Boiled oceans = ~300 bars; carbonate rocks = ~70 bars CO2; hot Earth ~400 bars.",
            "Natural greenhouse warming: ~33 C (reader also says ~23 C). CO2 up ~30% in a century.",
            "Fossil fuels release ~100x more CO2 than volcanoes.",
        ],
        "quick_check": [
            ("How do scientists learn what is inside Earth?", "By studying seismic waves from earthquakes -- how they bend and where they are blocked shows which layers are solid or liquid."),
            ("Which layer of Earth makes the magnetic field?", "The liquid metal outer core, as it swirls."),
            ("What does the ozone layer do, and in which layer of the atmosphere is it?", "It absorbs harmful ultraviolet light; it is near the top of the stratosphere."),
            ("Explain the greenhouse effect in two sentences.", "Sunlight warms the ground, which gives off infrared heat. Greenhouse gases like CO2 absorb that heat and keep the planet warmer."),
            ("Would Earth be better off with no greenhouse effect at all?", "No -- without it Earth would be frozen in a global ice age (about 33 C colder)."),
            ("What are the three possible sources of Earth's air and oceans?", "Gas trapped in the original building blocks, gas released by volcanoes, and water/gas delivered by comets and asteroids (evidence favors the last two)."),
        ],
        "cards": [
            {
                "term": "Earth's vital statistics",
                "badge": ("1 AU", "home", BLUE),
                "analogy": "Earth is the 'just right' bowl of porridge -- not too hot, not too cold.",
                "explanation": "1.00 AU, diameter 12,756 km, density 5.514 g/cm3 (densest planet), escape velocity 11.2 km/s, day 23 h 56 m, pressure 1 bar. The only planet with liquid water on its surface.",
                "why": "Every other world is compared to Earth = 1.",
            },
            {
                "term": "Seismic waves",
                "badge": ("WAVES", "seismic", PURPLE),
                "analogy": "Tapping a watermelon to tell what's inside without cutting it.",
                "explanation": "Earthquake waves travel through Earth, bend at layer boundaries and leave 'shadow zones'. Seismograph networks use them to map solid and liquid layers.",
                "why": "The same idea (indirect measurements) reveals hidden oceans on icy moons.",
            },
            {
                "term": "Earth's layers",
                "badge": ("4", "layers", GOLD),
                "analogy": "A peach: thin skin (crust), thick fruit (mantle), hard pit (core).",
                "explanation": "Crust (oceanic basalt ~6 km; continental granite 20-70 km), mantle to 2,900 km, liquid outer core (makes the magnetic field), solid inner core.",
                "why": "Layering and a magnetic field help a planet keep its air.",
            },
            {
                "term": "Ozone layer",
                "badge": ("O₃", "UV shield", ICE),
                "analogy": "Earth's sunscreen, high up in the sky.",
                "explanation": "Ozone (O3) near the top of the stratosphere absorbs harmful UV light, letting life live on land. CFCs damaged it; a worldwide ban stopped the damage.",
                "why": "Ozone only exists because life made oxygen -- a sign of life.",
            },
            {
                "term": "Atmosphere layers & escape",
                "badge": ("78/21", "N₂ / O₂", BLUE),
                "analogy": "The fastest kids at recess sometimes run right off the playground -- like light gas atoms.",
                "explanation": "Troposphere (weather) -> stratosphere (ozone) -> thin ionosphere above 100 km, where light atoms like hydrogen and helium leak into space. Air: 78% N2, 21% O2, 1% Ar.",
                "why": "Whether a planet keeps its air decides whether it stays habitable.",
            },
            {
                "term": "Greenhouse effect",
                "badge": ("CO₂", "heat blanket", RED),
                "analogy": "A car in the sun with its windows up.",
                "explanation": "Sunlight warms the ground; the ground gives off infrared; CO2, methane and water vapor trap it. Earth's natural greenhouse adds ~33 C -- without it we'd freeze.",
                "why": "The greenhouse effect sets the edges of the habitable zone.",
            },
            {
                "term": "Climate change",
                "badge": ("+30%", "CO₂", RED),
                "analogy": "Adding extra blankets on a warm night -- you can't cool off.",
                "explanation": "Burning fossil fuels (100x more CO2 than volcanoes) and cutting forests raised CO2 ~30% in a century. Result: record heat, melting ice, rising seas.",
                "why": "Links Earth's future to Venus' runaway greenhouse.",
            },
        ],
    },
    # ------------------------------------------------------------------ 5
    {
        "unit": 2,
        "name": "Solar System: Life on Early Earth & Cosmic Impacts",
        "description": "When life began, stromatolites, the tree of life, how photosynthesis filled the air with oxygen and built the ozone layer, why Earth has few craters, the Tunguska blast and the impact that ended the dinosaurs.",
        "goals": [
            "Give the key dates for the earliest life on Earth.",
            "Explain how life changed Earth's atmosphere (oxygen, ozone, less CO2).",
            "Describe the tree of life and why aliens would most likely be microbes.",
            "Explain why Earth has few craters and how impacts affected life.",
        ],
        "sections": [
            {
                "heading": "How long has life been here?",
                "body": (
                    "Earth's restless crust has erased most of its 'baby pictures', but a few clues survive. The oldest "
                    "surviving rocks are about 3.9 billion years old, and their chemistry shows that life ALREADY existed "
                    "then. (Some scientists see possible signs as old as 3.8 billion years, but that is debated.)\n\n"
                    "By 3.5 billion years ago, tiny MICROBES (living things too small to see) were building big colonies "
                    "called STROMATOLITES. A stromatolite forms when a sticky mat of blue-green bacteria traps mud in shallow "
                    "water, grows up on top of it, traps more mud, and so on -- a layer cake baked by microbes. The oldest "
                    "known one is 3.47 billion years old, from Western Australia, and stromatolites still grow today (for "
                    "example in Lake Thetis, Western Australia).\n\n"
                    "Plenty of FOSSILS (remains or traces of ancient life preserved in rock) exist only for the last 600 "
                    "million years -- less than 15% of Earth's history. For most of Earth's history, life was microscopic."
                ),
                "infographic": "earth_life_timeline",
            },
            {
                "heading": "How did life start?",
                "body": (
                    "We have little direct evidence, but we know early Earth's air had lots of carbon dioxide, some methane "
                    "and NO oxygen gas. That matters: oxygen is very 'grabby' and tends to break delicate molecules. Without "
                    "it, many chemical reactions can build AMINO ACIDS (the building blocks of proteins) and other "
                    "ingredients of life. So these ingredients were probably around very early.\n\n"
                    "For tens of millions of years, early life -- maybe little more than large molecules, a bit like today's "
                    "viruses -- probably lived in warm seas, 'eating' organic chemicals that had built up there. When that easy "
                    "food ran low, life began the long road of EVOLUTION (gradual change over many generations) toward the "
                    "huge variety we see today.\n\n"
                    "Clues from genes say the earliest surviving life forms liked high temperatures, so life may have started "
                    "in very hot places, like hot springs on the seafloor. A wilder idea: life started on Mars (which cooled "
                    "sooner) and was carried to Earth inside meteorites. Mars rocks really do land on Earth, but none has "
                    "shown signs of carrying microbes."
                ),
            },
            {
                "heading": "The tree of life",
                "body": (
                    "Every living thing carries a GENOME -- its complete set of DNA instructions. Your genome is 99.9% the "
                    "same as Julius Caesar's or Marie Curie's, and 99% the same as a chimpanzee's. Comparing genes shows that "
                    "ALL life on Earth comes from one common ancestor.\n\n"
                    "Using a piece of RNA that every species shares, scientists drew the 'tree of life'. It has three huge "
                    "branches called DOMAINS: BACTERIA, ARCHAEA and EUKARYA. Plants, animals and fungi are just short twigs "
                    "at the end of the eukarya branch! Most of life's variety is microbial -- there are more microbes in a "
                    "bucket of soil than stars in our Galaxy. So if we ever find aliens, they will most likely be microbes, "
                    "not little green people."
                ),
            },
            {
                "heading": "How life rebuilt the atmosphere",
                "body": (
                    "A turning point was PHOTOSYNTHESIS: using sunlight's energy to turn carbon dioxide and water into food "
                    "(sugars), giving off oxygen as 'waste'. Blue-green bacteria (also called cyanobacteria or blue-green "
                    "algae) did it first and gave rise to all plants.\n\n"
                    "At first the oxygen didn't stay in the air -- chemical reactions with the crust grabbed it as fast as it "
                    "formed. Slowly, as more plant life made more oxygen and rocks buried plant carbon, free oxygen began "
                    "piling up in the air about 2.4 billion years ago (one chapter of the reader says about 2 billion).\n\n"
                    "Oxygen then built the OZONE LAYER, which blocks deadly ultraviolet light. Before that, life had to stay "
                    "in the protective oceans and the continents were bare rock. With an ozone shield, life moved onto land, "
                    "and animals evolved to breathe oxygen. Funny thought: we breathe the waste product of plants!\n\n"
                    "Earth, Venus and Mars probably started with similar CO2-rich air. On Earth, liquid water and then life "
                    "pulled most of the CO2 out of the air and locked it into seafloor mud and CARBONATE rocks like "
                    "limestone. Without life, Earth would probably have a CO2 atmosphere like Venus and Mars. That is why "
                    "astronomers hope to spot life on other planets by studying their air."
                ),
            },
            {
                "heading": "Where are Earth's craters?",
                "body": (
                    "The Moon is covered in IMPACT CRATERS (bowl-shaped holes blasted out by crashing space rocks). It is "
                    "practically next door, so Earth must have been hit just as often. Our air burns up small pieces as "
                    "METEORS (shooting stars), but it is no shield against big rocks that blast craters several kilometers "
                    "wide.\n\n"
                    "The difference is that Earth is geologically active: plate tectonics keeps recycling the crust, and "
                    "wind, water and ice wear surfaces down (EROSION). Old craters get erased. Geologists have only recently "
                    "found the worn-down remains of many, like the 4-km Ouarkziz crater in Algeria, photographed from the "
                    "International Space Station.\n\n"
                    "A rule you will use again and again: MORE craters = OLDER surface; FEW craters = YOUNG, active surface."
                ),
            },
            {
                "heading": "Tunguska and the end of the dinosaurs",
                "body": (
                    "TUNGUSKA, 1908. On June 30, 1908, near the Tunguska River in Siberia, a space rock exploded about 8 km "
                    "above the ground. The blast flattened more than 1,000 square kilometers of forest, killed herds of "
                    "reindeer and knocked a man 80 km away out of his chair. Instruments around the world recorded the "
                    "pressure wave. It was a 5-MEGATON explosion (as strong as 5 million tons of explosives) from a stony "
                    "object only about 50 m across -- the size of a small office building.\n\n"
                    "IMPACTS AND EVOLUTION. Big impacts have changed the story of life. About 65 million years ago a massive "
                    "impact caused a MASS EXTINCTION -- the dinosaurs and most other living things died out. That cleared the "
                    "way for mammals, and eventually us. Even earlier, during the heavy bombardment (about 4.1 to 3.8 billion "
                    "years ago), giant impacts may have heated Earth's surface enough to sterilize it (kill everything)."
                ),
            },
        ],
        "word_bank": [
            ("Microbe", "A living thing too small to see without a microscope, like bacteria."),
            ("Stromatolite", "A layered rock mound built by mats of microbes trapping mud, one layer at a time."),
            ("Fossil", "The preserved remains or traces of an ancient living thing, found in rock."),
            ("Amino acids", "Small molecules that link together to build proteins -- building blocks of life."),
            ("Protein", "A large molecule that builds body parts and does most of the work inside cells."),
            ("Evolution", "The slow change in living things over many generations."),
            ("Genome", "The complete set of DNA instructions inside a living thing."),
            ("DNA", "The molecule that stores the instructions for building and running a living thing."),
            ("RNA", "A molecule related to DNA that helps turn DNA's instructions into proteins."),
            ("Domain", "One of the three biggest branches of the tree of life: bacteria, archaea and eukarya."),
            ("Bacteria", "Tiny single-celled living things; one of the three domains of life."),
            ("Archaea", "Single-celled microbes that look like bacteria but are a separate domain; many love extreme heat or salt."),
            ("Eukarya", "The domain of living things whose cells have a nucleus -- including plants, animals and fungi."),
            ("Photosynthesis", "How plants and some microbes use sunlight to turn carbon dioxide and water into food, releasing oxygen."),
            ("Cyanobacteria", "Blue-green bacteria that were the first to make oxygen by photosynthesis."),
            ("Carbonate rock", "Rock such as limestone that locks carbon dioxide inside it."),
            ("Impact crater", "A bowl-shaped hole made when a space rock crashes into a surface."),
            ("Meteor", "The streak of light made when a space rock burns up in the air -- a 'shooting star'."),
            ("Erosion", "Wearing away of rock and soil by wind, water or ice."),
            ("Megaton", "The energy of one million tons of explosives."),
            ("Mass extinction", "A time when a huge number of species die out quickly."),
            ("Sterilize", "To kill all living things in a place."),
        ],
        "key_facts": [
            "Oldest surviving rocks: ~3.9 billion years -- life already existed. Possible (debated) signs: 3.8 billion years.",
            "Stromatolites by 3.5 billion years ago; oldest known 3.47 billion years (Western Australia); still grow in Lake Thetis.",
            "Abundant fossils only for the last 600 million years (<15% of Earth's history).",
            "Tree of life: 3 domains -- bacteria, archaea, eukarya.",
            "Free oxygen built up ~2.4 billion years ago (reader also says ~2 billion) -> ozone layer -> life on land.",
            "Tunguska: June 30, 1908, Siberia; exploded ~8 km up; >1,000 km2 of forest flattened; 5 megatons; object ~50 m.",
            "Dinosaur-ending impact: 65 million years ago. Ouarkziz crater, Algeria: 4 km.",
        ],
        "quick_check": [
            ("What are stromatolites and why are they important?", "Layered mounds built by mats of microbes trapping mud. They are some of the oldest evidence of life (3.47 billion years) and of photosynthesis."),
            ("Why didn't oxygen build up in the air as soon as photosynthesis began?", "Chemical reactions with rocks in the crust grabbed the oxygen as fast as it was made."),
            ("Why could life only move onto land after oxygen built up?", "Oxygen formed the ozone layer, which blocks deadly ultraviolet light."),
            ("Why does Earth have far fewer craters than the Moon?", "Plate tectonics and erosion keep erasing them; the Moon is geologically dead, so its craters stay."),
            ("If we find alien life, what will it most likely be?", "Microbes -- most of life's diversity on Earth is microbial."),
        ],
        "cards": [
            {
                "term": "Earliest life",
                "badge": ("3.9", "bya rocks", GREEN),
                "analogy": "Finding footprints on the oldest page of a diary -- someone was already there.",
                "explanation": "Rocks ~3.9 billion years old already show chemical signs of life. Abundant fossils only cover the last 600 million years.",
                "why": "Life started quickly once Earth calmed down -- a hopeful hint for other worlds.",
            },
            {
                "term": "Stromatolites",
                "badge": ("3.47", "bya", GREEN),
                "analogy": "Layer cakes baked by microbes, one sticky layer at a time.",
                "explanation": "Mats of blue-green bacteria trap mud in layers. Oldest known: 3.47 billion years (Western Australia). They still grow in Lake Thetis.",
                "why": "A model 'biosignature' to look for in Mars rocks.",
            },
            {
                "term": "Tree of life",
                "badge": ("3", "domains", GREEN),
                "analogy": "Plants and animals are just a couple of twigs on a giant tree that's mostly microbes.",
                "explanation": "Three domains: bacteria, archaea, eukarya. All life shares one common ancestor; most diversity is microbial.",
                "why": "The search for life beyond Earth looks for microbes first.",
            },
            {
                "term": "Photosynthesis & oxygen",
                "badge": ("O₂", "~2.4 bya", GREEN),
                "analogy": "Life plugged into the Sun's power outlet -- and the 'exhaust' was oxygen.",
                "explanation": "Sunlight + CO2 + water -> food + oxygen. Oxygen built up ~2.4 billion years ago, formed the ozone layer, and let life colonize land.",
                "why": "Lots of oxygen in a planet's air is the strongest known sign of life.",
            },
            {
                "term": "How life changed Earth's air",
                "badge": ("−CO₂", "+O₂", BLUE),
                "analogy": "Living things acted like gardeners who remade the whole sky.",
                "explanation": "Water and life locked CO2 into rocks and seafloor mud, and photosynthesis added oxygen. Without life, Earth's air would be CO2 like Venus and Mars (~96%).",
                "why": "Why we study exoplanet air for signs of life.",
            },
            {
                "term": "Few craters on Earth",
                "badge": ("ERASED", "craters", ROCK),
                "analogy": "A beach where the waves keep smoothing away footprints.",
                "explanation": "Earth was hit as often as the Moon, but plate tectonics and erosion erase craters. More craters = older surface.",
                "why": "Crater counting dates surfaces on every world.",
            },
            {
                "term": "Tunguska (1908)",
                "badge": ("1908", "Siberia", RED),
                "analogy": "A space rock the size of an office building exploded like a giant bomb in the sky.",
                "explanation": "June 30, 1908: a ~50 m stony object exploded ~8 km up with 5 megatons of energy, flattening over 1,000 km2 of forest.",
                "why": "Small bodies are still a hazard to Earth.",
            },
            {
                "term": "Impacts & extinction",
                "badge": ("65", "Mya", RED),
                "analogy": "One unlucky space rock reshuffled the deck of life.",
                "explanation": "An impact 65 million years ago wiped out the dinosaurs and most living things, letting mammals take over.",
                "why": "Habitability isn't permanent -- impacts can reset a biosphere.",
            },
        ],
    },
    # ------------------------------------------------------------------ 6
    {
        "unit": 2,
        "name": "Solar System: Rocky Worlds -- Mercury, the Moon & How Planets Change",
        "description": "Why worlds that started alike ended up so different: the baked potato effect, Mercury and the Moon, the activity ladder from the Moon to Earth, why Mars has the tallest mountain, why big bodies are round, and how the rocky planets' atmospheres evolved.",
        "goals": [
            "Use 'composition, mass and distance' to explain why planets differ.",
            "Explain the baked potato effect and rank worlds by geological activity.",
            "Describe Mercury and the Moon.",
            "Explain why Olympus Mons is so tall and why big objects are round.",
            "Tell the story of how Venus, Earth and Mars got their atmospheres.",
        ],
        "sections": [
            {
                "heading": "Same start, different endings",
                "body": (
                    "Earth, Venus and Mars started out as rocky siblings, probably with similar atmospheres. Today one is a "
                    "blue living world, one is a scorching pressure cooker, and one is a cold desert. PLANETARY EVOLUTION is "
                    "the story of how planets change after they are born, through heat, impacts, volcanoes, their atmospheres "
                    "and their star. It depends mainly on three things:\n"
                    "• COMPOSITION -- what the world is made of,\n"
                    "• MASS -- how big it is,\n"
                    "• DISTANCE from the Sun.\n\n"
                    "After the giant-impact era (the first ~100 million years) and the heavy cratering (until ~4 billion "
                    "years ago), each world followed its own path. Planets can also change from outside: impacts, changes in "
                    "their orbits, and their star slowly brightening can strip atmospheres or change climates."
                ),
            },
            {
                "heading": "The baked potato effect",
                "body": (
                    "Take a big baked potato and a tiny one out of the oven. Which stays hot inside longer? The big one! "
                    "Planets work the same way.\n\n"
                    "GEOLOGICAL ACTIVITY -- volcanoes, earthquakes, moving crust -- needs heat inside the planet. That heat is "
                    "either left over from when the planet formed, or made by RADIOACTIVE DECAY (unstable atoms slowly "
                    "breaking apart). Bigger worlds hold their heat longer, so they stay active longer. Small worlds cool "
                    "fast and go 'geologically dead'.\n\n"
                    "The activity ladder, from smallest to biggest:\n"
                    "• THE MOON: big volcanic eruptions stopped about 3.3 billion years ago. Its mantle cooled and hardened; "
                    "moonquakes are nearly zero. Geologically dead.\n"
                    "• MERCURY: probably went quiet about the same time.\n"
                    "• MARS (in between): its southern crust formed by 4 billion years ago, its northern volcanic plains are "
                    "about as old as the Moon's dark plains, and its giant Tharsis volcanoes have been active on and off "
                    "almost to the present.\n"
                    "• VENUS: lots of volcanism but no plate tectonics; most of its surface is no older than about 500 million "
                    "years.\n"
                    "• EARTH (largest): global plate tectonics constantly recycles the surface -- most of it is less than 200 "
                    "million years old.\n\n"
                    "The big exception is TIDAL HEATING: Jupiter's small moon Io is the most volcanic world of all because "
                    "Jupiter's gravity keeps flexing it (see the Giant Planets chapter)."
                ),
                "infographic": "baked_potato",
            },
            {
                "heading": "Mercury: the scorched little planet",
                "body": (
                    "Mercury is the smallest planet and the closest to the Sun (0.39 AU). It races around the Sun in just "
                    "88 days -- the shortest year -- but spins slowly, once every 58.6 days. Its diameter is only 4,878 km "
                    "(a bit bigger than our Moon), yet its density is 5.4 g/cm3, so it must have a huge iron core.\n\n"
                    "Mercury is too small and too hot to hold on to an atmosphere, so there is no air to spread heat around. "
                    "The sunny side bakes at over 400 C while the night side drops below -170 C -- the biggest temperature "
                    "swing of any planet. Like the Moon, it is covered in craters; its biggest is the Caloris Basin, about "
                    "1,500 km across. Surprisingly, there may be water ice hiding in permanently shadowed craters near its "
                    "poles. It has no moons.\n\n"
                    "Mariner 10 and MESSENGER studied Mercury, and the European-Japanese mission BepiColombo (launched "
                    "October 20, 2018) is on its way to study its makeup, magnetic field and history -- and to test Einstein's "
                    "theory of gravity."
                ),
            },
            {
                "heading": "The Moon: a geologically dead record keeper",
                "body": (
                    "Our Moon is 3,476 km across with a density of 3.3 g/cm3, orbiting about 384,400 km from Earth once every "
                    "27.3 days. It is TIDALLY LOCKED -- it spins exactly once per orbit, so the same face always points at "
                    "Earth.\n\n"
                    "Most scientists think the Moon formed when a Mars-sized body crashed into the young Earth, throwing out "
                    "rocky debris that clumped together. That explains why the Moon is like Earth's rocky outer layers but "
                    "has little iron and almost no water or other volatiles -- it probably never had an atmosphere.\n\n"
                    "The bright HIGHLANDS are the oldest, most cratered areas. The dark MARIA (Latin for 'seas'; one is a "
                    "MARE) are huge plains of hardened lava that flooded giant impact basins billions of years ago. With no "
                    "air, no water and no plate tectonics, the Moon keeps its craters for billions of years, making it a "
                    "perfect record of the heavy bombardment. On the Moon and Mercury, the big mountains are rock thrown up "
                    "by giant impacts.\n\n"
                    "Apollo astronauts walked on the Moon and brought back rocks, and the Lunar Reconnaissance Orbiter "
                    "(launched June 28, 2009) is mapping it in high detail to prepare for future human visits."
                ),
            },
            {
                "heading": "Why Mars has the tallest mountain",
                "body": (
                    "Mountains form in different ways on different worlds. On the Moon and Mercury they are debris from huge "
                    "impacts. On Mars, most big mountains are volcanoes built by eruption after eruption from the same vent. "
                    "Earth's and Venus' highest mountains (Mount Everest, the Maxwell Mountains) were squeezed up when crust "
                    "was pushed together -- on Earth, by continents colliding.\n\n"
                    "Mountains on Earth and Venus top out at about 10 km above their surroundings. Mars' OLYMPUS MONS rises "
                    "more than 20 km -- nearly 30 km above Mars' lowest areas -- and is nearly 500 km wide: almost three "
                    "times as tall as Earth's tallest mountain. Two reasons:\n"
                    "1. NO MOVING PLATES. On Earth, a plate slides over a HOT SPOT (a place where hot rock rises from deep "
                    "inside), so instead of one giant volcano you get a chain of islands, like Hawaii. On Mars the crust stays "
                    "put, so one volcano can keep growing for hundreds of millions of years.\n"
                    "2. WEAKER GRAVITY. A mountain has to hold up its own weight. On Earth (and Venus, with almost the same "
                    "gravity) rock strength limits mountains to about 10 km -- Hawaii's Mauna Loa sags when new lava piles on. "
                    "Mars' gravity is only about one-third of Earth's, so much taller piles can stand."
                ),
                "infographic": "mountain_heights",
            },
            {
                "heading": "Why are big things round? (the 400 km rule)",
                "body": (
                    "Gravity pulls everything toward the center. The shape where every point on the surface is the same "
                    "distance from the center is a SPHERE, so gravity squeezes big objects into balls. Rock is strong, "
                    "though, and in a small object rock's strength can win against weak gravity.\n\n"
                    "For rocky objects the cutoff is about 400 km across. Bigger ones are always roughly round; smaller ones "
                    "can be almost any shape, like the potato-shaped asteroid Ida (about 60 km long), photographed by the "
                    "Galileo spacecraft. That is why being round 'by its own gravity' is part of the definition of a dwarf "
                    "planet."
                ),
            },
            {
                "heading": "How the rocky planets' air evolved",
                "body": (
                    "Planets got their atmospheres from gas escaping their insides (through volcanoes) and from impacts of "
                    "comets and asteroids rich in water and gases. Mercury was too small and hot to keep any, and the Moon "
                    "probably never had one.\n\n"
                    "At first, the air probably contained hydrogen-rich gases: carbon monoxide plus some ammonia and "
                    "methane. Ultraviolet sunlight split these molecules; the light hydrogen escaped to space, leaving "
                    "atmospheres rich in carbon dioxide.\n\n"
                    "Then each planet's WATER took a different path:\n"
                    "• MARS had a thick atmosphere and plenty of liquid water early on, but it lost the CO2 it needed for "
                    "greenhouse warming. It cooled, and its water froze.\n"
                    "• VENUS went the other way: a RUNAWAY GREENHOUSE boiled away its water forever.\n"
                    "• EARTH kept the balance for liquid water -- and life then removed CO2 and added oxygen.\n"
                    "With their water gone, Venus and Mars ended up with atmospheres of about 96% CO2 and a few percent "
                    "nitrogen. Earth is mostly nitrogen, low in CO2, and the only planet with free oxygen.\n\n"
                    "Which Solar System worlds could be habitable? Mercury, Venus, the Moon, the giant planets (no solid "
                    "surface) and most outer moons are out. The best bets all involve water: Mars (water underground and in "
                    "the past), Europa and Enceladus (hidden oceans), and Titan for a possible 'life as we don't know it'."
                ),
            },
        ],
        "word_bank": [
            ("Planetary evolution", "How a planet changes over time after it forms."),
            ("Geological activity", "Things like volcanoes, earthquakes and moving crust that reshape a world's surface."),
            ("Radioactive decay", "When unstable atoms slowly break apart and give off heat."),
            ("Baked potato effect", "Bigger worlds keep their inside heat longer, so they stay geologically active longer."),
            ("Tidal heating", "Heat made inside a moon or planet when another body's gravity keeps squeezing and stretching it."),
            ("Highlands", "The Moon's bright, old, heavily cratered regions."),
            ("Maria", "The Moon's dark, smooth plains of old hardened lava (Latin for 'seas'; one is a 'mare')."),
            ("Tidally locked", "When a body spins exactly once per orbit, so the same side always faces its partner."),
            ("Caloris Basin", "Mercury's largest impact crater, about 1,500 km across."),
            ("Olympus Mons", "A huge volcano on Mars and the tallest mountain in the Solar System, over 20 km high."),
            ("Hot spot", "A place where hot rock rises from deep inside a planet and makes volcanoes."),
            ("Tharsis", "A giant volcanic bulge on Mars with several huge volcanoes."),
            ("Runaway greenhouse", "A warming loop in which heat releases more greenhouse gas, which causes more heat -- it boiled away Venus' oceans."),
            ("Ejecta", "Rock thrown out of a crater by an impact."),
        ],
        "key_facts": [
            "A planet's fate depends on composition, mass and distance from the Sun.",
            "Activity ladder: Moon (dead ~3.3 billion years) ~ Mercury < Mars < Venus (surface <=500 Myr) < Earth (surface mostly <200 Myr).",
            "Mercury: 0.39 AU, year 88 days, day 58.6 days, 4,878 km, density 5.4, no moons, >400 C day / < -170 C night.",
            "Moon: 3,476 km, density 3.3, 384,400 km away, 27.3-day orbit, tidally locked.",
            "Olympus Mons: >20 km high (nearly 30 km above Mars' lowest areas), ~500 km wide -- no moving plates + 1/3 gravity.",
            "Rocky bodies larger than ~400 km are round; smaller ones can be lumpy (Ida, ~60 km).",
            "Venus and Mars air: ~96% CO2, a few % N2.",
        ],
        "quick_check": [
            ("Why is the Moon geologically dead while Earth is still active?", "The Moon is small, so it lost its internal heat quickly (baked potato effect). Earth is big and still hot inside."),
            ("Give two reasons Olympus Mons is so much taller than any mountain on Earth.", "Mars has no moving plates, so one volcano stays over its hot spot; and Mars' gravity is only about 1/3 of Earth's, so tall mountains don't collapse."),
            ("Why does Mercury have such huge temperature swings?", "It has no atmosphere to trap and spread heat, and it is close to the Sun with long days and nights."),
            ("An asteroid is 50 km across. Do you expect it to be round?", "No -- objects smaller than about 400 km can be lumpy because rock strength beats their weak gravity."),
            ("What happened to the water on Venus and on Mars?", "Venus lost it to a runaway greenhouse (boiled away and split apart); Mars lost much of its air, cooled, and its water froze or was lost."),
        ],
        "cards": [
            {
                "term": "Three controls on a planet's fate",
                "badge": ("C-M-D", "fate", GOLD),
                "analogy": "Three kids from the same family turn out differently depending on how big they grow and where they live.",
                "explanation": "Composition, mass and distance from the Sun decide how a world evolves after the early impacts end.",
                "why": "Use these three words to structure any 'why are these planets different?' answer.",
            },
            {
                "term": "Baked potato effect",
                "badge": ("BIG=HOT", "longer", ROCK),
                "analogy": "A big baked potato stays hot inside much longer than a tiny one.",
                "explanation": "Activity needs inner heat (left from formation or from radioactive decay). Bigger worlds keep it longer: Moon and Mercury dead, Mars in between, Venus and Earth still active. Exception: tidally heated moons like Io.",
                "why": "Inner heat drives volcanoes, magnetic fields and fresh air -- all linked to habitability.",
            },
            {
                "term": "Mercury",
                "badge": ("88 d", "year", "#b5b5b5"),
                "analogy": "A small, fast runner right next to a bonfire, with no jacket.",
                "explanation": "0.39 AU, 88-day year, 58.6-day spin, 4,878 km, dense iron core (5.4), no air, no moons; above 400 C by day, below -170 C at night. BepiColombo (2018) is headed there.",
                "why": "The extreme case of a world too small and hot to keep an atmosphere.",
            },
            {
                "term": "The Moon",
                "badge": ("27.3 d", "orbit", "#bdbdbd"),
                "analogy": "A dusty old notebook nobody has erased -- every crater is still written there.",
                "explanation": "3,476 km, density 3.3, 384,400 km away, tidally locked. Probably formed from a giant impact on Earth. Bright cratered highlands and dark lava 'maria'; dead for ~3.3 billion years.",
                "why": "Its craters record the heavy bombardment.",
            },
            {
                "term": "Olympus Mons",
                "badge": ("20+", "km high", MARS),
                "analogy": "On Mars you can stack a sandcastle much higher because the sand weighs less -- and the table never moves.",
                "explanation": "Over 20 km high and ~500 km wide, almost 3x Earth's tallest mountain. Reasons: no moving plates (the volcano stays over its hot spot) and only 1/3 of Earth's gravity.",
                "why": "A favorite 'explain with two reasons' question.",
            },
            {
                "term": "The 400 km rule",
                "badge": ("400", "km", ROCK),
                "analogy": "A small rock can be any lumpy shape, but a giant ball of rock gets squeezed round by its own weight.",
                "explanation": "Gravity pulls big objects into spheres. Rocky bodies over ~400 km across are round; smaller ones (like 60-km Ida) can be lumpy.",
                "why": "Connects to the 'round by its own gravity' rule for dwarf planets.",
            },
            {
                "term": "Evolution of rocky-planet air",
                "badge": ("CO₂", "96%", RED),
                "analogy": "Three pots of the same soup: one boiled dry (Venus), one froze (Mars), one stayed just right (Earth).",
                "explanation": "Volcanoes and impacts supplied gas; UV split hydrogen-rich gases, leaving CO2. Mars lost its CO2 and froze; Venus ran away and lost its water; Earth kept liquid water and life changed its air.",
                "why": "THE story of why only Earth stayed habitable.",
            },
        ],
    },
    # ------------------------------------------------------------------ 7
    {
        "unit": 2,
        "name": "Solar System: Venus -- Earth's Scorching Twin",
        "description": "Venus vs. Earth vs. Mars, its slow backward spin, exploring under the clouds with radar, lava plains, continents, volcanoes and coronae, crater ages, and the runaway greenhouse that turned an Earth-like world into an oven.",
        "goals": [
            "Compare Venus, Earth and Mars using the data table.",
            "Explain Venus' slow, backward rotation and why its day is longer than its year.",
            "Describe Venus' surface features and what crater counts say about its age.",
            "Explain the runaway greenhouse effect and why Venus' water loss can't be undone.",
        ],
        "sections": [
            {
                "heading": "Meet Earth's 'twin'",
                "body": (
                    "Venus is the planet that comes closest to Earth -- just 40 million km at its nearest (Mars never gets "
                    "closer than about 56 million km). It orbits the Sun at 0.72 AU (108 million km) on an almost perfect "
                    "circle, and it shines so brightly that, like Mercury, people call it the 'evening star' or 'morning "
                    "star'. Galileo saw that Venus shows a full set of PHASES (lit-up shapes, like the Moon's crescent and "
                    "full), which proved Venus goes around the Sun, not around Earth.\n\n"
                    "On paper Venus is Earth's twin: 0.82 times Earth's mass, almost the same density (5.3 vs 5.5), surface "
                    "gravity 0.91 of Earth's, escape velocity 10.4 km/s, and lots of geological activity. But step outside "
                    "and you would be crushed and cooked: the air presses down 90 times harder than Earth's (90 bars -- like "
                    "being 900 m under the ocean) and the surface is about 730 K (over 450 C, or 850 F) -- hotter than an "
                    "oven's self-cleaning cycle. How did twins turn out so different?"
                ),
                "infographic": "three_planets",
            },
            {
                "heading": "A day longer than a year",
                "body": (
                    "Thick clouds reflect about 70% of the sunlight, so even cameras in orbit can't see the ground. "
                    "Scientists mapped Venus with RADAR -- radio waves that pass through clouds and bounce back off the "
                    "surface. Radar also revealed its spin.\n\n"
                    "Venus rotates once every 243 Earth days, and BACKWARD (from east to west, called RETROGRADE). Its year is "
                    "only 225 Earth days, so a Venus day is longer than its year! Because it spins backward while orbiting, "
                    "the Sun returns to the same spot in Venus' sky every 117 Earth days -- that is one 'sunrise to sunrise'.\n\n"
                    "Why so slow and backward? The most likely cause is TIDES: the Sun's gravity tugging on Venus and its "
                    "heavy atmosphere slowed its spin (TIDAL FRICTION). Another idea is one or more big collisions while "
                    "Venus was forming."
                ),
            },
            {
                "heading": "Exploring under the clouds",
                "body": (
                    "Nearly 50 spacecraft have been launched to Venus, but only about half succeeded. Mariner 2 (USA, 1962) "
                    "made the first flyby. The Soviet Union sent most of the later missions, and Venera 7 (1970) was the "
                    "first probe to land on Venus and send back data -- an amazing feat inside a pressure cooker. NASA's "
                    "Pioneer Venus photographed the cloud tops in ultraviolet light, and the Magellan orbiter made detailed "
                    "radar maps of the whole surface."
                ),
            },
            {
                "heading": "The landscape: lava plains, continents and fresh craters",
                "body": (
                    "About 75% of Venus is low, flat LAVA PLAINS. They look a bit like Earth's ocean floors, but there are no "
                    "SUBDUCTION ZONES (places where one plate dives under another), so Venus never had plate tectonics. The "
                    "plains formed more like the Moon's maria: huge floods of lava.\n\n"
                    "Two 'continents' rise above the plains. APHRODITE, about the size of Africa, stretches a third of the way "
                    "around the equator. ISHTAR, in the north, is about the size of Australia and holds the MAXWELL "
                    "MOUNTAINS, 11 km high. They are named for James Clerk Maxwell, whose ideas about electricity and "
                    "magnetism led to radar; they are the only feature on Venus named after a man. Everything else is named "
                    "for women from history and myths.\n\n"
                    "CRATERS TELL TIME (for the SURFACE, not the planet). Venus' thick air stops small rocks: projectiles "
                    "smaller than about 1 km never reach the ground, so craters smaller than 10 km are rare, and 10-30 km "
                    "craters are often lumpy or doubled because the rock broke apart in the air (like the triple Stein "
                    "crater). Counting only big craters (30 km and up), the plains are just 300 to 600 million years old -- "
                    "between Earth's young ocean floors and its old continents. The largest crater, Mead, is 275 km across, a "
                    "bit bigger than Earth's Chicxulub crater. Nearly every crater looks fresh, so there is almost no "
                    "erosion. It seems Venus had a mysterious, planet-wide volcanic makeover 300 to 600 million years ago."
                ),
                "infographic": "venus_geology",
            },
            {
                "heading": "Volcanoes, pancakes and Miss Piggy",
                "body": (
                    "• Lava floods renew the plains and bury old craters. HOT SPOTS, where the mantle carries heat upward, "
                    "build younger volcanoes.\n"
                    "• SIF MONS, a large volcano, is about 500 km across but only 3 km high -- broader but lower than Hawaii's "
                    "Mauna Loa -- with a 40-km CALDERA (the collapsed crater at a volcano's top) and lava flows up to 500 km "
                    "long.\n"
                    "• Thousands of smaller volcanoes dot the surface, some only the size of a parking lot.\n"
                    "• PANCAKE DOMES are flat, round volcanoes about 25 km across and 2 km tall, made by thick, sludgy "
                    "(VISCOUS) lava that spreads out evenly.\n"
                    "• CORONAE are big round or oval bulges where hot rock pushed up the crust from below without breaking "
                    "through, surrounded by cracks and ridges. One, Fotla Corona, looks like Miss Piggy!\n\n"
                    "Slow churning in the mantle pushes and stretches the crust, cracking the plains into grids of ridges "
                    "(like the Lakshmi Plains) and tearing open rift valleys. Ishtar and the Maxwell Mountains were squeezed "
                    "up by compression, like Earth's Tibetan Plateau and Himalayas. Scientists nickname this style 'blob "
                    "tectonics'."
                ),
            },
            {
                "heading": "Why Venus is so hot: the runaway greenhouse",
                "body": (
                    "Venus is a bit closer to the Sun, but that explains only a little of its heat. The real culprit is the "
                    "greenhouse effect: Venus' air holds almost a MILLION times more carbon dioxide than Earth's. That thick "
                    "CO2 blanket traps infrared heat, and the ground has to get extremely hot before it can radiate away as "
                    "much energy as it receives. Its greenhouse effect adds about 510 C (Earth's adds about 33 C).\n\n"
                    "Was Venus always like this? Maybe not. Picture a young Venus with mild temperatures and oceans, its CO2 "
                    "dissolved in water or locked in rocks -- like Earth. Now add a little extra heat (the Sun slowly brightens "
                    "over time). More water evaporates and more gas escapes from rocks. More CO2 and water vapor make the "
                    "greenhouse stronger, which makes it hotter, which releases even more gas... This loop is the RUNAWAY "
                    "GREENHOUSE EFFECT. It is a FEEDBACK LOOP -- each step makes the next one stronger, like a snowball rolling "
                    "downhill. The planet ends up at a new, much hotter balance.\n\n"
                    "And it is a one-way trip. On Earth, oceans and rocks store most CO2 -- a safety valve. When Venus' oceans "
                    "boiled away, the valve was gone. Ultraviolet sunlight then split the water vapor molecules apart; the "
                    "light hydrogen escaped to space and the oxygen combined with surface rocks. Once water is lost this way, "
                    "it can never come back. So even if we moved Venus into a 'just right' orbit today, it still would not "
                    "have the water life needs.\n\n"
                    "Could Earth run away too? Nobody knows exactly where the tipping point is. But Venus proves a planet "
                    "can't keep heating forever without a dramatic change -- worth remembering as Earth's CO2 rises. Carl "
                    "Sagan was one of the first scientists to show that Venus' thick air acts like a giant greenhouse."
                ),
                "infographic": "runaway_greenhouse",
            },
        ],
        "word_bank": [
            ("Phases", "The changing lit-up shapes of a planet or moon (crescent, half, full) as we see different amounts of its sunny side."),
            ("Radar", "A way of 'seeing' by sending out radio waves and timing their echoes. It sees through clouds."),
            ("Retrograde", "Moving or spinning backward compared with most of the Solar System."),
            ("Tides", "Stretching and squeezing caused by the pull of another body's gravity."),
            ("Tidal friction", "Rubbing inside a body caused by tides, which slowly slows down its spin."),
            ("Lava plains", "Wide, flat areas made of hardened lava floods."),
            ("Subduction zone", "A place where one plate of crust dives beneath another."),
            ("Continent", "A large raised landmass. Venus has two: Aphrodite and Ishtar."),
            ("Caldera", "The large crater at the top of a volcano made when the ground collapses."),
            ("Viscous", "Thick and slow-flowing, like honey or sludge."),
            ("Pancake dome", "A flat, round volcano on Venus made by very thick lava."),
            ("Corona", "On Venus: a large round bulge in the crust pushed up by hot rock from below (plural: coronae)."),
            ("Blob tectonics", "A nickname for how Venus' crust is pushed and puckered by rising hot blobs, without moving plates."),
            ("Feedback loop", "A chain where a change causes more of the same change, making it grow faster and faster."),
            ("Runaway greenhouse effect", "A feedback loop where warming releases more greenhouse gas, causing more warming, until oceans boil away."),
        ],
        "key_facts": [
            "Venus: 0.72 AU (108 million km); year 225 days (0.61 y); day 243 days, retrograde; Sun returns every 117 days.",
            "Closest approach to Earth: 40 million km (Mars: ~56 million km).",
            "Mass 0.82 Earth; diameter 12,102 km; density 5.3; gravity 0.91; escape velocity 10.4 km/s; 90 bars; ~730 K.",
            "Clouds reflect ~70% of sunlight. Mariner 2 (1962) first flyby; Venera 7 (1970) first landing with data; Magellan radar map.",
            "75% lava plains; continents Aphrodite (Africa-size) and Ishtar (Australia-size) with Maxwell Mountains (11 km).",
            "Surface age 300-600 million years; Mead crater 275 km; Sif Mons ~500 km wide, 3 km high.",
            "~1 million times Earth's CO2; greenhouse warming ~510 C. Runaway greenhouse; water loss is irreversible.",
        ],
        "quick_check": [
            ("Why do we call Venus Earth's twin?", "It has almost the same size, mass (0.82 Earth), density and gravity as Earth, and it is geologically active."),
            ("How is it possible for Venus' day to be longer than its year?", "It rotates very slowly (243 days, backward) but orbits the Sun in only 225 days."),
            ("How did scientists map Venus' surface?", "With radar, because radio waves pass through the thick clouds (Magellan made the best map)."),
            ("Why are there almost no small craters on Venus?", "Its thick atmosphere breaks up or stops projectiles smaller than about 1 km."),
            ("Explain the runaway greenhouse in your own words.", "A little warming evaporates water and releases CO2; these gases trap more heat, causing more warming and more gas, until the oceans boil away."),
            ("Why can't Venus get its water back?", "UV light split the water vapor; the hydrogen escaped to space and the oxygen joined rocks, so the water is gone for good."),
        ],
        "cards": [
            {
                "term": "Venus at a glance",
                "badge": ("0.72", "AU", VENUS),
                "analogy": "Earth's twin who moved somewhere much too hot and wrapped up in a thick wool coat.",
                "explanation": "0.72 AU, closest planet to Earth (40 million km). Mass 0.82 Earth, density 5.3, gravity 0.91, but 90 bars of air and ~730 K at the surface. Galileo saw its phases.",
                "why": "The textbook example of a planet that lost its habitability.",
            },
            {
                "term": "Venus' backward spin",
                "badge": ("243 d", "retrograde", VENUS),
                "analogy": "On Venus your birthday comes before the end of a single day!",
                "explanation": "Spins once in 243 days, backward; year is 225 days; sunrise to sunrise takes 117 days. Likely slowed by the Sun's tides, or by giant impacts.",
                "why": "Tidal slowing is part of the tidal-locking story for exoplanets.",
            },
            {
                "term": "Exploring Venus",
                "badge": ("Venera", "7 (1970)", ROCK),
                "analogy": "Like parking a robot inside a pressure cooker on full blast.",
                "explanation": "Mariner 2 (1962) first flyby; Venera 7 (1970) first landing with data; Magellan mapped it by radar because clouds reflect ~70% of sunlight.",
                "why": "Mission firsts are common quick-answer questions.",
            },
            {
                "term": "Venus' surface",
                "badge": ("75%", "lava plains", ROCK),
                "analogy": "Flat lava 'oceans' with two rocky 'continents' poking up.",
                "explanation": "75% lava plains, no plate tectonics. Continents Aphrodite and Ishtar (Maxwell Mountains, 11 km). Volcanoes like Sif Mons, pancake domes and coronae.",
                "why": "Shows a planet can be active without plate tectonics.",
            },
            {
                "term": "Venus' crater ages",
                "badge": ("300-600", "Myr", BLUE),
                "analogy": "Counting dents in a car to guess how long it's been on the road.",
                "explanation": "Few small craters (thick air stops small rocks). Using craters over 30 km, the surface is only 300-600 million years old; craters look fresh, so erosion is tiny. Mead (275 km) is the largest.",
                "why": "Crater counting is used on every world.",
            },
            {
                "term": "Runaway greenhouse",
                "badge": ("LOOP", "runaway", RED),
                "analogy": "A snowball rolling downhill, getting bigger and faster.",
                "explanation": "Venus has ~1 million times Earth's CO2 and ~510 C of greenhouse warming. Extra heat -> more evaporation and gas -> more heat... The oceans boiled away; UV split the water and hydrogen escaped, so the loss is permanent.",
                "why": "It marks the INNER edge of the habitable zone.",
            },
        ],
    },
    # ------------------------------------------------------------------ 8
    {
        "unit": 2,
        "name": "Solar System: Mars -- Following the Water",
        "description": "The red planet's numbers and seasons, the 'canals' myth, thin CO2 air and dust storms, why water can't stay liquid, polar caps, ancient channels and today's salty streaks, the rovers' discoveries, buried ice, and Mars' story of habitability.",
        "goals": [
            "Give Mars' key numbers and explain its seasons and red color.",
            "Explain why liquid water can't last on Mars' surface today.",
            "Describe the evidence that water once flowed on Mars.",
            "Name the rovers and what each discovered.",
        ],
        "sections": [
            {
                "heading": "The red planet",
                "body": (
                    "Mars orbits the Sun at 227 million km (1.52 AU) and comes as close as about 56 million km to Earth. It "
                    "is red because its soil contains IRON OXIDES -- basically rust! That blood-red color is probably why "
                    "ancient people linked it with war.\n\n"
                    "• Year: 1.88 Earth years (686.98 days). Day: 24 hours 37 minutes -- very close to ours.\n"
                    "• Axis tilt: about 25 degrees, so Mars has seasons like Earth's -- each about six months long.\n"
                    "• Mass 0.11 Earth; diameter 6,790 km (about half of Earth's); density 3.9; gravity 0.38 of Earth's (you "
                    "would weigh less than half as much); escape velocity 5.0 km/s; surface area 0.28 of Earth's.\n"
                    "• Two tiny moons, Phobos and Deimos, found in 1877 by Asaph Hall -- probably captured asteroids.\n\n"
                    "Mars is bigger than the Moon and Mercury, so it kept a thin atmosphere and stayed geologically active "
                    "for a long time. Long ago it probably had a thick atmosphere and even seas -- and maybe life still "
                    "hides underground."
                ),
            },
            {
                "heading": "The canal craze (and the Face on Mars)",
                "body": (
                    "Even the best telescopes on Earth see details on Mars only about 100 km across, so no craters or "
                    "mountains show up -- just bright polar caps and dark patches that change with the seasons.\n\n"
                    "In 1877 the Italian astronomer Giovanni Schiaparelli reported faint straight lines he called 'canali' -- "
                    "Italian for channels. In English it was mistranslated as 'canals', which sounds like something built. "
                    "Percival Lowell built an observatory in Flagstaff, Arizona in 1894, drew maps covered with canals and "
                    "wrote books claiming a dying Martian civilization was piping water from the poles. His ideas inspired "
                    "H. G. Wells' novel The War of the Worlds (1897), and a 1938 radio version scared listeners into "
                    "thinking Martians had landed.\n\n"
                    "Bigger telescopes never found the canals. They were an OPTICAL ILLUSION: when our eyes glimpse dim, "
                    "random dots, our brains connect them into lines. The 'Face on Mars', a hill in a Viking photo, is the "
                    "same trick -- our brains love finding faces (this is called PAREIDOLIA). Sharper photos show an "
                    "ordinary MESA (a flat-topped hill). A good lesson in how science tests exciting claims."
                ),
            },
            {
                "heading": "Thin, dusty air",
                "body": (
                    "Mars' air presses down with only 0.007 bar -- less than 1% of Earth's, like the air 30 km above Earth. "
                    "It is 95% carbon dioxide, about 3% nitrogen and 2% argon. That is similar to Venus' recipe, but Venus has "
                    "about 13,000 times more air! Mars' thin air gives only about 2 C of greenhouse warming, so Mars is very "
                    "cold. Some of its air leaked into space, helped by its weak gravity (low escape velocity).\n\n"
                    "Winds can be fast, but thin air pushes weakly (the giant storm in the movie The Martian couldn't really "
                    "happen). Still, wind lifts fine red dust into planet-wide DUST STORMS, whirls up DUST DEVILS (which "
                    "sometimes clean rovers' solar panels!), piles up dunes and carves long ridges called YARDANGS.\n\n"
                    "Mars has three kinds of clouds: dust clouds, water-ice clouds (often around mountains, like on Earth), "
                    "and hazes of frozen carbon dioxide -- 'dry ice' crystals that need about 150 K (-125 C), colder than Earth "
                    "ever gets."
                ),
                "infographic": "mars_ice",
            },
            {
                "heading": "Why there are no puddles on Mars",
                "body": (
                    "Mars is cold, but the bigger problem is PRESSURE. Water's boiling point depends on air pressure: the "
                    "lower the pressure, the lower the boiling point (water boils at a lower temperature on a high mountain). "
                    "Below about 0.006 bar, water's boiling point drops as low as its freezing point. So on most of Mars, "
                    "ice skips the puddle stage and turns straight into vapor -- this is called SUBLIMATION, the same thing "
                    "dry ice does on Earth.\n\n"
                    "Salt helps: it lowers water's freezing point (that's why we salt icy roads in winter), so salty water "
                    "(BRINE) can sometimes stay liquid for a short time on Mars."
                ),
            },
            {
                "heading": "The polar caps",
                "body": (
                    "• SEASONAL CAPS: each winter, when it gets colder than about 150 K, carbon dioxide freezes out of the air "
                    "as a thin frost of dry ice, reaching down to about 50 degrees latitude by spring.\n"
                    "• SOUTH PERMANENT CAP: 350 km across -- frozen CO2 plus lots of water ice, staying at 150 K all summer.\n"
                    "• NORTH PERMANENT CAP: water ice, never smaller than 1,000 km across, about 3 km thick, with about 10 "
                    "million cubic km of ice (as much water as the Mediterranean Sea). It sits in a basin as big as Earth's "
                    "Arctic Ocean basin -- maybe once a shallow sea.\n"
                    "• LAYERED TERRAIN: near both poles, stacks of light and dark layers of dust and ice, each 10 to tens of "
                    "meters thick, record climate cycles every tens of thousands of years -- Martian 'ice ages' caused by "
                    "other planets tugging on Mars' orbit and tilt.\n"
                    "• In 2008 the PHOENIX lander dug a trench near the north pole and found bright white ice that slowly "
                    "vanished (sublimated) over a few days -- real frozen water!\n\n"
                    "A CLASSIC CALCULATION: volume of a layer = area x thickness. Earth's oceans equal a 3-km-deep layer over "
                    "the whole planet: about 1.5 x 10^18 cubic meters, or 1.5 x 10^21 kg of water. One Mars polar cap (2 km "
                    "thick, 400 km radius): pi x (4 x 10^5 m)^2 x 2,000 m = about 1 x 10^15 cubic meters, or 1 x 10^18 kg -- "
                    "only about 0.1% of Earth's oceans. (Earth's Greenland ice sheet, 2.85 x 10^15 cubic meters, holds about "
                    "2.85 times as much.)"
                ),
            },
            {
                "heading": "Follow the water: channels, gullies and salty streaks",
                "body": (
                    "All life on Earth needs liquid water, so the motto for finding life on Mars is 'FOLLOW THE WATER'. "
                    "Mars is covered in clues that water once flowed:\n\n"
                    "• RUNOFF CHANNELS: small, twisting valleys in the old southern highlands, a few meters deep, tens of "
                    "meters wide and 10-20 km long -- like the runoff from ancient rainstorms. Crater counts make them about 4 "
                    "billion years old, from a time when Mars was warmer and wetter.\n"
                    "• OUTFLOW CHANNELS: giants, 10 km or more wide and hundreds of km long. The biggest drain into the Chryse "
                    "basin, where the Pathfinder lander touched down. They were carved by sudden, catastrophic floods when "
                    "frozen ground (PERMAFROST) was melted, perhaps by volcanic heat.\n"
                    "• GULLIES: found by Mars Global Surveyor (whose camera could see objects the size of a truck). They cut "
                    "steep crater walls at high latitudes and are very young: no craters on them, and some cut across recent "
                    "dunes.\n"
                    "• RECURRING SLOPE LINEAE: dark streaks that grow downhill each warm season. In 2015, measurements found "
                    "HYDRATED SALTS (salts with water locked inside) in them, so salty water may trickle 100 m or more before "
                    "it evaporates or soaks in. Where that water comes from is still a mystery.\n\n"
                    "None of these are Lowell's canals -- they are too small to see from Earth, and not straight."
                ),
                "infographic": "mars_water",
            },
            {
                "heading": "Robot geologists on wheels",
                "body": (
                    "• SPIRIT (2004-2010) drove 7.73 km and lasted 20 times longer than planned. It aimed for an old lake bed "
                    "in Gusev crater -- but lava had covered it.\n"
                    "• OPPORTUNITY found layered SEDIMENTARY ROCK (rock built from layers of settled mud and sand) with "
                    "chemical signs of an evaporating salty lake, plus tiny balls of HEMATITE -- a mineral that forms in "
                    "water -- nicknamed 'blueberries'.\n"
                    "• CURIOSITY (landed 2012) explored Gale crater: cracked mudstones from an ancient lake and sandstone laid "
                    "down by flowing water. It showed that ancient Mars was HABITABLE -- it had liquid water, energy and the "
                    "chemical raw materials life needs.\n"
                    "• PERSEVERANCE is exploring Jezero crater (45 km wide), an old lake bed with a river DELTA (the fan of "
                    "mud a river drops where it enters a lake), collecting rock samples to bring back to Earth someday. It "
                    "carried INGENUITY, a little helicopter that made the first powered flight on another planet.\n\n"
                    "From orbit we also see dust-covered glaciers at mid-latitudes and 100-m-tall bands of ice exposed in "
                    "cliffs, just a few meters below the surface. They probably formed in warmer times, and future astronauts "
                    "could use that water."
                ),
            },
            {
                "heading": "The story of Mars",
                "body": (
                    "Early Mars had warmer, wetter times that could have supported life at the surface. Then it lost much of "
                    "its atmosphere -- including the CO2 it needed for greenhouse warming. As it cooled and dried, its lakes "
                    "shrank and became saltier and more acidic, until no liquid water was left at the surface, which became "
                    "bathed in harsh radiation from space. The surface became uninhabitable.\n\n"
                    "But underground, ice and very salty liquid water may still exist, and brine may even trickle on the "
                    "surface sometimes. If life ever took hold on Mars, its traces are hidden in the crust -- which is why "
                    "Mars is still one of the most promising places to look for past or present life."
                ),
            },
        ],
        "word_bank": [
            ("Iron oxide", "A compound of iron and oxygen -- rust. It makes Mars red."),
            ("Optical illusion", "Something your eyes and brain see that isn't really there, like the Martian 'canals'."),
            ("Pareidolia", "Our brain's habit of seeing faces or shapes in random patterns (like the 'Face on Mars')."),
            ("Mesa", "A flat-topped hill with steep sides."),
            ("Dust storm", "Wind lifting huge amounts of dust into the air; on Mars they can cover the whole planet."),
            ("Dust devil", "A small spinning whirlwind that picks up dust."),
            ("Yardang", "A long ridge carved out of rock by wind-blown sand."),
            ("Dry ice", "Frozen carbon dioxide. It turns straight from solid to gas."),
            ("Sublimation", "When a solid turns straight into a gas without melting first."),
            ("Brine", "Very salty water. Salt lets water stay liquid at colder temperatures."),
            ("Polar cap", "A cap of ice at a planet's north or south pole."),
            ("Latitude", "How far north or south of the equator a place is, measured in degrees."),
            ("Permafrost", "Ground that stays frozen all year."),
            ("Runoff channel", "A small winding valley carved by water flowing over the surface, like rain runoff."),
            ("Outflow channel", "A huge channel carved by a sudden, giant flood."),
            ("Gully", "A small channel cut into a steep slope."),
            ("Recurring slope lineae", "Dark streaks on Mars' slopes that grow each warm season, probably from trickles of salty water."),
            ("Hydrated salts", "Salts that have water molecules locked inside them."),
            ("Sedimentary rock", "Rock made from layers of mud, sand or other bits that settled and hardened, often in water."),
            ("Hematite", "An iron mineral that usually forms in water. Opportunity found tiny hematite 'blueberries'."),
            ("Delta", "A fan-shaped pile of mud and sand where a river flows into a lake or sea."),
            ("Habitable", "Able to support life: having liquid water, energy and the right chemical ingredients."),
            ("Rover", "A robot vehicle that drives around on another world."),
        ],
        "key_facts": [
            "Mars: 1.52 AU (227 million km); closest to Earth ~56 million km; year 1.88 y (686.98 days); day 24 h 37 min.",
            "Tilt ~25 degrees -> seasons about 6 months each. Moons Phobos and Deimos (1877, A. Hall).",
            "Mass 0.11 Earth; 6,790 km; density 3.9; gravity 0.38; escape velocity 5.0 km/s.",
            "Air: 0.007 bar; 95% CO2, ~3% N2, ~2% Ar; greenhouse warming ~2 C.",
            "Below ~0.006 bar liquid water can't last -- ice sublimates. Salt helps water stay liquid.",
            "North cap: water ice, >=1,000 km, ~3 km thick, ~10 million km3. South cap: 350 km, CO2 + water ice.",
            "Rovers: Spirit (Gusev), Opportunity ('blueberries'), Curiosity (Gale, ancient habitable lake), Perseverance (Jezero delta) + Ingenuity.",
            "Phoenix (2008) found water ice near the north pole. 2015: hydrated salts in recurring slope lineae.",
        ],
        "quick_check": [
            ("Why is Mars red?", "Its soil contains iron oxides -- rust."),
            ("Why can't liquid water last on Mars' surface?", "The air pressure is so low (below ~0.006 bar) that ice turns straight into vapor; it is also very cold."),
            ("What is the difference between runoff channels and outflow channels?", "Runoff channels are small valleys like rain runoff (~4 billion years old); outflow channels are huge channels carved by sudden giant floods."),
            ("What did Curiosity prove about ancient Mars?", "That Gale crater once held a lake with water, energy and raw materials -- a habitable environment."),
            ("Were Lowell's canals real?", "No. They were an optical illusion -- our brains connected faint dots into lines."),
            ("Why does Mars have only about 2 C of greenhouse warming?", "Its atmosphere is very thin (0.007 bar), so there is little gas to trap heat."),
        ],
        "cards": [
            {
                "term": "Mars at a glance",
                "badge": ("1.52", "AU", MARS),
                "analogy": "Earth's smaller, colder, rusty little sibling.",
                "explanation": "1.52 AU; year 1.88 y; day 24 h 37 min; 25-degree tilt gives seasons; mass 0.11 Earth; gravity 0.38; 0.007 bar of mostly CO2. Moons Phobos and Deimos.",
                "why": "The most promising place in the Solar System to look for past life.",
            },
            {
                "term": "The canals myth",
                "badge": ("canali", "illusion", RED),
                "analogy": "Connecting random dots in the dark into shapes that aren't there.",
                "explanation": "Schiaparelli's 'canali' (channels, 1877) became 'canals'; Lowell imagined Martians. Bigger telescopes showed an optical illusion. The 'Face on Mars' is just a mesa.",
                "why": "How science tests exciting claims.",
            },
            {
                "term": "Why no liquid water",
                "badge": ("0.006", "bar", ICE),
                "analogy": "On Mars, ice behaves like dry ice -- it skips the puddle stage.",
                "explanation": "Below ~0.006 bar the boiling point drops to the freezing point, so ice sublimates. Salt lowers the freezing point, so brine can sometimes flow briefly.",
                "why": "Habitability needs the right temperature AND pressure.",
            },
            {
                "term": "Mars' polar caps",
                "badge": ("CAPS", "CO₂ + H₂O", ICE),
                "analogy": "A permanent ice hat plus a seasonal frosty scarf of dry ice.",
                "explanation": "Seasonal caps are CO2 frost. North permanent cap: water ice, >=1,000 km, ~3 km thick. South: 350 km, CO2 + water ice. Layers record Martian ice ages. Phoenix found water ice in 2008.",
                "why": "Mars' biggest known water supply.",
            },
            {
                "term": "Channels & salty streaks",
                "badge": ("RIVERS", "long ago", BLUE),
                "analogy": "Runoff channels are creeks after a storm; outflow channels are a dam bursting.",
                "explanation": "Runoff channels (~4 billion years old, ancient rain), outflow channels (catastrophic floods), young gullies, and recurring slope lineae with hydrated salts (2015).",
                "why": "Evidence for water on Mars long ago -- and maybe today.",
            },
            {
                "term": "Mars rovers",
                "badge": ("4", "rovers", ROCK),
                "analogy": "Robot geologists with wheels, hunting for old lake beds.",
                "explanation": "Spirit (Gusev, lava-covered lake bed), Opportunity (evaporated salty lake, hematite 'blueberries'), Curiosity (Gale crater: ancient habitable lake), Perseverance (Jezero delta, sample collecting, Ingenuity helicopter).",
                "why": "Curiosity's 'habitable' result is a key 2027 fact.",
            },
            {
                "term": "Mars' habitability story",
                "badge": ("past?", "life", GREEN),
                "analogy": "A house whose lights went out long ago -- but maybe someone's still in the basement.",
                "explanation": "Warm, wet early Mars -> lost its air and greenhouse warming -> lakes got salty and acidic -> dry, radiation-blasted surface. Ice and brine may survive underground.",
                "why": "The storyline habitability questions expect you to explain.",
            },
        ],
    },
]
