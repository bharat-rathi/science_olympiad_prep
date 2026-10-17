"""Learning paths: Physical Science & Chemistry events (Hovercraft's path
lives in content/study_notes_2027.py)."""

from app.content.learning_paths._base import lesson

CIRCUIT_LAB = [
    lesson(
        "Charge, Coulomb's Law & Electric Fields",
        "The basics of electric charge and the forces between charges.",
        "CHARGE -- a property of matter, measured in coulombs (C); an electron is -1.6 x 10^-19 C. "
        "COULOMB'S LAW -- F = k q1 q2 / r^2 (k = 9 x 10^9 N m^2/C^2). ELECTRIC FIELD -- force per unit "
        "charge (N/C).",
        "Like charges repel, opposite charges attract, and the force gets weaker fast as they move "
        "apart -- double the distance and the force drops to a quarter.",
        "Charging by friction (rubbing a balloon), conduction (touching), and induction (bringing a "
        "charge near without touching). Conductors let charges move (metals); insulators don't "
        "(plastic, glass). Field lines point away from + and toward -; closer lines mean a stronger "
        "field. Charge is conserved and quantized. Coulomb's law fits the allowed math (algebra, at "
        "most two equations); practice ratio reasoning: tripling one charge triples the force; "
        "halving the distance quadruples it.",
        "Two charges 2 m apart feel a 36 N force. What is the force at 6 m? (Distance x3 -> force "
        "/9 = 4 N.)",
    ),
    lesson(
        "Voltage, Current & Resistance",
        "What each quantity means and its units.",
        "VOLTAGE (V, volts) -- energy per charge, the electrical \"push.\" CURRENT (I, amperes) -- "
        "charge flow per second (1 A = 1 C/s). RESISTANCE (R, ohms) -- opposition to current.",
        "A circuit is like water in pipes: voltage is the pressure, current is the flow rate, and "
        "resistance is how narrow the pipe is.",
        "Conventional current flows from + to -; electrons actually move the other way. Resistance of "
        "a wire: R = resistivity x length / area -- longer and thinner wires resist more; most metals "
        "resist more when hot. Prefixes: milli (10^-3), micro (10^-6), kilo (10^3), mega (10^6). "
        "Resistor color code: black 0, brown 1, red 2, orange 3, yellow 4, green 5, blue 6, violet 7, "
        "gray 8, white 9; third band = number of zeros; gold +/-5%, silver +/-10%. Example: "
        "yellow-violet-red = 4,700 ohms (4.7 k).",
        "Read the resistor: brown-black-orange-gold. (10 x 1,000 = 10 kilohms, +/-5%.)",
    ),
    lesson(
        "Ohm's Law, Power & Energy",
        "The core equations for every circuit problem.",
        "OHM'S LAW -- V = I R. POWER -- P = V I = I^2 R = V^2 / R (watts). ENERGY -- E = P t (joules, "
        "or kilowatt-hours). CAPACITY -- battery charge in mAh.",
        "Know any two of V, I, and R and you can find the third. Power tells how fast energy is used.",
        "Example: 9 V across 450 ohms -> I = 0.02 A (20 mA), P = 0.18 W. A 60 W bulb for 5 hours = 300 "
        "Wh = 0.3 kWh. Charge time from a label: a 3,000 mAh battery charged at 1 A (1,000 mA) takes "
        "about 3 hours (ignoring losses). Energy in a battery (Wh) = V x Ah: 3.7 V x 3 Ah = 11.1 Wh. "
        "Resistors must handle their power: P = I^2 R. Ohmic devices give a straight-line V-I graph; "
        "diodes and bulbs don't.",
        "A USB charger supplies 5 V at 2 A. Power? Time to deliver 4,000 mAh? (10 W; about 2 hours.)",
    ),
    lesson(
        "Series & Parallel Circuits",
        "Combining resistors and finding currents and voltages.",
        "SERIES -- one path; same current through every part. PARALLEL -- multiple paths; same voltage "
        "across each branch. EQUIVALENT RESISTANCE -- one resistor that would act the same.",
        "In series, resistances add and the battery's voltage is shared. In parallel, every branch "
        "gets the full voltage, and adding branches LOWERS the total resistance.",
        "Series: R = R1 + R2 + ...; voltage divides in proportion to resistance (voltage divider: V2 "
        "= V x R2 / (R1 + R2)). Parallel: 1/R = 1/R1 + 1/R2 + ...; for two, R = R1 R2 / (R1 + R2); "
        "n equal resistors R -> R/n; the total is always less than the smallest branch. Combination "
        "circuits: simplify from the inside out. Hands-on tasks include building a given equivalent "
        "resistance and making two LEDs equally bright (match their currents).",
        "A 6 ohm and a 3 ohm resistor in parallel, in series with 4 ohms. Total? (2 + 4 = 6 ohms.)",
    ),
    lesson(
        "Schematics & Components",
        "Reading circuit diagrams and identifying parts.",
        "SCHEMATIC -- a circuit diagram using standard symbols. GROUND -- the reference point (0 V). "
        "NODE -- a point where components connect.",
        "Schematics show how parts connect, not where they sit. Learn the symbols and you can build or "
        "troubleshoot any circuit.",
        "Symbols: battery (long line +, short line -), resistor (zigzag or box), potentiometer (with "
        "an arrow), capacitor (two parallel plates), diode (triangle and bar -- current flows toward "
        "the bar), LED (diode with arrows), switch (SPST, SPDT), lamp, fuse, ground, ammeter (A), "
        "voltmeter (V). An SPDT switch has a common terminal and two throws; two SPDT switches can "
        "make a 3-way light switch (control a bulb from two places). A short circuit bypasses the "
        "load; an open circuit has a break. Capacitors store charge (Q = C V) and block steady DC.",
        "Which direction does conventional current flow through a diode symbol? (Toward the bar, "
        "from anode to cathode.)",
    ),
    lesson(
        "Breadboard & Multimeter Skills",
        "Building on a breadboard and measuring safely and correctly.",
        "BREADBOARD -- a reusable board with connected rows. MULTIMETER -- measures voltage, current, "
        "and resistance. CONTINUITY -- whether there's an unbroken path.",
        "Most of your hands-on points come from building correctly and measuring correctly. Practice "
        "until it's automatic.",
        "Breadboard: the 5-hole rows are connected; the long side rails are power and ground; the "
        "center gap separates the two sides (place chips and parts across it). Voltmeter: in PARALLEL "
        "across the part, circuit on. Ammeter: in SERIES (break the circuit and put the meter in the "
        "path), with leads in the amp jack -- never across a battery. Ohmmeter: circuit OFF and the "
        "part disconnected (or one end lifted). Start on the highest range. Mystery-resistor task: "
        "with a known resistor in series, measure both voltages; the ratio equals the resistance "
        "ratio. Troubleshoot by measuring voltage at each node.",
        "A known 1 k resistor in series with a mystery one: 3 V across the known, 6 V across the "
        "mystery. Mystery value? (2 kilohms -- same current, so twice the voltage means twice the "
        "resistance.)",
    ),
    lesson(
        "Diodes & LEDs",
        "One-way current, forward voltage, and current-limiting resistors.",
        "DIODE -- lets current flow one way. PN JUNCTION -- where p-type and n-type semiconductor meet. "
        "FORWARD VOLTAGE (Vf) -- the drop across a conducting diode (~0.7 V silicon; ~1.8-3.3 V for "
        "LEDs).",
        "A diode is a one-way valve. An LED is a diode that glows. LEDs need a series resistor or "
        "they draw too much current and burn out.",
        "Forward bias: p side more positive -> conducts. Reverse bias: blocks (until breakdown). LED "
        "resistor: R = (Vsupply - Vf) / I. Example: 9 V supply, red LED Vf = 2 V, 20 mA -> R = 7 / "
        "0.02 = 350 ohms (use 390). The long leg (anode) goes toward +. Diodes rectify AC to DC. Two "
        "LEDs equally bright: give them equal current (series, or matched resistors in parallel). LED "
        "color depends on the semiconductor material (higher energy for blue, higher Vf).",
        "5 V supply, LED Vf = 3 V, desired 10 mA. Resistor? ((5 - 3) / 0.010 = 200 ohms.)",
    ),
    lesson(
        "Boolean Algebra & Logic Gates",
        "AND, OR, NOT, NAND, NOR, XOR, truth tables, and De Morgan's laws.",
        "LOGIC GATE -- a circuit that outputs 1 or 0 from its inputs. TRUTH TABLE -- every input "
        "combination and its output. BOOLEAN ALGEBRA -- the math of true/false.",
        "AND outputs 1 only if all inputs are 1. OR outputs 1 if any input is 1. NOT flips the input. "
        "Everything else is built from these.",
        "NAND = NOT AND; NOR = NOT OR (each is universal -- any circuit can be built from just one). "
        "XOR outputs 1 when the inputs differ. Notation: A.B (AND), A + B (OR), A' or bar-A (NOT). "
        "Laws: A + 0 = A, A.1 = A, A + A' = 1, A.A' = 0, A + AB = A. De Morgan: (A.B)' = A' + B' and "
        "(A + B)' = A'.B'. With n inputs, a truth table has 2^n rows. Build from a truth table: write "
        "the sum of products (an AND term for each row that outputs 1), then simplify.",
        "Simplify (A + B)' using De Morgan. (A'.B' -- NOT A AND NOT B.)",
    ),
    lesson(
        "Combinational Logic & Binary Arithmetic",
        "Binary numbers, adders, and multiplexers.",
        "BINARY -- base 2 (bits 0 and 1). HALF ADDER -- adds two bits (sum = XOR, carry = AND). FULL "
        "ADDER -- adds two bits plus a carry-in. MULTIPLEXER -- selects one of several inputs.",
        "Computers do arithmetic with logic gates. Binary place values are 1, 2, 4, 8, 16, and so on.",
        "Convert: 1011 = 8 + 0 + 2 + 1 = 11; 13 = 1101. Add: 0110 + 0011 = 1001 (6 + 3 = 9); carry "
        "when 1 + 1 = 10. A full adder: Sum = A XOR B XOR Cin; Cout = AB + Cin(A XOR B). Chain full "
        "adders for multi-bit sums (ripple-carry). A 2-to-1 multiplexer: Output = S'A + SB. A decoder "
        "turns a binary number into one active output line. 2027 math is capped at whole-number "
        "binary and binary addition.",
        "Add 1011 + 0110 in binary. (10001 = 17.)",
    ),
    lesson(
        "Kirchhoff's Laws",
        "Junction and loop rules for analyzing any circuit.",
        "KCL (CURRENT LAW) -- current into a junction = current out. KVL (VOLTAGE LAW) -- voltage rises "
        "and drops around any closed loop sum to zero.",
        "Charge isn't created or lost at a junction, and energy is conserved around a loop. Those two "
        "facts let you solve circuits that series/parallel rules can't.",
        "Steps: label currents with assumed directions; write KCL at junctions; write KVL around "
        "loops (going through a resistor with the current = -IR; through a battery from - to + = "
        "+V). Solve the equations (at most two at a time under 2027's math rules). A negative answer "
        "means the real current runs the other way. Example: one loop with a 12 V battery and 2 ohm "
        "and 4 ohm resistors: 12 - 2I - 4I = 0 -> I = 2 A.",
        "At a junction, 3 A and 2 A flow in and one wire carries 4 A out. What does the other wire "
        "carry? (1 A out.)",
    ),
    lesson(
        "Transistors, Flip-Flops & Op-Amps (State/Nationals)",
        "Higher-level components that show up at State and Nationals.",
        "BJT -- bipolar junction transistor (base, collector, emitter). FLIP-FLOP -- a circuit that "
        "stores one bit. OP-AMP -- a high-gain amplifier with two inputs.",
        "A transistor is a switch or amplifier controlled by a small current. Flip-flops give circuits "
        "memory. Op-amps amplify differences between voltages.",
        "NPN BJT: a small base current lets a larger collector current flow (Ic = beta x Ib); as a "
        "switch it is either cut off or saturated. Flip-flops: SR (set/reset; S = R = 1 is invalid for "
        "NOR-based), D (output follows D on a clock edge), JK, T (toggles). Counters and registers are "
        "built from them. Op-amp rules (ideal, with negative feedback): no current into the inputs; "
        "the inputs sit at the same voltage. Inverting amplifier gain = -Rf / Rin; non-inverting = "
        "1 + Rf / Rin. Without feedback it acts as a comparator.",
        "Non-inverting op-amp with Rf = 9 k and Rin = 1 k. Gain? (1 + 9 = 10.)",
    ),
    lesson(
        "Historical Figures",
        "The scientists behind the units and laws.",
        "Many units are named after people: volt (Volta), ampere (Ampere), ohm (Ohm), coulomb "
        "(Coulomb), watt (Watt), farad (Faraday), henry (Henry), tesla (Tesla), siemens (Siemens).",
        "History questions are quick points. Match each person to their discovery or invention.",
        "Benjamin Franklin: positive and negative charge, lightning is electricity (1752). Charles "
        "Coulomb: the force law (1785). Alessandro Volta: the first battery, the voltaic pile (1800). "
        "Andre-Marie Ampere: electrodynamics. Hans Christian Oersted: current makes a magnetic field "
        "(1820). Georg Ohm: V = IR (1827). Michael Faraday: electromagnetic induction, the dynamo. "
        "Gustav Kirchhoff: circuit laws (1845). James Clerk Maxwell: electromagnetic equations. "
        "Thomas Edison: practical incandescent bulb, DC power. Nikola Tesla: AC motors and power. "
        "George Boole: Boolean algebra. Bardeen, Brattain, and Shockley: the transistor (1947).",
        "Who first showed an electric current deflects a compass needle? (Hans Christian Oersted.)",
    ),
]

