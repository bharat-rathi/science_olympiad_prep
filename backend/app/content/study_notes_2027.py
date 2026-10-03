"""Study chapters written to cover what the 2027 Division B rules changed
or added, for events whose older chapters came from scioly.org wiki
snapshots that predate the 2027 Rules Manual.

Each chapter's rules facts (dimensions, scoring, topic lists) come from the
manual -- see content/official_rules.py for the full rules overview. The
explanatory science around them (heat transfer, storm scales, plant
diseases, ...) is standard textbook material, written plainly for middle
schoolers. Resources are titled "Study notes:" (see
deterministic.DETERMINISTIC_TITLE_PREFIXES) so they publish to students as
source notes like the wiki excerpts do.

Each entry: (chapter name, chapter description, resource title, text).
"""

RULES_URL = "https://www.soinc.org/"

THERMODYNAMICS_CHAPTERS = [
    (
        "Thermodynamics: 2027 Device -- Heat Collection",
        "The new 2027 device task: collect heat from a heat lamp to warm a cup of water, "
        "predict the final temperature, and how it's scored.",
        "Study notes: Thermodynamics 2027 device (2027 Rules Manual)",
        "THE TASK: before the tournament, build a device that COLLECTS heat from a heat lamp and "
        "uses it to warm 100 mL of room-temperature water in a clear 9 oz plastic party cup. This "
        "replaces the old task (insulating a beaker of hot water so it cools slowly) -- older notes "
        "about the insulated beaker no longer apply.\n\n"
        "THE SETUP (provided by the Event Supervisor): a clamp lamp with a metal reflector and a "
        "clear 100-125 W heat-lamp bulb (not LED, halogen, or ceramic), pointing straight down at "
        "the table. Bulb height above the table: 40-50 cm at Regionals, 40-55 cm at State (in 5 cm "
        "steps), 40-65 cm at Nationals (in 1 cm steps). Heating Time: 10 minutes at Regionals, "
        "10-15 minutes at State/Nationals (1-minute steps). The supervisor announces the height, "
        "Heating Time, bulb specs, room temperature, and water-bath temperature at the start.\n\n"
        "DEVICE RULES: with the cup in it, the device must fit in a 30.0 cm cube. The cup must be "
        "easy to put in and take out. Parts may be inside the cup but must never touch the water, "
        "and nothing may be added to the water. NOT allowed: any energy source (batteries, heaters, "
        "chemical reactions), thermometers or probes, thermoses, coolers, vacuum-sealed parts, or "
        "hazardous materials like fiberglass, mineral wool, or asbestos. Everything must be at room "
        "temperature when impounded and at the start.\n\n"
        "HOW A RUN GOES: 3 minutes of Device Setup Time (fix any violations now -- no changes "
        "after it). The supervisor pours 100 mL of water into the cup and tells you its starting "
        "temperature. You get 1 minute to put the cup in your device. The lamp turns on for the "
        "Heating Time -- hands off the device and lamp, or your device scores are zero. Write your "
        "predicted final temperature (in degrees C) before the time ends. When the lamp turns "
        "off, take the cup out and set it next to the device so the supervisor can measure it.\n\n"
        "SCORING (max 100): Exam Score = 50 x (your test score / best test score). Temperature "
        "Score = 30 x (your temperature gain / best gain). Prediction Score = 20 x (your PE / best "
        "PE), where PE = 1 - |final temp - predicted temp| / final temp. Each construction "
        "violation multiplies TS and PS by 0.7; each competition violation by 0.9.\n"
        "Example: start 21.0 C, final 29.0 C, you predicted 28.5 C. Gain = 8.0 C. "
        "PE = 1 - 0.5/29.0 = 0.983. If the best gain in the room was 10.0 C and the best PE was "
        "0.995, TS = 30 x 0.8 = 24.0 and PS = 20 x 0.983/0.995 = 19.8.\n\n"
        "THE PHYSICS THAT MATTERS: The lamp heats mostly by RADIATION (infrared and visible "
        "light). Intensity follows the inverse-square law -- double the distance and you get about "
        "a quarter of the energy -- so bulb height changes your result a lot. Dark, matte surfaces "
        "ABSORB more radiation; shiny surfaces REFLECT it, so reflectors can aim extra light at the "
        "cup. A clear cover lets light in but traps warm air (the greenhouse effect) and cuts "
        "CONVECTION losses. Insulation under and around the cup cuts CONDUCTION losses to the "
        "table. The heat the water gains is Q = m x c x deltaT: 100 mL of water is about 100 g and "
        "c = 4.18 J/(g C), so each 1 C of gain needs about 418 J.\n\n"
        "PREDICTION STRATEGY: test at home under a real 100-125 W heat lamp at several heights "
        "(40-65 cm) and heating times (10-15 min), always starting with room-temperature water. "
        "Record the gain for each combination and bring that table or graph to the event (prepared "
        "graphs and tables are allowed). On the day, look up the announced height and time and "
        "adjust for the starting temperature.",
    ),
]

