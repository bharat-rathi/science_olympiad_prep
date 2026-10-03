"""Chapters added so the study plan covers every item on the 2027 Division
B Solar System rules that the reader/wiki-based chapters didn't: the three
named extrasolar systems, the no-calculator habitability math, water's
forms and extremophiles (plus water delivery by small bodies), and the
2027 mission list with spacecraft design. Same lesson-chapter format as
lessons_unit1.py; facts are rounded published NASA/ESA values and standard
textbook science. Microlensing is added to the existing "Finding
Exoplanets" chapter in lessons_unit5.py, where the other methods live.
"""

from app.content.solar_system.svg import BLUE, GAS, GOLD, GREEN, ICE, PURPLE, RED, ROCK, SUN

HABITABILITY_MATH = {
    "unit": 5,
    "name": "Solar System: Habitability Math -- Light, Heat, Gases & Chemistry",
    "description": "The 2027 rules' no-calculator math: flux and albedo, Stefan-Boltzmann and Wien's laws, equilibrium temperature, the Doppler shift, tidal forces, the ideal gas law and keeping an atmosphere, Arrhenius reaction rates and chemical disequilibrium -- plus estimating and checking units.",
    "goals": [
        "Use the Stefan-Boltzmann and Wien laws to compare stars and planets.",
        "Estimate a planet's equilibrium temperature by scaling, without a calculator.",
        "Explain how albedo, distance and the greenhouse effect set a planet's temperature.",
        "Explain why small, hot planets lose light gases, using the ideal gas law.",
        "Explain how temperature controls reaction rates and why chemical disequilibrium matters for life.",
    ],
    "sections": [
        {
            "heading": "No calculator? No problem",
            "body": (
                "Calculators are NOT allowed in 2027 Solar System, so the math is about RATIOS and SCALING, not long "
                "arithmetic. Three tricks do most of the work:\n\n"
                "• SCALE, DON'T SOLVE. If a formula says T ~ 1/sqrt(d), then 4x the distance means 1/sqrt(4) = 1/2 the "
                "temperature. You never need the constants.\n"
                "• ORDER OF MAGNITUDE. Round to powers of ten: 3 x 10^8 m/s for light, 1.5 x 10^11 m for 1 AU. "
                "(30 m/s) / (3 x 10^8 m/s) = 10^-7.\n"
                "• DIMENSIONAL ANALYSIS. Check units. If you're solving for a speed, your answer must come out in m/s. "
                "If the units don't work, the formula is wrong.\n\n"
                "Many questions ask you to REARRANGE an equation (for example, solve L = 4 pi R^2 sigma T^4 for T) or to "
                "SKETCH a graph (how does temperature change with distance?). Practice those as much as plugging in numbers."
            ),
        },
        {
            "heading": "Glowing with heat: Stefan-Boltzmann and Wien",
            "body": (
                "Everything warm glows. Two laws describe that glow for an ideal glowing object (a BLACKBODY):\n\n"
                "STEFAN-BOLTZMANN LAW: the power given off by each square meter of surface = sigma x T^4, where T is in "
                "kelvin and sigma is a constant. Because of the 4th power, DOUBLING the temperature makes it 2^4 = 16 "
                "times brighter per square meter. A whole star's LUMINOSITY is L = 4 pi R^2 sigma T^4 (surface area x "
                "power per square meter). So a star can be bright because it is HOT or because it is BIG.\n"
                "Example: TRAPPIST-1 is a bit under half the Sun's temperature (2,550 K vs. 5,770 K) and about 1/9 of "
                "its radius. Estimate: (1/9)^2 x (1/2)^4 = 1/81 x 1/16 = about 1/1,300 of the Sun's luminosity. The "
                "measured value is about 1/1,800 -- the same order of magnitude, which is all an estimate needs.\n\n"
                "WIEN'S DISPLACEMENT LAW: hotter objects glow at SHORTER wavelengths. Peak wavelength = b / T, with "
                "b = about 2,900 micrometer-kelvins.\n"
                "• The Sun (5,800 K): 2,900 / 5,800 = 0.5 micrometers -- visible (green-yellow) light.\n"
                "• TRAPPIST-1 (2,550 K): about 1.1 micrometers -- near-INFRARED. Planets around red dwarfs get mostly "
                "infrared light, which matters for photosynthesis and for which telescopes can study them (JWST is an "
                "infrared telescope).\n"
                "• Earth (about 290 K): about 10 micrometers -- thermal infrared, which is the heat greenhouse gases trap."
            ),
            "infographic": "habitability_math",
        },
        {
            "heading": "Flux, albedo and a planet's temperature",
            "body": (
                "FLUX is the starlight energy hitting each square meter. It follows the inverse-square law you met in the "
                "Habitable Zone chapter: flux = L / (4 pi d^2), so twice as far means 1/4 the flux.\n\n"
                "ALBEDO is the fraction of that light a planet REFLECTS back to space (0 = perfectly black, 1 = perfect "
                "mirror). Reflected light doesn't heat the planet. Rough values: the Moon ~0.1 (dark rock), Earth ~0.3, "
                "Venus ~0.75 (bright clouds), and Enceladus' fresh ice reflects over 90% of sunlight -- NASA calls it the "
                "most reflective body in the Solar System.\n\n"
                "EQUILIBRIUM TEMPERATURE (T_eq) is the temperature a planet would settle at if the energy it absorbs "
                "equals the energy it radiates away, with NO greenhouse effect:\n"
                "T_eq = T_star x sqrt(R_star / 2d) x (1 - A)^(1/4)\n"
                "Earth's T_eq is about 255 K (-18 C). Earth is actually about 288 K (15 C): the ~33 degrees of difference "
                "is the greenhouse effect. Venus' real surface (~735 K) is hundreds of degrees above its T_eq -- a runaway "
                "greenhouse.\n\n"
                "SCALING TRICKS (same star, same albedo): T_eq ~ 1/sqrt(d).\n"
                "• A planet at 4 AU: 255 K / sqrt(4) = ~128 K.\n"
                "• A planet at 1/4 AU: 255 K x 2 = ~510 K.\n"
                "And for different stars at the same distance, T_eq ~ L^(1/4): a star 16 times brighter makes its "
                "planets 2 times hotter. A higher albedo always cools a planet, but only through the gentle 1/4 power."
            ),
        },
        {
            "heading": "Doppler shifts and tidal forces",
            "body": (
                "DOPPLER SHIFT (from the Finding Exoplanets chapter) as a formula: (change in wavelength) / (wavelength) "
                "= v / c, where v is the speed toward or away from us and c is the speed of light (3 x 10^8 m/s). Jupiter "
                "wobbles the Sun at about 13 m/s, so the shift is about 13 / (3 x 10^8) = about 4 x 10^-8 of the "
                "wavelength -- that is why the Doppler method needs extremely precise spectrographs. Blueshift = moving "
                "toward us; redshift = moving away.\n\n"
                "TIDAL FORCES: gravity pulls harder on the near side of a moon or planet than on its far side, stretching "
                "it. Gravity itself falls off as 1/r^2, but the STRETCH falls off as M / r^3. So:\n"
                "• Twice as far = 1/8 the tidal stretch.\n"
                "• Half as far = 8 times the stretch.\n"
                "That steep 1/r^3 is why Io (close to Jupiter) is volcanic while Callisto (far out) is quiet, why close-in "
                "planets like TRAPPIST-1's are tidally locked, and why TIDAL HEATING can keep oceans liquid inside "
                "Europa and Enceladus far from the Sun.\n\n"
                "ENERGY: kinetic energy = (1/2) m v^2 and gravitational potential energy = -G M m / r. Setting them equal "
                "gives escape velocity v = sqrt(2 G M / r) (see Gravity & Kepler's Laws): bigger, denser worlds are "
                "harder to escape."
            ),
        },
        {
            "heading": "Gases: the ideal gas law and keeping an atmosphere",
            "body": (
                "The IDEAL GAS LAW: P V = n R T (pressure x volume = amount of gas x a constant x temperature in kelvin). "
                "Useful rearrangements:\n"
                "• Fixed volume: double the temperature -> double the pressure.\n"
                "• Fixed pressure: double the temperature -> double the volume (warm air expands and rises).\n"
                "• More gas (n) at the same T and V -> more pressure. Venus has about 90 times Earth's surface pressure "
                "because its atmosphere holds vastly more gas.\n\n"
                "WHY SOME WORLDS LOSE THEIR AIR: gas molecules zoom around with kinetic energy set by temperature: "
                "(1/2) m v^2 ~ T, so a molecule's typical speed is v ~ sqrt(T / m).\n"
                "• LIGHT molecules move FASTER: hydrogen (mass 2) moves sqrt(32 / 2) = 4 times faster than oxygen "
                "(mass 32) at the same temperature.\n"
                "• HOTTER gas moves faster: 4x the temperature = 2x the speed.\n"
                "A planet keeps a gas for billions of years only if its ESCAPE VELOCITY is several times (about 6x) that "
                "gas's typical speed. That's why Earth lost its hydrogen but kept nitrogen and oxygen, why Jupiter keeps "
                "even hydrogen, and why Titan -- small but very cold (94 K) -- keeps a thick nitrogen atmosphere.\n\n"
                "Gas can also be STRIPPED by the solar wind if a planet has no global magnetic field to shield it -- one "
                "big reason Mars lost most of its air (measured by MAVEN). Planets close to flaring red dwarfs, like "
                "TRAPPIST-1's, face the same danger."
            ),
        },
        {
            "heading": "Chemistry: reaction rates and disequilibrium",
            "body": (
                "THE ARRHENIUS EQUATION tells how fast a chemical reaction goes: k = A e^(-Ea / RT), where Ea is the "
                "ACTIVATION ENERGY (the 'hill' molecules must climb to react) and T is the temperature in kelvin. You "
                "don't need to compute it -- just know what it says:\n"
                "• HOTTER = FASTER. A rough rule near room temperature: +10 C about doubles a reaction's rate.\n"
                "• A bigger activation energy = a slower reaction, and more sensitive to temperature.\n"
                "• Very cold worlds (Titan at 94 K) have extremely slow chemistry -- one reason scientists wonder whether "
                "life could work there at all. CATALYSTS (like the ENZYMES in cells) lower the hill and speed reactions up "
                "without being used up.\n\n"
                "CHEMICAL EQUILIBRIUM: left alone, a mix of chemicals reacts until it settles into a stable state and "
                "nothing more happens -- no more energy to use. CHEMICAL DISEQUILIBRIUM means a mix that SHOULD react but "
                "hasn't yet -- like a charged battery. It matters for habitability in two ways:\n"
                "1. AS FOOD: life gets energy by letting disequilibrium 'run downhill'. Europa's chemical battery "
                "(oxidants from the surface + reducing chemicals from the seafloor) and the hydrogen gas Cassini found in "
                "Enceladus' plume (2017) are both disequilibrium energy sources.\n"
                "2. AS A SIGN OF LIFE: Earth's air holds oxygen AND methane together. They destroy each other, so they "
                "only coexist because life keeps making both. Finding a strong disequilibrium like that on an exoplanet "
                "would be a powerful BIOSIGNATURE."
            ),
        },
    ],
    "word_bank": [
        ("Order of magnitude", "A rough size measured in powers of ten (10, 100, 1,000...)."),
        ("Dimensional analysis", "Checking that the units in a calculation work out, to catch mistakes."),
        ("Blackbody", "An ideal object that absorbs all light and glows only because of its temperature."),
        ("Stefan-Boltzmann law", "Power per square meter = sigma x T^4: twice as hot glows 16 times brighter."),
        ("Luminosity", "The total power a star gives off: L = 4 pi R^2 sigma T^4."),
        ("Wien's displacement law", "Peak wavelength = b / T: hotter objects glow at shorter (bluer) wavelengths."),
        ("Flux", "Energy arriving per square meter each second; falls off as 1/d^2."),
        ("Albedo", "The fraction of light a surface reflects (0 = black, 1 = mirror)."),
        ("Equilibrium temperature", "A planet's temperature if absorbed and emitted energy balance, with no greenhouse effect."),
        ("Tidal force", "The stretching caused by gravity pulling harder on the near side; falls off as 1/r^3."),
        ("Ideal gas law", "PV = nRT: links a gas's pressure, volume, amount and temperature."),
        ("Activation energy", "The energy 'hill' molecules must get over before they can react."),
        ("Arrhenius equation", "k = A e^(-Ea/RT): reaction rates rise steeply with temperature."),
        ("Catalyst", "Something that speeds up a reaction without being used up; enzymes are catalysts in cells."),
        ("Chemical disequilibrium", "A mixture that should react but hasn't yet -- stored chemical energy."),
    ],
    "key_facts": [
        "No calculator in 2027: scale with ratios, round to powers of ten, check units, rearrange equations.",
        "Stefan-Boltzmann: power/m^2 = sigma T^4 (2x T = 16x); L = 4 pi R^2 sigma T^4.",
        "Wien: peak = 2,900 µm·K / T. Sun 0.5 µm (visible); TRAPPIST-1 ~1.1 µm (IR); Earth ~10 µm.",
        "Albedo: Moon ~0.1, Earth ~0.3, Venus ~0.75, Enceladus > 0.9 (most reflective body in the Solar System).",
        "T_eq = T_star sqrt(R_star/2d) (1-A)^(1/4). Earth T_eq ~255 K vs. actual ~288 K (greenhouse +33). Same star: T_eq ~ 1/sqrt(d).",
        "Doppler: delta-lambda/lambda = v/c. Tidal stretch ~ M/r^3 (2x farther = 1/8).",
        "Gas speed ~ sqrt(T/m); H2 is 4x faster than O2. Keep a gas if escape velocity > ~6x its speed.",
        "Arrhenius: hotter = faster (~2x per +10 C). O2 + CH4 together = disequilibrium biosignature.",
    ],
    "quick_check": [
        ("Star A has twice the surface temperature of star B and the same radius. How much more luminous is it?", "2^4 = 16 times (Stefan-Boltzmann: L ~ R^2 T^4)."),
        ("A star is 2,900 K. At what wavelength does it glow brightest?", "2,900 / 2,900 = about 1 micrometer, in the near-infrared."),
        ("Earth's equilibrium temperature is ~255 K. Estimate it for a planet with the same albedo 9 AU from the Sun.", "255 / sqrt(9) = 255 / 3 = about 85 K."),
        ("Why is Earth's real average temperature higher than its equilibrium temperature?", "The greenhouse effect: water vapor and CO2 trap outgoing infrared, adding about 33 degrees."),
        ("A moon moves to half its distance from its planet. How does the tidal stretch change?", "It grows 2^3 = 8 times (tidal force ~ 1/r^3)."),
        ("Why can tiny, cold Titan keep a thick nitrogen atmosphere?", "At 94 K nitrogen molecules move slowly, so even Titan's low escape velocity holds them."),
        ("Why would finding oxygen and methane together on an exoplanet be exciting?", "They react and destroy each other, so something -- probably life -- must keep replacing both: chemical disequilibrium."),
    ],
    "cards": [
        {
            "term": "Stefan-Boltzmann law",
            "badge": ("T⁴", "power", GOLD),
            "analogy": "Turning up a stove burner a little makes it glow a LOT brighter.",
            "explanation": "Power per square meter = sigma x T^4. Double T -> 16x. A star's luminosity L = 4 pi R^2 sigma T^4, so big OR hot stars are bright.",
            "why": "Lets you compare stars and planets with pure ratios -- perfect for a no-calculator test.",
        },
        {
            "term": "Wien's displacement law",
            "badge": ("b/T", "peak", RED),
            "analogy": "A heated poker goes from dull red to orange to white as it gets hotter.",
            "explanation": "Peak wavelength = 2,900 µm·K / T. Sun (5,800 K) peaks at 0.5 µm (visible); red dwarfs peak in the infrared; Earth glows at ~10 µm.",
            "why": "Explains why red-dwarf planets get mostly infrared light and why we use infrared telescopes.",
        },
        {
            "term": "Albedo",
            "badge": ("A", "reflect", ICE),
            "analogy": "A white T-shirt stays cooler in the sun than a black one.",
            "explanation": "Fraction of light reflected. Moon ~0.1, Earth ~0.3, Venus ~0.75, Enceladus' fresh ice > 0.9 (most reflective in the Solar System). Reflected light doesn't heat the planet.",
            "why": "One of the three inputs to equilibrium temperature.",
        },
        {
            "term": "Equilibrium temperature",
            "badge": ("255 K", "Earth", GREEN),
            "analogy": "A bathtub with the tap and drain balanced -- the water level stops changing.",
            "explanation": "T_eq = T_star sqrt(R_star/2d) (1-A)^(1/4), with no greenhouse. Earth's is ~255 K; real Earth is ~288 K. Same star: T_eq ~ 1/sqrt(d).",
            "why": "The go-to calculation for 'could this planet have liquid water?'.",
        },
        {
            "term": "Tidal force (1/r³)",
            "badge": ("1/r³", "tides", PURPLE),
            "analogy": "Stretching taffy: pull one end harder than the other and it lengthens.",
            "explanation": "Tidal stretch ~ M / r^3: twice as far = 1/8. Drives tidal locking and tidal heating (Io, Europa, Enceladus, TRAPPIST-1 planets).",
            "why": "Tidal heating is how moons far from the Sun can still have liquid oceans.",
        },
        {
            "term": "Ideal gas law & escape",
            "badge": ("PV=nRT", "gases", GAS),
            "analogy": "A crowd of bouncing ping-pong balls -- the lightest, fastest ones fly over the fence first.",
            "explanation": "PV = nRT. Molecule speed ~ sqrt(T/m): H2 is 4x faster than O2. A world keeps a gas if escape velocity is ~6x the gas's speed; Titan's cold keeps its N2.",
            "why": "Explains which planets keep atmospheres -- a must for habitability.",
        },
        {
            "term": "Arrhenius equation",
            "badge": ("e^-Ea/RT", "rates", ROCK),
            "analogy": "Popcorn pops faster the hotter the pan.",
            "explanation": "k = A e^(-Ea/RT): reactions speed up steeply with temperature (~2x per +10 C near room temperature). Enzymes (catalysts) lower the activation-energy hill.",
            "why": "Cold worlds like Titan have very slow chemistry -- a challenge for life.",
        },
        {
            "term": "Chemical disequilibrium",
            "badge": ("O2+CH4", "biosig", BLUE),
            "analogy": "A charged battery: the energy is there until something lets it flow.",
            "explanation": "A mix that should react but hasn't. Food for life (Europa's chemical battery, H2 in Enceladus' plume) and a biosignature (Earth's O2 + CH4).",
            "why": "Ties chemistry to both habitability and detecting life.",
        },
    ],
}

