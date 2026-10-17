"""Learning paths: Technology & Engineering events."""

from app.content.learning_paths._base import lesson

BOOMILEVER = [
    lesson(
        "The Moment Arm in Cantilevers",
        "Why a load far from the wall is so hard to hold.",
        "CANTILEVER -- a structure fixed at one end and free at the other. MOMENT (TORQUE) -- force x "
        "perpendicular distance (N-m). MOMENT ARM -- the distance from the pivot to the line of the "
        "force.",
        "A boomilever sticks out from a wall and holds a load at its tip. The farther out the load, "
        "the bigger the turning effect the wall mount has to resist -- like holding a heavy bag at "
        "arm's length.",
        "Moment M = F x d. A 15 kg sand load weighs about 147 N; at 0.4 m from the wall that's about "
        "59 N-m. Doubling the distance doubles the moment. The structure resists that moment with a "
        "pair of forces: one member pulling at the top (tension) and one pushing at the bottom "
        "(compression). The deeper (taller) the structure at the wall, the smaller those forces: "
        "force is about M / depth. The 2027 contact-depth lines (20 cm base, 15 cm for the bonus) "
        "limit how deep your wall contact can be.",
        "Moment 60 N-m and a 0.15 m vertical gap between the top and bottom members at the wall. "
        "Approximate force in each? (60 / 0.15 = 400 N.)",
    ),
    lesson(
        "Tension & Compression Members",
        "Identifying which parts pull and which parts push.",
        "TENSION -- a pulling force that stretches a member. COMPRESSION -- a pushing force that "
        "squeezes it. TRUSS -- triangles of members joined at their ends.",
        "In a typical boomilever, the top member is in tension (it's pulled away from the wall) and "
        "the bottom member is in compression (it's pushed into the wall). Triangles keep the shape "
        "rigid.",
        "Tension members can be thin -- wood is strong in tension along the grain, so the limit is "
        "usually the joints. Compression members must be thicker or braced because they buckle. "
        "Diagonals in a truss carry shear, alternating between tension and compression. Quick test: "
        "imagine cutting a member -- if the two ends would spring apart, it was in tension; if they'd "
        "push into each other, compression. Optimized designs put mass into compression members and "
        "keep tension members light.",
        "In a boomilever with a horizontal top member attached high on the wall and a sloped bottom "
        "member meeting it at the load, which is in tension? (The top member.)",
    ),
    lesson(
        "Bending Moment at the Wall",
        "Calculating the moment and member forces where the structure attaches.",
        "BENDING MOMENT -- the internal moment at a cross-section. REACTION FORCES -- forces the wall "
        "puts back on the structure. EQUILIBRIUM -- net force and net moment are zero.",
        "Everything the load does has to be balanced at the wall. Use simple equilibrium to find the "
        "forces in the top and bottom members.",
        "Take moments about the bottom attachment point: tension T x depth h = load W x horizontal "
        "distance L, so T = W L / h. The bottom member's compression has a horizontal part equal to "
        "T and a vertical part that holds up W. Its total force is sqrt(T^2 + W^2). Example: W = "
        "147 N, L = 0.40 m, h = 0.15 m -> T = 392 N; compression about sqrt(392^2 + 147^2) = about "
        "419 N. Increasing depth h lowers both forces but adds mass -- the classic trade-off.",
        "If you double the depth h, what happens to the tension force? (It halves.)",
    ),
    lesson(
        "Common Joint Failures",
        "Why wood structures fail at their connections.",
        "GLUE JOINT -- an adhesive bond between members. SHEAR FAILURE -- layers sliding apart. "
        "GUSSET -- a small plate that reinforces a joint. END GRAIN -- the cut end of wood fibers "
        "(bonds poorly).",
        "Many boomilevers don't break in the middle of a stick -- they break where sticks are glued "
        "together. Strong joints matter as much as strong members.",
        "Failures: glue line shearing, wood tearing out at the glue line, end-grain butt joints "
        "pulling apart, and joints rotating. Fixes: more glue area (overlap or lap joints), gussets "
        "(wood only -- no tape), notched or sleeved joints, and thin glue lines that fully cure. "
        "Cyanoacrylate (CA) cures fast but is brittle; wood glue is tougher but slower. 2027 rules: "
        "wood bonded with adhesive only; you may laminate wood yourself but no plywood or commercial "
        "laminates; no painting, coating, or soaking wood in glue; no adhesive tape.",
        "Why are end-grain butt joints weak? (End grain soaks up glue and gives little bonding "
        "surface, so the joint pulls apart easily.)",
    ),
    lesson(
        "Buckling & Elongation",
        "How compression members buckle and tension members stretch.",
        "BUCKLING -- a compression member bowing sideways and collapsing. SLENDERNESS -- length relative "
        "to thickness. EULER BUCKLING -- critical load is proportional to E I / L^2. ELONGATION -- a "
        "tension member stretching.",
        "A long, skinny stick under compression snaps sideways long before the wood itself is "
        "crushed. Shorten it or brace it, and it can hold far more.",
        "Euler: P_critical = pi^2 E I / (K L)^2 -- halving the unbraced length quadruples the "
        "buckling load. I (moment of inertia) grows with the cube of thickness in the bending "
        "direction, so a deeper cross-section helps a lot. Bracing at midpoints shortens the "
        "effective length. Box or I-shaped laminated members are stiff for their mass. Tension "
        "members fail by stretching and then breaking, often at a flaw or knot; choose straight-"
        "grained wood. Wood density varies a lot -- weigh and sort your stock.",
        "A compression member buckles at 200 N. If you brace it at its midpoint, roughly what load? "
        "(About 800 N -- half the length gives 4 times the buckling load.)",
    ),
    lesson(
        "How Efficiency Is Scored",
        "The scoring formula and what it rewards.",
        "LOAD SUPPORTED -- the sand mass held (max 15,000 g). LOAD SCORED -- load supported plus a "
        "5,000 g bonus if earned. STRUCTURE MASS -- weighed to 0.01 g. SCORE -- Load Scored / Structure "
        "Mass.",
        "Score is a ratio, so a light structure that holds the full load beats a heavy one that holds "
        "the same load.",
        "Example: a 15.00 g structure holding 15,000 g scores 1,000; with the bonus (only touching "
        "above the 15 cm line and holding the full 15 kg), Load Scored = 20,000 g -> 1,333. A 10 g "
        "structure that fails at 9,000 g scores 900 -- lower. Tier 1 meets every rule; Tier 2 breaks "
        "one or more (and ranks below all Tier 1). Structures that can't hold the empty loading "
        "assembly (~1.5 kg) get participation points only. The Estimated Load you submit at check-in "
        "is a tiebreaker.",
        "A 12.50 g boomilever holds the full 15,000 g but doesn't earn the bonus. Score? (15,000 / "
        "12.5 = 1,200.)",
    ),
    lesson(
        "Mass Cuts & Efficiency",
        "Deciding where to remove mass without losing strength.",
        "SAFETY FACTOR -- strength divided by expected load. MASS BUDGET -- target mass for each part. "
        "OVERBUILT -- stronger than needed.",
        "If your design always holds 15 kg with room to spare, it's carrying extra mass. Trimming "
        "where you have the most margin raises your score.",
        "Test to failure and look at where it broke: the failure point is the weakest part; every "
        "other part is overbuilt. Lighten tension members and diagonals first (sand, choose lighter "
        "wood, thinner cross-sections), then fine-tune compression members. Don't cut the joints too "
        "much. Change one thing at a time and keep a log of masses and loads. Remember: since 15 kg "
        "is the cap, once you reliably hold it, every gram you remove raises the score directly.",
        "Your structure holds 15 kg every time and weighs 14 g. If you trim 2 g and it still holds, "
        "how does the score change? (From about 1,071 to 1,250.)",
    ),
    lesson(
        "Inspection Checklist",
        "Getting through check-in without violations.",
        "TIER 1 -- meets all rules. TIER 2 -- one or more violations. CONTACT DEPTH LINE -- the "
        "horizontal line on the wall your structure may only touch above (20 cm base, 15 cm bonus).",
        "A great structure that breaks a rule drops below every legal structure. Check the rules "
        "before you leave home.",
        "Check: wall contact only above the chosen contact-depth line; the loading block's bottom "
        "above the bolt centerline before sand goes in; materials are wood and adhesive only (no "
        "plywood, commercial laminates, paint, coatings, glue-soaked wood, or tape); dimensions and "
        "attachment features match the current rules diagram; the structure is labeled as required. "
        "Bring the rules and a ruler. Practice mounting and loading within the 6 minutes. Wear Z87+ "
        "eye protection (Eye Protection B).",
        "Your structure touches the wall below the 15 cm line but above the 20 cm line, and holds "
        "15 kg. Tier and bonus? (Tier 1, but no bonus -- the bonus requires touching only above the "
        "15 cm line.)",
    ),
    lesson(
        "Analyzing Test Logs",
        "Using test data to improve the design.",
        "TEST LOG -- a record of each build and test. FAILURE MODE -- how and where a structure broke. "
        "VARIABLE -- the one design change being tested.",
        "Your log turns testing into improvement. Without it, you'll repeat the same mistakes.",
        "Record for each build: date, design version, total mass and part masses, wood type and "
        "density, glue, load at failure, failure location and mode (buckled, joint sheared, member "
        "snapped), and photos. Look for patterns: if every failure is the same joint, fix that joint; "
        "if failure loads are inconsistent, check wood density and glue curing. Compute efficiency "
        "for every test, including partial loads. Graph mass vs load to find the sweet spot.",
        "Three builds all failed at the bottom compression member's midpoint. What's the next change? "
        "(Brace that member at midspan or deepen its cross-section.)",
    ),
    lesson(
        "Finding Failure Points",
        "Predicting and checking where a design will fail.",
        "STRESS CONCENTRATION -- a spot where stress builds up (notches, holes, sharp corners). WEAK "
        "LINK -- the first part to fail. PROOF LOAD -- a test load below failure.",
        "Every structure has a weakest link. Find it on purpose in testing, not by surprise at the "
        "tournament.",
        "Likely failure points: the compression member near the wall (highest compression, longest "
        "unbraced length), the tension member's attachment hardware, glue joints at the load end, "
        "and anywhere wood is notched. Load slowly and watch: bowing signals buckling; creaking at a "
        "joint signals shear. Use a slow-motion video to see the first part to fail. After a design "
        "change, the weak link moves -- test again. Aim for a design whose parts fail at about the "
        "same load.",
        "A member bows visibly sideways before the structure collapses. What failure mode? "
        "(Buckling in compression.)",
    ),
]