CRIME_BUSTERS = [
    lesson(
        "Lab Safety & Equipment",
        "Working safely and knowing the tools you'll use.",
        "PPE -- personal protective equipment (goggles, gloves, apron). SPOT PLATE -- a plate with "
        "small wells for testing tiny samples. PIPETTE -- a dropper for transferring liquids.",
        "Crime Busters is a hands-on chemistry lab. Safe habits are scored, and they keep you from "
        "contaminating the evidence.",
        "Wear eye protection; read every label; never taste; waft to smell. Use a clean scoop or "
        "toothpick for each sample to avoid cross-contamination. Common tools: spot plates, test "
        "tubes, beakers, hand lens or microscope, pH paper, droppers, a magnet, a conductivity "
        "tester, chromatography paper. The supervisor provides iodine reagent, 1 M HCl, "
        "chromatography materials, waste containers, and distilled water. Dispose of waste where "
        "directed and clean up -- neatness affects your efficiency.",
        "Why use a fresh toothpick for each powder? (To avoid cross-contaminating samples and getting "
        "false results.)",
    ),
    lesson(
        "Iodine & HCl Indicator Tests",
        "Two quick chemical tests that sort many white powders.",
        "IODINE TEST -- iodine turns blue-black with starch. HCl TEST -- dilute hydrochloric acid makes "
        "carbonates fizz (CO2 gas). REAGENT -- a chemical used in a test.",
        "Many unknown powders look the same. Adding a drop of iodine or acid quickly splits them into "
        "groups.",
        "Iodine: blue-black = starch (cornstarch, flour). Iodine stays yellow-brown on most others. "
        "HCl: fizzing = a carbonate or bicarbonate (calcium carbonate, baking soda); "
        "CaCO3 + 2HCl -> CaCl2 + H2O + CO2. Baking soda also fizzes with vinegar. Combine with water "
        "solubility and appearance to finish the ID (e.g. sugar dissolves and doesn't react; salt "
        "dissolves and forms cubic crystals; sand doesn't dissolve or react). Record each result "
        "immediately in a table.",
        "A white powder turns blue-black with iodine. What is it likely to be? (A starch -- "
        "cornstarch or flour.)",
    ),
    lesson(
        "Physical Property Testing",
        "Density, solubility, color, texture, and other physical clues.",
        "DENSITY -- mass / volume. SOLUBILITY -- whether a substance dissolves in water. TEXTURE -- how "
        "grains look and feel under a hand lens.",
        "Physical tests don't change the substance -- you just look, feel, and dissolve. They often "
        "narrow the field before you use any reagent.",
        "Look with a hand lens: halite and sugar crystals look cubic or glassy; sand has irregular "
        "grains; cornstarch is a fine powder that squeaks. Solubility in water: salt, sugar, baking "
        "soda dissolve; sand, calcium carbonate, cornstarch don't. Density: floats or sinks in water "
        "(useful for polymers and plastics -- polypropylene and polyethylene float; PET, PVC, and "
        "polystyrene usually sink). Other tests: magnetism (iron filings), conductivity of the "
        "solution (salt conducts; sugar doesn't), pH paper (baking soda is basic).",
        "A powder dissolves in water and the solution conducts electricity. Salt or sugar? (Salt -- "
        "it forms ions.)",
    ),
    lesson(
        "Chromatography & Rf Values",
        "Separating inks and dyes and calculating Rf.",
        "CHROMATOGRAPHY -- separating a mixture as a solvent carries it along paper. Rf -- distance the "
        "spot traveled / distance the solvent front traveled. STATIONARY PHASE -- the paper. MOBILE "
        "PHASE -- the solvent.",
        "Different dyes in an ink travel at different speeds, so they spread into separate color "
        "bands. Matching the pattern from a crime-scene note to a suspect's pen links them.",
        "Draw the start line in pencil (pen ink would run) above the solvent level. Mark the solvent "
        "front as soon as you remove the paper. Rf = spot distance / front distance, always between 0 "
        "and 1, with no units. Same ink + same solvent + same paper -> same Rf and pattern. Paper "
        "chromatography with water or alcohol; some events use TLC. Compare unknowns to known samples "
        "run on the same strip.",
        "A dye moves 3.0 cm while the solvent front moves 7.5 cm. Rf? (3.0 / 7.5 = 0.40.)",
    ),
    lesson(
        "Fiber Identification",
        "Telling natural and synthetic fibers apart by burning and by microscope.",
        "NATURAL FIBERS -- cotton (plant cellulose), wool and silk (animal protein). SYNTHETIC -- nylon, "
        "polyester, acrylic. BURN TEST -- how a fiber burns, smells, and what residue it leaves.",
        "Fibers transfer at crime scenes. A quick look under magnification and a careful burn test "
        "often identifies the fiber type.",
        "Microscope: cotton -- flat, twisted ribbon; wool -- scales on the surface; silk -- smooth, "
        "fine, and triangular in cross section; synthetics -- smooth, uniform rods. Burn test (only "
        "if allowed, with tongs and over a safe surface): cotton burns quickly, smells like burning "
        "paper, leaves soft gray ash; wool and silk burn slowly, smell like burning hair, leave a "
        "crushable black ash; nylon and polyester melt and shrink from the flame, leaving a hard bead "
        "(nylon smells like celery). Polymer items in Crime Busters are tested by density, burning, "
        "and appearance.",
        "A fiber smells like burning hair and leaves crushable ash. Natural or synthetic? (Natural "
        "animal protein -- wool or silk.)",
    ),
    lesson(
        "Separating & Identifying Mixtures",
        "Strategies for unknowns that are mixtures of two or three solids.",
        "MIXTURE -- two or more substances combined physically. FILTRATION -- separates an insoluble "
        "solid from a liquid. EVAPORATION -- recovers a dissolved solid.",
        "Mixtures give mixed results: a powder that partly dissolves and partly fizzes might be salt "
        "plus calcium carbonate. Separate it, then test each part.",
        "Method: add water and stir; filter. The filtrate holds the soluble part (evaporate a drop to "
        "see its crystals; test conductivity). The residue holds the insoluble part (test with HCl, "
        "iodine). Use a magnet for iron. Look for two kinds of grains under the hand lens. 2027 "
        "levels: Regionals up to 2 mixtures of 2 solids, State 2-4 mixtures of 2-3 solids, Nationals "
        "2-6. Only the starred solids on the list (calcium carbonate through white sand) appear in "
        "mixtures.",
        "A powder partly dissolves; the insoluble part fizzes in HCl. What two components are "
        "likely? (A soluble solid, such as salt or sugar, and calcium carbonate.)",
    ),
    lesson(
        "Crime Scenario Analysis",
        "Connecting evidence to suspects.",
        "SCENARIO -- the crime story with suspects. EVIDENCE -- physical and chemical findings. "
        "ALIBI -- a claim that a suspect was elsewhere.",
        "Read the scenario carefully: each suspect usually has a link to some substance, fiber, or "
        "ink. The evidence you identify points to the culprit.",
        "Make a matrix: suspects across the top, evidence down the side, and mark which evidence "
        "matches whom (a powder in a suspect's pocket, a pen whose ink matches, a fiber from their "
        "jacket). Note evidence that rules people OUT, too. The 2027 physical-evidence topics (1-2 at "
        "Regionals, more at higher levels) add things like fingerprints, hair, or soil. Base your "
        "conclusion on several independent pieces of evidence, not just one.",
        "Two suspects match the powder, but only one matches the ink. Who's the most likely culprit? "
        "(The suspect who matches both.)",
    ),
    lesson(
        "Reasoning from Evidence to Conclusion",
        "Writing a clear, logical justification for your answer.",
        "INFERENCE -- a conclusion drawn from evidence. CHAIN OF REASONING -- each step supported by "
        "the one before. CORROBORATION -- independent evidence that agrees.",
        "A correct answer with a clear explanation earns the most points. Show HOW the evidence leads "
        "to the conclusion.",
        "Structure: claim (\"Suspect B committed the crime\"), evidence (\"the white powder was "
        "identified as baking soda by its fizzing in HCl and solubility; B works in a bakery; the "
        "note's ink matched B's pen with Rf 0.45 and 0.72\"), and reasoning (\"no other suspect is "
        "linked to both\"). Acknowledge evidence that doesn't fit. Avoid overclaiming: \"consistent "
        "with\" is more accurate than \"proves\" for class evidence (shared by many sources).",
        "Is a common blue polyester fiber strong evidence on its own? Why? (No -- it's class evidence "
        "shared by many sources; it only supports other findings.)",
    ),
    lesson(
        "Data Recording & Observation",
        "Keeping clear records that earn points and avoid mistakes.",
        "OBSERVATION -- what you directly see, smell, or measure. DATA TABLE -- an organized grid of "
        "results. QUALITATIVE / QUANTITATIVE -- descriptions vs numbers.",
        "Write results down the moment you see them, in a table you set up before starting. "
        "Memory fails under time pressure.",
        "Set up a table before the event: rows for each unknown; columns for appearance, water "
        "solubility, iodine, HCl, conductivity, pH, magnet, other, and ID. Use specific words "
        "(\"rapid fizzing,\" \"blue-black,\" \"no change\") rather than \"yes\" or \"maybe.\" Record "
        "measurements with units (Rf to two decimals). Mark uncertain results and retest if time "
        "allows. Neat records also help you notice patterns and catch mixtures.",
        "Which is better recorded: \"reacted\" or \"vigorous bubbling within 2 seconds\"? (The second "
        "-- specific and repeatable.)",
    ),
    lesson(
        "Timed Station Practice",
        "Running the whole event efficiently against the clock.",
        "TIME BUDGET -- planned minutes per task. TRIAGE -- doing quick, sure tasks first. DIVIDE AND "
        "CONQUER -- partners split tasks.",
        "Crime Busters has many unknowns and little time. A plan for who does what, and in what order, "
        "is worth as many points as chemistry knowledge.",
        "Before starting: skim the whole packet; split the work (one partner on powders, one on "
        "chromatography and fibers). Start chromatography first -- it runs while you do other tests. "
        "Batch tests: put every powder on a spot plate and add iodine to all, then HCl to fresh "
        "samples of all. Keep a running answer sheet. Leave the last few minutes for the scenario "
        "question and cleanup. Practice full mock runs at home with a timer and the same kinds of "
        "unknowns.",
        "Why start chromatography before the powder tests? (It takes time to develop, so it can run "
        "while you do other work.)",
    ),
]