THERMODYNAMICS_TEST_CHECKLIST = (
    "Thermodynamics: 2027 Written Test Checklist",
    "The five areas the 2027 written test must cover, with the pieces the older chapters "
    "don't explain (intensive vs. extensive properties, engines, radiation).",
    "Study notes: Thermodynamics 2027 written test (2027 Rules Manual)",
    "THE TEST: at least 3 questions from EACH of these areas. Answers in metric units with "
    "proper significant figures. Math is limited to arithmetic (ratios, exponents, absolute "
    "value), solving one equation for one variable, and simple area/volume -- no trig or "
    "calculus.\n\n"
    "(1) Thermodynamic systems; intensive and extensive properties; what temperature is; the "
    "zeroth law; temperature scales and conversions; heat units.\n"
    "(2) Phases of matter, phase changes, phase diagrams, latent vs. sensible heat, the ideal "
    "gas law.\n"
    "(3) Kinds of heat transfer, thermal conductivity, heat capacity, specific heat.\n"
    "(4) Processes (adiabatic, isothermal, isochoric, isobaric), thermodynamic cycles, engines, "
    "efficiency, and the first and second laws.\n"
    "(5) History: Kelvin, Joseph Black, Joule, Carnot, Planck, Clausius, Boltzmann, Maxwell.\n"
    "STATE/NATIONAL ONLY: radiant exitance, blackbody radiation, the Stefan-Boltzmann law, and "
    "the third law.\n\n"
    "INTENSIVE VS. EXTENSIVE PROPERTIES: an EXTENSIVE property depends on how much stuff you "
    "have -- mass, volume, total energy, heat capacity. Cut the system in half and it halves. "
    "An INTENSIVE property does not depend on amount -- temperature, pressure, density, specific "
    "heat. Cut the system in half and it stays the same. Dividing one extensive property by "
    "another gives an intensive one (mass / volume = density).\n\n"
    "HEAT ENGINES & EFFICIENCY: a heat engine takes heat Q_hot from a hot source, turns part of "
    "it into work W, and dumps the rest Q_cold into a cold sink: W = Q_hot - Q_cold. Efficiency "
    "= W / Q_hot. No engine can beat the Carnot efficiency 1 - T_cold / T_hot (temperatures in "
    "kelvin). Example: T_hot = 500 K, T_cold = 300 K gives at most 1 - 300/500 = 40%.\n\n"
    "RADIATION (State/National): every object emits radiation depending on its temperature. A "
    "BLACKBODY is a perfect absorber and emitter. RADIANT EXITANCE is the power radiated per "
    "square meter of surface. Stefan-Boltzmann law: exitance = sigma x T^4, with sigma = "
    "5.67 x 10^-8 W/(m^2 K^4) -- double the kelvin temperature and the power goes up 16 times. "
    "THIRD LAW: as temperature approaches absolute zero, a perfect crystal's entropy approaches "
    "zero, and absolute zero can never actually be reached.\n\n"
    "HISTORY QUICK LIST: Joseph Black -- latent heat and specific heat. Joule -- mechanical "
    "equivalent of heat. Carnot -- ideal heat engine. Clausius -- second law, entropy. Kelvin -- "
    "absolute temperature scale. Maxwell and Boltzmann -- kinetic theory and statistical "
    "mechanics. Planck -- blackbody radiation, start of quantum theory.",
)
THERMODYNAMICS_CHAPTERS.append(THERMODYNAMICS_TEST_CHECKLIST)

