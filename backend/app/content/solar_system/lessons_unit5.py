"""Unit 5 -- Habitability Beyond the Solar System (the 2027 theme): planets
forming around other stars, how exoplanets are found, the exoplanet zoo
(hot Jupiters, hot Neptunes, cold Jupiters, super-Earths) and migration,
the habitable zone, and astrobiology. Same lesson-chapter format as
lessons_unit1.py.
"""

from app.content.solar_system.svg import BLUE, GAS, GOLD, GREEN, ICE, PURPLE, RED, ROCK, SUN

HOT = "#ff7a3d"

UNIT5 = [
    # ------------------------------------------------------------------ 14
    {
        "unit": 5,
        "name": "Solar System: Planets Forming Around Other Stars",
        "description": "Baby pictures of planetary systems: how a star gets its disk, why we hunt dust in infrared, disk sizes and lifetimes, the race from dust to planetesimals, the 10-Earth-mass giant threshold, debris disks, and the famous images of HL Tau and Fomalhaut.",
        "goals": [
            "Explain how young stars get protoplanetary disks and how we see them.",
            "Give the timeline of how disks change and how fast planets form.",
            "Describe the steps from dust to planetesimals to giant planets.",
            "Describe debris disks, HL Tau and Fomalhaut.",
        ],
        "sections": [
            {
                "heading": "Watching other systems being born",
                "body": (
                    "We can't watch our own Solar System form -- that was 4.5 billion years ago. But we can watch OTHER "
                    "planetary systems forming right now, around young stars in star-forming regions such as the Orion Nebula "
                    "and the Taurus region.\n\n"
                    "Stars form when dense pockets of a cold MOLECULAR CLOUD (a cloud of gas and dust where atoms have joined "
                    "into molecules) collapse under their own gravity. It is a runaway process: the more the clump shrinks, "
                    "the stronger its gravity gets. About half the time the collapsing protostar splits up or pairs with "
                    "others, making a BINARY (two-star) or multiple-star system; the rest of the time it collapses alone, "
                    "like our Sun. Either way, the spinning material speeds up as it shrinks (conservation of angular "
                    "momentum) and flattens into a disk around the star.\n\n"
                    "These PROTOPLANETARY DISKS (also called circumstellar disks) are modern copies of our solar nebula. "
                    "Because nearly all very young stars have one, astronomers conclude that disks -- and probably planets -- "
                    "form together with stars."
                ),
            },
            {
                "heading": "Why we hunt dust instead of planets",
                "body": (
                    "Planets are tiny and faint, lost in their star's glare. But BEFORE planets form, the same material is "
                    "spread out as countless dust grains, each warmed by the young star and glowing in INFRARED light. Spread "
                    "out, the dust has an enormous glowing surface area; once it is packed inside planets, almost all of it is "
                    "hidden. So the infrared glow is strongest before planets form -- and the hunt for planets starts with "
                    "hunting that glow. That's why infrared telescopes like the James Webb Space Telescope (JWST) are such "
                    "important tools.\n\n"
                    "Disks can also be seen as dark SILHOUETTES against bright glowing gas behind them, as Hubble photographed "
                    "in the Orion Nebula. (Dark patches mean the dust is blocking light, not that nothing is there.) Those disks "
                    "are 2 to 8 times the size of Pluto's orbit, around stars no more than about a million years old.\n\n"
                    "DISK FACTS:\n"
                    "• They are 10 to 1,000 AU across. (For scale: Pluto's orbit is about 80 AU across and the Kuiper Belt "
                    "about 100 AU.)\n"
                    "• They hold 1-10% of the Sun's mass -- more than all our planets put together.\n"
                    "• JWST has found molecules in disks such as benzene, ethane, acetic acid (the main ingredient of vinegar) "
                    "and formaldehyde."
                ),
            },
            {
                "heading": "The planet-building clock",
                "body": (
                    "Astronomers can estimate a young star's age by comparing its temperature and brightness on a chart called "
                    "the H-R DIAGRAM (Hertzsprung-Russell diagram). Lining up disks by age shows how they change:\n\n"
                    "• Younger than about 1-3 million years: the disk stretches from right next to the star out to tens or "
                    "hundreds of AU.\n"
                    "• Older: the inner part has lost its dust, so the disk looks like a DONUT with the star in the hole.\n"
                    "• By about 10 million years: the dense inner parts of most disks are gone.\n\n"
                    "Calculations show that a growing planet carves exactly that kind of hole. As it grows a few AU from the "
                    "star, it clears a dust-free lane. Gas and dust between the star and planet fall onto the star in about "
                    "50,000 years, while the planet's gravity stops material outside its orbit from moving in -- just as "
                    "Saturn's shepherd moons keep ring edges sharp. If planets make the holes, then planets form in only about "
                    "3 to 30 million years: a quick side effect of a star being born."
                ),
            },
            {
                "heading": "From dust to planets: a race against time",
                "body": (
                    "1. Tiny dust grains collide and stick together (ACCRETION). Bigger clumps grow faster because they grab "
                    "more of the small ones.\n"
                    "2. DANGER ZONE: at about 10 cm, clumps feel a 'headwind' of DRAG from the disk's gas, and their orbits can "
                    "quickly shrink, plunging them into the star. They must race past about 100 m in size...\n"
                    "3. ...and reach about 1 km, when they become PLANETESIMALS and are safe from the drag.\n"
                    "4. The biggest planetesimals keep sweeping up smaller ones until a few large planets remain.\n"
                    "5. If a planet passes about 10 EARTH MASSES, its gravity can grab hydrogen gas from the disk, and it "
                    "balloons into a GIANT planet. But it must hurry: the young star's strengthening STELLAR WIND can blow "
                    "the disk's gas away within about 10 million years.\n\n"
                    "Debris left over is either swallowed by planets or flung out, and it is gone after about 30 million years "
                    "-- unless something keeps making more."
                ),
                "infographic": "planet_growth",
            },
            {
                "heading": "Debris disks and shepherd planets",
                "body": (
                    "Growing planets stir up the leftover comets and asteroids, which smash together at high speed and make "
                    "fresh dust. A disk kept dusty this way is a DEBRIS DISK. Over a few hundred million years the collisions "
                    "die down, and debris disks fade from view by about 400-500 million years. (Our own Solar System's heavy "
                    "bombardment ended when the Sun was about 500 million years old -- the same pattern!) A little icy "
                    "material stays behind, like our Kuiper Belt.\n\n"
                    "Even when the planets are invisible, their gravity herds dust into clumps, arcs, rings and gaps -- much "
                    "bigger than the planets and much easier to photograph. Brighter parts of a ring simply mean more dust, "
                    "because more dust gives off more infrared light. So we can detect planets by the patterns they leave."
                ),
            },
            {
                "heading": "HL Tau and Fomalhaut",
                "body": (
                    "HL TAU is a newborn star, only about 1 million years old, about 450 light-years away in the Taurus "
                    "star-forming region. It is wrapped in so much dust that it is hidden in visible light. In 2014 the ALMA "
                    "radio telescope array (the Atacama Large Millimeter/submillimeter Array, 66 antennas in Chile's desert) "
                    "used MILLIMETER-WAVE light, which passes through dust, to reveal a disk of bright rings and dark gaps "
                    "carved by several young planets. A growing PROTOPLANET moves faster than the disk gas and dust around it, "
                    "and its gravity reaches much farther than its own size, so it sweeps up material and clears a lane. HL "
                    "Tau showed planets can form faster than we thought -- within the first million years.\n\n"
                    "FOMALHAUT is a hot, young star about 25 light-years away. Its dusty disk was discovered in 1983, but "
                    "JWST's infrared image revealed for the first time THREE nested dust belts stretching out to about 150 AU "
                    "(23 billion km) -- roughly twice the size of our Kuiper Belt."
                ),
            },
        ],
        "word_bank": [
            ("Molecular cloud", "A cold, dense cloud of gas and dust in space where stars are born."),
            ("Binary star", "Two stars orbiting each other."),
            ("Protoplanetary disk", "A flat, spinning disk of gas and dust around a young star, where planets form."),
            ("Circumstellar disk", "Any disk of material around a star (circum = around, stellar = star)."),
            ("Infrared", "Invisible light that warm objects give off as heat; JWST sees in infrared."),
            ("Silhouette", "A dark shape seen against a bright background."),
            ("H-R diagram", "A chart that plots stars' temperature against brightness; used to estimate a young star's age."),
            ("Accretion", "Growing by collecting and sticking smaller pieces together."),
            ("Drag", "A force that slows something moving through a gas or liquid, like a headwind."),
            ("Planetesimal", "A solid building block of a planet, about 1 km or larger."),
            ("Earth mass", "A unit of mass equal to Earth's mass, used to describe planets."),
            ("Stellar wind", "A stream of gas blowing outward from a star."),
            ("Debris disk", "A dusty disk around an older star, kept supplied by colliding comets and asteroids."),
            ("Protoplanet", "A large, still-growing body on its way to becoming a planet."),
            ("ALMA", "The Atacama Large Millimeter/submillimeter Array: 66 radio antennas in Chile that see through dust."),
            ("Millimeter waves", "Radio-like light with wavelengths around a millimeter; it passes through dust."),
            ("JWST", "The James Webb Space Telescope, an infrared space telescope launched December 25, 2021."),
        ],
        "key_facts": [
            "About half of collapsing protostars form binary or multiple stars.",
            "Disks: 10-1,000 AU across; 1-10% of the Sun's mass. Pluto's orbit ~80 AU across; Kuiper Belt ~100 AU.",
            "Disk ages: <1-3 Myr full disk; then donut; inner disk gone by ~10 Myr. Planets form in ~3-30 Myr.",
            "Dust -> 10 cm danger zone (drag) -> must pass 100 m -> 1 km planetesimals. ~10 Earth masses -> grabs gas -> giant.",
            "Gas can be blown away within ~10 Myr; leftover dust gone ~30 Myr unless resupplied; debris disks fade by 400-500 Myr.",
            "HL Tau: ~1 Myr old, ~450 ly, ALMA image 2014 (rings and gaps). Fomalhaut: ~25 ly, 3 belts to ~150 AU (JWST).",
            "JWST found benzene, ethane, acetic acid and formaldehyde in disks.",
        ],
        "quick_check": [
            ("Why do astronomers look for glowing dust instead of the planets themselves?", "Spread-out dust has a huge surface glowing in infrared, while planets are tiny and lost in the star's glare."),
            ("What does a donut-shaped disk suggest?", "A planet has probably formed and cleared the inner region of dust."),
            ("Why is the 10 cm stage dangerous for growing clumps?", "Gas drag makes their orbits shrink so they can spiral into the star unless they grow past ~100 m quickly."),
            ("What lets a planet become a giant?", "Reaching about 10 Earth masses, so its gravity can grab hydrogen gas from the disk -- before the gas is blown away."),
            ("What did ALMA's image of HL Tau show?", "Rings and gaps carved by young planets in a disk only about a million years old."),
        ],
        "cards": [
            {
                "term": "Protoplanetary disks",
                "badge": ("SPIN", "+ flatten", PURPLE),
                "analogy": "A spinning skater pulls in her arms and spins faster -- a collapsing cloud does the same and flattens.",
                "explanation": "Collapsing cloud clumps spin up and flatten into disks around young stars (Orion, Taurus). About half form binaries. Nearly all young stars have disks.",
                "why": "Disks are where every planet -- habitable or not -- is born.",
            },
            {
                "term": "Hunting disks in infrared",
                "badge": ("IR", "glow", RED),
                "analogy": "It's easier to spot a whole field of glowing embers than the few logs they later become.",
                "explanation": "Dust warmed by the star glows in infrared -- strongest before planets form. Disks are 10-1,000 AU across and hold 1-10% of a Sun's mass. JWST found benzene and acetic acid in them.",
                "why": "Why JWST matters for planet formation.",
            },
            {
                "term": "Donut disks & timing",
                "badge": ("3-30", "Myr", GOLD),
                "analogy": "A planet acts like a snowplow, clearing a lane through the dusty disk.",
                "explanation": "Full disks before ~1-3 Myr, donut-shaped later, inner disk gone by ~10 Myr. Planets clear the holes, so they form in ~3-30 million years.",
                "why": "Planet formation is fast compared with a star's life.",
            },
            {
                "term": "The 10 cm danger zone",
                "badge": ("10 cm", "danger!", RED),
                "analogy": "A snowball rolling downhill -- if it stays small too long, the wind blows it into a fire.",
                "explanation": "At ~10 cm, gas drag drags clumps into the star unless they grow past ~100 m fast, reaching ~1 km planetesimals.",
                "why": "Shows planet building is a race against time.",
            },
            {
                "term": "10 Earth-mass threshold",
                "badge": ("10 M⊕", "grab gas", GAS),
                "analogy": "Once heavy enough, a planet becomes a gas vacuum cleaner.",
                "explanation": "Above ~10 Earth masses a planet captures hydrogen and balloons into a giant -- if the stellar wind hasn't blown the gas away (within ~10 Myr).",
                "why": "Explains where and when giant planets can form.",
            },
            {
                "term": "Debris disks",
                "badge": ("400-500", "Myr fade", ROCK),
                "analogy": "The dusty cloud from planet-building, kept dusty by fender-benders between comets.",
                "explanation": "Colliding comets and asteroids keep resupplying dust; disks fade by 400-500 Myr. Hidden planets herd dust into rings, arcs and gaps.",
                "why": "Indirect evidence of planets we can't see.",
            },
            {
                "term": "HL Tau & Fomalhaut",
                "badge": ("ALMA", "+ JWST", ICE),
                "analogy": "HL Tau looks like a bullseye of grooves carved by baby planets.",
                "explanation": "HL Tau (~1 Myr old, ~450 ly): ALMA's 2014 millimeter image showed rings and gaps. Fomalhaut (~25 ly): JWST found three nested belts out to ~150 AU.",
                "why": "The most famous images of planet formation in action.",
            },
        ],
    },
    # ------------------------------------------------------------------ 15
    {
        "unit": 5,
        "name": "Solar System: Finding Exoplanets",
        "description": "How we find planets we can't see: the center of mass wobble, astrometry, the Doppler (radial velocity) method and 51 Pegasi b, selection effects, transits and the transit-depth formula, Kepler, CoRoT and TESS, transit timing, gravitational microlensing, and direct imaging of HR 8799.",
        "goals": [
            "Explain why exoplanets are hard to see directly.",
            "Explain the Doppler method and what it measures.",
            "Explain the transit method and calculate a transit depth.",
            "Explain how combining methods gives a planet's density.",
            "Describe the main planet-hunting telescopes and direct imaging.",
            "Explain how gravitational microlensing finds planets and what kinds it finds best.",
        ],
        "sections": [
            {
                "heading": "The mosquito and the spotlight",
                "body": (
                    "An EXOPLANET is a planet that orbits a star other than the Sun. Photographing one is like trying to see a "
                    "mosquito buzzing next to a giant searchlight -- while you look from an airplane. The searchlight is easy; "
                    "the mosquito is hopeless. Earth, for example, reflects less than a billionth of the Sun's light.\n\n"
                    "So astronomers mostly use INDIRECT methods: instead of seeing the planet, they watch what the planet does "
                    "to its star -- a tiny wobble, or a tiny dimming when it passes in front. The first exoplanet around a "
                    "normal, Sun-like (MAIN-SEQUENCE) star was found in 1995. Today thousands are known, and we know most stars "
                    "form with planets."
                ),
            },
            {
                "heading": "Everybody wobbles: center of mass and astrometry",
                "body": (
                    "Gravity pulls both ways. A star doesn't sit perfectly still while a planet circles it -- both orbit "
                    "their shared CENTER OF MASS, like a grown-up and a small child holding hands and spinning: the child "
                    "swings in a big circle while the grown-up just shuffles in a small one. A Jupiter-like planet with 1/1000 "
                    "of its star's mass makes the star swing in an orbit 1/1000 as big as the planet's.\n\n"
                    "ASTROMETRY means precisely measuring a star's position in the sky to catch that tiny shuffle. From Alpha "
                    "Centauri (about 4.25 light-years away), Jupiter's orbit would span 10 ARCSECONDS, but the Sun's loop only "
                    "0.010 arcseconds (1 arcsecond is 1/3600 of a degree -- about the width of a coin seen from 4 km away), "
                    "repeating every 12 years. Measuring that is so hard that very few planets have been found this way."
                ),
            },
            {
                "heading": "The Doppler (radial velocity) method",
                "body": (
                    "Remember how an ambulance siren sounds higher as it comes toward you and lower as it drives away? That "
                    "is the DOPPLER EFFECT, and light does it too. When a wobbling star moves toward us, the dark lines in its "
                    "SPECTRUM (its rainbow of colors) shift slightly toward blue -- a BLUESHIFT. When it moves away, they shift "
                    "toward red -- a REDSHIFT. Measuring these shifts gives the star's RADIAL VELOCITY: its speed toward or away "
                    "from us.\n\n"
                    "• Jupiter makes the Sun's speed change by about 13 m/s (about 30 mph, city driving speed!) every 12 years.\n"
                    "• The size of the speed change doesn't depend on how far away the star is -- only on getting a bright, "
                    "sharp spectrum with a big telescope.\n"
                    "• One full wobble = one orbit, so we learn the planet's year (and from Kepler's laws, its distance).\n"
                    "• The size of the wobble gives the planet's MINIMUM mass -- 'minimum' because we usually can't tell how "
                    "tilted the orbit is.\n"
                    "• Several planets around one star can be untangled from the combined wobble.\n"
                    "• It works best for BIG planets CLOSE to their stars. It has found hundreds of planets, including one "
                    "around Proxima Centauri, the nearest star.\n\n"
                    "THE FIRST ONE: 51 PEGASI b (1995). Michel Mayor and Didier Queloz of the Geneva Observatory used the "
                    "Doppler method on 51 Pegasi, a Sun-like star about 40 light-years away near the Great Square of Pegasus. "
                    "Surprise: its planet orbits in just 4.2 days (Mercury takes 88), only about 7 million km from its star, "
                    "heated to a few thousand degrees, with at least half Jupiter's mass. It was the first 'hot Jupiter', and "
                    "it won them the 2019 Nobel Prize in physics."
                ),
                "infographic": "doppler_method",
            },
            {
                "heading": "Beware the selection effect",
                "body": (
                    "Why were so many of the first planets found hot Jupiters? Big planets close to their stars make the "
                    "biggest, fastest wobbles, and their short orbits can be confirmed quickly. So the method 'selects' them as "
                    "easy finds. This is a SELECTION EFFECT (or observational bias): the way you search decides what you find. "
                    "It's like looking for friends only at events that require a student ID -- you'd think everyone is a "
                    "student! As telescopes improved and watched longer, smaller and more distant planets turned up too, and "
                    "after correcting for the bias, small planets turn out to be MORE common than giant ones."
                ),
            },
            {
                "heading": "The transit method",
                "body": (
                    "If we happen to see a planet's orbit edge-on, the planet passes in front of its star once every orbit -- "
                    "a TRANSIT -- blocking a tiny bit of light. A graph of the star's brightness over time (a LIGHT CURVE) shows "
                    "a small dip: (1) out of transit, (2) INGRESS as the planet starts crossing, (3) the full dip.\n\n"
                    "TRANSIT DEPTH (how much the star dims) = (radius of planet / radius of star)^2. That's because the planet's "
                    "dark disk covers part of the star's bright disk, and a circle's area is pi x R^2.\n"
                    "• Jupiter (radius 71,400 km) in front of the Sun (695,700 km): (71,400 / 695,700)^2 = about 0.01, or 1%.\n"
                    "• Earth (6,371 km) in front of a star half the Sun's size (347,850 km): about 0.0003, or 0.03% -- much "
                    "harder to spot. Smaller stars make small planets easier to find.\n\n"
                    "What transits tell us:\n"
                    "• The time between dips = the planet's year -> its distance (Kepler's third law).\n"
                    "• The depth -> the planet's SIZE (if we know the star's size).\n"
                    "• Doppler MASS + transit SIZE -> DENSITY -> what the planet is made of!\n\n"
                    "In 1999 the first transiting planet was found, around the star HD 209458: it passes in front for about 3 "
                    "hours every 3.5 days. It has about 70% of Jupiter's mass but a radius 35% bigger, so it must be a world of "
                    "gas and liquid. During transit, starlight shining through its atmosphere showed the fingerprint of SODIUM "
                    "-- the first chemical detected in an exoplanet's air. Today this TRANSIT SPECTROSCOPY is how we read "
                    "exoplanet atmospheres."
                ),
                "infographic": "transit_method",
            },
            {
                "heading": "Space telescopes on the hunt",
                "body": (
                    "From space (above the blurring of Earth's air), transits as small as a Mars-size planet can be detected.\n\n"
                    "• CoRoT (French and European space agencies, launched 2007): found 32 transiting planets, including the "
                    "first with an Earth-like size and density; a computer failure ended it in 2012.\n"
                    "• KEPLER (NASA, launched 2009): stared at more than 150,000 stars in one patch of sky near the "
                    "constellation Cygnus to find out how common planets of different sizes are. It needed three spinning "
                    "REACTION WHEELS to point steadily (it carried four). By May 2013 two had failed -- exactly 4 years and 1 "
                    "day after it started its 4-year mission! It kept working for two more years in other directions, then ran "
                    "out of fuel in 2018. It found thousands of planets.\n"
                    "• TESS (Transiting Exoplanet Survey Satellite): now surveys nearer, brighter stars all over the sky -- "
                    "almost 600 planets and about 7,400 candidates by the end of 2024.\n"
                    "• JWST (launched December 21, 2021 per the wiki; NASA lists December 25) studies exoplanet atmospheres in "
                    "infrared."
                ),
                "infographic": "detection_compare",
            },
            {
                "heading": "When does a dip count as a discovery?",
                "body": (
                    "One dip could be a glitch near the telescope's limit. A second dip of the same depth might belong to a "
                    "different planet. Only a THIRD dip with the same depth AND the same spacing counts as a discovery. "
                    "Because Kepler needed three transits, it could only find planets with years shorter than about a third of "
                    "its observing time -- planets with Earth-like 1-year orbits only showed up in its fourth year. Kepler's "
                    "'discovery space' was planets with orbits under about 400 days and sizes bigger than Mars.\n\n"
                    "Extra proof helps: a matching Doppler wobble (usually impossible for Earth-size planets), or finding more "
                    "planets around the same star. In crowded systems, planets tug on each other so their transits arrive a few "
                    "minutes early or late -- measuring these TRANSIT TIMING VARIATIONS reveals the planets' masses. Citizen "
                    "scientists have even spotted transits that computers missed!"
                ),
            },
            {
                "heading": "Direct imaging: actually taking a picture",
                "body": (
                    "Direct imaging works best for YOUNG GIANT planets far from their stars, because they still glow in "
                    "infrared with heat left over from forming. Special optics (like a CORONAGRAPH, which blocks the star's "
                    "light, like holding your hand up to block the Sun) and computer tricks remove the star's glare. Infrared "
                    "is the best light to use, because planets get brighter in infrared while Sun-like stars get dimmer.\n\n"
                    "In 2008, three planets were photographed around the star HR 8799 in Pegasus; a fourth, closer one appeared "
                    "in 2010 (Keck telescopes). Their colors reveal temperatures (planet 1 seems to have thick clouds), and "
                    "their spectra reveal gases: hydrogen in planet 1's atmosphere and methane in planet 4's. One challenge is "
                    "making sure a dot is a planet and not a BROWN DWARF -- a 'failed star', too small to fuse hydrogen. "
                    "Imaging an Earth-size planet is still extremely hard, even from space."
                ),
            },
            {
                "heading": "Gravitational microlensing: a lens made of gravity",
                "body": (
                    "Einstein's theory of gravity (general relativity) says mass BENDS the path of light. If a nearer star "
                    "drifts almost exactly in front of a much more distant star, the nearer star's gravity acts like a "
                    "magnifying glass: it bends and focuses the background star's light, so the background star brightens "
                    "smoothly and then fades over days to weeks. The nearer star is the LENS; the distant one is the SOURCE. "
                    "This is GRAVITATIONAL MICROLENSING.\n\n"
                    "If the lens star has a PLANET, the planet's own small gravity adds a short extra BLIP to the light "
                    "curve -- lasting a few days for a Jupiter-mass planet and only a few hours for an Earth-mass one. The shape "
                    "of the blip reveals the planet's mass compared with its star and how far apart they are.\n\n"
                    "• STRENGTHS: it finds planets thousands of light-years away (toward the crowded center of the galaxy), "
                    "it works best for planets about 1-10 AU from their stars -- cold planets the transit and Doppler "
                    "methods struggle with -- it can detect planets as small as Earth, and it can even find ROGUE (free-"
                    "floating) planets with no star at all.\n"
                    "• WEAKNESSES: the alignment happens only ONCE and never repeats, so it can't be checked again, and the "
                    "host star is usually too faint and far to study afterward. Surveys must watch millions of stars "
                    "every night to catch the rare events.\n\n"
                    "The first planet found this way was announced in 2004 (OGLE-2003-BLG-235 b), by ground surveys like "
                    "OGLE, MOA and KMTNet. NASA's Nancy Grace Roman Space Telescope (launched August 2026) will run a huge microlensing "
                    "survey toward the galactic center and is expected to find more than a thousand planets this way."
                ),
                "infographic": "microlensing",
            },
        ],
        "word_bank": [
            ("Exoplanet", "A planet orbiting a star other than our Sun."),
            ("Main-sequence star", "A normal adult star fusing hydrogen in its core, like the Sun."),
            ("Center of mass", "The balance point that a star and its planet both orbit around."),
            ("Astrometry", "Measuring the exact positions of stars to catch tiny wobbles."),
            ("Arcsecond", "A tiny angle: 1/3600 of a degree."),
            ("Doppler effect", "The change in pitch of sound, or color of light, when the source moves toward or away from you."),
            ("Spectrum", "The rainbow of colors in light, with dark lines that act like a fingerprint."),
            ("Blueshift", "Light shifted toward blue because its source is moving toward us."),
            ("Redshift", "Light shifted toward red because its source is moving away from us."),
            ("Radial velocity", "How fast something moves toward or away from us."),
            ("Minimum mass", "The smallest a planet's mass could be; the Doppler method gives this because the orbit's tilt is unknown."),
            ("Hot Jupiter", "A giant gas planet orbiting extremely close to its star."),
            ("Selection effect", "When the way you search makes some kinds of objects easier to find, giving a lopsided picture."),
            ("Transit", "When a planet passes in front of its star and blocks a little light."),
            ("Light curve", "A graph of an object's brightness over time."),
            ("Ingress", "The moment a planet starts to move in front of its star."),
            ("Transit depth", "How much a star dims during a transit: (planet radius / star radius)^2."),
            ("Transit spectroscopy", "Studying starlight that passes through a planet's atmosphere during a transit to find its gases."),
            ("Reaction wheel", "A spinning wheel a spacecraft uses to point steadily without fuel."),
            ("Transit timing variations", "Transits arriving early or late because neighboring planets tug on each other; used to find masses."),
            ("Direct imaging", "Taking an actual picture of an exoplanet by blocking its star's light."),
            ("Coronagraph", "A device in a telescope that blocks a star's light so faint things next to it can be seen."),
            ("Brown dwarf", "A 'failed star' -- bigger than a planet but too small to fuse hydrogen."),
            ("Gravitational microlensing", "When a nearer star's gravity magnifies a distant star's light; a planet adds a short blip."),
            ("Lens star", "The nearer star whose gravity bends and focuses light in a microlensing event."),
            ("Source star", "The distant background star that gets magnified during microlensing."),
            ("Rogue planet", "A free-floating planet that doesn't orbit any star."),
        ],
        "key_facts": [
            "First exoplanet around a Sun-like star: 51 Pegasi b, 1995, Mayor & Queloz (Doppler); 4.2-day orbit; 2019 Nobel Prize.",
            "Jupiter makes the Sun wobble ~13 m/s over 12 years. Doppler gives period + MINIMUM mass; best for big, close planets.",
            "Astrometry: Sun's loop seen from Alpha Centauri = 0.010 arcsec (Jupiter's orbit = 10 arcsec).",
            "Transit depth = (Rp/Rs)^2. Jupiter/Sun ~1%; Earth/half-Sun ~0.03%. Need 3 equal, evenly spaced dips.",
            "Mass (Doppler) + size (transit) = density. HD 209458 b (1999): first transit; sodium in its air.",
            "CoRoT 2007-2012 (32 planets); Kepler 2009-2018 (150,000+ stars near Cygnus; 2 reaction wheels failed 2013); TESS: ~600 planets + ~7,400 candidates by end of 2024.",
            "Direct imaging: HR 8799 (3 planets 2008, 4th 2010) -- young, hot giants far from their star; infrared best.",
            "Microlensing: lens star's gravity magnifies a source star; planet = short blip. Best for cold planets 1-10 AU out, far away, even rogue planets; one-time, can't repeat. First 2004 (OGLE); Roman will find 1,000+.",
            "2027 rules limit detection methods to: transits, radial velocity, microlensing and direct imaging.",
        ],
        "quick_check": [
            ("Why does the Doppler method give only a minimum mass?", "We usually don't know how tilted the orbit is, so part of the star's motion may be hidden from us."),
            ("A planet has 1/10 the radius of its star. What is the transit depth?", "(1/10)^2 = 1/100 = 1%."),
            ("What can you learn by combining the Doppler and transit methods?", "Mass (Doppler) and size (transit), which give the planet's density -- whether it is rocky or gassy."),
            ("Why were most early exoplanets hot Jupiters?", "Selection effect: big planets close to their stars make the biggest, fastest signals, so they are found first."),
            ("Why did Kepler struggle to find planets with 1-year orbits?", "It needed three transits, so a 1-year planet needed 3 years of watching -- they only appeared in its fourth year."),
            ("Which planets are easiest to directly image?", "Young giant planets far from their stars, glowing in infrared with leftover heat."),
            ("In a microlensing light curve, what does a short extra blip mean?", "The lens star has a planet; the planet's gravity briefly adds extra magnification."),
            ("Give one strength and one weakness of microlensing.", "Strength: finds cold, distant or even rogue planets, down to Earth mass. Weakness: the event happens once and can't be repeated or followed up easily."),
        ],
        "cards": [
            {
                "term": "Exoplanet",
                "badge": ("EXO", "planet", GOLD),
                "analogy": "A planet with a different 'home sun' than ours.",
                "explanation": "A planet orbiting another star. Seeing one directly is like spotting a mosquito next to a searchlight from an airplane, so most are found by their effects on their star.",
                "why": "Every 'beyond the Solar System' question starts here.",
            },
            {
                "term": "Center of mass & astrometry",
                "badge": ("0.010", "arcsec", PURPLE),
                "analogy": "A grown-up and a toddler spinning hand in hand: the toddler zooms, the grown-up shuffles.",
                "explanation": "Star and planet orbit their center of mass. Astrometry tries to see the star's tiny shuffle (the Sun's is 0.010 arcsec from Alpha Centauri) -- extremely hard.",
                "why": "Know why astrometry is the 'hard' method.",
            },
            {
                "term": "Doppler (radial velocity) method",
                "badge": ("RV", "wobble", BLUE),
                "analogy": "An ambulance siren's pitch rising and falling -- the star's light 'pitch' shifts as it wobbles.",
                "explanation": "Blueshift toward us, redshift away. Gives the period and minimum mass; works best for big, close planets. Jupiter wobbles the Sun by ~13 m/s.",
                "why": "The most-tested detection method.",
            },
            {
                "term": "51 Pegasi b",
                "badge": ("1995", "first!", SUN),
                "analogy": "A gas giant racing around its star in under a week.",
                "explanation": "Mayor and Queloz (1995): ~40 ly away, 4.2-day orbit, ~7 million km from its star, at least half Jupiter's mass. The first hot Jupiter; Nobel Prize 2019.",
                "why": "Classic 'first exoplanet' question.",
            },
            {
                "term": "Transit method",
                "badge": ("DIP", "transit", GOLD),
                "analogy": "A moth flying in front of a porch light -- you can't see the moth, but the light flickers.",
                "explanation": "A planet crossing its star dims it. Time between dips = year; depth = size. Three matching dips are needed.",
                "why": "Most known exoplanets were found this way.",
            },
            {
                "term": "Transit depth formula",
                "badge": ("(Rp/Rs)²", "depth", GOLD),
                "analogy": "A coin in front of a flashlight blocks light in proportion to its area.",
                "explanation": "Depth = (Rp/Rs)^2. Jupiter/Sun = (71,400/695,700)^2 ~ 1%. Earth in front of a half-Sun star ~ 0.03%.",
                "why": "A guaranteed calculation type.",
            },
            {
                "term": "Density from two methods",
                "badge": ("1999", "HD 209458", GAS),
                "analogy": "Knowing how heavy AND how big a ball is tells you if it's a bowling ball or a beach ball.",
                "explanation": "Doppler mass + transit size = density. HD 209458 b: 70% of Jupiter's mass but 35% bigger -> gas giant; sodium found in its air during transit.",
                "why": "Transit spectroscopy is how we'll search for biosignatures.",
            },
            {
                "term": "Kepler, CoRoT & TESS",
                "badge": ("150K", "stars", BLUE),
                "analogy": "Kepler was a lifeguard watching one pool of stars for years.",
                "explanation": "CoRoT (2007-2012, 32 planets). Kepler (2009-2018, 150,000+ stars near Cygnus; reaction wheels failed 2013). TESS (bright nearby stars, ~600 planets by 2024).",
                "why": "Mission names, dates and goals are quick-answer questions.",
            },
            {
                "term": "Direct imaging",
                "badge": ("HR 8799", "4 planets", PURPLE),
                "analogy": "Photographing a firefly next to a lighthouse -- block the lighthouse first.",
                "explanation": "Works for young, hot giants far from their stars, in infrared, with a coronagraph. HR 8799: 3 planets imaged in 2008, a 4th in 2010.",
                "why": "Future life searches will need direct images and spectra.",
            },
            {
                "term": "Gravitational microlensing",
                "badge": ("LENS", "gravity", ICE),
                "analogy": "A passing star acts like a magnifying glass sliding over a faraway streetlight -- and a planet is a speck of dust that adds a flicker.",
                "explanation": "A nearer star's gravity bends and brightens a distant star's light for days to weeks; a planet adds an hours-to-a-day blip. Finds cold, far-away and rogue planets, but each event happens only once.",
                "why": "One of the four detection methods named in the 2027 rules; Roman will use it.",
            },
        ],
    },
    # ------------------------------------------------------------------ 16
    {
        "unit": 5,
        "name": "Solar System: The Exoplanet Zoo -- Hot Jupiters, Super-Earths & Moving Planets",
        "description": "What we've found: planets are everywhere, super-Earths and mini-Neptunes, hot Jupiters (0.36-13.6 Jupiter masses), hot Neptunes and cold Jupiters, the mass-radius diagram, multi-planet systems like Kepler-62, planet migration, and the 'roller derby' picture.",
        "goals": [
            "Describe how common planets are and the most common kinds.",
            "Define hot Jupiters, hot Neptunes, cold Jupiters, super-Earths and mini-Neptunes.",
            "Use the mass-radius idea to judge what a planet is made of.",
            "Explain how hot Jupiters got so close to their stars (migration).",
        ],
        "sections": [
            {
                "heading": "Planets are everywhere",
                "body": (
                    "Before 1995, astronomers knew only one planetary system -- ours -- and assumed others would look similar: "
                    "rocky planets close in, giants a few AU out, everyone on neat circular orbits. Systems like ours do exist, "
                    "but many are wildly different, and some kinds of planets don't exist in our Solar System at all.\n\n"
                    "• Kepler's data suggest about HALF of all stars (or more) have planets -- at least 100 BILLION planets in "
                    "our Galaxy alone.\n"
                    "• Most planets found so far are bigger than Earth, but that is a selection effect. After correcting for "
                    "it, small rocky planets are MORE common than giants.\n"
                    "• The most common sizes are ones we don't have: between Earth and Neptune. SUPER-EARTHS have about 2 to 10 "
                    "times Earth's mass; MINI-NEPTUNES are a bit bigger and probably wrapped in thick gas.\n"
                    "• Another kind we lack: giants several times more massive than Jupiter."
                ),
                "infographic": "exoplanet_zoo",
            },
            {
                "heading": "Hot Jupiters, hot Neptunes and cold Jupiters",
                "body": (
                    "HOT JUPITERS are gas giant exoplanets with extremely close, hot orbits around their stars -- often just a "
                    "few days long, much closer than Mercury is to the Sun.\n"
                    "• They are scorching, often over 1,000 K, which creates strange atmospheres.\n"
                    "• Many are probably tidally locked, with one side always facing the star.\n"
                    "• To count as a hot Jupiter, a planet's mass is between about 0.36 and 13.6 JUPITER MASSES (a Jupiter mass "
                    "is Jupiter's own mass, about 318 Earths). This range is a very commonly asked test question -- put it on "
                    "your note sheet!\n"
                    "• They are mostly hydrogen and helium.\n"
                    "• They are the easiest planets to find with the Doppler wobble method, because their huge mass and tight "
                    "orbits make big, fast wobbles. 51 Pegasi b was the first.\n\n"
                    "HOT NEPTUNES are similar but smaller, more like Neptune or Uranus. They have less atmosphere than hot "
                    "Jupiters and denser cores, because the star's radiation strips their gas away. They are ice giants, so "
                    "they contain heavier substances like water, ammonia and methane. They often orbit within about 1 AU of "
                    "their stars.\n\n"
                    "COLD JUPITERS are gas giants like hot Jupiters -- but cold, because they orbit far from their star, BEYOND "
                    "THE FROST LINE: the distance from a young star where it is cold enough for volatile compounds such as "
                    "water, ammonia and methane to freeze into ice grains. Our own Jupiter is a cold Jupiter."
                ),
                "infographic": "jupiter_types",
            },
            {
                "heading": "Mass vs. size: what is it made of?",
                "body": (
                    "When a planet has both a measured mass and radius, we can compare it with model planets made of pure "
                    "iron, pure rock, pure water or pure hydrogen.\n\n"
                    "• Like adding clay to a clay ball, adding mass usually makes a planet bigger.\n"
                    "• But above about 1,000 Earth masses, extra mass makes a planet SMALLER! Its stronger gravity squeezes "
                    "everything tighter. (Jupiter is about 320 Earth masses.)\n"
                    "• Real planets are layered (Earth has a solid iron inner core, liquid outer core, rocky mantle and crust, "
                    "and a thin atmosphere). Modelers start with simple 2-3 layer models -- narrowing down the possibilities "
                    "is a good first step in science. Venus and Earth plot between the pure-iron and pure-rock lines, as "
                    "expected.\n\n"
                    "PUFFY HOT JUPITERS: many hot Jupiters are INFLATED -- less dense than even pure hydrogen should be! They "
                    "soak up so much starlight that energy gets trapped deep inside and puffs them up, and slightly oval "
                    "orbits let the star raise tides in them that add more heat. Cold Jupiters in wide orbits shouldn't be "
                    "inflated, unless they are very young."
                ),
            },
            {
                "heading": "Families of planets",
                "body": (
                    "The first multi-planet system around another star, Upsilon Andromedae, was found in 1999 with the Doppler "
                    "method. By the end of 2025 more than 1,000 multi-planet systems were known: many with two planets, some "
                    "with five, and one with EIGHT, like ours. Most are very compact, with several planets closer to their "
                    "star than Mercury is to the Sun.\n\n"
                    "KEPLER-62 is a good example: all but one of its planets are bigger than Earth (super-Earths), one (62d) is "
                    "mini-Neptune size and probably gassy, and the smallest is about Mars' size. Only the outer two orbit "
                    "farther out than Mercury does from the Sun. Its HABITABLE ZONE is smaller and closer in than the Sun's "
                    "because the star is fainter.\n\n"
                    "Kepler also found planets circling CLOSE DOUBLE STARS -- a sky with two suns, like Tatooine in Star Wars -- "
                    "and KEPLER-444: five planets, from Mercury-size to Venus-size, around a star more than 11 billion years "
                    "old, born when the Milky Way was only about 2 billion years old. So rocky planets were forming very early "
                    "in our Galaxy's history."
                ),
            },
            {
                "heading": "How did hot Jupiters get there? Migration",
                "body": (
                    "Hot Jupiters were a big puzzle. A giant planet needs ice to build its core, and ice can't survive that "
                    "close to a star. So hot Jupiters must have formed far out, beyond the frost line, and then MIGRATED "
                    "(moved) inward. Two ways this can happen:\n\n"
                    "1. DISK DRAG: while gas is still in the disk, the planet moves faster than the gas and dust, feels a kind "
                    "of 'headwind', loses orbital energy (angular momentum) to the disk and spirals inward. Many probably "
                    "plunge into their star; somehow some stop in time.\n"
                    "2. SCATTERING: in a crowded young system, close encounters between sibling planets can fling a giant onto "
                    "a very stretched orbit that dips close to the star; then tides and friction shrink and round out its orbit "
                    "near the star.\n\n"
                    "Clues: many exoplanets have very ECCENTRIC (oval) orbits, and some giants orbit at right angles to their "
                    "star's spin -- or even backward -- which suggests planet-planet kicks or a passing star. Only a few percent "
                    "of planetary systems have hot Jupiters.\n\n"
                    "Our own planets may have moved too: Uranus and Neptune probably formed closer in and were pushed outward "
                    "(the Nice Model), and an early Jupiter might have migrated inward and swept away close-in rocky planets "
                    "that other systems still have."
                ),
                "infographic": "hot_jupiter_migration",
            },
            {
                "heading": "From polite skaters to roller derby",
                "body": (
                    "The old picture of planet formation, based only on our Solar System, imagined planets as polite ice "
                    "skaters all gliding the same direction in neat circles. Exoplanets changed that to a ROLLER DERBY: planets "
                    "crash, change direction, migrate, and sometimes get thrown out of their system entirely. The basic idea "
                    "-- planets form in disks around young stars -- still holds. But it is dangerous to draw big conclusions "
                    "from just one example, and surprising new data is exactly how science moves forward."
                ),
            },
        ],
        "word_bank": [
            ("Super-Earth", "A planet about 2 to 10 times Earth's mass -- bigger than Earth but smaller than Neptune."),
            ("Mini-Neptune", "A planet a bit bigger than a super-Earth, probably wrapped in thick gas."),
            ("Hot Jupiter", "A gas giant (0.36-13.6 Jupiter masses) orbiting extremely close to its star, often in just a few days."),
            ("Jupiter mass", "A unit of mass equal to Jupiter's mass (about 318 Earth masses)."),
            ("Hot Neptune", "A Neptune-like ice giant orbiting close to its star, with a dense core and thinner atmosphere."),
            ("Cold Jupiter", "A gas giant orbiting beyond its star's frost line, far from the star -- like our Jupiter."),
            ("Frost line", "The distance from a young star beyond which water, ammonia and methane freeze into ice."),
            ("Inflated", "Puffed up -- bigger and less dense than expected."),
            ("Multi-planet system", "A star with two or more known planets."),
            ("Habitable zone", "The range of distances from a star where a planet's surface could hold liquid water."),
            ("Migration", "When a planet moves to a new orbit after it forms."),
            ("Scattering", "When gravity from a close encounter flings a planet onto a new orbit."),
            ("Eccentric orbit", "A stretched, oval-shaped orbit."),
            ("Angular momentum", "The 'amount of spin' or orbital motion something has."),
        ],
        "key_facts": [
            "About half (or more) of stars have planets -> at least 100 billion planets in the Milky Way.",
            "Most common sizes: between Earth and Neptune. Super-Earths: 2-10 Earth masses.",
            "Hot Jupiter: 0.36-13.6 Jupiter masses; orbits of days; often >1,000 K; often tidally locked; easiest by Doppler.",
            "Hot Neptunes: smaller, denser cores, gas stripped; contain water/ammonia/methane; often within ~1 AU.",
            "Cold Jupiters: gas giants beyond the frost line.",
            "Above ~1,000 Earth masses, more mass -> smaller radius. Jupiter ~320 Earth masses.",
            "First multi-planet system: Upsilon Andromedae (1999). >1,000 systems by end of 2025; one with 8 planets.",
            "Migration: disk drag or planet-planet scattering. A few percent of systems have hot Jupiters.",
        ],
        "quick_check": [
            ("What mass range defines a hot Jupiter?", "About 0.36 to 13.6 Jupiter masses."),
            ("How is a hot Neptune different from a hot Jupiter?", "It is smaller, has less atmosphere and a denser core (radiation stripped its gas), and contains heavier ices like water, ammonia and methane."),
            ("What makes a Jupiter 'cold'?", "It orbits beyond the frost line, far from its star, where water, ammonia and methane freeze."),
            ("Why must hot Jupiters have migrated?", "Giant planets need ice to build their cores, and ice can't exist that close to a star, so they formed farther out and moved in."),
            ("Which size of planet is most common in the Galaxy, as far as we know?", "Planets between Earth and Neptune in size (super-Earths and mini-Neptunes) -- which our Solar System doesn't have."),
        ],
        "cards": [
            {
                "term": "How common are planets?",
                "badge": ("100B+", "in Galaxy", GOLD),
                "analogy": "Almost every house on the street turns out to have a backyard.",
                "explanation": "About half or more of stars have planets: at least 100 billion in the Milky Way. Small planets are more common than giants once selection effects are corrected.",
                "why": "More planets = better odds of habitable worlds.",
            },
            {
                "term": "Super-Earths & mini-Neptunes",
                "badge": ("2-10", "Earth masses", "#6fb07a"),
                "analogy": "The 'medium' size on a menu where our Solar System only ordered small and extra-large.",
                "explanation": "Super-Earths: 2-10 Earth masses. Mini-Neptunes: a bit bigger and gassy. The most common sizes found -- yet absent in our Solar System.",
                "why": "Many habitable-zone candidates are super-Earths.",
            },
            {
                "term": "Hot Jupiters",
                "badge": ("0.36-13.6", "M_Jup", HOT),
                "analogy": "A marshmallow held right next to a campfire -- scorching and puffed up.",
                "explanation": "Gas giants with orbits of days, often over 1,000 K and tidally locked; masses 0.36-13.6 Jupiter masses; mostly H and He; easiest to find by Doppler. Often inflated.",
                "why": "The mass range is a favorite test question.",
            },
            {
                "term": "Hot Neptunes",
                "badge": ("HOT", "Neptunes", "#7fb8d8"),
                "analogy": "A hot Jupiter's smaller cousin that had its puffy layers blown away.",
                "explanation": "Smaller than hot Jupiters, less atmosphere, denser cores (radiation strips their gas); ice giants with water, ammonia and methane; often within ~1 AU.",
                "why": "Exoplanet classification questions often list them.",
            },
            {
                "term": "Cold Jupiters",
                "badge": ("COLD", "beyond frost", ICE),
                "analogy": "A gas giant living in the freezer section, far from its star.",
                "explanation": "Gas giants orbiting beyond the frost line, where water, ammonia and methane freeze into ice. Our Jupiter is one.",
                "why": "Hot vs. cold Jupiter is all about the frost line.",
            },
            {
                "term": "Mass-radius diagram",
                "badge": ("M vs R", "makeup", PURPLE),
                "analogy": "Adding clay makes a clay ball bigger -- until it's so heavy it squishes itself smaller.",
                "explanation": "Compare a planet's mass and radius with pure iron, rock, water and hydrogen models. Above ~1,000 Earth masses, more mass = smaller. Inflated hot Jupiters are less dense than pure hydrogen.",
                "why": "How we decide if an exoplanet is rocky (possibly habitable).",
            },
            {
                "term": "Planet migration",
                "badge": ("INWARD", "migration", HOT),
                "analogy": "A kid born in the backyard who later moved into the kitchen right next to the stove.",
                "explanation": "Giants form beyond the frost line, then move in by disk drag or by planet-planet scattering. Oval and tilted orbits are clues. Uranus and Neptune probably moved outward.",
                "why": "The standard explanation for hot Jupiters.",
            },
            {
                "term": "Roller derby",
                "badge": ("DERBY", "new model", RED),
                "analogy": "Old idea: polite skaters. New idea: roller derby.",
                "explanation": "Planets crash, migrate, change direction and get thrown out. Formation in disks still holds, but one example (ours) was misleading.",
                "why": "Great summary for essay questions.",
            },
        ],
    },
    # ------------------------------------------------------------------ 17
    {
        "unit": 5,
        "name": "Solar System: Habitability & the Habitable Zone",
        "description": "What 'habitable' means (water, CHNOPS elements, energy), the habitable zone and the inverse-square law, why Venus, Earth and Mars differ despite similar sunlight, habitable zones around red dwarfs, Proxima Centauri b, moving zones, tidal locking, and how many Earth-like planets there may be.",
        "goals": [
            "List what life as we know it needs.",
            "Define the habitable zone and use the inverse-square law.",
            "Explain why distance alone doesn't decide habitability.",
            "Compare habitable zones around different stars, including red dwarfs.",
            "Explain why being in the habitable zone is no guarantee of life.",
        ],
        "sections": [
            {
                "heading": "What does 'habitable' mean?",
                "body": (
                    "A HABITABLE environment is one that could host life. Scientists focus on life chemically like ours, "
                    "since completely different chemistries ('life as we don't know it') are still pure guesswork. Life as we "
                    "know it needs three things:\n\n"
                    "1. LIQUID WATER. Life needs a SOLVENT -- a liquid where chemicals can dissolve, meet and react to build the "
                    "molecules of life. For us that is water. Water is common in the universe, but it has to be LIQUID, which "
                    "only happens within a certain range of temperature AND pressure (remember Mars, where low pressure makes "
                    "ice turn straight into gas). That is why the motto of exploration is 'FOLLOW THE WATER'.\n"
                    "2. THE RIGHT ELEMENTS. Our biochemistry is built mostly from six elements: carbon, hydrogen, nitrogen, "
                    "oxygen, phosphorus and sulfur -- remember 'CHNOPS' (say 'shnops'). CARBON is the superstar: each carbon "
                    "atom can form four BONDS (connections), with other carbons and with the other elements, so it can build an "
                    "almost endless variety of large molecules.\n"
                    "3. ENERGY. Sunlight (used in photosynthesis) or chemical energy (like the communities around deep-sea "
                    "vents, or maybe in Europa's ocean).\n\n"
                    "When the Curiosity rover proved ancient Mars was 'habitable', it meant all three -- water, energy and raw "
                    "materials -- were present in Gale crater."
                ),
                "infographic": "life_recipe",
            },
            {
                "heading": "The habitable zone",
                "body": (
                    "The HABITABLE ZONE (HZ) is the range of distances from a star where a planet's SURFACE could hold liquid "
                    "water. It is often called the GOLDILOCKS ZONE: not too hot, not too cold. In our Solar System, Venus' "
                    "surface is far above water's boiling point, Mars' is almost always below freezing, and Earth, in between, "
                    "is 'just right'.\n\n"
                    "But distance isn't the whole story. A planet's temperature depends on its RADIATION BUDGET -- the energy "
                    "coming in and going out:\n"
                    "• how much light, and what kind, its star gives off,\n"
                    "• how far the planet is from the star,\n"
                    "• how much light the planet reflects back into space (its albedo),\n"
                    "• how well its atmosphere traps heat (the greenhouse effect),\n"
                    "• and how winds and ocean currents spread heat around the planet."
                ),
                "infographic": "habitable_zone",
            },
            {
                "heading": "The inverse-square law",
                "body": (
                    "Starlight spreads out as it travels, like spray paint: from twice as far away, the same paint covers 4 "
                    "times the area, so each spot gets 1/4 as much. The light hitting each square meter drops with the SQUARE "
                    "of the distance -- the INVERSE-SQUARE LAW:\n\n"
                    "brightness compared to Earth = 1 / (distance in AU)^2\n\n"
                    "• Twice as far (2 AU): 1/2^2 = 1/4 the light.\n"
                    "• Ten times as far (10 AU): 1/100 the light.\n"
                    "• Venus (0.72 AU): 1/(0.72)^2 = 1.92 -- about twice Earth's sunlight per square meter.\n"
                    "• Mars (1.52 AU): 1/(1.52)^2 = 0.43 -- a little less than half.\n"
                    "• Jupiter (5.2 AU): 1/27, less than 4% of Earth's sunlight."
                ),
            },
            {
                "heading": "Same sunlight, three different worlds",
                "body": (
                    "Here is a twist. Venus' bright clouds reflect about twice as much sunlight as Earth does, and Mars "
                    "reflects only about half as much. So, after reflection, all three planets actually ABSORB roughly the same "
                    "amount of solar energy! Then why are they so different? Their atmospheres:\n\n"
                    "• EARTH: water vapor and CO2 give about 33 C of greenhouse warming -- enough to keep the oceans liquid.\n"
                    "• MARS: thin air, only about 2 C of warming.\n"
                    "• VENUS: a massive CO2 atmosphere, about 510 C of warming!\n\n"
                    "So Mars is much colder, and Venus much hotter, than Earth would be in their orbits. To judge whether a "
                    "planet is habitable you need to know its ATMOSPHERE as well as its distance."
                ),
                "infographic": "greenhouse_numbers",
            },
            {
                "heading": "Different stars, different zones",
                "body": (
                    "Stars come in many types. Hot, bright, bluish stars have habitable zones far out; dim, cool, reddish "
                    "stars have them close in. Astronomers label stars by letters: our Sun is a G-TYPE star; slightly cooler "
                    "ones are K-TYPE; the coolest, dimmest common stars are M-TYPE, or RED DWARFS.\n\n"
                    "• Around red dwarfs, the habitable zone is 3 to 30 times closer than around Sun-like stars.\n"
                    "• Red dwarfs are by far the most common stars in the Galaxy, and they live the longest, so their planets "
                    "matter a lot -- though they have some downsides for life (they can blast their planets with flares, and "
                    "their close-in planets are probably tidally locked).\n\n"
                    "EXAMPLE: PROXIMA CENTAURI, the nearest star to the Sun (an M dwarf 4.2 light-years away), has a planet at "
                    "least 1.3 times Earth's mass (announced in 2016, found by the Doppler method). It orbits in about 11 days "
                    "at just 0.05 AU, which may place it in its star's habitable zone -- but whether it is actually friendly to "
                    "life is hotly debated."
                ),
            },
            {
                "heading": "Tidal locking and habitability",
                "body": (
                    "Planets in close orbits -- like those in red dwarfs' habitable zones -- are often tidally locked: one side "
                    "always faces the star. That gives them a side of endless day and a side of endless night. The day side "
                    "could overheat and the night side could freeze, and the planet's water might all freeze out on the dark "
                    "side.\n\n"
                    "But a thick atmosphere and oceans can carry heat around the planet. Some scientists think such a world "
                    "could still be habitable, perhaps in a ring of permanent twilight between day and night. This is one of "
                    "the big open questions about planets like Proxima Centauri b."
                ),
            },
            {
                "heading": "Habitable zones on the move",
                "body": (
                    "Stars like the Sun slowly get brighter during their lives, so their habitable zones creep outward over "
                    "time. The Sun is at least 30% brighter than it was 4 billion years ago. That means:\n"
                    "• Venus was once inside the habitable zone, and may have had oceans.\n"
                    "• Young Earth received too little sunlight to stay unfrozen with today's atmosphere -- yet rocks show it "
                    "had liquid water billions of years ago (probably a thicker greenhouse blanket helped). This is called the "
                    "FAINT YOUNG SUN puzzle.\n\n"
                    "The CONTINUOUSLY HABITABLE ZONE is the range of orbits that stay inside the habitable zone for the star's "
                    "whole life -- much narrower than the habitable zone at any one moment."
                ),
            },
            {
                "heading": "In the zone isn't enough -- and how many Earths?",
                "body": (
                    "Being in the habitable zone is no guarantee of life, or even of water. Venus today has almost no water, so "
                    "even if we moved it into a 'just right' orbit, it still couldn't support life like ours. 'Habitable zone' "
                    "means 'liquid water COULD exist on the surface', not 'something lives there'.\n\n"
                    "How many Earth-like planets might there be?\n"
                    "• Nearly 300 known planets and candidates orbit in their stars' habitable zones, and more than 10% of "
                    "those are roughly Earth-size.\n"
                    "• More than 40% of stars may have at least one Earth-size planet in their habitable zone.\n"
                    "• Most Sun-like stars host at least one planet, and multi-planet systems are common.\n\n"
                    "Only a few candidates truly resemble Earth. Does an Earth twin need exactly Earth's size? Probably not. "
                    "Does it need a Sun-like star, or could K- and M-type stars work? We don't know yet. Most astronomers think "
                    "the single most important feature of an 'Earth analog' is orbiting in the habitable zone, where liquid "
                    "surface water is possible. New telescopes may soon test these planets' air for gases made by life."
                ),
            },
        ],
        "word_bank": [
            ("Habitable", "Able to support life -- for life as we know it: liquid water, the right elements and energy."),
            ("Solvent", "A liquid that other substances dissolve in, so they can mix and react. For life on Earth, it's water."),
            ("CHNOPS", "The six main elements of life: carbon, hydrogen, nitrogen, oxygen, phosphorus, sulfur."),
            ("Bond", "A connection that holds atoms together in a molecule."),
            ("Molecule", "Two or more atoms joined together, like H2O (water)."),
            ("Habitable zone", "The range of distances from a star where a planet's surface could keep liquid water."),
            ("Goldilocks zone", "A nickname for the habitable zone -- not too hot, not too cold."),
            ("Radiation budget", "The balance between the energy a planet absorbs from its star and the energy it gives off."),
            ("Albedo", "How much light a planet reflects. Bright clouds and ice have a high albedo."),
            ("Inverse-square law", "Light (or gravity) gets weaker with the square of distance: twice as far = 1/4 as much."),
            ("G-type star", "A yellow star like the Sun."),
            ("K-type star", "An orange star, a bit cooler and dimmer than the Sun."),
            ("Red dwarf", "A small, cool, dim M-type star -- the most common kind of star in the Galaxy."),
            ("Flare", "A sudden, powerful burst of energy from a star's surface."),
            ("Faint young Sun puzzle", "The mystery of how early Earth stayed warm enough for liquid water when the young Sun was dimmer."),
            ("Continuously habitable zone", "Orbits that stay inside the habitable zone for the star's entire life."),
            ("Earth analog", "A planet that is similar to Earth -- an 'Earth twin'."),
        ],
        "key_facts": [
            "Life needs: liquid water (solvent), CHNOPS elements (carbon forms 4 bonds), and energy (sunlight or chemical).",
            "HZ = distances where surface liquid water could exist. Depends on star, distance, albedo, greenhouse, heat transport.",
            "Inverse-square: light = 1/d^2. Venus gets 1.92x, Mars 0.43x Earth's sunlight per square meter.",
            "Greenhouse warming: Earth ~33 C, Mars ~2 C, Venus ~510 C.",
            "M-dwarf HZ is 3-30x closer than for G-type stars; M dwarfs are the most common, longest-lived stars.",
            "Proxima Centauri b: >=1.3 Earth masses, 11-day orbit, 0.05 AU, announced 2016; star 4.2 ly away.",
            "Sun 30%+ brighter than 4 billion years ago -> HZ moves outward; continuously habitable zone is narrower.",
            "~300 HZ planets/candidates, >10% Earth-size; >40% of stars may have an Earth-size HZ planet.",
        ],
        "quick_check": [
            ("What three things does life as we know it need?", "Liquid water, the right elements (CHNOPS, especially carbon) and a source of energy."),
            ("A planet orbits at 3 AU from a Sun-like star. How much sunlight does it get compared with Earth?", "1/3^2 = 1/9 as much per square meter."),
            ("Venus gets about twice Earth's sunlight, so why is it 'only' as warm as it is because of its atmosphere?", "Its clouds reflect about twice as much light, so it absorbs about the same energy as Earth; its huge CO2 greenhouse (~510 C) makes it so hot."),
            ("Why are red dwarf habitable-zone planets often tidally locked?", "Their habitable zones are very close to the star, and close planets get tidally locked."),
            ("Is a planet in the habitable zone guaranteed to have life?", "No -- it only means liquid water could exist on its surface. Venus-like planets may have no water at all."),
            ("Why does the Sun's habitable zone move over time?", "The Sun slowly brightens (at least 30% in 4 billion years), pushing the zone outward."),
        ],
        "cards": [
            {
                "term": "Habitable environment",
                "badge": ("W+E+R", "needs", GREEN),
                "analogy": "A working kitchen: you need water, ingredients and a way to turn on the stove.",
                "explanation": "Life as we know it needs liquid water (a solvent), the elements of life (CHNOPS) and energy (sunlight or chemical). Curiosity showed ancient Gale crater had all three.",
                "why": "The core definition for the whole 2027 theme.",
            },
            {
                "term": "CHNOPS & carbon",
                "badge": ("CHNOPS", "elements", GREEN),
                "analogy": "Carbon is the LEGO brick with four connectors, so it can build almost anything.",
                "explanation": "Carbon, hydrogen, nitrogen, oxygen, phosphorus, sulfur. Carbon forms four bonds, making endless big molecules.",
                "why": "Know the six elements and why carbon is special.",
            },
            {
                "term": "Habitable zone",
                "badge": ("HZ", "Goldilocks", GREEN),
                "analogy": "Around a campfire: too close you roast, too far you freeze, in between is just right.",
                "explanation": "Distances where a planet's surface could keep liquid water. Depends on the star's light, distance, reflection, greenhouse effect and heat transport.",
                "why": "THE key concept for habitability beyond the Solar System.",
            },
            {
                "term": "Inverse-square law",
                "badge": ("1/d²", "light", GOLD),
                "analogy": "Spray paint from twice as far covers 4 times the area, so each spot gets 1/4 the paint.",
                "explanation": "Light per square meter = 1/d^2. Venus (0.72 AU) gets 1.92x Earth's; Mars (1.52 AU) gets 0.43x.",
                "why": "A go-to calculation.",
            },
            {
                "term": "Same sunlight, different worlds",
                "badge": ("2/33/510", "°C", RED),
                "analogy": "Three people with the same paycheck: one saves nothing (Mars), one saves sensibly (Earth), one hoards it all (Venus).",
                "explanation": "After reflection, Venus, Earth and Mars absorb similar energy. Greenhouse warming makes the difference: Mars ~2 C, Earth ~33 C, Venus ~510 C.",
                "why": "Habitability needs the atmosphere AND the distance.",
            },
            {
                "term": "Red dwarf habitable zones",
                "badge": ("M", "3-30x closer", "#ff6b4a"),
                "analogy": "A small candle's warm circle is tiny; a bonfire's is huge.",
                "explanation": "M dwarfs' HZs are 3-30x closer than the Sun's. They're the most common, longest-lived stars, but flares and tidal locking are concerns.",
                "why": "Most nearby HZ planets orbit red dwarfs.",
            },
            {
                "term": "Proxima Centauri b",
                "badge": ("4.2", "light-yrs", "#ff6b4a"),
                "analogy": "Our nearest neighbor star has a planet huddled close, like hands warming at a tiny heater.",
                "explanation": "At least 1.3 Earth masses, 11-day orbit at 0.05 AU, around the nearest star (M dwarf, 4.2 ly). Announced 2016. Maybe in the HZ; habitability debated.",
                "why": "The nearest potentially habitable exoplanet.",
            },
            {
                "term": "Moving & continuous HZ",
                "badge": ("+30%", "brighter Sun", SUN),
                "analogy": "As a campfire grows, the comfy spot keeps moving farther away.",
                "explanation": "Sun-like stars brighten, so the HZ moves outward (Venus was once in it). The continuously habitable zone stays habitable for the star's whole life -- much narrower.",
                "why": "Explains the faint young Sun puzzle.",
            },
            {
                "term": "HZ isn't a guarantee",
                "badge": ("HZ ≠", "life", RED),
                "analogy": "A house in a nice neighborhood doesn't help if it has no plumbing.",
                "explanation": "The HZ means liquid water COULD exist. Venus has almost no water, so it would fail even in a perfect orbit. ~300 HZ planets/candidates are known.",
                "why": "A common trick question.",
            },
        ],
    },
    # ------------------------------------------------------------------ 18
    {
        "unit": 5,
        "name": "Solar System: Astrobiology -- Searching for Life",
        "description": "The science of life in the universe: chemical evolution and star stuff, the Copernican principle, the Fermi paradox, life's building blocks in space, Miller-Urey and hydrothermal vents, the RNA world, and biosignatures we could spot on distant planets.",
        "goals": [
            "Define astrobiology and the Copernican principle.",
            "Explain the Fermi paradox and some possible answers.",
            "Describe where life's building blocks have been found in space.",
            "Explain the Miller-Urey experiment and the RNA world idea.",
            "Name biosignatures we could look for on exoplanets.",
        ],
        "sections": [
            {
                "heading": "What is astrobiology?",
                "body": (
                    "ASTROBIOLOGY (also called exobiology or bioastronomy) is the science of life in the universe: how it "
                    "began, how it changes, where else it might exist, and what its future is. It is a team sport -- "
                    "astronomers, planetary scientists, chemists, geologists and biologists all work on it together. "
                    "Astrobiologists study how life began on Earth, why Earth's life is so adaptable, which other worlds might "
                    "be habitable, and how to actually search for life there."
                ),
            },
            {
                "heading": "The chemical evolution of the universe",
                "body": (
                    "After the Big Bang, about 14 billion years ago, the universe held almost only hydrogen and helium. Stars "
                    "then forged the heavier elements -- iron, silicon, magnesium and oxygen for planets, and carbon, nitrogen "
                    "and oxygen for life. In space, these elements combined into compounds, including ORGANIC MOLECULES "
                    "(molecules containing carbon) and HYDROCARBONS (only hydrogen and carbon), the basis of our biochemistry.\n\n"
                    "About 5 billion years ago a cloud collapsed into the Sun, planets and comets. The third planet cooled "
                    "enough to collect liquid water, and comets (like Hyakutake, seen in 1996) can deliver water and organic "
                    "chemicals. Eventually, molecules formed that could COPY THEMSELVES (REPLICATE) -- the key first step for "
                    "life. Billions of years of evolution followed, sometimes reset by impacts, producing creatures who can "
                    "wonder about their own origins. This long chain of events is the CHEMICAL EVOLUTION of the universe."
                ),
            },
            {
                "heading": "The Copernican principle and the Fermi paradox",
                "body": (
                    "Every time humans claimed Earth was special, we turned out to be wrong. Copernicus and Galileo showed Earth "
                    "isn't the center of the Solar System. The Sun is an ordinary star, halfway through its life like billions "
                    "of others, and our spot in the Milky Way isn't special either. Planets form naturally whenever stars "
                    "form, and there are probably billions of 'exo-Earths' in our Galaxy. The idea that there is nothing "
                    "special about our place in the universe is the COPERNICAN PRINCIPLE. Applied to life, it suggests life "
                    "probably exists elsewhere -- most scientists would be surprised if it didn't. The real open question is "
                    "whether carbon-based biochemistry is common or rare. Finding even one example of life that started "
                    "separately from ours -- say, on Europa -- would help answer it.\n\n"
                    "THE FERMI PARADOX: if life and intelligence are common, civilizations around older stars could have had a "
                    "billion-year head start and spread probes or messages across the Galaxy. Physicist Enrico Fermi asked: "
                    "'So where is everybody?' A PARADOX is a puzzle where two reasonable ideas seem to clash. Possible answers:\n"
                    "• Life is common, but intelligence or technology is rare.\n"
                    "• A galactic network will form, but hasn't had time yet.\n"
                    "• Their signals are all around us, but we can't detect them.\n"
                    "• Advanced species deliberately leave young civilizations like ours alone.\n"
                    "• Civilizations tend to destroy themselves.\n"
                    "Nobody knows the answer yet!"
                ),
            },
            {
                "heading": "Life's ingredients are everywhere",
                "body": (
                    "We haven't found clear evidence of life beyond Earth yet, but its building blocks are all over space:\n\n"
                    "• METEORITES contain AMINO ACIDS (the building blocks of PROTEINS, which build our tissues and do the "
                    "cell's work) and SUGARS whose structure shows they came from space.\n"
                    "• COMETS' gas and dust contain organic molecules.\n"
                    "• Radio astronomers have found more than 100 kinds of molecules in giant gas-and-dust clouds between the "
                    "stars, including formaldehyde and alcohol -- mostly in dusty regions where new stars and planets form.\n"
                    "• JWST has found benzene and acetic acid in planet-forming disks."
                ),
                "infographic": "life_recipe",
            },
            {
                "heading": "Making life's building blocks in a lab",
                "body": (
                    "Starting in the early 1950s, STANLEY MILLER and HAROLD UREY at the University of Chicago filled a flask "
                    "with gases meant to copy early Earth's air, added water, and zapped it with electric sparks like "
                    "lightning. They produced building blocks of proteins and NUCLEIC ACIDS (like DNA) -- the 'primordial soup' "
                    "experiment.\n\n"
                    "The catch: their best results needed hydrogen-rich ('reducing') gases like ammonia and methane, but early "
                    "Earth's air was probably mostly carbon dioxide, like Venus and Mars today.\n\n"
                    "Another candidate kitchen: HYDROTHERMAL VENTS, where seawater gets superheated as it circulates through hot "
                    "rock under the seafloor. They could make organic compounds without needing a special atmosphere, and "
                    "today whole ecosystems live around them in total darkness -- a model for life in Europa's or Enceladus' "
                    "oceans. Probably both Earth and space contributed organic molecules. Life might even have been 'seeded' "
                    "from elsewhere -- but that only moves the question of how it started somewhere else."
                ),
            },
            {
                "heading": "From chemistry to biology: the RNA world",
                "body": (
                    "Even the simplest life needs two abilities: a way to get ENERGY from its surroundings, and a way to STORE "
                    "INFORMATION and copy itself. In modern cells, PROTEINS do the chemical work and DNA (deoxyribonucleic acid) "
                    "stores the instructions. But proteins are needed to build DNA, and DNA is needed to build proteins -- a "
                    "'chicken-and-egg' problem!\n\n"
                    "One solution is RNA (ribonucleic acid), a molecule that can both store information and do some chemical "
                    "work. Many scientists now favor an early 'RNA WORLD', where RNA did both jobs before DNA and proteins took "
                    "over.\n\n"
                    "Timeline reminder: the heavy bombardment (3.8-4.1 billion years ago) may have sterilized Earth's surface; "
                    "there are fossil microbes in 3.5-billion-year-old rocks and possible signs of life back to 3.8 billion "
                    "years. The most important invention after life itself was PHOTOSYNTHESIS, working by at least 3.4 billion "
                    "years ago; it filled the air with oxygen (~2.4 billion years ago) and built the ozone layer. If life "
                    "starts whenever conditions are right, finding a second example nearby would mean the universe is probably "
                    "full of life."
                ),
            },
            {
                "heading": "Biosignatures: spotting life light-years away",
                "body": (
                    "We can't send probes to other stars, so we must read the LIGHT from distant planets. From about 6 billion "
                    "km away, Voyager 1 photographed Earth as the 'PALE BLUE DOT' -- less than one pixel. Could a speck like "
                    "that reveal life? A BIOSIGNATURE (or BIOMARKER) is a sign of life that we could detect from far away.\n\n"
                    "• We need a BIOSPHERE (all the life on a planet) big enough to change the whole planet. Earth is the only "
                    "world in our Solar System where life visibly changes the air and the reflected light. Life hidden under "
                    "Mars' surface or under icy moons' crusts probably couldn't be seen from far away.\n"
                    "• Photosynthetic life needs SURFACE water and sunlight -- that's why the search focuses on surface liquid "
                    "water in habitable zones.\n"
                    "• OXYGEN: more than 20% of Earth's air is oxygen made by photosynthesis -- very hard to explain without "
                    "life.\n"
                    "• GAS COMBINATIONS: methane or nitrous oxide found TOGETHER with oxygen are strong hints, because they "
                    "destroy each other and must keep being refilled.\n"
                    "• COLOR: plants make Earth look greener in visible light and reflect extra near-infrared light.\n"
                    "• We can now measure the atmospheric spectra of some exoplanets, for example during transits.\n\n"
                    "The plan: find roughly Earth-size planets in habitable zones and look for gases or colors that are hard "
                    "to explain without life. Space telescopes that can do this take many years to plan, build and launch -- "
                    "but it may be one of the greatest searches humans ever attempt."
                ),
                "infographic": "biomarkers",
            },
        ],
        "word_bank": [
            ("Astrobiology", "The science of life in the universe: its origin, evolution, where it could be, and its future."),
            ("Organic molecule", "A molecule containing carbon, like sugars, fats and amino acids."),
            ("Hydrocarbon", "A molecule made only of hydrogen and carbon, like methane."),
            ("Replicate", "To make a copy of itself."),
            ("Chemical evolution", "The long chain of events from simple atoms after the Big Bang to the complex molecules of life."),
            ("Copernican principle", "The idea that there is nothing special about Earth's place in the universe."),
            ("Fermi paradox", "The puzzle: if intelligent life is common, why haven't we seen any sign of it?"),
            ("Paradox", "A puzzle where two reasonable ideas seem to contradict each other."),
            ("Amino acids", "Small molecules that link together to make proteins."),
            ("Protein", "A large molecule that builds body parts and does the chemical work in cells."),
            ("Nucleic acids", "DNA and RNA -- molecules that store and carry genetic information."),
            ("Primordial soup", "The idea of an early ocean full of organic chemicals where life might have started."),
            ("Reducing gases", "Hydrogen-rich gases like ammonia and methane."),
            ("Hydrothermal vent", "A hot spring on the seafloor; it might have helped make life's first chemicals."),
            ("DNA", "Deoxyribonucleic acid -- the molecule that stores the instructions for life."),
            ("RNA", "Ribonucleic acid -- a molecule that can store information AND do some chemical work."),
            ("RNA world", "The idea that early life used RNA for both storing information and doing chemistry, before DNA and proteins."),
            ("Biosignature", "A sign of life, such as a gas in a planet's air, that we could detect from far away. Also called a biomarker."),
            ("Biosphere", "All the living things on a planet, together."),
            ("Nitrous oxide", "A gas (N2O) made by microbes on Earth; with oxygen, it would be a hint of life."),
            ("Pale Blue Dot", "Voyager 1's famous photo of Earth from about 6 billion km away, less than one pixel wide."),
        ],
        "key_facts": [
            "Astrobiology = exobiology = bioastronomy: origin, evolution, distribution and future of life in the universe.",
            "Big Bang ~14 billion years ago: only H and He (and a little Li); stars made the rest.",
            "Copernican principle: Earth's place isn't special. Fermi paradox: 'where is everybody?'",
            "Meteorites contain amino acids and sugars; >100 molecules found in interstellar clouds (formaldehyde, alcohol).",
            "Miller-Urey (early 1950s, University of Chicago): sparks + gases -> building blocks; but needed reducing gases.",
            "Hydrothermal vents: organics without a special atmosphere; ecosystems without sunlight.",
            "RNA world solves the DNA/protein chicken-and-egg problem.",
            "Biosignatures: lots of O2; methane or N2O together with O2; green color/near-infrared; measured via spectra. Pale Blue Dot: Voyager 1, ~6 billion km.",
        ],
        "quick_check": [
            ("What is the Copernican principle?", "The idea that there is nothing special about Earth's place in the universe -- so life may exist elsewhere."),
            ("Give two possible answers to the Fermi paradox.", "Any two of: intelligence is rare; a galactic network hasn't formed yet; we can't detect their signals; they leave us alone on purpose; civilizations destroy themselves."),
            ("What did the Miller-Urey experiment show, and what was its weakness?", "Sparks in a mix of gases made building blocks of life; but it used hydrogen-rich gases, while early Earth's air was probably mostly CO2."),
            ("Why is the 'RNA world' idea popular?", "RNA can both store information and do chemical work, solving the problem that DNA and proteins each need the other."),
            ("Why is oxygen together with methane a good biosignature?", "They react and destroy each other, so finding both means something (probably life) keeps making them."),
        ],
        "cards": [
            {
                "term": "Astrobiology",
                "badge": ("ASTRO", "+ BIO", GREEN),
                "analogy": "A team sport where astronomers, chemists, geologists and biologists all play together.",
                "explanation": "The study of life's origin, evolution, distribution and future in the universe (also exobiology, bioastronomy).",
                "why": "The field the 2027 theme belongs to.",
            },
            {
                "term": "Chemical evolution",
                "badge": ("STARS", "made us", SUN),
                "analogy": "Stars are cosmic kitchens that cooked every ingredient in your body except hydrogen.",
                "explanation": "Big Bang -> H and He; stars made carbon, oxygen, iron and more; these formed organic molecules in space and on planets, leading to self-copying molecules and life.",
                "why": "Explains where life's ingredients came from.",
            },
            {
                "term": "Copernican principle",
                "badge": ("NOT", "special", BLUE),
                "analogy": "Your town is one of millions of towns -- other towns probably have kids like you too.",
                "explanation": "Earth isn't the center; the Sun is ordinary; our place in the Galaxy is ordinary. So life probably isn't unique to Earth.",
                "why": "Common in astrobiology essay questions.",
            },
            {
                "term": "Fermi paradox",
                "badge": ("WHERE?", "are they", PURPLE),
                "analogy": "If the Galaxy is a huge party, why is our corner so quiet?",
                "explanation": "If intelligent life is common, where is it? Maybe intelligence is rare, we can't detect them, they ignore us, or civilizations self-destruct.",
                "why": "A classic 'list possible explanations' question.",
            },
            {
                "term": "Building blocks in space",
                "badge": ("100+", "molecules", ICE),
                "analogy": "Space is a giant pantry already stocked with life's basic ingredients.",
                "explanation": "Meteorites carry amino acids and sugars; comets carry organics; 100+ molecules found in interstellar clouds; JWST sees organics in disks.",
                "why": "The ingredients for life are likely everywhere.",
            },
            {
                "term": "Miller-Urey & vents",
                "badge": ("1950s", "lab life", GOLD),
                "analogy": "Making 'primordial soup' in a jar with lightning sparks.",
                "explanation": "Miller and Urey made building blocks from gases and sparks, but needed reducing gases. Hydrothermal vents could make organics without that.",
                "why": "Know the result AND the limitation.",
            },
            {
                "term": "RNA world",
                "badge": ("RNA", "first?", PURPLE),
                "analogy": "Chicken or egg? RNA may be the 'egg' that does both jobs.",
                "explanation": "Proteins need DNA and DNA needs proteins. RNA can store information and do chemistry, so early life may have used RNA alone.",
                "why": "A key open question about life's origin.",
            },
            {
                "term": "Biosignatures",
                "badge": ("O₂+CH₄", "signs", GREEN),
                "analogy": "Smelling cookies from outside a house -- you can't see the baker, but someone's baking.",
                "explanation": "Planet-wide signs of life seen in light: lots of oxygen, methane or nitrous oxide together with oxygen, green color and near-infrared glow from plants.",
                "why": "How we'll actually search for life beyond the Solar System.",
            },
        ],
    },
]