ELASTIC_LAUNCHED_GLIDER = [
    lesson(
        "Hand-Glide Trim",
        "Getting a smooth, straight glide before launching with the elastic.",
        "TRIM -- small adjustments that set how the glider flies. STALL -- the nose rises, speed drops, "
        "and it falls. DIVE -- nose too low, flies fast into the floor.",
        "Before using the launcher, toss the glider gently by hand. A well-trimmed glider flies in a "
        "long, flat, smooth line.",
        "If it stalls (climbs, slows, drops), add a little nose weight or reduce elevator up-angle. "
        "If it dives, remove nose weight or add a touch of up-elevator. Turns are set with the rudder "
        "or by slightly tilting the stabilizer. Make tiny changes -- one at a time. Check the wings "
        "aren't warped (a twist causes rolling). Remember the mass rules: more than 3.5 g and less "
        "than 10.0 g throughout the flight.",
        "Your glider climbs, slows, and drops in a hand toss. First fix? (Add a little nose weight or "
        "reduce up-elevator.)",
    ),
    lesson(
        "Launch Angle Tests",
        "Finding the launch angle that gives the best height and glide.",
        "LAUNCH ANGLE -- the angle above horizontal at launch. APEX -- the highest point. TRANSITION -- "
        "switching from climb to glide.",
        "Launch too flat and you don't gain height. Launch too steep and the glider may loop or stall. "
        "There's a best angle for your glider and elastic.",
        "Test angles (for example 60, 70, 80, 85 degrees) with the same elastic stretch. Record peak "
        "height, transition quality, and flight time. Many designs launch nearly vertical with a "
        "slight bank so the glider rolls into its glide circle. Wind-free indoor conditions differ "
        "from outdoors. Keep stretch consistent (mark the launcher) so you're only testing angle.",
        "Why keep the elastic stretch the same while testing angle? (So that angle is the only "
        "variable changed.)",
    ),
    lesson(
        "Avoiding Over-Power",
        "Why too much launch energy can lower your flight time.",
        "OVER-POWER -- more launch energy than the glider can handle. FLUTTER -- rapid wing vibration "
        "at high speed. CEILING STRIKE -- hitting the ceiling.",
        "More stretch gives more height -- up to a point. Too much speed can twist the wings, make "
        "the glider loop, or crash it into the ceiling.",
        "Signs of over-power: looping at the top, wing flutter or warping, erratic transitions, and "
        "ceiling hits (which waste the flight). Fixes: less stretch, stiffer wings (spars, thicker "
        "leading edges), a more vertical launch to bleed speed upward. Find the stretch that gives "
        "the best height without problems, given the ceiling height of the venue. Launch handle rules: "
        "under 1 m long, with non-metallic elastic that stays attached to the handle.",
        "Your glider loops at the top of each strong launch. What change? (Reduce the stretch, or "
        "stiffen the wings.)",
    ),
    lesson(
        "Circular Flight Path in the Gym",
        "Why indoor gliders fly in circles and how to set the turn.",
        "GLIDE CIRCLE -- the glider's turning path. TURN RADIUS -- the circle's size. BANK -- the "
        "wing's tilt in a turn.",
        "Indoors, a glider flying straight would hit a wall. So it's trimmed to circle -- a gentle, "
        "wide circle wastes the least energy.",
        "Too-tight circles lose height quickly (steep bank); too-wide circles drift into walls. Set "
        "the circle with rudder offset or stabilizer tilt, and the launch direction. Launch circle "
        "and glide circle are often in the same direction. Watch for spiral dives (the bank keeps "
        "increasing) -- add a little dihedral or reduce the rudder. Know the venue size; adjust for "
        "smaller gyms.",
        "The glider's circle keeps tightening into a spiral dive. A fix? (Reduce rudder offset or add "
        "dihedral to stabilize the bank.)",
    ),
    lesson(
        "Elastic to Kinetic to Potential Energy",
        "The energy story of a launch.",
        "ELASTIC POTENTIAL ENERGY -- stored in stretched elastic. KINETIC ENERGY -- 1/2 m v^2. "
        "GRAVITATIONAL POTENTIAL ENERGY -- m g h.",
        "Stretched elastic stores energy, the launch converts it to speed, and the climb converts that "
        "speed to height. Then the glide spends the height slowly.",
        "Ideal: elastic PE -> KE -> m g h. Example: 0.5 J of elastic energy reaching a 7 g (0.007 kg) "
        "glider -> max h = 0.5 / (0.007 x 9.8) = about 7.3 m (less in reality, due to drag and "
        "losses). Lighter gliders climb higher for the same energy but are more fragile. A glider's "
        "time aloft = height / sink rate, so either climb higher or sink slower (good glide). Not all "
        "the elastic's energy goes to the glider (some stays in the band and handle).",
        "Two gliders get the same launch energy; one is 5 g and one is 8 g. Which can climb higher "
        "(ignoring drag)? (The 5 g glider.)",
    ),
    lesson(
        "Center of Gravity & Tail Volume",
        "Balancing the glider for stable flight.",
        "CENTER OF GRAVITY (CG) -- the balance point. TAIL VOLUME -- tail area x tail moment arm / "
        "(wing area x wing chord), a measure of how strong the tail's stabilizing effect is. STATIC "
        "STABILITY -- returning to level after a disturbance.",
        "A glider must balance at the right spot -- usually about a quarter to a half of the way back "
        "on the wing. Too far forward: it dives. Too far back: it's unstable and stalls.",
        "Find CG by balancing the glider on your fingertips. Typical CG for gliders: around 40-60% of "
        "the wing chord with a lifting tail, or forward of that with a non-lifting tail. A bigger "
        "tail or longer tail boom (more tail volume) adds stability and allows a farther-back CG. "
        "Adjust with clay on the nose. Re-trim after any repair. The blunt-nose rule applies to the "
        "nose (it must not touch the end of a lip-balm cap pushed onto it).",
        "Moving the CG backward makes a glider more or less stable? (Less stable.)",
    ),
    lesson(
        "Launch-to-Glide Transition",
        "The moment at the top that makes or breaks a flight.",
        "TRANSITION -- the change from fast climb to slow glide. APEX -- the top of the climb. ROLL-OUT "
        "-- the glider rolling from vertical into its glide circle.",
        "A good transition is smooth: the glider slows at the top, rolls over, and settles into a gentle "
        "glide with little height lost.",
        "Bad transitions: whip stall (stalls and drops), loops (too much speed or up-elevator), "
        "diving out (nose falls). Fixes: adjust the launch bank so the glider rolls out the right way; "
        "tweak elevator and rudder; use a wing tip tilt that helps the roll. Film flights in slow "
        "motion to see what happens at the apex. A small height loss at transition can cost many "
        "seconds of glide.",
        "The glider stalls hard right at the apex. Likely causes? (Too much up-elevator, CG too far "
        "back, or too steep/slow at apex.)",
    ),
    lesson(
        "Scoring & Flight Log Analysis",
        "How flights are scored and how the log bonus works.",
        "OFFICIAL FLIGHT -- one that counts (up to 5). TRIM FLIGHT -- practice. TIME ALOFT -- median of "
        "3 timers. FLIGHT LOG BONUS -- x1.2 complete, x1.1 partial, x1.0 none.",
        "Your score is the sum of your three longest official flights, multiplied by the log bonus.",
        "Within a 6-minute flight period you may make trim flights and up to 5 official flights, and "
        "must announce which before each launch. Score = (sum of top 3) x log multiplier. A complete "
        "log needs 10+ test flights recording peak height, relaxed elastic length, flight time, and "
        "at least one more parameter of your choice, all with units. Use your log to pick the best "
        "settings for the venue and predict flight times. Violations rank a team below all teams "
        "without them.",
        "Your top three flights are 40, 38, and 37 s, with a complete log. Score? ((115) x 1.2 = "
        "138.)",
    ),
    lesson(
        "Current-Year Launcher & Glider Rules",
        "The 2027 rules for the glider, measurement box, and launcher.",
        "MEASUREMENT BOX -- a team-provided lidless box the glider must fit inside. BLUNT NOSE -- a "
        "nose that won't reach the end of a lip-balm cap. LAUNCH HANDLE -- the stick holding the "
        "elastic.",
        "Small rule details decide whether a flight counts. Build the box and test the nose before "
        "the tournament.",
        "2027: glider mass more than 3.5 g and less than 10.0 g throughout flight; in flight "
        "configuration it must fit inside your lidless Measurement Box (outside dimensions within "
        "32.0 x 24.0 x 47.0 cm); the nose pushed into a lip-balm cap (about 1.57 cm deep x 1.37 cm "
        "wide) must not touch the end; any material except boron filament; kits can't have pre-glued "
        "joints or pre-covered surfaces; launch handle under 1 m with non-metallic elastic that stays "
        "on the handle. Bring up to 2 gliders.",
        "Your glider weighs 3.4 g. Is it legal? (No -- it must be more than 3.5 g.)",
    ),
    lesson(
        "Flight Path Sketch Interpretation",
        "Reading sketches of flight paths to diagnose problems.",
        "FLIGHT PATH -- the shape the glider traces in the air. SIDE VIEW / TOP VIEW -- sketches showing "
        "climb and circle shapes.",
        "A sketch of the flight path tells you what to fix: the shape of the climb, the transition, and "
        "the glide circle.",
        "Side view: a steep straight climb then a smooth flattening = good; a loop at the top = "
        "over-power or too much up-elevator; a dip after the apex = poor transition; a steady steep "
        "descent = poor glide (CG forward or too much drag). Top view: a tightening spiral = spiral "
        "instability; a wide drifting circle = too little turn. Practice sketching your own flights "
        "and noting the fix. Logs that include sketches make trimming faster.",
        "A side-view sketch shows the glider climbing then looping over the top. What does this "
        "suggest? (Too much launch speed or up-elevator.)",
    ),
]