WATER_AND_EXTREMOPHILES = {
    "unit": 5,
    "name": "Solar System: Water's Many Forms, Life's Building Blocks & Extremophiles",
    "description": "Liquid water, crystalline and amorphous ice, brines and clathrates; reading composition from spectra; how comets and asteroids delivered water and organics (Rosetta, OSIRIS-REx); the four families of life's molecules; and extremophiles, chemolithoautotrophs and tardigrades.",
    "goals": [
        "Describe liquid water, crystalline and amorphous ice, brines and clathrates, and where each is found.",
        "Explain how spectra reveal what a surface or atmosphere is made of.",
        "Explain the evidence on whether comets or asteroids delivered Earth's water and organics.",
        "Name the four families of biological molecules.",
        "Describe extremophiles, chemolithoautotrophs and tardigrades, and why they matter for life elsewhere.",
    ],
    "sections": [
        {
            "heading": "Water isn't just water",
            "body": (
                "'Follow the water' means following LIQUID water -- but water shows up in many forms, and each one changes "
                "where liquid could hide.\n\n"
                "• LIQUID WATER needs the right temperature AND pressure. At its TRIPLE POINT (0.01 C and 611 pascals, "
                "about 0.006 of Earth's air pressure) ice, liquid and vapor can all exist together. Mars' average surface "
                "pressure is right around that value, which is why liquid water there boils or freezes almost at once.\n"
                "• CRYSTALLINE ICE: molecules locked in a neat, repeating pattern. Ordinary ice (called ice Ih) is "
                "hexagonal -- which is why snowflakes have six sides. Under the huge pressures deep inside Ganymede and "
                "Titan, water squeezes into denser crystal forms (like ice VI) that sink, so an ocean can be sandwiched "
                "between ice layers.\n"
                "• AMORPHOUS ICE: water frozen so cold and fast (below about 130 K) that the molecules never line up -- "
                "like glass instead of a crystal. It is thought to be the most common form of water ice in the universe: it coats "
                "interstellar dust grains and is found in comets, and it can trap other gases inside.\n"
                "• BRINES: salty water. Dissolved salt LOWERS the freezing point, so brines stay liquid far below 0 C. "
                "Perchlorate salts on Mars can keep water liquid down to about -70 C; the oceans of Europa and Enceladus "
                "are salty; and the bright spots in Ceres' Occator crater are salt (sodium carbonate) left behind by "
                "briny water.\n"
                "• CLATHRATES: ice 'cages' that trap gas molecules such as methane or CO2 inside. On Earth, methane "
                "clathrate ('fire ice') sits on the seafloor and in permafrost. Clathrates may store methane inside "
                "Titan (refilling its atmosphere) and trap gases on Mars and in comets."
            ),
            "infographic": "water_forms",
        },
        {
            "heading": "Reading composition from light",
            "body": (
                "How do we know what a world is made of from millions of kilometers away? SPECTROSCOPY. When light is "
                "spread into a spectrum, atoms and molecules leave dark ABSORPTION features at wavelengths that act like "
                "fingerprints.\n\n"
                "• Water ice absorbs strongly near 1.5 and 2.0 micrometers in the infrared -- that is how ice is mapped on "
                "Europa, Ganymede and comets. Crystalline and amorphous ice even have slightly different fingerprints, "
                "which tells us how cold and how old the ice is.\n"
                "• Clay minerals and salts that only form in water show up from orbit (Mars Reconnaissance Orbiter's CRISM "
                "spectrometer mapped clays on Mars).\n"
                "• Gases in an exoplanet's air are read during transits (transit spectroscopy): JWST found carbon dioxide "
                "on the hot gas giant WASP-39 b.\n\n"
                "Geologic shapes are evidence too -- dry riverbeds, deltas and outflow channels on Mars (see the Mars "
                "chapter) show where liquid water once flowed even though none flows today."
            ),
        },
        {
            "heading": "Special delivery: did comets or asteroids bring our water?",
            "body": (
                "Early Earth was probably too hot to hold much water as it formed, so some or most of the oceans may have "
                "been DELIVERED later by small bodies. The clue scientists use is the D/H RATIO: how much DEUTERIUM "
                "('heavy hydrogen', with an extra neutron) the water holds compared with normal hydrogen. Water from "
                "different places in the early Solar System has different D/H ratios -- like a return address.\n\n"
                "• ROSETTA (ESA) orbited comet 67P/Churyumov-Gerasimenko from 2014 to 2016. Its water had about THREE "
                "times Earth's D/H ratio, so comets like 67P can't have supplied most of our oceans. Rosetta also found "
                "glycine (an amino acid) and phosphorus around the comet -- ingredients for life.\n"
                "• Carbon-rich asteroids (and the meteorites that come from them) have water much closer to Earth's D/H, "
                "so asteroids are the favorite suspects.\n"
                "• OSIRIS-REx (NASA) returned about 121 grams of asteroid BENNU to Earth in September 2023. In the "
                "pristine sample scientists found 14 of the 20 amino acids life uses in proteins, all five nucleobases "
                "used in DNA and RNA, ammonia, and salts left behind when salty water evaporated -- showing that life's "
                "ingredients, and briny water, existed on small bodies early on."
            ),
        },
        {
            "heading": "The four families of life's molecules",
            "body": (
                "All life we know is built from four families of large carbon-based molecules:\n\n"
                "• PROTEINS: chains of AMINO ACIDS (life uses 20 kinds). They build tissues and act as ENZYMES that speed "
                "up chemical reactions.\n"
                "• NUCLEIC ACIDS: DNA and RNA, chains of NUCLEOTIDES that store and copy genetic information using the "
                "bases A, G, C and T (in DNA) or U (in RNA).\n"
                "• LIPIDS: fats and oils. They form CELL MEMBRANES -- the bubble-like boundary that keeps a cell's "
                "chemistry inside. Lipids naturally form little bubbles in water.\n"
                "• CARBOHYDRATES: sugars and starches. They store energy, and the sugar ribose forms the backbone of RNA.\n\n"
                "Meteorites, comets and the Bennu sample show that simple versions of these building blocks (amino acids, "
                "nucleobases, sugars) form naturally in space."
            ),
        },
        {
            "heading": "Extremophiles: life where it 'shouldn't' be",
            "body": (
                "EXTREMOPHILES are organisms that THRIVE in conditions that would kill most life. Every new one widens "
                "the list of places where life might exist beyond Earth.\n\n"
                "• THERMOPHILES and HYPERTHERMOPHILES love heat: a microbe nicknamed 'Strain 121' grows at 121 C near "
                "deep-sea hydrothermal vents.\n"
                "• PSYCHROPHILES love cold, growing below 0 C in sea ice and salty brines -- relevant to icy moons and Mars.\n"
                "• HALOPHILES love salt, living in water about 10 times saltier than the ocean.\n"
                "• ACIDOPHILES live at pH near 0; ALKALIPHILES at pH 11 or higher.\n"
                "• PIEZOPHILES (BAROPHILES) thrive under crushing pressure at the bottom of the Mariana Trench.\n"
                "• RADIATION-RESISTANT microbes like Deinococcus radiodurans survive radiation doses thousands of "
                "times higher than would kill a human.\n\n"
                "CHEMOLITHOAUTOTROPHS break into three parts: CHEMO (energy from chemical reactions, not sunlight) + "
                "LITHO ('rock' -- inorganic chemicals like hydrogen, sulfur or iron) + AUTOTROPH ('self-feeder' -- builds "
                "its own food from CO2). They power whole ecosystems at hydrothermal vents in total darkness. METHANOGENS "
                "are an example: they combine hydrogen gas and CO2 to make methane and energy. That is exactly why the "
                "hydrogen gas Cassini found in Enceladus' plume is so exciting -- it is the kind of food chemolithoautotrophs "
                "eat, in an ocean with no sunlight."
            ),
            "infographic": "extremophiles",
        },
        {
            "heading": "Tardigrades: the toughest animals",
            "body": (
                "TARDIGRADES ('water bears') are eight-legged animals about half a millimeter long that live in moss, "
                "soil and water all over Earth. When their home dries out, they curl into a shriveled state called a "
                "TUN and almost stop their metabolism (CRYPTOBIOSIS). In that state they have survived being frozen to "
                "near absolute zero, heated well above boiling for a few minutes, squeezed at pressures thousands of times "
                "Earth's air pressure, heavy radiation -- and in 2007, 10 days exposed to the vacuum and radiation of "
                "space on the FOTON-M3 mission.\n\n"
                "Careful with the word: tardigrades SURVIVE extremes but don't grow and reproduce in them, so scientists "
                "call them EXTREMOTOLERANT rather than true extremophiles. They show how tough life can be -- and why "
                "spacecraft are cleaned carefully so we don't carry Earth life to other worlds (planetary protection)."
            ),
        },
    ],
    "word_bank": [
        ("Triple point", "The temperature and pressure where ice, liquid water and vapor can all exist together (0.01 C, 611 Pa)."),
        ("Crystalline ice", "Ice whose molecules sit in a neat, repeating pattern; ordinary ice is hexagonal."),
        ("Amorphous ice", "Ice frozen so cold and fast that the molecules never line up into a crystal."),
        ("Brine", "Very salty water; salt lowers its freezing point so it stays liquid below 0 C."),
        ("Perchlorate", "A salt found in Martian soil that keeps brines liquid at very low temperatures."),
        ("Clathrate", "An ice 'cage' that traps gas molecules such as methane or CO2 inside."),
        ("Spectroscopy", "Spreading light into its colors to read the fingerprints of the chemicals that made or absorbed it."),
        ("Absorption feature", "A dark dip in a spectrum where a substance soaked up a particular wavelength."),
        ("Deuterium", "'Heavy hydrogen': hydrogen with one proton AND one neutron."),
        ("D/H ratio", "How much deuterium water holds compared with normal hydrogen -- a clue to where the water came from."),
        ("Protein", "A chain of amino acids; builds tissues and acts as enzymes."),
        ("Nucleotide", "The repeating unit of DNA and RNA, containing a base (A, G, C, T or U)."),
        ("Lipid", "A fat or oil molecule; lipids form cell membranes."),
        ("Carbohydrate", "A sugar or starch; stores energy, and ribose sugar is part of RNA."),
        ("Extremophile", "An organism that thrives in extreme heat, cold, salt, acid, pressure or radiation."),
        ("Psychrophile", "A cold-loving extremophile that grows below 0 C."),
        ("Halophile", "A salt-loving extremophile."),
        ("Piezophile", "A pressure-loving extremophile (also called a barophile)."),
        ("Chemolithoautotroph", "A microbe that gets energy from inorganic chemicals and builds its own food from CO2 -- no sunlight needed."),
        ("Methanogen", "A microbe that makes methane from hydrogen and CO2."),
        ("Tardigrade", "A tiny 'water bear' animal that survives extremes by drying into a dormant tun."),
        ("Cryptobiosis", "A state where an organism's metabolism almost stops so it can survive harsh conditions."),
    ],
    "key_facts": [
        "Triple point of water: 0.01 C, 611 Pa -- about Mars' surface pressure, so liquid water there is barely possible.",
        "Ice Ih = ordinary hexagonal crystalline ice; high-pressure ices (e.g. ice VI) inside Ganymede/Titan.",
        "Amorphous ice: forms below ~130 K, no crystal; thought to be the most common ice in the universe (dust grains, comets).",
        "Brines stay liquid far below 0 C (Mars perchlorates ~-70 C); Ceres' bright spots = salt.",
        "Clathrates: ice cages trapping CH4/CO2 ('fire ice'); may resupply Titan's methane.",
        "Rosetta: comet 67P water D/H ~3x Earth's -> not the main source of our oceans; glycine + phosphorus found.",
        "OSIRIS-REx: ~121 g of Bennu returned Sept 2023; 14 of 20 protein amino acids, all 5 nucleobases, ammonia, evaporated-brine salts.",
        "Four molecule families: proteins, nucleic acids, lipids (membranes), carbohydrates.",
        "Chemolithoautotroph = chemical energy + inorganic food + makes own food from CO2; methanogens use H2 + CO2 (Enceladus' H2!).",
        "Tardigrades survived 10 days in open space (FOTON-M3, 2007); extremotolerant, not true extremophiles.",
    ],
    "quick_check": [
        ("Why does a brine stay liquid at temperatures where pure water freezes?", "Dissolved salt lowers the freezing point."),
        ("How is amorphous ice different from ordinary ice, and where is it found?", "Its molecules aren't arranged in a crystal pattern; it forms below ~130 K, on interstellar dust and in comets."),
        ("What is a clathrate?", "Ice that traps gas molecules like methane or CO2 inside cages of water molecules."),
        ("What did Rosetta's D/H measurement of comet 67P suggest about Earth's oceans?", "67P's water had ~3x Earth's D/H, so comets like it didn't supply most of Earth's water."),
        ("Name two life-related findings in the Bennu sample.", "Any two: 14 of the 20 protein amino acids, all five nucleobases, ammonia, salts from evaporated brine."),
        ("Break 'chemolithoautotroph' into its three parts.", "Chemo = energy from chemicals; litho = from inorganic (rock) chemicals; autotroph = makes its own food from CO2."),
        ("Why are tardigrades called extremotolerant rather than extremophiles?", "They survive extremes in a dormant state but don't grow and reproduce in them."),
    ],
    "cards": [
        {
            "term": "Forms of water",
            "badge": ("H₂O", "5 forms", BLUE),
            "analogy": "The same LEGO bricks can be a loose pile, a neat wall or a cage around a toy.",
            "explanation": "Liquid; crystalline ice (hexagonal Ih, high-pressure ices inside big moons); amorphous ice (no crystal, below ~130 K); brines (salty, liquid below 0 C); clathrates (gas-trapping cages).",
            "why": "The 2027 rules list each form by name.",
        },
        {
            "term": "Triple point",
            "badge": ("611 Pa", "0.01 C", ICE),
            "analogy": "A three-way intersection where ice, water and vapor can all meet.",
            "explanation": "At 0.01 C and 611 Pa all three phases coexist. Mars' surface pressure is about this low, so liquid water there quickly boils or freezes.",
            "why": "Explains why Mars has ice and vapor but no lasting puddles.",
        },
        {
            "term": "Clathrate",
            "badge": ("CAGE", "CH4 / CO2", GOLD),
            "analogy": "A jail made of ice with gas molecules locked inside each cell.",
            "explanation": "Water-ice cages that trap gases like methane or CO2. 'Fire ice' on Earth's seafloor; may store and slowly release methane inside Titan.",
            "why": "A way icy worlds can store and resupply atmospheric gases.",
        },
        {
            "term": "D/H ratio",
            "badge": ("D/H", "3x", PURPLE),
            "analogy": "A postmark that tells you which post office a letter came from.",
            "explanation": "Deuterium-to-hydrogen ratio in water. Rosetta found comet 67P's water at ~3x Earth's, so asteroids (closer match) are the favored source of our oceans.",
            "why": "The key evidence for 'delivery of water from small bodies'.",
        },
        {
            "term": "OSIRIS-REx & Bennu",
            "badge": ("121 g", "Bennu", ROCK),
            "analogy": "A cosmic pantry sample showing what ingredients were on the shelf 4.5 billion years ago.",
            "explanation": "Sample landed in Utah, Sept 24, 2023. Contains 14 of 20 protein amino acids, all 5 nucleobases, ammonia and salts from evaporated brine.",
            "why": "Direct proof that small bodies carry life's building blocks and once held briny water.",
        },
        {
            "term": "Four molecules of life",
            "badge": ("4", "families", GREEN),
            "analogy": "Bricks (proteins), blueprints (nucleic acids), walls (lipids) and fuel (carbohydrates).",
            "explanation": "Proteins (amino-acid chains, enzymes), nucleic acids (DNA/RNA, nucleotides), lipids (cell membranes), carbohydrates (sugars; ribose in RNA).",
            "why": "The rules list all four under 'basic biology and chemistry'.",
        },
        {
            "term": "Extremophiles",
            "badge": ("121 C", "Strain 121", RED),
            "analogy": "Survivalists who move into the places everyone else avoids -- and love it there.",
            "explanation": "Thermophiles (Strain 121 at 121 C), psychrophiles (below 0 C), halophiles, acidophiles/alkaliphiles, piezophiles, radiation-resistant Deinococcus.",
            "why": "Each one widens where life could survive beyond Earth.",
        },
        {
            "term": "Chemolithoautotroph",
            "badge": ("NO SUN", "needed", GAS),
            "analogy": "A microbe that 'eats rocks and breathes chemicals' and still cooks its own meals.",
            "explanation": "Energy from inorganic chemicals (H2, sulfur, iron) and food built from CO2. Methanogens use H2 + CO2 -- the H2 Cassini found at Enceladus could feed them.",
            "why": "The best model for life in dark subsurface oceans.",
        },
        {
            "term": "Tardigrades",
            "badge": ("TUN", "water bear", SUN),
            "analogy": "A camper who packs into a sleeping bag and waits out any storm.",
            "explanation": "Half-millimeter animals that dry into a tun (cryptobiosis) and survive freezing, heat, pressure, radiation and 10 days in open space (2007). Extremotolerant, not extremophiles.",
            "why": "Shows life's toughness and why planetary protection matters.",
        },
    ],
}