HOVERCRAFT_CHAPTERS = [
    (
        "Hovercraft: 2027 Build Specs",
        "What the 2027 rules allow on the vehicle -- size, electrical parts, batteries, safety "
        "shielding, the timing dowel -- and the physics of lift and thrust.",
        "Study notes: Hovercraft 2027 build specs (2027 Rules Manual)",
        "SIZE: levitated and ready to run, the vehicle must fit in a 40.0 x 40.0 x 40.0 cm box. "
        "It must not damage or change the track.\n\n"
        "IT MUST REALLY HOVER: the vehicle has to float on a cushion of air. The supervisor may "
        "push it down slightly -- if it rises back up, it's levitating. Touching the track surface "
        "or the inside of the rails is allowed; touching the top or outside of the rails is not. "
        "ALL lift and thrust must come from air pressure.\n\n"
        "ELECTRICAL PARTS ALLOWED: batteries, wires (and battery holders/connectors), mechanical "
        "switches, relays, resistors (including potentiometers and rheostats), capacitors, and up "
        "to TWO motors (brushless is fine). No integrated circuits (except ones built into a "
        "commercial motor) and nothing with a laser.\n\n"
        "SAFETY RULES (fail these and you can't run -- participation points only): every propeller "
        "or impeller, including ones underneath, must be shielded so a 3/8\" dowel can't touch it. "
        "Only commercial batteries with their original, readable labels. NO lithium or lead "
        "batteries (so think alkaline or NiMH). Total voltage across any two points must not "
        "exceed 12.0 V by the labels. Every motor needs an easy-to-reach, hand-operated mechanical "
        "switch -- no starting by plugging in batteries or twisting wires.\n\n"
        "TIMING DOWEL: a 1/4\" or thicker wooden dowel, mounted vertically within 3.0 cm of the "
        "front edge, with its top at least 20.0 cm above the track while hovering. It must be the "
        "first part of the vehicle to cross the start and finish lines (photogate beams sit about "
        "17 cm high).\n\n"
        "NICKEL LOAD: the vehicle may carry supervisor-supplied U.S. nickels -- up to 4 full rolls "
        "(40 nickels, about 200 g each), 1 half roll (20 nickels), and 20 loose nickels (about 5 g "
        "each), roughly 5 g to 1 kg in total. You can't open or alter the rolls, and you can't use "
        "tape or glue to hold them -- design a tray, rack, or pocket that holds rolls securely.\n\n"
        "LIFT PHYSICS: a fan pushes air under the hull into a cushion (a skirt helps trap it). The "
        "cushion pressure times the hull's footprint area must equal the vehicle's weight, so a "
        "bigger footprint needs less pressure to lift the same load. Extra nickels mean you need "
        "more lift. THRUST PHYSICS: a rear propeller pushes air backward, so the craft moves "
        "forward (Newton's third law). Because a hovercraft has almost no friction, it keeps "
        "speeding up until air drag balances the thrust -- which is why calibrating speed with "
        "real runs matters.",
    ),
    (
        "Hovercraft: Runs, Target Time & Scoring",
        "How a 2027 run works, the Distance/Time/Mass score formulas with a worked example, and "
        "how to practice hitting any Target Time.",
        "Study notes: Hovercraft 2027 runs and scoring (2027 Rules Manual)",
        "BEFORE YOU RUN: impound the vehicle (batteries stored separately), spare parts, and any "
        "notes you'll need -- no new notes after impound. Tools and two Class III calculators don't "
        "need to be impounded. Eye protection B is required while setting up and running.\n\n"
        "THE TRACK: 45.0 cm wide between rails at least 30 mm high; the timed section is 185.0 cm "
        "from the start line to the finish line, with a cushioned barrier just past the finish. "
        "You may dry-sweep and measure the track but not wet it or ask for it to be moved.\n\n"
        "TARGET TIME (TT): announced at the start of your time, the same for every team: 6.0-18.0 "
        "s, in 1.0 s steps at Regionals and 0.5 s steps at State/Nationals. You get 8 minutes to "
        "adjust and make up to 2 runs -- NO practice runs. You choose how many nickels to carry, "
        "and it can differ between runs.\n\n"
        "A RUN: place the vehicle (with nickels) behind the start line; the supervisor holds a "
        "wooden block in front of it. Turn the motors on, hands off, count \"3, 2, 1, launch,\" and "
        "the block is removed. Timing runs from the dowel crossing the start line to the dowel "
        "crossing the finish line. If it hasn't crossed the start within 3 s, it doesn't count as "
        "a run. A run is INCOMPLETE if the vehicle stops moving for 3 s or hasn't finished by "
        "2 x TT -- then the distance still left to the finish is measured. Touching the vehicle "
        "mid-run scores that run as zero.\n\n"
        "SCORING: Final Score = your best Run Score. Run Score = DS + TS + MS.\n"
        "Distance Score DS = 40 for a complete run; otherwise 40 x (185 - cm left) / 185.\n"
        "Time Score TS = 40 x (1 - |run time - TT| / TT) for a complete run (never below 0); 0 for "
        "an incomplete run.\n"
        "Mass Score MS = (4 x R + 0.1 x N) x (185 - cm left) / 185, where R = full rolls (the half "
        "roll counts 0.5) and N = loose nickels. Maximum 20 (all 4.5 rolls + 20 loose).\n"
        "Example: TT = 10.0 s. You carry 2 full rolls + 10 loose nickels and finish in 10.5 s. "
        "DS = 40. TS = 40 x (1 - 0.5/10) = 38. MS = 4 x 2 + 0.1 x 10 = 9. Run Score = 87.\n\n"
        "THE RAMP: you may launch from a supervisor-provided 5 cm-high ramp, but that run's DS is "
        "halved and its MS is 0 -- only worth it if your craft can't start reliably otherwise.\n"
        "PENALTIES (multiply DS, TS, MS): x0.7 if you missed impound, x0.8 per construction "
        "violation, x0.9 per competition violation. Anything falling off during a run = one "
        "construction violation, and fallen nickels don't count.\n"
        "TIEBREAKERS: best TS, then fewest construction violations, then best MS, then second-best "
        "run.\n\n"
        "STRATEGY: Time (40) is worth twice the Mass Score (20), so first get a craft that finishes "
        "reliably near ANY target time. Build a calibration chart at home: run time vs. number of "
        "rolls carried (and battery charge). On the day, look up the TT and pick the load that "
        "lands closest. Fresh, identical batteries make your chart trustworthy.",
    ),
]

