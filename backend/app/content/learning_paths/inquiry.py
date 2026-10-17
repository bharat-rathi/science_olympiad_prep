"""Learning paths: Inquiry & Nature of Science events."""

from app.content.learning_paths._base import lesson

CODEBUSTERS = [
    lesson(
        "Letter Frequency & Cryptanalysis Basics",
        "Using how often letters appear to break substitution ciphers.",
        "PLAINTEXT -- the original message. CIPHERTEXT -- the encrypted message. FREQUENCY ANALYSIS -- "
        "counting letters to guess substitutions. CRIB -- a known piece of plaintext.",
        "In English, some letters are far more common than others. If one ciphertext letter shows up "
        "most often, it probably stands for E.",
        "English order: E, T, A, O, I, N, S, H, R, D, L, U (\"ETAOIN SHRDLU\"). Common short words: "
        "THE, AND, A, I, OF, TO, IN, IS, THAT. Common pairs: TH, HE, IN, ER, AN; doubles: LL, EE, SS, "
        "OO, TT. Patterns help: a one-letter word is A or I; an apostrophe-S or -T. The packet "
        "includes a resource sheet with English and Spanish frequencies, Morse, Porta and Atbash "
        "tables, and Baconian mappings -- no calculators or notes are allowed.",
        "The most frequent ciphertext letter is Q, and the most common three-letter word is QZM. "
        "Guess? (Q might be E or T; QZM is likely THE, so Q = T, Z = H, M = E.)",
    ),
    lesson(
        "Caesar/Shift & Atbash Ciphers",
        "The simplest substitution ciphers.",
        "CAESAR CIPHER -- every letter shifted the same number of places. ATBASH -- the alphabet "
        "reversed (A <-> Z, B <-> Y). KEY -- the shift amount.",
        "Caesar shifts the whole alphabet by a fixed amount. Atbash flips it. Both are easy once you "
        "spot the pattern.",
        "Caesar with shift 3: A -> D, B -> E, ... X -> A. To decrypt, shift back. Only 25 possible "
        "shifts, so you can test them quickly; or find E's position. Atbash: A=Z, B=Y, C=X, ... M=N "
        "(and it's its own inverse). Both are monoalphabetic -- each letter always maps to the same "
        "cipher letter. Write the alphabet across the top of your paper to work fast.",
        "Decrypt the Atbash ciphertext SVOOL. (HELLO.)",
    ),
    lesson(
        "Aristocrat Solving",
        "Solving substitution ciphers with word spacing.",
        "ARISTOCRAT -- a monoalphabetic substitution cipher that keeps spaces and punctuation. PATTERN "
        "WORD -- a word with repeated letters (e.g. PEOPLE = ABCADB).",
        "Aristocrats keep word breaks, so look for short words and repeated-letter patterns. Fill in a "
        "few letters, and the rest follow.",
        "Strategy: count frequencies; try THE and AND on three-letter words; one-letter words are A "
        "or I; apostrophes give 'S, 'T, 'LL, 'RE. Pattern words: THAT (ABCA), THERE (ABCDC), LITTLE "
        "(ABCCAD). In 2027, no letter ever decrypts to itself in Aristocrats, Patristocrats, "
        "and Xenocrypts. Question 1 is an Aristocrat with a Timing Bonus = 2 x (600 - seconds) if "
        "solved within 10 minutes. Two or fewer errors earns full credit.",
        "A cipher word has the pattern ABCA. Name two English words that fit. (THAT, DEAD -- or "
        "others like HIGH.)",
    ),
    lesson(
        "Patristocrat Solving",
        "Substitution ciphers without word spaces.",
        "PATRISTOCRAT -- a substitution cipher written in groups of five letters, with no word "
        "breaks. DIGRAPH / TRIGRAPH -- common two- and three-letter combinations.",
        "Without spaces you can't use short words, so you lean on frequency and common letter "
        "combinations instead.",
        "Find the most frequent letter (likely E or T). Look for the most common trigraph (often THE "
        "or ING) and digraph (TH, HE, IN, ER). Spot doubled letters (LL, SS, EE). Q is almost always "
        "followed by U. Try a crib if given. Once a few letters are in, words appear. Patristocrats "
        "are slower than Aristocrats, so practice regularly.",
        "In a Patristocrat, the trigraph KXG appears five times. Good first guess? (THE.)",
    ),
    lesson(
        "K1 Alphabets & Keyword Recovery",
        "Keyed alphabets where the keyword is in the plaintext alphabet.",
        "K1 ALPHABET -- the keyword (duplicate letters removed) and the remaining letters form the "
        "PLAINTEXT alphabet, matched to a normal ciphertext alphabet (often shifted). KEYWORD -- the "
        "word used to build the alphabet.",
        "Some ciphers build their alphabet from a keyword. Once you've decoded a few letters, you can "
        "rebuild the whole alphabet and read off the keyword -- which fills in the letters you're "
        "missing.",
        "K1: plaintext row = KEYWORD + remaining letters in order; ciphertext row = A-Z (possibly "
        "shifted). Example keyword GARDEN: plaintext GARDENBCFHIJKLMOPQSTUVWXYZ over ciphertext "
        "ABCDEFG... Recovery: write the plaintext letters you've found in order of their ciphertext "
        "letters; a run of consecutive alphabet letters (B C F H I J...) shows where the keyword ends. "
        "Questions may ask you to name the keyword.",
        "In a K1 alphabet, the plaintext row begins MOUSE... What comes after the keyword (if the "
        "keyword is MOUSE)? (The rest of the alphabet in order, skipping M, O, U, S, E: ABCDFGHIJKL...)",
    ),
    lesson(
        "K2 & K3 Alphabets",
        "Keyed alphabets in the ciphertext row, or in both rows.",
        "K2 -- the keyword alphabet is the CIPHERTEXT row under a normal plaintext alphabet. K3 -- the "
        "same keyword alphabet in both rows, with an offset.",
        "These are the same idea as K1, just with the keyword placed differently. Recovery works the "
        "same way: line up what you know and look for the keyword.",
        "K2: plaintext A-Z; ciphertext = KEYWORD + remaining letters (possibly shifted). To recover, "
        "write the ciphertext letters in plaintext order and look for the keyword at the start of a "
        "run. K3: both rows use the same keyed alphabet, offset by some amount (so no letter maps to "
        "itself). Practice building each from a keyword so you recognize them instantly.",
        "Which alphabet type puts the keyword in the ciphertext row under a regular A-Z plaintext? "
        "(K2.)",
    ),
    lesson(
        "Xenocrypts (Spanish)",
        "Solving substitution ciphers in Spanish.",
        "XENOCRYPT -- an Aristocrat in a foreign language (Spanish in Codebusters). N-TILDE -- "
        "usually written as N. ACCENTS -- dropped.",
        "Spanish has different common letters and words. Use Spanish frequency and short words "
        "instead of English ones.",
        "Spanish frequency starts roughly E, A, O, S, R, N, I, D, L, C. Common words: DE, LA, QUE, EL, "
        "EN, Y, LOS, SE, DEL, LAS, UN, POR, CON, NO, UNA. Endings: -CION, -ADO, -MENTE, plurals in -S "
        "and -ES. Double letters: LL, RR, CC. Q is followed by U (QUE, QUI). One-letter words: Y, A, "
        "O. No letter decrypts to itself.",
        "A two-letter cipher word appears more than any other in a Spanish xenocrypt. Two good "
        "guesses? (DE or LA -- then try EL and EN.)",
    ),
    lesson(
        "Baconian Cipher",
        "Hiding a message in a two-symbol code.",
        "BACONIAN CIPHER -- each letter is a 5-symbol group of A's and B's (A = AAAAA, B = AAAAB, ...). "
        "STEGANOGRAPHY -- hiding a message inside something else.",
        "Each letter becomes five binary-like symbols. Those A/B symbols can be disguised as two "
        "kinds of anything: two fonts, upper vs lower case, two symbols, even words.",
        "Use the resource sheet's mapping (it may use the 24-letter version where I/J and U/V share "
        "codes). Step 1: decide which characters are \"A\" and which are \"B\" (try one assignment; if "
        "you get nonsense, swap). Step 2: split into groups of five. Step 3: look each up. Treat the "
        "A/B assignment as a binary number: AAAAA = 0 = A, AAAAB = 1 = B, AABAA = 4 = E (in the "
        "26-letter version).",
        "Decode AABBB using A=0, B=1 and the 26-letter version. (00111 = 7 = H.)",
    ),
    lesson(
        "Porta Cipher",
        "A polyalphabetic cipher with a keyword and 13 tables.",
        "PORTA CIPHER -- a reciprocal polyalphabetic cipher using 13 alphabets selected by a keyword. "
        "RECIPROCAL -- encrypting and decrypting are the same operation.",
        "Each keyword letter picks one of 13 table rows. Because Porta is reciprocal, you use the same "
        "table to encrypt and to decrypt.",
        "Write the keyword repeatedly above the ciphertext. For each pair, use the table row for that "
        "key letter (AB, CD, EF, ... YZ share rows) and swap the letter with its partner in that row. "
        "A letter in the first half (A-M) always maps to the second half (N-Z), and vice versa. "
        "Crib-based cryptanalysis: if you know some plaintext, you can work out which table row was "
        "used, giving the key letter (one of two possibilities per row), and then the keyword "
        "length.",
        "In a Porta cipher, can plaintext A ever encrypt to B? (No -- first-half letters always map to "
        "the second half, N-Z.)",
    ),
    lesson(
        "Columnar Transposition",
        "Rearranging letters by columns, and reconstructing the grid.",
        "TRANSPOSITION -- letters are rearranged, not substituted. COLUMNAR -- write the message in "
        "rows, read out by columns in a key order. COMPLETE COLUMNAR -- every column is full.",
        "Transposition keeps the same letters as the plaintext -- so frequencies look like normal "
        "English. The challenge is putting them back in the right order.",
        "Encrypt: write the plaintext in rows under a key of N columns; read columns in the key's "
        "alphabetical order. Decrypt: number of rows = length / columns; cut the ciphertext into "
        "column-length chunks; arrange them under the key order; read across. If the number of "
        "columns is unknown, try divisors of the message length. Use a crib: find where the crib's "
        "letters line up in rows. In 2027, crib positions are marked on every crib problem except the "
        "Complete Columnar.",
        "A 24-letter message is a complete columnar with 6 columns. How many rows? (4.)",
    ),
    lesson(
        "Nihilist & Checkerboard Ciphers",
        "Ciphers built on a Polybius square.",
        "POLYBIUS SQUARE -- a 5x5 grid (I/J combined) where each letter becomes a row-column number "
        "pair. NIHILIST -- adds a numeric key to the Polybius numbers. CHECKERBOARD -- a Polybius "
        "square with keyword-labeled rows and columns.",
        "Turn letters into two-digit numbers using a grid, then disguise those numbers with a key. "
        "Undo the key and you're back to grid coordinates.",
        "Polybius: build the grid from a keyword (keyword letters first, then the rest). Nihilist: "
        "convert plaintext and key letters to numbers; ciphertext = plaintext number + key number "
        "(repeating key). Decrypt by subtracting the key's number; e.g. 57 - 23 = 34 = row 3, column "
        "4. Numbers over 100 or with a carry signal larger sums. Checkerboard: rows and columns are "
        "labeled with letters from keywords, so each plaintext letter becomes two letters.",
        "Nihilist ciphertext 46, key value 23. Plaintext coordinates? (46 - 23 = 23 = row 2, column "
        "3.)",
    ),
    lesson(
        "Fractionated Morse",
        "Morse code split into threes and substituted with letters.",
        "FRACTIONATED MORSE -- plaintext to Morse (with x between letters and xx between words), split "
        "into groups of three symbols, and each triple mapped to a letter via a keyed alphabet. "
        "TRIGRAPH -- a group of three symbols.",
        "First the message becomes dots, dashes, and separators. Then every three symbols become one "
        "letter. To decrypt, reverse both steps.",
        "There are 26 usable triples (from ..., ..-, ..x, ... to xx- ; xxx is never used), one per "
        "letter of a keyed alphabet. Decrypt: build the triple table from the keyword, replace each "
        "ciphertext letter with its triple, join them, split at x (letter) and xx (word), and read "
        "the Morse. A crib speeds things up: Morse for the crib tells you some triples directly. Use "
        "the resource sheet's Morse table.",
        "Why can't xxx appear in fractionated Morse? (It would mean three separators in a row, which "
        "never occurs -- one x separates letters, two separate words.)",
    ),
    lesson(
        "Homophonic Ciphers",
        "Substitution with several cipher symbols per letter.",
        "HOMOPHONIC CIPHER -- a substitution where common letters have several possible cipher "
        "symbols (homophones), flattening letter frequencies.",
        "Because E might be written five different ways, simple frequency counts don't work as well. "
        "You need patterns and cribs instead.",
        "Look for repeated groups of symbols that might be common words, use the given crib to pin "
        "down several homophones, and note that each homophone still maps to just one plaintext "
        "letter. Groups of symbols that appear in the same context probably stand for the same "
        "letter. 2027: the Homophonic cipher is on the list, and at least one Special Bonus question "
        "must be a Homophonic -- Special Bonuses pay 150, 400, or 750 points for 1, 2, or 3 solved "
        "with no errors.",
        "Why does a homophonic cipher defeat simple frequency analysis? (Common letters are spread "
        "across several symbols, so no single symbol stands out.)",
    ),
    lesson(
        "Cryptarithms",
        "Letter-for-digit arithmetic puzzles.",
        "CRYPTARITHM -- an arithmetic problem where each letter stands for a different digit. "
        "CONSTRAINT PROPAGATION -- using each deduction to limit the remaining options. LEADING DIGIT "
        "-- the first letter of a number can't be 0.",
        "Each letter is a digit; different letters are different digits. Start with columns that give "
        "the most information, like a carry into a new leftmost column.",
        "Classic: SEND + MORE = MONEY -> M must be 1 (a carry from adding two 4-digit numbers), so O "
        "is 0, and so on. Steps: list constraints (carries are 0 or 1 in addition), find forced "
        "values, test small cases. Answers need zero errors for full credit in 2027. After solving, "
        "the digits often spell a word when arranged in order (0-9).",
        "In AB + AB = CDA, what must C be? (1 -- the sum of two 2-digit numbers is under 200.)",
    ),
    lesson(
        "Exam Strategy",
        "Timing, choosing bonus questions, and keeping errors down.",
        "TIMING BONUS -- 2 x (600 - seconds) on question 1, earned within 10 minutes. SPECIAL BONUS -- "
        "up to 3 non-Aristocrat/Patristocrat/Xenocrypt questions. ERROR RULE -- two or fewer errors = "
        "full credit; each extra error costs 100 points.",
        "Codebusters rewards speed AND accuracy. Plan who solves what before the test starts.",
        "Teams of up to 3, about 50 minutes, writing utensils only. Have your fastest Aristocrat "
        "solver take question 1 for the timing bonus and call time as soon as it's done. Divide the "
        "rest by specialty (one person for Patristocrats and Xenocrypts, one for math-based ciphers). "
        "Attempt Special Bonus questions you're confident in -- they pay only with no errors. Check "
        "work: an error-free answer is worth more than a fast messy one. Skip and come back if stuck. "
        "Practice timed full tests as a team.",
        "Question 1 is solved in 4 minutes 10 seconds. Timing bonus? (2 x (600 - 250) = 700 "
        "points.)",
    ),
]