EXTRASOLAR_SYSTEMS = {
    "unit": 5,
    "name": "Solar System: The 2027 Exoplanet Systems -- TRAPPIST-1, Kepler-452 & LHS 1140",
    "description": "The three extrasolar systems named in the 2027 rules: TRAPPIST-1's seven Earth-sized planets around a tiny flaring red dwarf, Kepler-452 b, 'Earth's older cousin' around a Sun-like star, and LHS 1140 b, a possible water world -- using every tool from Unit 5.",
    "goals": [
        "Describe each system's star, planets, distance and discovery method.",
        "Explain which planets sit in their habitable zones and what could still make them uninhabitable.",
        "Explain what JWST has learned about TRAPPIST-1 and LHS 1140.",
        "Explain why Kepler-452 b's mass and even its existence are uncertain.",
        "Compare the three systems with each other and with the Sun and Earth.",
    ],
    "sections": [
        {
            "heading": "TRAPPIST-1: seven Earths around a tiny star",
            "body": (
                "TRAPPIST-1 is an ULTRACOOL RED DWARF about 40 light-years away in the constellation Aquarius. It is "
                "tiny: about 9% of the Sun's mass and only a little bigger than Jupiter, with a surface around 2,550 K "
                "(the Sun is about 5,770 K). It gives off well under 1% of the Sun's light -- mostly infrared.\n\n"
                "In 2016 the TRAPPIST telescope in Chile (TRAnsiting Planets and PlanetesImals Small Telescope) found "
                "three planets transiting the star; in 2017 NASA's Spitzer Space Telescope and ground telescopes revealed "
                "SEVEN, named b through h in order from the star. All seven are ROCKY and roughly EARTH-SIZED (about 0.76 "
                "to 1.13 Earth radii, from 2021 measurements). Their 'years' last only 1.5 to 19 days -- the whole system would fit inside "
                "Mercury's orbit.\n\n"
                "• MASSES from TRANSIT TIMING: the planets tug on each other, so their transits come a little early or "
                "late. Measuring those shifts gave each planet's mass, and with the transit sizes, their densities: all "
                "similar to each other and a bit less dense than Earth (less iron, or some water).\n"
                "• RESONANT CHAIN: neighboring planets' periods form simple ratios (like 3:2 and 4:3), so the system is "
                "linked like gears -- a sign the planets migrated inward together while forming.\n"
                "• HABITABLE ZONE: planets e, f and g sit in it (d is near its inner edge). Because the star is so dim, "
                "its habitable zone is very close in."
            ),
            "infographic": "trappist1",
        },
        {
            "heading": "Can TRAPPIST-1's planets be habitable?",
            "body": (
                "Being in the habitable zone is a start, not a guarantee. TRAPPIST-1's planets face three big tests:\n\n"
                "1. TIDAL LOCKING. Orbiting so close, they are probably tidally locked: one side in permanent day, the "
                "other in permanent night. A thick atmosphere or ocean could carry heat around; without one, the night "
                "side may freeze the air solid. Tides from the star and neighbors may also heat their interiors.\n"
                "2. A FLARING STAR. Red dwarfs like TRAPPIST-1 throw off frequent FLARES of X-ray and ultraviolet light, "
                "especially when young. That radiation can strip away atmospheres and water.\n"
                "3. KEEPING AN ATMOSPHERE. This is what JWST is testing. In 2023 it measured the infrared heat glowing "
                "from TRAPPIST-1 b's dayside (about 500 K) and from TRAPPIST-1 c: both look like bare or nearly bare rock "
                "with NO thick carbon-dioxide atmosphere like Venus' (later JWST heat maps agreed). Planets e, f and g, farther "
                "out, are the next big targets: in 2025 JWST's first spectra of TRAPPIST-1 e ruled out a thick, "
                "hydrogen-rich atmosphere, but an Earth-like, nitrogen-rich atmosphere is still possible -- more "
                "observations are underway.\n\n"
                "The upside: red dwarfs live for TRILLIONS of years (the Sun gets about 10 billion), so a planet that "
                "does keep its air would have an enormously long time for life to develop. And red dwarfs are the most "
                "common stars in the galaxy, so the answer for TRAPPIST-1 tells us about most planets everywhere."
            ),
        },
        {
            "heading": "Kepler-452 b: Earth's older cousin?",
            "body": (
                "In July 2015 NASA announced KEPLER-452 b, found by the Kepler space telescope using the transit method. "
                "Its star, Kepler-452 in the constellation Cygnus, is a lot like our Sun: the same G2 type and nearly the "
                "same temperature, but about 1.5 billion years OLDER (about 6 billion years), about 10% wider and about "
                "20% brighter. It is far away -- first estimated at about 1,400 light-years, and later measurements "
                "(from the Gaia mission) put it closer to 1,800.\n\n"
                "The planet orbits in 385 days at a similar distance to Earth's and receives only about 10% more energy "
                "than Earth does -- right in the habitable zone. That made headlines as 'Earth 2.0' or 'Earth's older "
                "cousin'. Its radius is about 1.6 times Earth's.\n\n"
                "WHY THE QUESTION MARKS:\n"
                "• NO MASS. The star is too faint for the Doppler method to weigh the planet, so we don't know its "
                "density. At 1.6 Earth radii it sits right at the size where planets switch from mostly rocky to "
                "mini-Neptunes with thick gas; if rocky, it might be about 5 Earth masses.\n"
                "• MAYBE NOT A PLANET. Kepler saw only a few transits, and in 2018 a re-analysis concluded the signal "
                "couldn't be confidently confirmed -- it might be noise. A lesson from the 'Finding Exoplanets' chapter: "
                "one, two or even three dips need checking.\n"
                "• AN AGING STAR. As Sun-like stars age they brighten, so the habitable zone drifts outward. If 452 b is "
                "rocky with oceans, it may be heading toward a runaway greenhouse -- a glimpse of Earth's far future."
            ),
        },
        {
            "heading": "LHS 1140 b: a water world next door?",
            "body": (
                "LHS 1140 is a red dwarf about 48 light-years away in the constellation Cetus -- bigger and warmer than "
                "TRAPPIST-1 (about 18% of the Sun's mass, about 3,100 K) and calmer, with fewer flares. Its planet LHS 1140 b "
                "was discovered in 2017 by the MEarth project, a set of small ground telescopes watching red dwarfs for "
                "transits.\n\n"
                "• Size about 1.7 Earth radii and mass about 5.6 Earth masses (from the Doppler method) -- so both "
                "density and composition can be estimated. It orbits every 24.7 days in the habitable zone, receiving "
                "about 40% of the sunlight Earth gets. Its equilibrium temperature is roughly 225 K.\n"
                "• It is TOO LIGHT FOR ITS SIZE to be pure rock like Earth. Two possibilities: a WATER WORLD whose mass may "
                "be roughly 10-20% water, or a MINI-NEPTUNE wrapped in hydrogen gas.\n"
                "• JWST observations in 2024 showed no puffy hydrogen atmosphere, which favors the water world, and gave "
                "tentative hints of a NITROGEN-rich atmosphere like Earth's -- still to be confirmed. Models suggest a "
                "frozen 'snowball' surface, possibly with a liquid 'bullseye' ocean about 4,000 km across where the star "
                "shines straight down on the tidally locked day side.\n"
                "• STILL DEBATED (2026): a July 2026 study using a ground telescope reported HELIUM escaping from the "
                "planet -- evidence of an atmosphere. But four JWST transits analyzed in August 2026 found no helium, so "
                "the signal may be false or may come and go. Watch for updates; a test may treat this as uncertain.\n"
                "• A second planet, LHS 1140 c (about 1.3 Earth radii, 3.8-day orbit), is too hot to be habitable.\n\n"
                "Because LHS 1140 is close, small and quiet, and b transits, it is one of the BEST targets anywhere for "
                "studying a habitable-zone planet's atmosphere."
            ),
            "infographic": "three_systems",
        },
        {
            "heading": "Putting the three side by side",
            "body": (
                "• STARS: two red dwarfs (TRAPPIST-1, LHS 1140) and one Sun-like star (Kepler-452). Red dwarfs make "
                "small planets easier to find (deeper transits, bigger wobbles) and their habitable zones close in, but "
                "they flare and tidally lock their planets.\n"
                "• DISTANCE: TRAPPIST-1 (~40 ly) and LHS 1140 (~48 ly) are near enough for JWST to study their planets' "
                "atmospheres. Kepler-452 (~1,800 ly) is far too faint.\n"
                "• WHAT WE KNOW: TRAPPIST-1's planets have measured sizes AND masses (transit timing). LHS 1140 b has both "
                "(transit + Doppler). Kepler-452 b has only a size -- and an uncertain one.\n"
                "• THE QUESTION EACH ONE ANSWERS: TRAPPIST-1 -- can rocky planets around active red dwarfs keep air? "
                "LHS 1140 b -- what are water worlds like? Kepler-452 b -- how common are Earth-like planets around "
                "Sun-like stars, and how carefully must we check a discovery?\n\n"
                "Test tip: questions often give you a light curve or a table of planet data and ask you to work out a "
                "radius, density, or which planets are in the habitable zone -- the same skills as the rest of Unit 5."
            ),
        },
    ],
    "word_bank": [
        ("Ultracool red dwarf", "One of the smallest, coolest, dimmest kinds of star, like TRAPPIST-1."),
        ("Red dwarf (M dwarf)", "A small, cool, red star; the most common kind of star in the galaxy."),
        ("Transit timing", "Measuring how much early or late a planet's transits are to find the masses of planets that tug on each other."),
        ("Resonant chain", "A set of planets whose orbital periods form simple whole-number ratios, linking them like gears."),
        ("Stellar flare", "A sudden blast of X-ray and ultraviolet radiation from a star; red dwarfs flare often."),
        ("Super-Earth", "A planet bigger than Earth but smaller than Neptune that may be rocky."),
        ("Mini-Neptune", "A small planet with a thick gas envelope, too puffy to be rocky."),
        ("Water world", "A planet with a large fraction of its mass (maybe tens of percent) made of water."),
        ("Snowball planet", "A planet whose surface is frozen over, possibly with liquid water underneath or in patches."),
        ("Gaia", "A European space telescope that precisely measures the positions and distances of over a billion stars."),
        ("MEarth project", "A set of small robotic telescopes that watches red dwarfs for transiting planets."),
        ("Validation", "Proving a planet signal is a real planet and not noise or a mimic like an eclipsing binary star."),
    ],
    "key_facts": [
        "TRAPPIST-1: ultracool M8 red dwarf, ~40 ly (Aquarius), ~9% Sun's mass, ~2,550 K. 7 rocky Earth-sized planets b-h (2016-2017, TRAPPIST + Spitzer), periods 1.5-19 days.",
        "TRAPPIST-1 e, f, g in the habitable zone; masses from transit timing; resonant chain; likely tidally locked; flaring star.",
        "JWST 2023: TRAPPIST-1 b (~500 K dayside) and c -- no thick CO2 atmosphere.",
        "Kepler-452 b (2015): Sun-like G2 star ~1.5 Gyr older, ~1,800 ly (Cygnus); 385-day orbit; ~1.6 Earth radii; ~10% more energy than Earth; no mass; 2018 re-analysis doubts it's confirmed.",
        "LHS 1140 b (2017, MEarth): red dwarf ~48 ly (Cetus); 1.7 Earth radii, 5.6 Earth masses, 24.7 days, ~40% Earth's sunlight; too light for rock -> water world or mini-Neptune.",
        "JWST 2024: no hydrogen-rich air on LHS 1140 b; tentative nitrogen; maybe icy with a ~4,000 km liquid 'bullseye' ocean. 2026: ground-based helium detection disputed by JWST. LHS 1140 c is too hot.",
    ],
    "quick_check": [
        ("How were the masses of TRAPPIST-1's planets measured?", "Transit timing variations: the planets tug on each other, shifting when their transits happen."),
        ("Which TRAPPIST-1 planets are in the habitable zone?", "e, f and g (d is near the inner edge)."),
        ("Give two reasons a TRAPPIST-1 planet in the habitable zone might still not be habitable.", "Any two: tidal locking, frequent flares stripping the atmosphere, no atmosphere found (JWST on b and c)."),
        ("Why don't we know Kepler-452 b's density?", "Its star is too faint and far for the Doppler method, so its mass was never measured."),
        ("Why is LHS 1140 b thought to be water-rich?", "Its density is too low for pure rock like Earth's, and JWST found no puffy hydrogen atmosphere, favoring a water world over a mini-Neptune."),
        ("Why are TRAPPIST-1 and LHS 1140 better JWST targets than Kepler-452?", "They are close (~40-48 ly), and small stars make their planets' signals larger; Kepler-452 is ~1,800 ly away and faint."),
    ],
    "cards": [
        {
            "term": "TRAPPIST-1",
            "badge": ("7", "planets", "#ff8a6a"),
            "analogy": "Seven Earth-sized marbles circling a glowing ember, all inside Mercury's orbit.",
            "explanation": "Ultracool red dwarf ~40 ly away, ~9% of the Sun's mass. Seven rocky planets b-h found by transits (2016-2017), years of 1.5-19 days; e, f, g in the habitable zone.",
            "why": "Named in the 2027 rules -- the most-studied red-dwarf planet system.",
        },
        {
            "term": "Transit timing & resonant chain",
            "badge": ("TTV", "masses", GOLD),
            "analogy": "Runners on a track who bump elbows, each arriving a little early or late.",
            "explanation": "TRAPPIST-1's planets tug each other, shifting transit times -- that gave their masses. Their periods form simple ratios, linked like gears.",
            "why": "Explains how we know these planets are rocky.",
        },
        {
            "term": "JWST & TRAPPIST-1",
            "badge": ("500 K", "b dayside", ICE),
            "analogy": "Checking a stove top's glow to see if a lid (atmosphere) is covering it.",
            "explanation": "2023: TRAPPIST-1 b (~500 K) and c show no thick CO2 atmosphere -- bare or nearly bare rock. The test now moves to e, f and g.",
            "why": "The big question: can red-dwarf planets keep air?",
        },
        {
            "term": "Kepler-452 b",
            "badge": ("385 d", "452 b", SUN),
            "analogy": "An older cousin who lives in a house just like yours -- if they really exist.",
            "explanation": "2015, Kepler transits. Sun-like star ~1.5 Gyr older, ~1,800 ly away. 1.6 Earth radii, 385-day year, ~10% more energy than Earth. No mass; 2018 study says not confidently confirmed.",
            "why": "Teaches habitable zones around Sun-like stars AND why discoveries need checking.",
        },
        {
            "term": "LHS 1140 b",
            "badge": ("H₂O?", "1140 b", "#ff9a5a"),
            "analogy": "A bowling-ball-sized planet that turns out to weigh like a snowball -- it must hold lots of water.",
            "explanation": "Red dwarf ~48 ly away. 1.7 Earth radii, 5.6 Earth masses, 24.7-day orbit in the habitable zone. Too light for rock: likely a water world; JWST found no hydrogen-rich air.",
            "why": "One of the best habitable-zone planets for atmosphere studies.",
        },
        {
            "term": "Red dwarf trade-offs",
            "badge": ("M", "dwarfs", RED),
            "analogy": "A cozy campfire: you must sit very close, and it spits sparks.",
            "explanation": "Pros: most common stars, live trillions of years, small planets easy to detect. Cons: habitable zone very close -> tidal locking; frequent flares strip atmospheres.",
            "why": "Two of the three 2027 systems orbit red dwarfs.",
        },
    ],
}