METEOROLOGY_SEVERE_WEATHER = (
    "Meteorology: 2027 Topic -- Severe Weather & Storms",
    "The 2027 topic list from the rules, with the scales, thresholds, and radar features to "
    "know -- the core of this year's test.",
    "Study notes: Meteorology 2027 topic list (2027 Rules Manual)",
    "2027 TOPIC: Severe Weather & Storms. At least HALF the questions use maps, graphs, images, "
    "photos, charts, or tables -- practice reading data, not just memorizing.\n\n"
    "OBSERVATION TOOLS: surface stations (ASOS, mesonets), radiosondes (weather balloons), buoys, "
    "aircraft, satellites (visible, infrared, water vapor), and Doppler radar. RADAR PRODUCTS: "
    "reflectivity (how much precipitation -- base and composite), velocity (motion toward/away "
    "from the radar), correlation coefficient (a drop shows non-rain targets like tornado "
    "debris), storm-relative motion, wind profiles.\n\n"
    "DATA & FORECAST TOOLS: surface maps and station models, decoding METARs, hodographs (wind "
    "shear at different heights), computer models, and Stuve diagrams (clouds, wind shear, "
    "stability). STATE/NATIONAL ONLY: Skew-T diagrams, Lifting Condensation Level (LCL -- the "
    "height where rising air becomes saturated and clouds form), and CAPE (Convective Available "
    "Potential Energy -- fuel for updrafts; bigger CAPE, stronger storms).\n\n"
    "INGREDIENTS FOR SEVERE WEATHER: moisture, instability, lift (fronts, drylines, mountains), "
    "and wind shear. Also: jet streams, air masses, atmospheric rivers, how oceans and big lakes "
    "feed storms (fetch, heat content), and how terrain strengthens or weakens them.\n\n"
    "SEVERE THUNDERSTORMS: the U.S. National Weather Service calls a thunderstorm severe if it "
    "has hail 1 inch or larger, winds of 58 mph or more, or a tornado. Types: single-cell, "
    "multicell, supercell (rotating updraft called a mesocyclone), and mesoscale convective "
    "complexes (MCCs). LIGHTNING: charge separates inside the cloud as ice and graupel collide; "
    "types include cloud-to-ground, intracloud, and cloud-to-cloud.\n\n"
    "PRECIPITATION: formation by collision-coalescence (warm clouds) and the Bergeron process "
    "(ice crystals grow at the expense of droplets), plus riming and aggregation. Snow, sleet, "
    "freezing rain, and freezing drizzle depend on the temperature layers the precipitation "
    "falls through. Heavy rain causes flash, river, and urban flooding, debris flows, and "
    "mudslides. STATE/NATIONAL ONLY: intensity-duration-frequency (IDF) curves and return "
    "periods.\n\n"
    "WINDS: straight-line winds, downdrafts, downbursts (microburst: under 4 km across; "
    "macroburst: larger), gust fronts, squall lines, derechos (long-lived, widespread wind "
    "storms), and downslope winds. On radar, a BOW ECHO signals damaging straight-line winds.\n\n"
    "TORNADOES & WATERSPOUTS: rated by damage on the Enhanced Fujita (EF) scale, used since "
    "February 1, 2007 (the older Fujita F scale before that). EF0 65-85 mph, EF1 86-110, EF2 "
    "111-135, EF3 136-165, EF4 166-200, EF5 over 200. Radar signs: hook echo (reflectivity), a "
    "tight velocity couplet / tornadic vortex signature (TVS), and a debris ball (with a "
    "correlation-coefficient drop).\n\n"
    "HURRICANES (typhoons, cyclones): life cycle -- Invest, Tropical Depression, Tropical Storm "
    "(39-73 mph), Hurricane (74+ mph), Major Hurricane (Category 3+). Saffir-Simpson scale: Cat 1 "
    "74-95 mph, Cat 2 96-110, Cat 3 111-129, Cat 4 130-156, Cat 5 157+. Structure: eye, eyewall, "
    "spiral rain bands. Storm surge is the ocean pushed ashore by wind and low pressure, often "
    "the deadliest hazard. Wind shear, land, cool water, and El Nino/La Nina (ENSO) affect "
    "tracks and strength.\n\n"
    "WINTER STORMS, DROUGHT & HEAT: blizzards, nor'easters, lake-effect snow, ice storms; "
    "droughts and heat waves (definitions, causes, effects).\n\n"
    "SAFETY: a WATCH means conditions are right for the hazard -- be prepared; a WARNING means "
    "it is happening or about to -- act now. Know safe actions for tornadoes, hurricanes, flash "
    "floods (\"turn around, don't drown\"), storm surge, and lightning.\n\n"
    "HISTORIC CASES (you interpret data, no memorizing): hurricanes Galveston (1900), Andrew "
    "(1992), Katrina (2005), Sandy (2012), Ida (2021), Ian (2022), Hilary (2023), Helene (2024), "
    "Erin (2025), Melissa (2025); the Blizzard of March 1888; the 1930s Dust Bowl; the Xenia, "
    "Ohio tornado (1974) and the April 2011 tornado outbreaks; the Great Flood of 1993; the "
    "Storm of the Century (March 1993).\n\n"
    "BINDER TIP: you're allowed one three-ring binder and are expected to include a U.S. map "
    "with state names. Add the EF and Saffir-Simpson tables, radar example images, and a "
    "station-model decoder.",
)