FOOD_SCIENCE = [
    lesson(
        "Milk Composition & Dairy Chemistry",
        "What milk is made of and why it behaves the way it does.",
        "EMULSION -- tiny droplets of one liquid spread through another (fat in water). COLLOID -- "
        "particles spread through a medium without settling. LACTOSE -- milk sugar.",
        "Milk is mostly water (about 87%) with fat, proteins, lactose, and minerals. The fat floats as "
        "tiny droplets and the proteins as tiny clusters -- that's why milk looks white.",
        "Typical cow's milk: ~87% water, ~4.8% lactose, ~3.3% protein (about 80% casein, 20% whey), "
        "~3.5% fat (whole milk), and minerals such as calcium and phosphate. Casein forms micelles "
        "held together with calcium phosphate. Fat globules are wrapped in a membrane; "
        "homogenization breaks them smaller so cream doesn't rise. Lactose is a disaccharide "
        "(glucose + galactose). Cream is milk with more fat (heavy cream about 36%+). Milk's pH is "
        "about 6.6-6.8. 2027 topic: milk and dairy products.",
        "Why does cream rise to the top of unhomogenized milk? (Fat is less dense than water, and the "
        "large globules float.)",
    ),
    lesson(
        "Proteins: Casein, Denaturation & Coagulation",
        "How milk proteins change to make curds.",
        "CASEIN -- the main milk protein, in micelles. DENATURATION -- a protein unfolding (losing its "
        "shape). COAGULATION -- proteins clumping into a gel or curd. ISOELECTRIC POINT -- the pH "
        "where a protein has no net charge (casein about pH 4.6).",
        "Add acid to milk and the casein clumps into curds, leaving watery whey. That's how simple "
        "cheeses like paneer and ricotta are made.",
        "Casein micelles normally repel each other because of negative charges. Acid (vinegar, lemon "
        "juice) lowers the pH toward 4.6, neutralizing the charge so the micelles clump. Heat speeds "
        "coagulation. Rennet (an enzyme) curdles milk differently, by cutting kappa-casein. Whey "
        "proteins denature with heat but don't curdle with acid as much. Variables for the 2027 curd "
        "task: acid type and amount, milk fat level, temperature, stirring, and draining time. "
        "Lab task: curdle 120 mL milk with vinegar or lemon juice and drain 15 minutes in "
        "cheesecloth.",
        "At about what pH does casein curdle? (Around 4.6, its isoelectric point.)",
    ),
    lesson(
        "Fats: Emulsions & Butter",
        "How cream becomes butter.",
        "FAT GLOBULE -- a tiny fat droplet with a membrane. CHURNING -- agitation that breaks the "
        "membranes. PHASE INVERSION -- an oil-in-water emulsion (cream) turning into water-in-oil "
        "(butter). BUTTERMILK -- the liquid left behind.",
        "Shake cream long enough and the fat droplets crash together, break their coats, and stick "
        "into butter, squeezing out the buttermilk.",
        "Stages when shaking cream: liquid -> whipped (air bubbles stabilized by fat) -> grainy -> "
        "butter suddenly separates from buttermilk. Temperature matters: cream around 10-15 C works "
        "best -- too warm and the fat is too soft and greasy, too cold and it's too hard to clump. The "
        "2027 task uses 150 mL of cream at about 13 C. Higher-fat cream gives more butter. Rinse "
        "butter in cold water to remove buttermilk; then mass it. Emulsifiers (like lecithin) "
        "stabilize emulsions; homogenization helps prevent separation.",
        "Why does very warm cream make poor butter? (The fat is too soft, so it smears instead of "
        "clumping into firm butter.)",
    ),
    lesson(
        "Freezing Point Depression & Ice Cream",
        "Why salt makes ice colder and how ice cream freezes.",
        "FREEZING POINT DEPRESSION -- dissolved particles lower the freezing point of a liquid. LATENT "
        "HEAT OF FUSION -- energy absorbed when ice melts. OVERRUN -- the air whipped into ice cream.",
        "Salt on ice lowers its melting point, so the ice melts and absorbs heat, making the brine "
        "much colder than 0 C -- cold enough to freeze the ice-cream mix.",
        "Freezing point depression: delta-T = i x Kf x m (Kf for water = 1.86 C/m; i = particles per "
        "unit -- 2 for NaCl). Rock salt and ice can reach about -10 to -20 C. The mix (milk/cream, "
        "sugar, flavor) has its own lowered freezing point because of dissolved sugar. Small ice "
        "crystals make smooth ice cream: freeze fast and shake constantly. Fat and air give "
        "creaminess. The 2027 task: shaken-bag ice cream that must stand on its own for 5 seconds, "
        "scored 0.1 point per mm of height -- so you want it firm.",
        "Why shake the bag constantly? (Agitation keeps ice crystals small and adds air, making it "
        "smooth and firm.)",
    ),
    lesson(
        "Lab Techniques: Measuring, Temperature & Timing",
        "Accurate measuring and control of conditions.",
        "GRADUATED CYLINDER -- measures liquid volume (read the meniscus bottom at eye level). BALANCE "
        "-- measures mass. PRECISION / ACCURACY -- repeatable vs correct.",
        "Food Science scores depend on careful measuring: exact volumes, correct temperatures, and "
        "consistent timing.",
        "Read graduated cylinders at eye level at the bottom of the meniscus. Tare the balance with "
        "the container on it. Use a thermometer in the liquid, not touching the container. Time "
        "steps with a stopwatch. Keep everything else constant between trials (same container, same "
        "shaking method, same temperature). Record all values with units and the right number of "
        "decimal places. Know the conversion: 1 mL of water is about 1 g.",
        "Where do you read a water meniscus in a graduated cylinder? (At the bottom of the curve, at "
        "eye level.)",
    ),
    lesson(
        "Experiment Design with One Independent Variable",
        "Designing fair tests for the notebook.",
        "INDEPENDENT VARIABLE -- the one thing you change. DEPENDENT VARIABLE -- what you measure. "
        "CONTROLLED VARIABLES -- everything you keep the same. CONTROL -- a baseline trial.",
        "Each notebook experiment must change exactly ONE thing so you know what caused the result.",
        "Examples: curd mass vs type of acid (vinegar vs lemon juice) with the same milk, volume, "
        "temperature, and drain time; butter mass vs cream temperature; ice-cream height vs salt "
        "amount. State a hypothesis (\"If the cream is 13 C instead of 20 C, then the butter mass "
        "will be greater because...\"). Repeat trials (at least 3) and average. Graph the results. "
        "2027 notebook: at least 3 experiments for EACH of the three lab tasks, one independent "
        "variable each, on the Food Science Experiment Form (only the first 3 per task are graded).",
        "In a test of lemon juice vs vinegar for curdling, name two controlled variables. (Milk "
        "volume and type, temperature, amount of acid, drain time -- any two.)",
    ),
    lesson(
        "Notebook Preparation",
        "Filling out the Food Science Experiment Form for full credit.",
        "EXPERIMENT FORM -- the required template for each notebook experiment. CONCLUSION -- whether "
        "the data supported the hypothesis, and why.",
        "The notebook is graded points you can earn entirely before the tournament. Treat it like a "
        "mini lab report for each experiment.",
        "For each experiment: question, hypothesis, independent and dependent variables, controlled "
        "variables, materials, step-by-step procedure, data table with units, graph, results, "
        "conclusion (supported or not, with the science reason), and sources of error and ideas for "
        "improvement. Each experiment is worth up to 2 points. Make sure every experiment changes "
        "only one variable and covers all three lab tasks (ice cream, curd mass, butterfat). Keep it "
        "neat and labeled; double-check that procedures could be repeated by someone else.",
        "How many experiments per lab task are graded? (The first 3 for each task.)",
    ),
    lesson(
        "Ice Cream Lab Task",
        "Practicing the shaken-bag ice cream task for maximum height.",
        "SELF-STANDING -- holds its shape without support. HEIGHT SCORE -- 0.1 point per mm.",
        "You need ice cream firm enough to stand on its own for 5 seconds -- and as tall as possible.",
        "Recipe basics: milk or cream, sugar, flavoring in a small sealed bag, inside a larger bag of "
        "ice and rock salt. Firmness factors: higher fat content (cream holds air and structure), "
        "less sugar (too much lowers the freezing point and keeps it soft), more salt and ice for a "
        "colder bath, longer and harder shaking. Insulate hands with a towel. Practice forming the "
        "tallest freestanding shape and getting it out of the bag quickly. Log each trial for your "
        "notebook (variable changed, height, time).",
        "Why can adding too much sugar hurt your height score? (Sugar lowers the mix's freezing "
        "point, so the ice cream stays soft.)",
    ),
    lesson(
        "Curd Mass Lab Task",
        "Practicing the curdling task to match the supervisor's mass.",
        "CURD -- the coagulated protein (and trapped fat). WHEY -- the remaining liquid. SCORE -- team "
        "mass / supervisor mass x 10 (max 10).",
        "Curdle 120 mL of milk with vinegar or lemon juice, drain 15 minutes in cheesecloth, and mass "
        "the curd. The goal is a high mass relative to the supervisor's.",
        "Factors: warm milk curdles more completely (heat to about 80-90 C, if allowed); enough acid "
        "to reach about pH 4.6; whole milk gives more curd (fat is trapped); gentle stirring keeps "
        "curds large; consistent draining (don't squeeze unless the rules allow). Measure acid "
        "precisely. Practice to find the amount of acid that gives the most curd for your milk, and "
        "record it in your notebook experiments.",
        "Your curd is 30 g; the supervisor's is 40 g. Score? (30 / 40 x 10 = 7.5.)",
    ),
    lesson(
        "Butterfat Lab Task",
        "Practicing butter-making to separate and mass milk fat.",
        "BUTTER -- mostly fat with some water and milk solids. YIELD -- butter mass from a given cream "
        "volume. SCORE -- team mass / supervisor mass x 10 (max 10).",
        "Shake 150 mL of cream (about 13 C) until it turns into butter, separate the buttermilk, and "
        "mass the butter.",
        "Use a sealed jar, filled no more than halfway so the cream can slosh. Shake hard; expect "
        "whipped cream, then a sudden split into yellow clumps and liquid. Keep shaking briefly to "
        "gather the butter, pour off buttermilk, rinse with cold water, and press out liquid. "
        "Temperature control is key (cool cream). Higher-fat cream increases yield. Losing butter on "
        "the jar walls costs mass -- scrape carefully.",
        "Why fill the jar only halfway? (The cream needs room to slosh so fat globules collide.)",
    ),
    lesson(
        "Integrating All Three Lab Tasks",
        "Running the tasks the way they'll appear at a tournament.",
        "LAB TASK COUNT -- Regionals 1, State 1-2, Nationals 2-3. MULTITASKING -- running tasks in "
        "parallel.",
        "At higher levels you may do two or three tasks in one session. Plan which steps can overlap.",
        "Start the slowest step first: curds need draining time (15 minutes), so curdle early, then "
        "shake butter or ice cream while the curd drains. Partners can split tasks. Have a printed "
        "checklist and a timer. Practice full sessions with all three tasks so the timing feels "
        "natural. Clean up as you go.",
        "With all three tasks, which should you start first? (Curd mass -- it needs 15 minutes of "
        "draining.)",
    ),
    lesson(
        "Notebook Review & Final Preparation",
        "Checking the notebook and packing for the tournament.",
        "REVIEW -- checking against the rules. RUBRIC -- the scoring criteria.",
        "In the final week, check the notebook against the rules line by line and pack everything "
        "you need.",
        "Notebook checklist: 3+ experiments per task on the official form; one independent variable "
        "each; complete data tables, graphs, and conclusions; consistent units; names and team number "
        "as required. Review the science behind each task (casein and pH, phase inversion, freezing "
        "point depression) for written questions. Pack: required notebook, safety equipment, and "
        "whatever the rules let you bring; confirm what the supervisor provides. Do one last timed "
        "practice of each task.",
        "What's the most common reason a notebook experiment loses points? (Changing more than one "
        "variable or missing parts of the form.)",
    ),
]