EXPERIMENTAL_DESIGN = [
    lesson(
        "A Testable Question",
        "Writing a clear statement of the problem.",
        "STATEMENT OF PROBLEM -- the question the experiment answers. TESTABLE -- can be answered by "
        "measuring something.",
        "Your question should name what you'll change and what you'll measure: \"How does X affect "
        "Y?\"",
        "Good: \"How does the height a ball is dropped from affect how high it bounces?\" Weak: \"Do "
        "balls bounce?\" The question must be about the assigned topic and materials (drifting off "
        "topic costs up to x0.75). Include the independent and dependent variables in the wording. "
        "The first 20 minutes are for designing and running the experiment with Part I of the form.",
        "Rewrite \"What about paper airplanes?\" as a testable question. (Example: \"How does wing "
        "length affect how far a paper airplane flies?\")",
    ),
    lesson(
        "A Directed Hypothesis",
        "Predicting the direction of the effect, with a reason.",
        "HYPOTHESIS -- a testable prediction. DIRECTED -- states the direction (increase/decrease). "
        "RATIONALE -- the scientific reason.",
        "Use an \"If..., then..., because...\" structure so the prediction and its reason are both "
        "clear.",
        "Example: \"If the drop height increases, then the bounce height will increase, because the "
        "ball will have more gravitational potential energy to convert.\" A directed hypothesis "
        "names the direction of change. It doesn't have to be right -- it has to be testable and "
        "reasoned. Avoid \"I think\" and vague words like \"affect.\"",
        "Is \"Temperature will affect dissolving\" directed? (No -- it doesn't say whether dissolving "
        "speeds up or slows down.)",
    ),
    lesson(
        "Independent, Dependent & Controlled Variables",
        "Identifying the three kinds of variables.",
        "INDEPENDENT VARIABLE (IV) -- what you deliberately change. DEPENDENT VARIABLE (DV) -- what you "
        "measure. CONTROLLED VARIABLES -- conditions kept the same.",
        "Change one thing (IV), measure one result (DV), and hold everything else constant.",
        "Name at least 3 controlled variables specifically (\"same ball,\" \"same floor surface,\" "
        "\"same person releasing\"). The IV should have at least 3 levels (more is better) so you can "
        "see a trend. Include units for the IV and DV. Scorers want the levels of the IV listed, not "
        "just the variable's name.",
        "In the ball-drop experiment, which is the DV: drop height or bounce height? (Bounce height.)",
    ),
    lesson(
        "Control Groups & Constants",
        "The difference between a control and controlled variables.",
        "CONTROL (STANDARD OF COMPARISON) -- a trial used as a baseline. CONSTANT -- a factor kept the "
        "same in every trial.",
        "A control lets you compare: what happens without the change, or at a normal level? Constants "
        "keep the comparison fair.",
        "Examples: in a fertilizer test, the plant with no fertilizer is the control; in a ramp-height "
        "test, a standard height might be the control. Not every experiment has a \"no treatment\" "
        "group, but you should name the standard of comparison. Controlled variables (constants) are "
        "different -- they're everything held the same in all trials.",
        "Testing salt's effect on boiling point: what's a good control? (Pure water with no salt.)",
    ),
    lesson(
        "Materials List",
        "Listing materials with quantities and sizes.",
        "MATERIALS LIST -- every item used, with amounts and sizes. SPECIFICITY -- enough detail that "
        "someone could gather the same things.",
        "Someone else should be able to gather exactly what you used from your list.",
        "Include quantities and sizes: \"1 tennis ball (6.5 cm diameter),\" \"1 meter stick,\" \"masking "
        "tape (about 30 cm).\" List everything, including the measuring tools (your allowed "
        "timepiece, linear measuring device, and Class II calculator are for normal use only, never "
        "as part of the experiment). Use metric units.",
        "Improve this entry: \"some water.\" (Example: \"200 mL tap water at room temperature.\")",
    ),
    lesson(
        "A Repeatable Procedure",
        "Writing steps someone else could follow exactly.",
        "PROCEDURE -- numbered, step-by-step instructions. REPEATED TRIALS -- doing each level more "
        "than once. REPLICABLE -- others could repeat it and get similar results.",
        "Write the procedure so a stranger could do your experiment and get the same kind of data.",
        "Number the steps; include how to measure (\"measure from the floor to the bottom of the "
        "ball\"); state the IV levels and how many trials per level (at least 3); describe how "
        "controls are maintained; include safety notes. Use precise amounts and units. A diagram is "
        "fine if it's labeled. The procedure is a tiebreaker category, so it matters.",
        "Why is \"drop the ball and see\" a weak step? (It doesn't say from what height, how it's "
        "released, or how the bounce is measured.)",
    ),
    lesson(
        "Qualitative Observations",
        "Recording what you notice besides the numbers.",
        "QUALITATIVE -- descriptive (color, sound, texture, behavior). QUANTITATIVE -- numeric. "
        "OBSERVATION -- noted during the experiment, not made up afterward.",
        "Numbers tell part of the story. Write down what else you notice: the ball spun, the paper "
        "tore, a trial seemed off.",
        "Record observations during the experiment, tied to specific trials. Good ones help explain "
        "outliers (\"trial 3 hit the edge of the table\") and suggest errors. They should be "
        "objective: \"the ball wobbled\" rather than \"the ball was bad.\" Collect real on-site data -- "
        "falsified or no data costs x0.25.",
        "Is \"the solution turned cloudy after 30 seconds\" qualitative or quantitative? "
        "(Qualitative, with a quantitative time noted.)",
    ),
    lesson(
        "Data Tables",
        "Building a clear, complete table.",
        "DATA TABLE -- organized results with a title, labeled columns, and units. AVERAGE -- the mean "
        "of the trials.",
        "Put the IV in the first column and the DV trials next, with an average column at the end.",
        "Include: a descriptive title (\"Effect of Drop Height on Bounce Height\"), column headings "
        "with units, all trials, and averages. Use consistent decimal places matching your "
        "measuring tool's precision. Don't leave blanks -- if a trial failed, note why. The data table "
        "is a tiebreaker category.",
        "Where do units belong in a data table? (In the column headings, not repeated in every cell.)",
    ),
    lesson(
        "Choosing & Labeling the Graph",
        "Picking the right graph type and labeling it fully.",
        "LINE GRAPH -- continuous IV (height, time). BAR GRAPH -- categorical IV (types of ball). "
        "SCATTER PLOT -- shows relationships, with a best-fit line. AXES -- x = IV, y = DV.",
        "If the IV is numbers on a scale, use a line or scatter graph. If it's categories, use a bar "
        "graph.",
        "Requirements: a title, labeled axes with units, IV on the x-axis, DV on the y-axis, even "
        "scales, a legend if needed, plotted averages (often with all trials or range shown). Use "
        "most of the grid. Draw a best-fit line for continuous data rather than connecting dots. The "
        "graph is a tiebreaker category.",
        "Which graph type fits \"Bounce height of four different ball types\"? (A bar graph -- the IV "
        "is categorical.)",
    ),
    lesson(
        "Basic Statistics",
        "Mean, median, mode, range, and more at State/Nationals.",
        "MEAN -- average. MEDIAN -- the middle value. MODE -- the most common value. RANGE -- max - min. "
        "STANDARD DEVIATION -- a measure of spread.",
        "Statistics summarize your data and show how consistent it is.",
        "Report mean (or median if there are outliers) and range for each IV level. Low range = more "
        "consistent data. State/Nationals add statistics rows (worth more points: Part II = 67 points "
        "at State/Nationals vs 55): e.g. standard deviation, slope of the best-fit line, and "
        "percent difference. Interpret statistics in words: \"The range was small (0.4 cm), so the "
        "trials were consistent.\"",
        "Trials: 12, 14, 13, 30 cm. Which is a better summary, mean or median? (Median, 13.5 cm -- 30 "
        "is an outlier.)",
    ),
    lesson(
        "Interpreting Data (CER)",
        "Answering the problem statement using claim, evidence, and reasoning.",
        "CER -- claim, evidence, reasoning. CLAIM -- the answer to your question. EVIDENCE -- specific "
        "data. REASONING -- the science explaining why.",
        "State what you found, point to the numbers that show it, and explain the science behind it.",
        "Example: \"Claim: higher drop heights produce higher bounces. Evidence: average bounce rose "
        "from 22 cm at 50 cm drop to 61 cm at 150 cm drop. Reasoning: more potential energy at release "
        "means more kinetic energy at impact, so more energy is available for the rebound.\" Say "
        "whether the hypothesis was supported. CER is the first tiebreaker.",
        "What's missing from \"The hypothesis was supported\"? (Specific evidence from the data and "
        "the scientific reasoning.)",
    ),
    lesson(
        "Experimental Errors",
        "Naming specific errors and their effects.",
        "SYSTEMATIC ERROR -- pushes all results one way (a miscalibrated ruler). RANDOM ERROR -- "
        "unpredictable variation (reaction time). HUMAN ERROR -- too vague to earn credit on its own.",
        "\"Human error\" doesn't earn points. Name the specific error, which way it pushed the results, "
        "and how to fix it.",
        "Example: \"Reading the bounce height by eye was imprecise by about 2 cm; this random error "
        "spread the trials. Filming against a meter stick would reduce it.\" Systematic example: "
        "\"The ruler started 0.5 cm from its end, so all heights were 0.5 cm too high.\" Link errors "
        "to your observations.",
        "Why does \"we made mistakes\" score poorly? (It doesn't identify a specific error, its "
        "effect, or a fix.)",
    ),
    lesson(
        "Real-World Applications",
        "Connecting your results to something practical.",
        "APPLICATION -- where your findings are useful outside the lab.",
        "Show why your experiment matters: who would use the result, and how?",
        "Example: bounce height vs drop height applies to designing sports balls, choosing playground "
        "surfaces, or packaging that protects falling objects. Be specific and tie the application "
        "to your actual result. State/Nationals add applications rows to Part II.",
        "Give one application for an experiment on how insulation thickness affects cooling rate. "
        "(Example: choosing how thick to make a lunch box's insulation.)",
    ),
    lesson(
        "Improvements & Further Experiments",
        "Suggesting how to make the experiment better and what to test next.",
        "IMPROVEMENT -- a change that would make the same experiment more accurate. FURTHER EXPERIMENT "
        "-- a new question that builds on yours.",
        "Improvements fix your errors. Further experiments ask the next question.",
        "Improvement: \"Use a video camera to measure bounce height to the nearest 0.5 cm.\" \"Do 5 "
        "trials per level instead of 3.\" Further experiment: \"Test how surface type affects bounce "
        "height at a fixed drop height.\" Each should be specific and tied to what you learned. "
        "Remember the general multipliers: x0.95 for not cleaning up; unsafe behavior = "
        "disqualification.",
        "Is \"test a different variable\" a good further-experiment suggestion? (Not on its own -- "
        "name the variable and why it's worth testing.)",
    ),
]