BOTANY_CHAPTERS = [
    (
        "Botany: Plant Diseases & Nutrient Deficiencies",
        "On the 2027 Division B list: what causes plant disease, famous examples, how to spot "
        "nutrient deficiencies, and how diseases are managed.",
        "Study notes: Botany plant diseases and nutrient deficiencies (2027 rules topic)",
        "WHY THIS CHAPTER: the 2027 Division B rules list \"plant diseases, including nutrient "
        "deficiencies and infections\". Older notes (including the wiki pages behind the other "
        "Botany chapters) called this Division C only -- it's on the Division B test now.\n\n"
        "THE DISEASE TRIANGLE: a disease needs three things at once -- a susceptible HOST plant, a "
        "PATHOGEN that can cause disease, and an ENVIRONMENT that favors it (often warm and wet). "
        "Remove any one side and the disease can't happen.\n\n"
        "KINDS OF PATHOGENS: FUNGI cause the most plant diseases -- rusts, smuts, powdery mildew, "
        "Dutch elm disease (spread by bark beetles), and chestnut blight (first found in New York in "
        "1904), which killed about 4 billion American chestnut trees in the first half of the 1900s. WATER MOLDS (oomycetes, fungus-like) -- "
        "Phytophthora infestans caused late blight of potatoes and the Irish Potato Famine "
        "(beginning in 1845). BACTERIA -- fire blight of apples and pears, and crown gall, caused by "
        "Agrobacterium tumefaciens, which inserts its own DNA into plant cells (scientists use it "
        "to make GMOs). VIRUSES -- tobacco mosaic virus was the first virus ever discovered; plant "
        "viruses are often spread by insects such as aphids. Also NEMATODES (tiny roundworms that "
        "attack roots) and PARASITIC PLANTS like dodder and mistletoe.\n\n"
        "SYMPTOM WORDS: chlorosis (yellowing), necrosis (dead brown tissue), wilting, leaf spots, "
        "blight (sudden widespread browning and death), cankers (sunken dead areas on stems or "
        "bark), galls (swollen growths), mosaic (patchy light and dark leaf color), rot, and "
        "stunting.\n\n"
        "NUTRIENT DEFICIENCIES: plants need MACRONUTRIENTS in large amounts -- nitrogen (N), "
        "phosphorus (P), potassium (K), calcium (Ca), magnesium (Mg), sulfur (S) -- and "
        "MICRONUTRIENTS in tiny amounts -- iron, manganese, zinc, copper, boron, molybdenum, "
        "chlorine, nickel. KEY TRICK: MOBILE nutrients (N, P, K, Mg) can be moved from old leaves "
        "to new ones, so their deficiency shows up in OLDER, lower leaves first. IMMOBILE nutrients "
        "(Ca, Fe, S, B) can't be moved, so symptoms show up in YOUNG, new growth first.\n"
        "Nitrogen: older leaves turn evenly pale yellow; plant is stunted.\n"
        "Phosphorus: dark green to purplish or reddish older leaves; poor roots and growth.\n"
        "Potassium: older leaves brown and scorched along the edges.\n"
        "Magnesium: older leaves yellow BETWEEN the veins (interveinal chlorosis), veins stay green.\n"
        "Iron: interveinal chlorosis on YOUNG leaves (common in alkaline soil).\n"
        "Sulfur: young leaves turn yellow overall.\n"
        "Calcium: new growth is distorted or dies; blossom-end rot in tomatoes.\n\n"
        "MANAGING DISEASE: plant resistant varieties, rotate crops, remove infected plants "
        "(sanitation), improve air flow and avoid wet leaves, quarantine new plants, use "
        "fungicides or other treatments when needed, and fix soil nutrients with fertilizer or "
        "compost after a soil test. Combining these is called Integrated Pest Management (IPM).",
    ),
    (
        "Botany: Plant Evolution, GMOs & Food Production",
        "Three other topics on the 2027 list the older chapters skip: paleobotany and plant "
        "evolution, genetically modified organisms, and how foods and plant products are produced.",
        "Study notes: Botany evolution, GMOs and food production (2027 rules topics)",
        "PALEOBOTANY & PLANT EVOLUTION: land plants evolved from freshwater green algae "
        "(charophytes). The first land plants, similar to liverworts and mosses, appeared about 470 "
        "million years ago (Ordovician). Vascular plants with xylem and phloem followed by about "
        "430 million years ago (Silurian) -- Cooksonia is a famous early one. The first forests and "
        "the first seeds appeared in the Devonian (around 385-360 million years ago). In the "
        "Carboniferous, giant tree-sized lycophytes (like Lepidodendron) and ferns filled swamps "
        "whose remains became much of today's coal. Gymnosperms (conifers, cycads, ginkgoes) "
        "dominated the age of dinosaurs (Mesozoic). Flowering plants (angiosperms) appeared about "
        "130-140 million years ago (Early Cretaceous) and spread quickly alongside pollinating "
        "insects. Plant fossils include compressions (flattened imprints), petrified wood "
        "(minerals replace the tissue), amber (fossil tree resin), and pollen and spores -- "
        "studying fossil pollen is called palynology.\n\n"
        "GMOs (GENETICALLY MODIFIED ORGANISMS): plants whose DNA has been changed in a lab, often "
        "by adding a gene from another species. Methods: Agrobacterium (a bacterium that naturally "
        "inserts DNA into plant cells), the gene gun (shooting DNA-coated metal particles into "
        "cells), and newer gene editing like CRISPR. Examples: the Flavr Savr tomato (1994, first "
        "GM food sold in stores, slower softening); Bt corn and Bt cotton (make a protein from the "
        "bacterium Bacillus thuringiensis that kills certain insect pests); herbicide-tolerant "
        "(\"Roundup Ready\") soybeans; Rainbow papaya (resists ringspot virus and saved Hawaii's "
        "papaya crop); Golden Rice (makes beta-carotene to fight vitamin A deficiency); and Arctic "
        "apples (don't brown when cut). Benefits: higher yields, less insecticide, more nutrition. "
        "Concerns: pests and weeds evolving resistance, genes spreading to wild relatives, and "
        "labeling and seed-ownership debates.\n\n"
        "FOOD & PLANT PRODUCTS: people domesticated crops starting about 10,000 years ago -- wheat "
        "and barley in the Fertile Crescent (Middle East), rice in China, and maize (corn) in "
        "Mexico about 9,000 years ago from a wild grass called teosinte. Today rice, wheat, and maize supply most of the "
        "world's calories. The Green Revolution (1950s-1960s) used Norman Borlaug's high-yield dwarf "
        "wheat (he won the 1970 Nobel Peace Prize), similar high-yield rice from the International Rice "
        "Research Institute, fertilizer, and irrigation to greatly increase food "
        "production. Other plant products: cotton and linen (fibers), lumber and paper (wood), "
        "rubber (latex of the rubber tree), coffee, cocoa, and tea (beverages), sugar from sugar "
        "cane and sugar beets, vegetable oils (soy, palm, canola), and many medicines.",
    ),
]