THERMODYNAMICS = [
    lesson(
        "Systems & Properties",
        "Defining a thermodynamic system and its intensive and extensive properties.",
        "SYSTEM -- the part being studied. SURROUNDINGS -- everything else. OPEN / CLOSED / ISOLATED -- "
        "exchanges matter and energy / energy only / neither. INTENSIVE -- independent of amount "
        "(temperature, density). EXTENSIVE -- depends on amount (mass, volume, energy).",
        "First decide what your system is. Then ask what crosses its boundary -- heat, work, or matter.",
        "Examples: a pot of boiling water without a lid is open; a sealed can is closed; an ideal "
        "thermos approximates isolated. State variables (P, V, T, internal energy) depend only on "
        "the state, not the path; heat and work are path-dependent. Dividing an extensive property "
        "by mass gives an intensive one (specific heat, density). Equilibrium: thermal (same T), "
        "mechanical (same P), chemical.",
        "Is the temperature of a sample intensive or extensive? (Intensive -- it doesn't depend on "
        "how much you have.)",
    ),
    lesson(
        "Temperature, Scales & the Zeroth Law",
        "Temperature scales, conversions, and heat units.",
        "TEMPERATURE -- a measure of average particle kinetic energy. ZEROTH LAW -- if A and B are each "
        "in equilibrium with C, they're in equilibrium with each other. CALORIE -- 4.184 J.",
        "Temperature tells which way heat flows: from hot to cold. The zeroth law is why "
        "thermometers work.",
        "Conversions: K = C + 273.15; F = (9/5) C + 32; C = (F - 32) x 5/9. Absolute zero = 0 K = "
        "-273.15 C = -459.67 F. Water: freezes 0 C/32 F, boils 100 C/212 F at 1 atm. Rankine is the "
        "absolute Fahrenheit scale (R = F + 459.67). Energy units: joule, calorie (4.184 J), food "
        "Calorie = kilocalorie, BTU (about 1,055 J). Thermometer types: liquid expansion, "
        "thermocouples, thermistors, infrared.",
        "Convert 25 C to Fahrenheit and kelvin. (77 F; 298.15 K.)",
    ),
    lesson(
        "Heat Transfer: Conduction, Convection, Radiation",
        "The three ways heat moves, and thermal conductivity.",
        "CONDUCTION -- through direct contact. CONVECTION -- by moving fluid. RADIATION -- by "
        "electromagnetic waves (no medium needed). THERMAL CONDUCTIVITY (k) -- how well a material "
        "conducts heat.",
        "Touching a hot pan is conduction; warm air rising is convection; feeling the sun's warmth is "
        "radiation. The 2027 device task is all about COLLECTING radiant heat from a lamp.",
        "Conduction rate: Q/t = k A (delta T) / L -- more area and temperature difference, less "
        "thickness, more heat. Metals have high k (copper ~400 W/m-K); air and foam are low (~0.03). "
        "Convection: natural (density-driven) or forced (fan). Radiation: dark, matte surfaces absorb "
        "and emit well; shiny surfaces reflect. A clear cover lets light in but slows heat loss (the "
        "greenhouse effect).",
        "Why would a matte black surface help a heat-collecting device? (It absorbs more of the "
        "lamp's radiation than a shiny or light surface.)",
    ),
    lesson(
        "Heat Capacity & Calorimetry",
        "Q = m c delta-T and solving calorimetry problems.",
        "SPECIFIC HEAT (c) -- energy to raise 1 g by 1 C (water: 4.18 J/g-C). HEAT CAPACITY -- for a "
        "whole object (J/C). CALORIMETRY -- measuring heat exchange.",
        "Water takes a lot of energy to warm up. The heat needed depends on mass, the material's "
        "specific heat, and the temperature change.",
        "Q = m c (delta T). Example: warming 100 g of water by 5 C needs 100 x 4.18 x 5 = 2,090 J. "
        "Calorimetry: heat lost = heat gained (in an isolated system). Mixing 50 g of 80 C water with "
        "50 g of 20 C water -> 50 C. For a metal in water: m_metal c_metal (T_metal - T_f) = m_w c_w "
        "(T_f - T_w). Metals have low specific heats (aluminum ~0.90, copper ~0.39 J/g-C), so they "
        "heat and cool quickly.",
        "How much energy raises 100 mL (100 g) of water from 20 C to 30 C? (100 x 4.18 x 10 = 4,180 "
        "J.)",
    ),
    lesson(
        "Phases, Latent Heat & Phase Diagrams",
        "Phase changes, latent vs sensible heat, and reading phase diagrams.",
        "SENSIBLE HEAT -- changes temperature. LATENT HEAT -- changes phase at constant temperature. "
        "HEAT OF FUSION (water 334 J/g). HEAT OF VAPORIZATION (water 2,260 J/g). TRIPLE POINT -- where "
        "solid, liquid, and gas coexist.",
        "While ice melts or water boils, the temperature stays flat -- all the energy goes into "
        "changing the phase.",
        "Heating curve: warm the ice (sensible), melt (flat, latent), warm the water, boil (flat), "
        "warm the steam. Q = m L for phase changes. Example: melting 10 g of ice = 3,340 J. Phase "
        "diagram: axes of pressure and temperature; lines show phase boundaries; the critical point "
        "ends the liquid-gas line. Water's solid-liquid line slopes left (ice melts under pressure) "
        "because ice is less dense than water. Sublimation (dry ice) and deposition (frost).",
        "Why does the temperature stay at 100 C while water boils? (The energy is going into breaking "
        "bonds to change phase -- latent heat.)",
    ),
    lesson(
        "The Ideal Gas Law",
        "PV = nRT and the gas laws it contains.",
        "IDEAL GAS LAW -- PV = nRT (R = 8.314 J/mol-K or 0.0821 L-atm/mol-K). BOYLE'S LAW -- P1V1 = "
        "P2V2 (constant T). CHARLES'S LAW -- V1/T1 = V2/T2 (constant P). GAY-LUSSAC'S LAW -- P1/T1 = "
        "P2/T2 (constant V).",
        "Gas pressure, volume, and temperature are linked. Squeeze a gas and its pressure rises; heat "
        "it and it expands or its pressure rises.",
        "Always use kelvin. Combined gas law: P1V1/T1 = P2V2/T2. At STP (0 C, 1 atm) one mole "
        "occupies about 22.4 L. Example: 2 L of gas at 300 K heated to 450 K at constant pressure -> "
        "3 L. Real gases deviate at high pressure and low temperature. Kinetic theory: pressure comes "
        "from particle collisions; average kinetic energy is proportional to T.",
        "A sealed container at 300 K and 1 atm is heated to 600 K. New pressure? (2 atm.)",
    ),
    lesson(
        "Thermodynamic Processes",
        "Isothermal, adiabatic, isochoric, and isobaric processes on PV diagrams.",
        "ISOTHERMAL -- constant temperature. ADIABATIC -- no heat exchange (Q = 0). ISOCHORIC -- "
        "constant volume (no work). ISOBARIC -- constant pressure. WORK -- area under the PV curve.",
        "Each process holds one thing fixed. On a pressure-volume graph, work done by the gas is the "
        "area under the curve.",
        "Isobaric: W = P (delta V). Isochoric: W = 0, so delta U = Q. Isothermal (ideal gas): delta U "
        "= 0, so Q = W. Adiabatic: Q = 0, so delta U = -W -- compressing warms the gas (bike pump), "
        "expanding cools it (spray cans, rising air in the atmosphere). On a PV diagram, adiabats are "
        "steeper than isotherms. A cycle's net work is the enclosed area.",
        "A gas expands at a constant 200 kPa from 0.010 to 0.030 m^3. Work done by the gas? "
        "(200,000 x 0.020 = 4,000 J.)",
    ),
    lesson(
        "First & Second Laws",
        "Energy conservation and why heat flows hot to cold.",
        "FIRST LAW -- delta U = Q - W (change in internal energy = heat added minus work done BY the "
        "system). SECOND LAW -- heat flows spontaneously from hot to cold; total entropy of an "
        "isolated system never decreases. ENTROPY -- a measure of disorder or energy spread.",
        "Energy can't be created or destroyed (first law), and you can't turn heat completely into "
        "work or make heat flow uphill for free (second law).",
        "Sign convention: Q > 0 heat added; W > 0 work done by the system. (Some chemistry texts use "
        "delta U = Q + W with W done ON the system -- check the convention.) Example: 500 J added, "
        "200 J of work done -> delta U = +300 J. Second-law statements: Kelvin-Planck (no engine "
        "converts heat entirely to work) and Clausius (no device moves heat from cold to hot without "
        "work). Perpetual motion machines violate one or both.",
        "A gas absorbs 800 J and does 300 J of work. Change in internal energy? (+500 J.)",
    ),
    lesson(
        "Engines, Cycles & Carnot Efficiency",
        "Heat engines, refrigerators, and the maximum possible efficiency.",
        "HEAT ENGINE -- converts heat to work. EFFICIENCY -- W / Q_hot. CARNOT EFFICIENCY -- 1 - "
        "T_cold / T_hot (kelvin), the maximum possible. COP -- coefficient of performance for heat "
        "pumps and refrigerators.",
        "Every engine takes heat from a hot source, turns part of it into work, and dumps the rest "
        "into a cold sink. The bigger the temperature gap, the more efficient it can be.",
        "Engine: Q_hot = W + Q_cold. Example: a Carnot engine between 600 K and 300 K -> max "
        "efficiency 50%. Real cycles: Otto (gasoline), Diesel, Rankine (steam power plants), Brayton "
        "(jet turbines). Refrigerators and heat pumps use work to move heat from cold to hot: COP "
        "(fridge) = Q_cold / W; Carnot COP = T_cold / (T_hot - T_cold). Real efficiencies are well "
        "below Carnot because of friction and irreversible heat flow.",
        "Max efficiency of an engine running between 500 K and 300 K? (1 - 300/500 = 40%.)",
    ),
    lesson(
        "Historical Figures",
        "The scientists who built thermodynamics.",
        "Units and laws named for people: kelvin (Lord Kelvin), joule (Joule), Celsius, Fahrenheit, "
        "Carnot cycle, Boltzmann constant.",
        "History questions are quick points. Connect each person to their key idea.",
        "Daniel Fahrenheit: mercury thermometer, F scale (1724). Anders Celsius: C scale (1742). "
        "Joseph Black: latent heat and specific heat. James Watt: improved steam engine. Count "
        "Rumford: heat from friction (cannon boring) challenged caloric theory. Sadi Carnot: ideal "
        "engine efficiency (1824). James Joule: mechanical equivalent of heat. Rudolf Clausius: "
        "entropy, the second law. Lord Kelvin: absolute temperature scale. Ludwig Boltzmann: "
        "statistical entropy (S = k ln W). Josiah Willard Gibbs: free energy. Walther Nernst: third "
        "law.",
        "Who showed that mechanical work could be converted into a fixed amount of heat? (James "
        "Joule.)",
    ),
    lesson(
        "Device Design for Heat Collection (2027)",
        "Designing the 2027 device that collects heat from a lamp into 100 mL of water.",
        "ABSORPTIVITY -- how much incoming radiation a surface absorbs. EMISSIVITY -- how well it emits "
        "its own heat. GLAZING -- a clear cover that traps heat. REFLECTOR -- directs light onto the "
        "target.",
        "The 2027 task is the reverse of past years: instead of keeping hot water hot, your device "
        "must HEAT 100 mL of water in a clear cup using light from a heat lamp. Absorb as much as "
        "possible and lose as little as possible.",
        "Rules: a 100-125 W clear heat bulb in a clamp lamp pointing down; bulb height 40-50 cm at "
        "Regionals (more range at State/Nationals); heating 10 minutes (10-15 at State/Nationals); "
        "100 mL water in a 9 oz clear cup supplied by the supervisor; device with cup fits a 30 cm "
        "cube; parts may be inside the cup but can't touch the water; nothing added to the water. "
        "Banned: any energy source, thermometers or probes, thermoses, coolers, vacuum-sealed parts, "
        "hazardous insulation. Parts start at room temperature. Ideas: a dark absorber wrapped around "
        "or under the cup (not touching the water); reflectors (foil) to concentrate light onto the "
        "cup; a clear top or window to trap heat while letting light in; insulation below and around "
        "the sides to cut conduction and convection losses; small air gaps.",
        "Why might a clear plastic cover over the device raise the final temperature? (It lets light "
        "in but slows heat lost by convection -- like a greenhouse.)",
    ),
    lesson(
        "Prediction Calibration",
        "Using practice runs to predict your device's temperature change.",
        "CALIBRATION -- relating conditions to results with test data. EXTRAPOLATION -- predicting "
        "beyond the data range. INTERPOLATION -- predicting between data points.",
        "Part of the score depends on how well you predict your result. That prediction is only as "
        "good as your practice data.",
        "Do many practice runs at the bulb heights and heating times allowed at your level. Record "
        "starting water temperature, room temperature, bulb height, time, and the final temperature. "
        "Graph temperature rise vs bulb height (and vs time). Radiant intensity falls with distance, "
        "so expect a curve, not a straight line. Use the graph to predict at the announced height "
        "and time. Control variables: the same bulb wattage and type, the same cup, and water starting "
        "at room temperature. Keep your graph in your notes for the event.",
        "Your data show rises of 12 C at 40 cm and 8 C at 50 cm. A good first prediction at 45 cm? "
        "(About 10 C -- interpolate.)",
    ),
    lesson(
        "Radiant Exitance, Blackbody & Third Law (State/Nationals)",
        "Blackbody radiation, Stefan-Boltzmann, and the third law.",
        "RADIANT EXITANCE -- power radiated per unit area (W/m^2). BLACKBODY -- a perfect absorber and "
        "emitter. STEFAN-BOLTZMANN LAW -- M = e sigma T^4 (sigma = 5.67 x 10^-8 W/m^2-K^4). THIRD LAW -- "
        "the entropy of a perfect crystal is zero at absolute zero.",
        "Everything warmer than absolute zero radiates. The hotter it is, the much more it radiates -- "
        "power rises with the fourth power of kelvin temperature.",
        "Doubling T (kelvin) increases radiated power 16 times. Net radiation between an object and "
        "its surroundings: P = e sigma A (T^4 - T_surr^4). Wien's law: peak wavelength = 2,898 "
        "micrometer-K / T -- a heat lamp filament (~2,500-3,000 K) peaks around 1 micrometer, in the "
        "near-infrared, which is why heat lamps heat well. Emissivity e is between 0 and 1 (matte "
        "black near 1, polished metal near 0). Third law: absolute zero can't be reached in a finite "
        "number of steps.",
        "If an object's kelvin temperature doubles, by what factor does its radiated power change? "
        "(16 times.)",
    ),
    lesson(
        "Entropy & Enthalpy (Division C reference)",
        "Enthalpy, entropy, and spontaneity -- listed for Division C State/Nationals.",
        "ENTHALPY (H) -- heat content at constant pressure (delta H < 0 exothermic). ENTROPY (S) -- "
        "energy dispersal/disorder. GIBBS FREE ENERGY -- delta G = delta H - T delta S (delta G < 0 is "
        "spontaneous).",
        "This topic is listed for Division C at State and Nationals. It's useful background for Division "
        "B teams that want a head start, but check your own level's rules before studying it hard.",
        "Exothermic reactions release heat (combustion, delta H < 0); endothermic absorb it (melting, "
        "cold packs). Entropy rises with melting, boiling, dissolving, and more gas molecules. delta "
        "S = Q_rev / T for reversible heat transfer. Spontaneity: delta H < 0 and delta S > 0 -> always "
        "spontaneous; delta H > 0 and delta S < 0 -> never; mixed cases depend on temperature (ice "
        "melts above 0 C because T delta S outweighs delta H). Hess's law adds reaction enthalpies.",
        "Melting ice absorbs heat yet happens spontaneously above 0 C. Why? (The entropy increase "
        "times T outweighs the positive delta H, so delta G < 0.)",
    ),
]