PING_PONG_PARACHUTE = [
    lesson(
        "Terminal Velocity",
        "Why a falling parachute stops speeding up.",
        "TERMINAL VELOCITY -- the constant speed when drag equals weight. DRAG -- air resistance. "
        "WEIGHT -- m g.",
        "As the ball and parachute fall faster, air drag grows until it balances gravity. Then they "
        "fall at a steady speed -- the slower that speed, the longer the time aloft.",
        "At terminal velocity, drag = weight: (1/2) rho v^2 Cd A = m g, so v_t = sqrt(2 m g / (rho Cd "
        "A)). A bigger canopy area or higher drag coefficient lowers v_t; a heavier payload raises "
        "it. A ping pong ball is about 2.7 g, so the parachute's own mass matters a lot. Score = "
        "longest time aloft from a single launch (middle of 3 timers).",
        "If you quadruple canopy area, how does terminal velocity change? (It halves -- v_t is "
        "proportional to 1/sqrt(A).)",
    ),
    lesson(
        "The Drag Equation",
        "Each variable in the drag equation and what you control.",
        "DRAG EQUATION -- F_d = (1/2) rho v^2 Cd A. rho -- air density (~1.2 kg/m^3). Cd -- drag "
        "coefficient (shape-dependent). A -- reference area.",
        "Drag grows with speed squared, area, and how \"draggy\" the shape is. You control the area "
        "and shape of the parachute.",
        "Doubling speed quadruples drag. Cd for a round canopy is about 0.75-1.5 depending on shape "
        "(cupped canopies are higher than flat sheets). A spill hole lowers Cd slightly but steadies "
        "the descent (less oscillation). You can't change air density, but note that warm or "
        "high-altitude air is less dense (slightly faster fall).",
        "Which variable in the drag equation has the biggest effect if doubled? (Velocity -- drag "
        "goes up 4 times.)",
    ),
    lesson(
        "Canopy Area & Fall Time",
        "How parachute size affects time aloft.",
        "CANOPY -- the parachute fabric. SURFACE AREA -- for a circle, pi r^2. SINK RATE -- descent "
        "speed.",
        "Bigger parachutes fall slower -- but they're heavier, harder to pack, and slower to open.",
        "Time aloft is roughly peak height / sink rate (plus the climb). Doubling diameter quadruples "
        "area and halves the sink rate (v proportional to 1/sqrt(A)). Diminishing returns: the canopy's "
        "own mass adds to the weight, and a large chute may not deploy before the rocket's apex. Use "
        "very light material (thin plastic, like a garbage bag; Mylar is banned in 2027). Test several "
        "sizes and log the results.",
        "Diameter goes from 30 cm to 60 cm with the same total mass. Sink rate change? (About half -- "
        "area is 4 times as large.)",
    ),
    lesson(
        "Parachute Packing",
        "Folding the parachute so it deploys reliably.",
        "PACKING -- folding and placing the parachute. DEPLOYMENT -- opening in flight. TANGLE -- shroud "
        "lines wrapping and preventing opening.",
        "A perfect parachute is useless if it doesn't open. Pack the same way every time.",
        "Fold the canopy in a consistent pattern (e.g. fold in half, then into thirds, then roll "
        "loosely), keep shroud lines straight and stacked together, and avoid wrapping lines tightly "
        "around the canopy. Don't pack it too tightly or it won't open. Dust with talc (if allowed) to "
        "reduce sticking. Practice packing until it's fast and repeatable -- you get 5 minutes for 2 "
        "launches. A payload that doesn't separate from the rocket earns x0.90.",
        "Why should shroud lines never be wrapped tightly around the folded canopy? (They can hold it "
        "closed or tangle, so it fails to open.)",
    ),
    lesson(
        "Analyzing the Practice Log",
        "Using flight data to choose the launch pressure.",
        "PRACTICE LOG -- the required record of test flights. LAUNCH PRESSURE -- psi in the bottle. "
        "PEAK HEIGHT -- estimated maximum altitude.",
        "Your practice log shows which launch pressure gives the longest time aloft without hitting "
        "the ceiling. It's also required -- missing or incomplete logs cost points.",
        "2027 log: 10+ test flights recording pressure (psi), estimated peak height (feet), and time "
        "aloft (seconds), plus at least two more parameters (e.g. parachute size, fin design, "
        "temperature, deployment success). Graph pressure vs height and pressure vs time aloft. Pick "
        "the pressure that gets close to, but safely under, the announced ceiling height. Teams "
        "without a complete log are capped at a supervisor-set safe pressure; multipliers x0.85 for "
        "an incomplete log, x0.70 for none.",
        "Your log shows 50 psi reaches 22 ft and 60 psi reaches 27 ft. The ceiling is 25 ft. What "
        "pressure should you choose? (A bit under 60 -- around 54-55 psi -- to get high without a "
        "ceiling strike.)",
    ),
    lesson(
        "This Year's Rules (Rocket & Lofting)",
        "The 2027 rules for the rocket, payload, and launch.",
        "PRESSURE VESSEL -- the bottle. BLUNT NOSE -- a bottle cap placed on the nose must not touch "
        "its tip. CEILING STRIKE -- anything touching the ceiling on the way up (x0.25).",
        "The rules on materials and construction are strict. Build to them from the start.",
        "2027: the rocket is one 1-liter-or-smaller plastic carbonated-beverage bottle, unaltered (no "
        "cutting, sanding, hot glue, super glue, or spray paint), with its label present. Fins and "
        "parts attach with TAPE ONLY, at least 5 cm above the bottle opening; no metal anywhere; no "
        "Mylar. Blunt nose. Air pressure from the pump is the only energy source -- no water. "
        "Parachutes attach to the ball with tape only. Bring up to two rockets, two unaltered "
        "standard ping pong balls, two parachutes, and the practice log; a manual bicycle pump with "
        "gauge that fits the supplied Schrader-valve launcher is allowed.",
        "Can you use a 2-liter bottle? (No -- the bottle must be 1 liter or smaller.)",
    ),
    lesson(
        "Shroud-Line Symmetry",
        "Why equal lines matter for a steady descent.",
        "SHROUD LINES -- the strings connecting canopy to payload. SYMMETRY -- equal length and spacing. "
        "OSCILLATION -- swinging back and forth.",
        "If one line is shorter, the canopy tilts and slides sideways, spilling air -- it falls faster "
        "and may drift.",
        "Use equal-length lines (measure carefully), spaced evenly around the canopy edge (e.g. 6 or 8 "
        "lines). Line length about equal to the canopy diameter is a common starting point. Tie or "
        "tape all lines to a single point on the ball. A small spill hole in the center reduces "
        "oscillation. Check symmetry before each launch.",
        "A parachute glides off to one side every time. Likely cause? (Uneven shroud lines -- the "
        "canopy is tilted.)",
    ),
    lesson(
        "How Terminal Velocity Changes",
        "Predicting the effect of payload mass and canopy size.",
        "PAYLOAD -- what the parachute carries (the ping pong ball plus parachute). WING LOADING (for "
        "parachutes) -- mass per canopy area.",
        "Heavier payload -> faster fall. Bigger canopy -> slower fall. The balance between them sets "
        "the time aloft.",
        "v_t is proportional to sqrt(m / A): doubling mass raises v_t by about 41% (sqrt 2); doubling "
        "area lowers it by about 29%. Since the ball's mass is fixed, reduce the mass of tape, lines, "
        "and canopy. Lighter isn't always better if it makes deployment unreliable. Use your log to "
        "check predictions.",
        "You add 1 g of tape to a 3 g payload. Roughly how does v_t change? (sqrt(4/3) = about 15% "
        "faster.)",
    ),
    lesson(
        "Deployment Timing",
        "Getting the parachute to open at the right moment.",
        "APEX -- the rocket's highest point. EJECTION -- the payload leaving the rocket. DEPLOYMENT "
        "DELAY -- time from ejection to a fully open canopy.",
        "The parachute should open near the top of the flight. Too early wastes height; too late wastes "
        "time falling fast.",
        "Bottle rockets usually separate passively: the payload sits loosely in or on a nose cone "
        "and slides out as the rocket slows and tips over at apex. Design so separation happens near "
        "apex: a loose-fitting cone, a rocket that turns over cleanly. A chute that opens late loses "
        "seconds in free fall. Non-separation costs x0.90. Test and note deployment success in your "
        "log (a good extra parameter).",
        "The parachute opens only after the ball has fallen halfway down. Effect on score? (Lower "
        "time aloft -- the ball fell fast for part of the descent.)",
    ),
    lesson(
        "Parachute Physics in Other Events",
        "How drag and descent connect to gliders and other flight events.",
        "DRAG -- the same equation in every flight event. LIFT -- the upward force on a wing. GLIDE "
        "RATIO -- horizontal distance per height lost.",
        "Parachutes slow a fall with drag. Gliders and rubber-powered planes use lift to stay up. Both "
        "rely on understanding air forces.",
        "Elastic Launched Glider: time aloft = height / sink rate, just like the parachute; gliders "
        "lower sink rate with lift. Wright Stuff (Division C) uses rubber-powered propellers and "
        "light structures. Shared skills: logging flights, trimming for stability, minimizing mass, "
        "and estimating heights. Teammates can share test spaces and timing setups.",
        "What does a parachute have in common with a glider's descent? (Both want a low sink rate; "
        "time aloft = height / sink rate.)",
    ),
]