ROLLER_COASTER = [
    lesson(
        "Energy Concepts in Roller Coasters",
        "Why coasters run on potential and kinetic energy.",
        "POTENTIAL ENERGY (PE) -- energy of height, m g h. KINETIC ENERGY (KE) -- energy of motion, "
        "1/2 m v^2. CONSERVATION OF ENERGY -- total energy stays constant (some becomes heat).",
        "A coaster ball starts high with stored energy. As it rolls down, PE turns into KE; as it "
        "climbs, KE turns back into PE. Friction slowly drains the total.",
        "The ball can never climb higher than its starting point (it's losing energy to friction). "
        "Speed at the bottom of a drop of height h (ideal) = sqrt(2 g h). Rolling balls also store "
        "rotational energy (for a solid ball, KE_total = 7/10 m v^2), so they move slower than a "
        "sliding block would. The first drop sets the energy budget for the whole track.",
        "A ball starts 50 cm high. Can it make it over a 55 cm hill? (No -- it can't gain energy.)",
    ),
    lesson(
        "Potential & Kinetic Energy Calculations",
        "Solving PE and KE problems for coaster design.",
        "PE = m g h. KE = 1/2 m v^2 (translational). g = 9.8 m/s^2.",
        "Most coaster questions are energy conversions: a height becomes a speed, or a speed becomes a "
        "height.",
        "Example: a 20 g (0.020 kg) ball at 0.5 m has PE = 0.020 x 9.8 x 0.5 = 0.098 J. Ignoring "
        "friction and rotation, speed at the bottom = sqrt(2 x 9.8 x 0.5) = 3.1 m/s. For a rolling "
        "solid sphere: v = sqrt(10 g h / 7) = 2.6 m/s. Energy lost between two points = PE difference "
        "- KE change. Percent efficiency = useful energy out / energy in x 100%. Mass cancels in speed "
        "calculations, so heavier balls don't go faster in theory -- but they're less affected by air "
        "drag.",
        "A ball drops 0.2 m. Ideal sliding speed at the bottom? (sqrt(2 x 9.8 x 0.2) = about "
        "2.0 m/s.)",
    ),
    lesson(
        "Energy Losses: Rolling Resistance & Flex",
        "Where energy goes and how to control it.",
        "ROLLING RESISTANCE -- energy lost as the ball and track deform. FLEX -- the track bending "
        "under the ball. AIR DRAG -- friction with the air.",
        "Real coasters lose energy everywhere: bumpy joints, soft track, sharp turns. Fewer losses "
        "mean a more predictable run.",
        "Sources: rolling resistance, sliding friction on curves, track flex and vibration (energy "
        "into the track), joint bumps (sudden impacts), air drag. Stiff, smooth track and smooth "
        "joints cut losses. On the other hand, for a long Target Time you may WANT controlled losses "
        "(gentle slopes, switchbacks, a brake region) to slow the ball. The goal is repeatable losses, "
        "not necessarily zero losses.",
        "A ball slows noticeably every time it crosses one joint. What's happening? (The joint bump "
        "converts kinetic energy to sound and heat -- smooth it.)",
    ),
    lesson(
        "Designing for the Target Time",
        "Building in adjustable delays to hit 30-60 s.",
        "TARGET TIME (TT) -- 30-60 s, revealed just before set-up. TIME SCORE -- 5 points per full "
        "second up to TT, minus 5 per second past it. ADJUSTABLE SECTION -- a part you can change to "
        "tune time.",
        "With TT up to 60 s, your ball needs a long path or slow sections. You also need a quick way to "
        "add or remove time on the day.",
        "Time Score = 5 points per full second up to the Target Time, minus 5 per full second past it "
        "(up to 2 x TT); a ball that doesn't finish scores 0 for time. So arriving slightly early is "
        "safer than late. Slow sections: gentle zigzag ramps, switchbacks, a long shallow spiral, a "
        "funnel. Adjustable features: a removable switchback, a gate that routes the ball through an "
        "extra section, an adjustable slope. Calibrate: time each configuration and keep a chart of "
        "settings vs time. Rules require a mechanism that safely stops the ball after the finish.",
        "TT = 45 s. Your run takes 43.6 s. Time score? (43 full seconds x 5 = 215 points.)",
    ),
    lesson(
        "Transport-Proof Joints & Stability",
        "Building track that survives travel and set-up.",
        "JOINT -- where track sections connect. ALIGNMENT -- sections lining up smoothly. RIGIDITY -- "
        "resistance to bending or twisting.",
        "A coaster that works perfectly at home can fail at the tournament if a joint shifts in the "
        "car. Design for travel.",
        "Use keyed or pinned joints that only fit one way; glue joints that never need to come apart; "
        "build a sturdy frame that resists twisting; pack it in a padded box. Make removable parts "
        "easy to reseat (alignment marks, dowels). Re-test after a car ride. The Start and Finish "
        "lines must be fixed after impound, and the device must stay within 30.0 cm wide x 80.0 cm "
        "long x 60.0 cm high (excluding the ball).",
        "What's a good way to make a removable section reattach in exactly the same place? (Use "
        "alignment pins or keyed joints and alignment marks.)",
    ),
    lesson(
        "Meeting Time & Size Targets",
        "Balancing time, size, elevator, and loop points.",
        "SIZE SCORE -- (60 - height) + (30 - width) + (80 - length) in cm. ELEVATOR SCORE -- 50 points "
        "per working elevator type. LOOP SCORE -- 3 points per cm of loop height.",
        "Every part of the score pulls in a different direction: smaller is better for Size, but a long "
        "time and a tall loop need space. Decide where your points come from.",
        "Final Score = the better run's Size + Time + Elevator + Loop scores. Example: a 50 x 25 x 70 cm "
        "device earns (60-50) + (30-25) + (80-70) = 25 size points. Time at TT = 45 s is up to 225 "
        "points -- usually the biggest part. Two working elevator types = 100 points. A 15 cm loop = "
        "45 points. So time and elevators dominate; don't sacrifice reliability for a few size points.",
        "Size 55 x 28 x 75 cm. Size score? ((60-55) + (30-28) + (80-75) = 12.)",
    ),
    lesson(
        "Repeatability After Transport",
        "Getting the same time run after run.",
        "REPEATABILITY -- getting the same result on repeated trials. STANDARD DEVIATION -- spread of "
        "run times. LEVELING -- making the base flat.",
        "A run time that varies by 3 seconds can cost 15 points. Find and remove the sources of "
        "variation.",
        "Sources of variation: uneven tables (bring shims and a level), loose joints, a ball that "
        "isn't round or is dirty, inconsistent release (the rules use a supervisor-provided #2 pencil "
        "to release the ball), dust, and humidity on wooden track. Do 10 runs at a setting and look "
        "at the spread. You get 8 minutes with unlimited practice runs before up to 2 scored runs -- "
        "use practice runs to check the time and adjust.",
        "Run times at one setting: 44.1, 44.3, 46.8, 44.2 s. What does the 46.8 suggest? (A random "
        "disturbance -- a sticking spot or a bump -- worth investigating.)",
    ),
    lesson(
        "This Year's Required Features",
        "The 2027 rules for the ball, elevators, loop, and track.",
        "TYPE 1 ELEVATOR -- first-class lever + wheel and axle. TYPE 2 ELEVATOR -- second-class lever + "
        "pulley. IMA -- ideal mechanical advantage (must be under 1). LOOP -- an open concave track "
        "that crosses itself.",
        "Elevators and the loop are big point earners, but each has exact rules.",
        "2027: ball at least 1 cm in diameter, always visible, released by pulling a supervisor-"
        "provided #2 pencil; no magnets, electronics, springs, or rubber bands. Up to 2 elevator "
        "types (Type 1: first-class lever + wheel and axle; Type 2: second-class lever + pulley), "
        "each with IMA under 1 and lifting the ball at least 10 cm. One optional loop: an open (not "
        "fully enclosed) concave track that self-intersects; the ball must stay on the track and be "
        "unsupported from below at the top. Exactly one labeled Start Line and Finish Line, fixed "
        "after impound; a safe stopping mechanism.",
        "Why does the elevator's IMA have to be under 1? (The rules require it -- it means the input "
        "moves less distance than the ball is lifted, i.e. the mechanism trades force for distance.)",
    ),
    lesson(
        "Energy Accounting & Thermodynamics",
        "Tracking where the ball's energy goes from start to finish.",
        "ENERGY ACCOUNTING -- listing every energy input and output. DISSIPATION -- energy turning into "
        "heat and sound. WORK BY ELEVATOR -- energy an elevator adds to lift the ball.",
        "Start with the ball's PE at the start line. Add the energy elevators give it. Subtract every "
        "loss. What's left is its KE at the finish.",
        "Total energy input = m g h_start + work done by elevators (m g h_lift each). Losses become "
        "thermal energy (the track and ball warm very slightly) and sound. The second law says these "
        "losses can't be fully recovered. Energy-based questions might ask for the energy lost "
        "between two points (PE lost - KE gained) or the minimum height needed to clear a loop "
        "(ideally h >= 2.7 R for a rolling ball, more in practice).",
        "A 0.02 kg ball loses 0.3 m of height and gains 0.03 J of KE. Energy lost to friction? "
        "(0.02 x 9.8 x 0.3 = 0.059 J of PE lost - 0.03 J = about 0.029 J.)",
    ),
    lesson(
        "Troubleshooting Common Problems",
        "Fixing the problems that show up most often.",
        "JAM -- the ball gets stuck. DERAILMENT -- the ball leaves the track. STALL -- the ball stops "
        "on a slope.",
        "Most problems come from too little energy at a point, too much speed on a curve, or a bad "
        "joint. Diagnose one section at a time.",
        "Ball stops on a flat section -> add slope or reduce friction. Ball flies off a curve -> bank "
        "the curve, add guard rails, or reduce speed before it. Ball misses the elevator -> adjust "
        "the ramp end and catch. Ball doesn't complete the loop -> start the loop lower than the "
        "drop height allows, smooth the entrance, or raise the drop. Inconsistent times -> check "
        "joints and leveling. Keep a list of problems found at each practice and the fix.",
        "The ball derails on a sharp turn every time. Two fixes? (Bank the turn or add rails; reduce "
        "the ball's speed entering the turn.)",
    ),
]