MISSIONS_2027 = {
    "unit": 6,
    "name": "Solar System: The 2027 Mission List -- How Spacecraft Explore",
    "description": "How missions and telescopes are designed (mission types, power, radiation, instruments, tradeoffs, planetary protection), then every mission on the 2027 list -- Venus Express, DAVINCI, VERITAS, Perseverance, Mars Reconnaissance Orbiter, MAVEN, Galileo, Europa Clipper, JUICE, Cassini-Huygens, Dragonfly, OSIRIS-REx, Rosetta, Kepler, JWST and Roman -- with its goals, instruments and results.",
    "goals": [
        "Compare flybys, orbiters, landers, rovers, probes, sample returns and telescopes.",
        "Explain the tradeoffs in power, radiation protection, mass and communication.",
        "Match each instrument type to what it measures.",
        "For each of the 16 listed missions, state its target, agency, dates and main science goal or result.",
        "Explain how telescope design (mirror size, wavelength, location, field of view) matches its science.",
    ],
    "sections": [
        {
            "heading": "Designing a mission: every choice is a tradeoff",
            "body": (
                "MISSION TYPES, from simplest to hardest:\n"
                "• FLYBY: zoom past once (Voyager). Cheap, but only a snapshot.\n"
                "• ORBITER: circle a world for years and map it (MRO, MAVEN, JUICE).\n"
                "• ATMOSPHERIC PROBE: fall through the air measuring as it goes (Galileo's probe, DAVINCI, Huygens).\n"
                "• LANDER / ROVER: touch the surface; rovers drive to new spots (Perseverance), Dragonfly flies.\n"
                "• SAMPLE RETURN: bring material home for Earth's best labs (OSIRIS-REx).\n"
                "• SPACE TELESCOPE: study many targets from afar (Kepler, JWST, Roman).\n\n"
                "ENGINEERING TRADEOFFS:\n"
                "• POWER: sunlight drops as 1/d^2 -- at Jupiter (5.2 AU) it's about 1/27 of Earth's. Europa Clipper and "
                "JUICE carry huge solar arrays; Cassini, Perseverance and Dragonfly use RADIOISOTOPE (nuclear) power "
                "(RTGs) that works anywhere, even in the dark or under Titan's haze.\n"
                "• RADIATION: Jupiter's radiation belts fry electronics, so Europa Clipper keeps its electronics in a thick "
                "metal VAULT and only swoops past Europa instead of orbiting it.\n"
                "• HEAT: Venus' surface (about 465 C, 90 times Earth's pressure) destroyed every Soviet Venera lander "
                "within about two hours.\n"
                "• MASS: each kilogram needs more fuel and a bigger rocket. GRAVITY ASSISTS (slingshots past planets) save "
                "fuel but add years.\n"
                "• COMMUNICATION: signals take minutes to hours and weaken with distance, so far-away probes send data "
                "slowly and must make some decisions on their own.\n"
                "• PLANETARY PROTECTION: spacecraft are cleaned so we don't bring Earth microbes to worlds that might have "
                "life -- and Galileo and Cassini were deliberately crashed into Jupiter and Saturn so they could never hit "
                "Europa or Enceladus."
            ),
            "infographic": "mission_design",
        },
        {
            "heading": "The instrument toolbox",
            "body": (
                "• CAMERAS (visible and near-infrared): shapes, colors, landforms. MRO's HiRISE can see objects about a "
                "meter across from orbit.\n"
                "• SPECTROMETERS: split light to identify chemicals -- minerals on a surface (MRO's CRISM found clays on "
                "Mars), gases in an atmosphere, ices on moons.\n"
                "• MASS SPECTROMETERS: 'sniff' gas or dust directly and weigh each molecule (Cassini found hydrogen in "
                "Enceladus' plume this way).\n"
                "• RADAR: radio waves see through clouds (mapping Venus) and into ice (ice-penetrating radar on Europa "
                "Clipper and JUICE). An ALTIMETER measures height; SYNTHETIC APERTURE RADAR (SAR) builds detailed maps.\n"
                "• MAGNETOMETERS: measure magnetic fields. A salty ocean conducts electricity, so Jupiter's field "
                "'induces' a field inside it -- that's how Galileo discovered Europa's hidden ocean.\n"
                "• GRAVITY SCIENCE: tiny Doppler shifts in the radio signal reveal how mass is spread inside a world.\n"
                "• THERMAL (infrared) IMAGERS: temperature maps -- warm spots can mark active vents.\n"
                "• PARTICLE and PLASMA sensors: measure the charged particles that strip atmospheres (MAVEN)."
            ),
        },
        {
            "heading": "Venus: Venus Express, DAVINCI and VERITAS",
            "body": (
                "• VENUS EXPRESS (ESA; launched November 2005, orbited Venus 2006-2014). Built quickly and cheaply by "
                "reusing the design of Mars Express. From a polar orbit it studied Venus' atmosphere: a huge swirling "
                "VORTEX over the south pole, SUPER-ROTATING winds that circle the planet in about 4 days (much faster than "
                "the planet's 243-day spin), lightning, and hydrogen and oxygen escaping to space in a 2-to-1 ratio -- "
                "water being lost. Infrared maps of hot, fresh-looking lava flows hinted that Venus may still be "
                "volcanically active.\n"
                "• DAVINCI (NASA; launch targeted for about December 2030): 'Deep Atmosphere Venus Investigation of Noble gases, "
                "Chemistry, and Imaging'. After flybys, a probe will DESCEND through the atmosphere for about an hour, "
                "measuring noble gases (like argon and xenon), the D/H ratio of water and other chemistry layer by layer, "
                "and photographing the rugged Alpha Regio highlands on the way down. Main question: did Venus once have "
                "an OCEAN, and how did it lose it?\n"
                "• VERITAS (NASA; launch targeted for about 2031): 'Venus Emissivity, Radio Science, InSAR, Topography, And "
                "Spectroscopy'. An orbiter with interferometric radar to map the surface's heights in detail through "
                "the clouds, plus an infrared EMISSIVITY mapper that peeks through narrow 'windows' in the clouds to tell "
                "rock types apart. Goals: find active volcanoes and signs of plate tectonics, and look for rocks like "
                "granite that on Earth usually need water to form.\n"
                "Note: the 2026 White House budget request proposed cancelling both Venus missions; Congress kept funding "
                "them, but their dates could still slip."
            ),
        },
        {
            "heading": "Mars: MRO, MAVEN and Perseverance",
            "body": (
                "• MARS RECONNAISSANCE ORBITER (MRO) (NASA; launched 2005, at Mars since 2006). HiRISE, the most powerful "
                "camera ever sent to another planet; CRISM, a spectrometer that mapped clays and other minerals that "
                "form in water; SHARAD radar that found buried ice. It also scouts landing sites and RELAYS data from "
                "rovers to Earth.\n"
                "• MAVEN (NASA; 'Mars Atmosphere and Volatile EvolutioN', launched November 2013, orbited Mars from "
                "September 2014 until contact was lost in December 2025; NASA declared it lost in June 2026). It measures how the SOLAR WIND and solar storms strip gas from Mars' upper atmosphere. "
                "Its results show Mars has lost most of its original atmosphere to space -- possible because Mars lost "
                "its global magnetic field long ago -- turning a once wetter, thicker-aired world into a cold desert.\n"
                "• PERSEVERANCE (NASA rover; launched July 2020, landed February 18, 2021 in JEZERO CRATER, an ancient "
                "lake with a river delta). Its job: look for signs of ancient life and COLLECT rock samples in sealed "
                "tubes for a future return to Earth. It carried the Ingenuity helicopter (first powered flight on another "
                "planet) and MOXIE, which made oxygen from Mars' CO2 air. In July 2024 it sampled a rock nicknamed 'Cheyava "
                "Falls' with 'leopard spot' patterns; a peer-reviewed study (Nature, September 2025) called them a "
                "POTENTIAL biosignature -- only further study, ideally in labs on Earth, could tell for sure. Nuclear-powered (RTG)."
            ),
        },
        {
            "heading": "Jupiter's moons: Galileo, Europa Clipper and JUICE",
            "body": (
                "• GALILEO (NASA; launched 1989, orbited Jupiter 1995-2003). Dropped a PROBE into Jupiter's atmosphere "
                "(1995). Its magnetometer detected magnetic fields induced inside Europa, Ganymede and Callisto -- "
                "evidence of salty subsurface oceans. It found Ganymede has its own magnetic field and spotted Dactyl, "
                "the first moon of an asteroid (Ida). Its main antenna never fully opened, so it sent data far more "
                "slowly than planned. It was crashed into Jupiter in 2003 to protect Europa.\n"
                "• EUROPA CLIPPER (NASA; launched October 14, 2024, arrives 2030). The largest planetary spacecraft NASA "
                "has built. It will make about 49 close flybys of Europa while orbiting Jupiter, using ice-penetrating "
                "radar, cameras, spectrometers, a magnetometer and a mass spectrometer to measure the ice shell and ocean "
                "and test whether Europa has the ingredients for life (water, chemistry, energy).\n"
                "• JUICE (ESA; 'JUpiter ICy moons Explorer', launched April 14, 2023, arrives 2031). It will study "
                "Ganymede, Callisto and Europa, then in 2034 enter orbit around GANYMEDE -- the first spacecraft ever to "
                "orbit a moon other than our own. Ganymede is the only moon with its own magnetic field and likely hides "
                "an ocean between ice layers. Solar-powered, with some of the largest solar arrays ever flown."
            ),
        },
        {
            "heading": "Saturn's moons: Cassini-Huygens and Dragonfly",
            "body": (
                "• CASSINI-HUYGENS (NASA/ESA/Italy; launched 1997, at Saturn 2004-2017; RTG-powered). Cassini discovered "
                "Enceladus' south-pole geysers and flew through them: its mass spectrometer found water, salts, organic "
                "molecules and HYDROGEN GAS -- signs of a warm ocean with hydrothermal activity and possible chemical "
                "energy for life. Its radar mapped Titan's methane lakes and seas. The HUYGENS probe parachuted to Titan's "
                "surface on January 14, 2005. Cassini ended by diving into Saturn in 2017.\n"
                "• DRAGONFLY (NASA; launch planned for July 2028, arrival at Titan in 2034). A car-sized, nuclear-powered "
                "ROTORCRAFT with eight rotors that will fly from place to place across Titan -- easy, because Titan's air "
                "is thick and its gravity weak. It will land in the Shangri-La dune fields (the landing dune field was named Ahmakiq Undae in 2026) and work its way to Selk crater, where "
                "an impact may have mixed liquid water with organic material, to study PREBIOTIC chemistry (the chemistry "
                "before life)."
            ),
        },
        {
            "heading": "Small bodies: OSIRIS-REx and Rosetta",
            "body": (
                "• OSIRIS-REX (NASA; launched September 2016, arrived at asteroid 101955 BENNU December 2018). Bennu turned "
                "out to be a loose RUBBLE PILE -- the sampling arm sank into it like a ball pit during its touch-and-go "
                "grab (October 20, 2020). The sample capsule landed in Utah on September 24, 2023 with about 121 grams "
                "(see the Water & Extremophiles chapter for what was inside). The spacecraft continues as OSIRIS-APEX "
                "to asteroid Apophis in 2029.\n"
                "• ROSETTA (ESA; launched 2004, orbited comet 67P/CHURYUMOV-GERASIMENKO 2014-2016). The first spacecraft "
                "to orbit a comet and the first to land on one: its lander PHILAE touched down on November 12, 2014, but "
                "bounced into a shadowy spot where its solar panels got too little light -- a power tradeoff in action. "
                "Rosetta watched the comet's jets switch on as it neared the Sun, measured its water's D/H ratio and found "
                "organic molecules. It ended with a controlled landing on the comet in September 2016."
            ),
        },
        {
            "heading": "Telescopes: Kepler, JWST and Roman",
            "body": (
                "TELESCOPE DESIGN: a bigger mirror (APERTURE) collects more light and sees finer detail; the WAVELENGTH "
                "decides what you can see (infrared for cool objects and molecules); being in SPACE avoids the blurring "
                "and absorption of Earth's air; and there's a tradeoff between a wide FIELD OF VIEW (survey lots of sky) "
                "and deep, detailed looks at one spot.\n\n"
                "• KEPLER (NASA; 2009-2018): a 0.95-meter telescope that stared at ~150,000 stars in Cygnus and Lyra to "
                "catch transits. It found over 2,600 confirmed planets and showed that planets are common (see Finding "
                "Exoplanets).\n"
                "• JWST (NASA/ESA/CSA; launched December 25, 2021): a 6.5-meter mirror of 18 gold-coated hexagons, "
                "orbiting near the Sun-Earth L2 point about 1.5 million km away. It sees INFRARED, so it must be very "
                "cold: a five-layer sunshield the size of a tennis court blocks the Sun's heat. It reads exoplanet "
                "atmospheres (CO2 on WASP-39 b, TRAPPIST-1 b and c, LHS 1140 b) and studies icy moons and comets.\n"
                "• NANCY GRACE ROMAN SPACE TELESCOPE (NASA; launched August 30, 2026 on a Falcon Heavy, nine months ahead of "
                "schedule, heading to the Sun-Earth L2 point like JWST). Its 2.4-meter mirror is the same size as "
                "Hubble's, but its view is at least 100 times WIDER. Its Galactic Bulge survey will use MICROLENSING to find over a thousand planets, including cold planets far from their stars and "
                "free-floating 'rogue' planets, and its CORONAGRAPH will test technology for directly imaging planets "
                "around nearby stars."
            ),
            "infographic": "mission_list",
        },
    ],
    "word_bank": [
        ("Flyby", "A mission that passes a world once without stopping."),
        ("Orbiter", "A spacecraft that circles a world to study it for a long time."),
        ("Atmospheric probe", "A craft that falls through a planet's air, measuring it on the way down."),
        ("Sample return", "A mission that collects material and brings it back to Earth."),
        ("RTG", "Radioisotope thermoelectric generator: makes electricity from the heat of radioactive plutonium."),
        ("Gravity assist", "Swinging past a planet to gain speed or change direction without using fuel."),
        ("Planetary protection", "Rules for not carrying Earth life to other worlds (or bringing alien life back)."),
        ("Spectrometer", "An instrument that splits light to identify the chemicals present."),
        ("Mass spectrometer", "An instrument that weighs molecules to identify gases and dust it collects."),
        ("Synthetic aperture radar (SAR)", "Radar that combines many echoes to make detailed maps, even through clouds."),
        ("Ice-penetrating radar", "Radar that sends radio waves down through ice to see layers and water beneath."),
        ("Magnetometer", "An instrument that measures magnetic fields; can reveal hidden salty oceans."),
        ("Induced magnetic field", "A field created inside a conducting layer (like a salty ocean) by a changing outside field."),
        ("Emissivity", "How well a surface gives off heat at a given wavelength; differs between rock types."),
        ("Super-rotation", "Venus' winds racing around the planet much faster than the planet itself spins."),
        ("Rubble pile", "An asteroid made of loose rocks held together weakly by gravity, like Bennu."),
        ("Prebiotic chemistry", "Chemical reactions that build life's ingredients before life exists."),
        ("Aperture", "The diameter of a telescope's main mirror or lens; bigger collects more light."),
        ("Field of view", "How much of the sky a telescope sees at once."),
        ("L2 point", "A stable spot about 1.5 million km beyond Earth, away from the Sun, where JWST orbits."),
    ],
    "key_facts": [
        "Power: sunlight ~1/d^2 (Jupiter ~1/27 of Earth's) -> big solar arrays (Clipper, JUICE) or RTGs (Cassini, Perseverance, Dragonfly).",
        "Galileo & Cassini crashed on purpose (2003, 2017) for planetary protection. Galileo's magnetometer -> Europa's ocean.",
        "Venus Express (ESA, 2006-2014): polar vortex, super-rotation, H:O escaping 2:1, hints of fresh lava. DAVINCI = descent probe (target ~Dec 2030); VERITAS = radar + emissivity orbiter (target ~2031).",
        "MRO (2006-): HiRISE, CRISM clays, SHARAD ice, relay. MAVEN (2014-2025, contact lost Dec 2025): solar wind stripped Mars' air. Perseverance (Jezero, Feb 2021): sample caching, MOXIE, Ingenuity, 'Cheyava Falls'.",
        "Europa Clipper: launched Oct 14, 2024, arrives 2030, ~49 Europa flybys, radiation vault. JUICE (ESA): launched Apr 14, 2023, arrives 2031, orbits Ganymede 2034 (first moon orbiter besides ours).",
        "Cassini at Saturn 2004-2017; Enceladus plume: water, salts, organics, H2. Huygens on Titan Jan 14, 2005. Dragonfly: rotorcraft, launch July 2028, Titan 2034.",
        "OSIRIS-REx: Bennu (rubble pile), TAG Oct 20, 2020, ~121 g landed Sept 24, 2023 -> OSIRIS-APEX to Apophis. Rosetta: 67P 2014-2016, Philae landed Nov 12, 2014.",
        "Kepler 0.95 m, 2009-2018, 2,600+ planets. JWST 6.5 m, infrared, L2, launched Dec 25, 2021. Roman 2.4 m, launched Aug 30, 2026, 100x+ Hubble's view, microlensing survey + coronagraph.",
    ],
    "quick_check": [
        ("Why do Europa Clipper and JUICE need such large solar arrays?", "Sunlight at Jupiter is only about 1/27 as strong as at Earth (inverse-square law)."),
        ("Why does Europa Clipper fly by Europa instead of orbiting it?", "Jupiter's intense radiation near Europa would damage it; flybys limit the dose."),
        ("How did Galileo detect Europa's ocean?", "Its magnetometer measured a magnetic field induced inside Europa, which needs a salty, conducting ocean."),
        ("Name the Venus mission that will drop a probe through the atmosphere, and the one that will map the surface with radar.", "DAVINCI (descent probe); VERITAS (radar orbiter)."),
        ("What did MAVEN show about Mars' atmosphere?", "The solar wind has stripped much of it away to space over billions of years."),
        ("What will make JUICE a first?", "In 2034 it will orbit Ganymede -- the first spacecraft to orbit a moon other than Earth's."),
        ("Why does JWST need a huge sunshield?", "It observes infrared light, so it must stay very cold or its own heat would swamp the faint signals."),
        ("Which method will the Roman Space Telescope use to find over a thousand exoplanets?", "Gravitational microlensing (in its Galactic Bulge survey)."),
    ],
    "cards": [
        {
            "term": "Mission types",
            "badge": ("6", "types", GOLD),
            "analogy": "Driving past a town, moving in, digging in the garden, or mailing home a souvenir.",
            "explanation": "Flyby, orbiter, atmospheric probe, lander/rover, sample return, space telescope -- more detail usually means more cost and risk.",
            "why": "The rules ask about 'general engineering principles' and tradeoffs.",
        },
        {
            "term": "Solar vs. nuclear power",
            "badge": ("1/27", "at Jupiter", SUN),
            "analogy": "Solar panels are a garden that needs sun; an RTG is a battery that never needs charging.",
            "explanation": "Sunlight drops as 1/d^2. Europa Clipper and JUICE use giant solar arrays; Cassini, Perseverance and Dragonfly use RTGs (plutonium heat -> electricity).",
            "why": "A classic design-tradeoff question.",
        },
        {
            "term": "Instrument toolbox",
            "badge": ("TOOLS", "science", GREEN),
            "analogy": "A doctor's kit: camera = eyes, spectrometer = blood test, radar = X-ray, magnetometer = compass.",
            "explanation": "Cameras (shape), spectrometers (composition), mass spectrometers (sniff gases), radar (through clouds/ice), magnetometers (oceans), gravity science (insides).",
            "why": "Lets you predict what any mission can measure.",
        },
        {
            "term": "Venus Express",
            "badge": ("ESA", "2006-14", GAS),
            "analogy": "A weather satellite parked over a planet-sized pressure cooker.",
            "explanation": "ESA orbiter reusing Mars Express' design: south-pole vortex, super-rotating winds, lightning, water escaping as H and O (2:1), hints of recent lava flows.",
            "why": "On the 2027 list -- and evidence Venus lost its water.",
        },
        {
            "term": "DAVINCI & VERITAS",
            "badge": ("2030s", "Venus", ROCK),
            "analogy": "One diver plunging straight down, one mapmaker circling overhead.",
            "explanation": "DAVINCI: descent probe measuring noble gases, D/H and chemistry, imaging Alpha Regio -- did Venus have an ocean? VERITAS: radar topography + emissivity rock mapping -- volcanoes, tectonics.",
            "why": "Future Venus missions on the 2027 list.",
        },
        {
            "term": "MRO & MAVEN",
            "badge": ("MARS", "orbiters", RED),
            "analogy": "MRO is Mars' photographer; MAVEN is the detective asking where its air went.",
            "explanation": "MRO (2006-): HiRISE camera, CRISM found water-formed clays, SHARAD radar found ice, relays rover data. MAVEN (2014 to Dec 2025, when contact was lost): measured solar-wind stripping of Mars' atmosphere.",
            "why": "Mars' past water and lost atmosphere are core habitability topics.",
        },
        {
            "term": "Perseverance",
            "badge": ("Jezero", "2021", RED),
            "analogy": "A field geologist packing rock samples into labeled jars for a later pickup.",
            "explanation": "Landed Feb 18, 2021 in Jezero Crater's old lake delta. Caches samples for return, carried Ingenuity and MOXIE (made O2), found 'Cheyava Falls' potential biosignature (2024).",
            "why": "Our best current search for ancient Martian life.",
        },
        {
            "term": "Europa Clipper & JUICE",
            "badge": ("2030-31", "Jupiter", ICE),
            "analogy": "Two detectives arriving at the same mansion to investigate different rooms.",
            "explanation": "Clipper (NASA): launched Oct 2024, ~49 Europa flybys from 2030, radiation vault. JUICE (ESA): launched Apr 2023, arrives 2031, orbits Ganymede from 2034 -- a first.",
            "why": "The ocean-world missions of this decade.",
        },
        {
            "term": "Galileo (mission)",
            "badge": ("1995", "Jupiter", GAS),
            "analogy": "A compass that twitched near Europa and gave away a hidden ocean.",
            "explanation": "Orbited Jupiter 1995-2003, dropped an atmospheric probe, magnetometer found induced fields (oceans) in Europa, Ganymede and Callisto, crashed into Jupiter to protect Europa.",
            "why": "Source of the evidence for Europa's ocean.",
        },
        {
            "term": "Cassini-Huygens & Dragonfly",
            "badge": ("Titan", "2005/2034", GOLD),
            "analogy": "Cassini was the scout, Huygens the parachutist, Dragonfly the explorer who flies from site to site.",
            "explanation": "Cassini (2004-2017): Enceladus plume with H2 and organics, Titan's lakes; Huygens landed Jan 14, 2005. Dragonfly: rotorcraft, launch July 2028, Titan 2034, prebiotic chemistry.",
            "why": "Enceladus and Titan are top habitability targets.",
        },
        {
            "term": "OSIRIS-REx & Rosetta",
            "badge": ("SAMPLE", "Bennu + 67P", ROCK),
            "analogy": "One brought a scoop of asteroid home; the other moved in next door to a comet.",
            "explanation": "OSIRIS-REx: Bennu rubble pile, ~121 g returned Sept 24, 2023, now OSIRIS-APEX. Rosetta: orbited 67P 2014-2016, Philae landed Nov 12, 2014, D/H ~3x Earth's.",
            "why": "Small bodies and the delivery of water and organics.",
        },
        {
            "term": "Kepler, JWST & Roman",
            "badge": ("6.5 m", "JWST", BLUE),
            "analogy": "Kepler counted fireflies, JWST sniffs their glow, Roman will sweep the whole field.",
            "explanation": "Kepler (0.95 m, 2009-2018): transits, 2,600+ planets. JWST (6.5 m, infrared, L2, Dec 25, 2021): exoplanet atmospheres. Roman (2.4 m, launched Aug 30, 2026, 100x+ Hubble's view): microlensing survey + coronagraph.",
            "why": "Telescope design and exoplanet results are both on the 2027 list.",
        },
    ],
}