WRITE_IT_DO_IT = [
    lesson(
        "Coordinate System & Face Naming",
        "Agreeing on directions and names before the event.",
        "REFERENCE FRAME -- an agreed set of directions (front/back, left/right, top/bottom). FACE -- a "
        "flat side of a piece. ORIENTATION -- which way a piece points.",
        "The builder can't see the object, so you and your partner need a shared language for "
        "directions. Set it up before the tournament.",
        "Define: the table edge nearest the builder is \"front\"; left and right from the builder's "
        "view; \"up\" is away from the table. Name faces of common pieces (\"long face,\" \"end face\"). "
        "Agree on how to describe angles (\"tilted 45 degrees toward the right\") and measurements "
        "(\"about 3 cm\"). Abbreviations are allowed without definitions, and numerals, single "
        "letters, and scientific symbols are fine -- but no drawings or diagrams.",
        "Why agree on \"front\" before the event? (So the builder places pieces facing the same "
        "direction the writer intended.)",
    ),
    lesson(
        "Attachment Language Basics",
        "Describing exactly how pieces connect.",
        "ATTACHMENT -- how two pieces join. INSERT / STACK / ALIGN -- precise action words. FLUSH -- "
        "edges lined up exactly.",
        "Most points come from correct connections. Say which piece, which spot, and how they join.",
        "Template: \"Take the [color, size, type] piece. Attach its [end/face/hole] to the [location] "
        "of [piece] so that it [points/extends] [direction].\" Use counting: \"the third hole from the "
        "left.\" Name pieces once and reuse the name (\"call this piece A\"). Avoid vague words like "
        "\"near,\" \"put,\" or \"the other one.\" Scoring: each piece scores for correct size, color, "
        "location, orientation, and connection; correct connections past a wrong one still count.",
        "Improve: \"Put the stick near the block.\" (Example: \"Insert one end of the 10 cm red stick "
        "into the center hole on the top face of the blue cube, so the stick points straight up.\")",
    ),
    lesson(
        "Writer Drills",
        "Practicing descriptions on simple models.",
        "WRITER -- describes the object in 25 minutes. MODEL -- the object to copy.",
        "Start small: write instructions for a 3-5 piece model and have someone build it. See where "
        "the build went wrong and fix your wording.",
        "Order instructions logically: describe the overall shape first (\"the object is an L shape "
        "about 20 cm long\"), then build from a base piece outward. Number steps. Describe each piece "
        "fully the first time. Check each step: could it be read two ways? The writer has 25 minutes "
        "(no advantage to finishing early) and can't touch the object unless allowed.",
        "Why describe the overall shape first? (It gives the builder a mental picture to check each "
        "step against.)",
    ),
    lesson(
        "Builder Drills",
        "Practicing building exactly from written instructions.",
        "BUILDER -- builds from the instructions in 20 minutes. LITERAL READING -- doing exactly what's "
        "written.",
        "The builder's job is to follow instructions literally and carefully, not to guess what looks "
        "right.",
        "Read the overview and all steps once before starting. Lay out and sort the pieces. Follow "
        "each step exactly; if unclear, choose the most literal reading and move on. Check orientation "
        "with the agreed directions. Build time breaks ties, so be efficient but accurate. Unused "
        "parts aren't penalized, so don't force pieces in.",
        "An instruction is ambiguous. What should the builder do? (Choose the most literal "
        "interpretation using the agreed conventions, then continue.)",
    ),
    lesson(
        "Role Swap Practice",
        "Practicing both roles to understand each other.",
        "ROLE SWAP -- switching writer and builder roles in practice.",
        "When you've been the builder, you write better instructions -- you know what's confusing.",
        "Practice both ways with the same partner. After each round, compare the build to the object "
        "and talk through every mistake: was it the writing or the reading? Build a shared list of "
        "phrases that work. Decide who is stronger in each role for the tournament. Teams are exactly "
        "2.",
        "What's the main benefit of switching roles in practice? (Each partner learns what makes "
        "instructions clear or confusing from the other side.)",
    ),
    lesson(
        "Time Management",
        "Using the writer's 25 and builder's 20 minutes well.",
        "TIME BUDGET -- planned time per step. PRIORITIZING -- doing high-value parts first.",
        "Run out of time and the rest of the object scores nothing. Plan your minutes.",
        "Writer: about 2-3 minutes studying the object and planning; most of the time writing "
        "piece-by-piece; the last few minutes re-reading for ambiguity. Describe every piece at least "
        "briefly before adding detail -- a rough description of all pieces beats perfect detail on "
        "half. Builder: skim first, then build steadily; don't spend too long on one unclear step. "
        "Practice with a timer.",
        "With 5 minutes left and 4 pieces undescribed, what should the writer do? (Give a brief "
        "description of each remaining piece first, then add details.)",
    ),
    lesson(
        "Avoiding Vague Adjectives",
        "Replacing vague descriptions with measurable ones.",
        "VAGUE -- open to interpretation (\"big,\" \"small,\" \"near,\" \"long\"). PRECISE -- "
        "measurable or comparative (\"the longer of the two,\" \"5 cm\").",
        "\"The big ball\" means nothing if you don't know what the builder has. Use measurements and "
        "comparisons.",
        "Instead of \"big,\" say \"the 4 cm ball\" or \"the largest of the three balls.\" Instead of "
        "\"near,\" say \"touching\" or \"1 cm away.\" Instead of \"a little tilted,\" say \"tilted about 30 "
        "degrees.\" Count holes, segments, or studs (LEGO). Name colors precisely, but don't rely on "
        "color alone when shades differ.",
        "Rewrite \"Put the long straw a bit to the left.\" (Example: \"Place the 15 cm straw 2 cm to "
        "the left of the cup, parallel to the front edge.\")",
    ),
    lesson(
        "Finding Missing Details",
        "Catching what your instructions leave out.",
        "MISSING DETAIL -- information the builder needs but wasn't given (orientation, which end, "
        "which face).",
        "Most errors come from details the writer saw but forgot to write: which end, which side up, "
        "which hole.",
        "For every piece, check: size, color, type, location, orientation (which way it points or "
        "faces), and connection (which part touches which). Re-read as if you're the builder seeing "
        "only the words. Common misses: which side of a piece faces up, whether a stick goes all the "
        "way through, the angle between parts.",
        "A step says \"attach the rod to the cube.\" What details are missing? (Which face of the "
        "cube, which end of the rod, and which direction the rod points.)",
    ),
    lesson(
        "Review & Refine",
        "Polishing instructions before time runs out.",
        "REVISION -- improving clarity. AMBIGUITY -- more than one possible meaning.",
        "In the last minutes, read your instructions as the builder will. Fix anything that could be "
        "read two ways.",
        "Check numbering and that piece names are consistent. Cross out and clarify unclear phrases "
        "(editing marks are allowed). Make sure every piece of the object is mentioned. Add a final "
        "summary check (\"when finished, the object should be about 25 cm tall and look like a T\"). "
        "Remember: drawing a subsection = Tier 2; drawing the whole model = disqualification.",
        "Why add a final description of the finished object? (It lets the builder check the overall "
        "shape and catch mistakes.)",
    ),
]