SCRAMBLER = [
    lesson(
        "Energy of a Falling Mass",
        "How a dropping weight powers the vehicle.",
        "GRAVITATIONAL PE -- m g h. FALLING MASS -- the weight whose drop drives the Scrambler. "
        "TRANSMISSION -- the string, pulleys, and axle that turn the drop into wheel motion.",
        "The Scrambler stores energy by lifting a mass. When released, the mass falls, pulling a string "
        "that spins the axle and drives the vehicle forward.",
        "Energy available = m g h (e.g. a 1 kg mass falling 0.8 m = 7.8 J). That energy becomes the "
        "vehicle's KE plus losses. The string wraps around the axle: distance traveled per drop "
        "depends on the drop length and the ratio of wheel radius to axle radius. Rules: the whole "
        "Scrambler (with egg, falling mass, and floor cushion) fits a 100.0 x 50.0 cm base x 100.0 cm "
        "high box, and the falling mass may never touch the floor.",
        "A 0.5 kg mass falls 0.9 m. Energy available? (0.5 x 9.8 x 0.9 = about 4.4 J.)",
    ),
    lesson(
        "Energy Bar Graphs",
        "Showing energy changes visually.",
        "ENERGY BAR GRAPH (LOL diagram) -- bars for each energy type at two moments. THERMAL ENERGY -- "
        "energy lost to friction.",
        "Bar graphs show where energy is at the start and the end of a run. The total height must "
        "match if no energy enters or leaves the system.",
        "At release: all PE in the falling mass. Mid-run: some PE converted to the vehicle's KE, some "
        "to thermal energy. At the stop: KE back to zero; all the energy is thermal (in the brakes, "
        "bearings, floor contact) plus the mass's remaining PE. The bars help explain why a heavier "
        "falling mass gives a faster run, and why braking must absorb the KE.",
        "After the Scrambler stops, where has the falling mass's lost PE gone? (Mostly to thermal "
        "energy -- friction in the brakes, bearings, and wheels.)",
    ),
    lesson(
        "Calibration Charts",
        "Building a chart to hit any Target Distance.",
        "TARGET DISTANCE -- 7.00-10.00 m, announced after impound. CALIBRATION CHART -- a table or "
        "graph of setting vs distance. STOPPING MECHANISM -- the automatic brake.",
        "You won't know the target distance until the event. A calibration chart tells you which "
        "brake setting gives each distance.",
        "Common brake: a wing nut on a threaded axle that travels toward a stop as the wheels turn -- "
        "the number of axle turns sets the distance. Run the vehicle at several settings across "
        "7-10 m and record distances (several runs each). Graph and draw a best-fit line. At the "
        "event, read the setting for the announced distance. Calibrate on the floor type you expect. "
        "Target steps: 0.25 m at Regionals, 0.10 m State, 0.01 m Nationals.",
        "At 30 turns the vehicle travels 7.5 m; at 40 turns, 10.0 m. Setting for 8.5 m? (34 turns, "
        "assuming a straight-line relationship.)",
    ),
    lesson(
        "Energy Losses in String, Axle & Floor",
        "Where Scrambler energy goes and how to control it.",
        "BEARING FRICTION -- friction where the axle turns. ROLLING RESISTANCE -- energy lost at the "
        "wheels. STRING SLIP -- string sliding on the axle instead of turning it.",
        "Every bit of friction costs speed. More importantly for score, inconsistent friction makes "
        "distances unpredictable.",
        "Reduce axle friction with smooth bearings (ball bearings or polished bushings), straight "
        "axles, and wheels aligned with the axle. Lightweight wheels with a hard tread roll better. "
        "Keep the string from rubbing on the frame. Floor type changes rolling resistance and "
        "traction. Run time adds to the score (lower is better), so a faster vehicle helps -- but "
        "accuracy (2 points per cm from the target) matters more.",
        "Your vehicle travels 15 cm farther on smooth tile than on a gym floor at the same setting. "
        "Why? (Lower rolling resistance on the smooth floor.)",
    ),
    lesson(
        "Alignment & Steering",
        "Keeping the vehicle running straight.",
        "ALIGNMENT -- wheels pointing exactly forward. TOE-IN -- front of the wheels angled inward. YAW "
        "-- turning left or right.",
        "Score is the distance from the egg tip to the target POINT, not just along the line. A vehicle "
        "that drifts sideways loses points even at the right distance.",
        "Check that axles are parallel and perpendicular to the frame; wheels shouldn't wobble. Small "
        "differences in wheel diameter cause curving. Add an adjustable steering wheel or axle slot "
        "to correct drift. Use a laser or alignment device to aim at the start (alignment devices are "
        "impounded with the vehicle). Test straightness over the full 10 m and adjust. Toe-in can "
        "improve straight tracking in some designs.",
        "The vehicle consistently curves 20 cm to the right over 9 m. A fix? (Adjust the steering or "
        "axle alignment slightly left, then re-test.)",
    ),
    lesson(
        "Measurement Point & Scoring",
        "How runs are measured and scored.",
        "VEHICLE DISTANCE -- cm from the egg tip to the Target Point. RUN TIME -- seconds. LOW SCORE "
        "WINS. FAILED RUN -- 2,500 distance points.",
        "The egg is the front of the vehicle, and the measurement is from its tip to the target point. "
        "Lower scores are better.",
        "Run Score = 100 + 2.0 x Vehicle Distance (cm) + Run Time (s) + Can Bonus + penalties. Can "
        "Bonus = -0.5 x (110 - Inside Can Distance) for driving between two cans on the Bonus Line. "
        "Penalties: +150 competition violation, +300 construction violation, +50 unmodified kit; a "
        "failed run scores 2,500 distance points; not impounded +5,000. Breaking the egg, touching "
        "the barrier with anything but the egg, or the egg tip passing the barrier's front are "
        "violations. Final = the better of two runs.",
        "Vehicle stops 12 cm from the target point in 4.5 s, no bonus or penalties. Score? (100 + 24 + "
        "4.5 = 128.5.)",
    ),
    lesson(
        "Inspection Practices",
        "Passing impound and inspection.",
        "IMPOUND -- handing in the vehicle before your slot. KIT MODIFICATION FORM -- documents at least "
        "2 functional changes to a kit. EGG MOUNT -- the regulated holder for the egg.",
        "Inspection checks the rules before you run. A violation costs hundreds of points, so check "
        "everything at home.",
        "Check: fits the 100.0 x 50.0 x 100.0 cm box with egg, falling mass, and cushion; falling mass "
        "can't touch the floor; stopping is automatic and inside the vehicle; no electronics, remote "
        "control, or tethers; egg mount -- wooden backstop 5.0 x 5.0 cm, at least 1.1 cm thick (no "
        "balsa), two 1/4\"-3/8\" dowels sticking out 3.0-4.0 cm with their bottoms 5.0-10.0 cm above "
        "the track; the egg is the vehicle's foremost point, taped on by the team; started with an "
        "unsharpened #2 pencil. Kits need at least 2 documented functional modifications. Impound the "
        "vehicle, spare parts, alignment devices, and papers (falling mass detached).",
        "What's the penalty for running an unmodified kit? (+50 points.)",
    ),
    lesson(
        "Floor Type & Calibration",
        "Why the floor changes your chart.",
        "COEFFICIENT OF FRICTION -- how grippy a surface is. SURFACE TYPE -- tile, wood gym, carpet, "
        "concrete.",
        "Your vehicle rolls differently on each floor. A chart made on tile may be off on a gym floor.",
        "If your stopping mechanism counts axle turns, distance per turn depends on wheel slip and "
        "rolling: slipping wheels travel less per turn on slick floors when accelerating hard. "
        "Calibrate on several floors and note the differences, or find out the tournament floor and "
        "practice on a similar surface. Use practice runs or the first run to correct. Clean the "
        "wheels before each run.",
        "Your vehicle goes 8.00 m at home but 7.85 m at the tournament at the same setting. How should "
        "you adjust for run 2? (Add turns to cover the extra 0.15 m, using your chart's distance per "
        "turn.)",
    ),
    lesson(
        "String Slippage",
        "How string slip throws off distance and how to stop it.",
        "SLIPPAGE -- the string sliding instead of gripping the axle. WRAP -- turns of string around "
        "the axle. TAPER -- an axle shape that changes the string's leverage.",
        "If the string slips, the falling mass's motion doesn't fully turn the axle, so the vehicle "
        "travels less (and less predictably).",
        "Fixes: tie the string through a hole in the axle or use a hook; wrap neatly without "
        "overlapping; use a string that doesn't stretch (braided fishing line); add a rubber sleeve "
        "for grip. Overlapping wraps change the effective axle radius and the vehicle's speed. Check "
        "that the string fully releases at the end of the drop so it doesn't drag. Consistent wraps "
        "= consistent runs.",
        "Why can overlapping wraps change your distance? (They increase the effective axle radius "
        "partway through the drop, changing how the energy is delivered.)",
    ),
    lesson(
        "Changing Mass or Drop Height",
        "Predicting how the vehicle changes with more mass or height.",
        "DROP HEIGHT -- the distance the mass falls. MASS RATIO -- the falling mass compared to the "
        "vehicle mass.",
        "More falling mass or a longer drop gives more energy, so the vehicle goes faster -- but it "
        "also needs to brake harder and may be less stable.",
        "Energy scales with m x h: doubling either doubles the energy. Faster runs lower run time "
        "points, but sudden starts can spin wheels or jolt the egg. A brake that counts axle turns "
        "sets distance mostly independently of speed, but too much speed causes skidding past the "
        "stop point. Balance: enough energy for a quick run, smooth acceleration, reliable stopping. "
        "Test each change against your calibration chart.",
        "If you double the falling mass, how does the available energy change? (It doubles.)",
    ),
]
