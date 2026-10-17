"""Learning paths: Earth & Space Science events (Solar System is not here --
its chapters live in content/solar_system and are left untouched)."""

from app.content.learning_paths._base import lesson

DYNAMIC_PLANET = [
    lesson(
        "Hydrologic Cycle Components & Fluxes",
        "Where Earth's water is stored and how it moves between stores.",
        "RESERVOIR -- a place water is stored (ocean, ice, groundwater, lakes, atmosphere). FLUX -- "
        "the rate water moves between reservoirs. RESIDENCE TIME -- average time water stays in a "
        "reservoir.",
        "Water cycles endlessly: evaporation and transpiration lift it into the air, condensation "
        "makes clouds, precipitation brings it down, and runoff and infiltration carry it back.",
        "Storage (approximate): oceans about 97%; ice and snow about 2%; groundwater under 1%; lakes, "
        "rivers, soil moisture, and the atmosphere are tiny fractions. Of fresh water, about two-thirds "
        "is ice and most of the rest is groundwater. Processes: evaporation, transpiration "
        "(together evapotranspiration), sublimation, condensation, precipitation, interception, "
        "infiltration, percolation, runoff, baseflow. Residence time = storage / flux: about 9 days "
        "in the atmosphere, thousands of years in deep groundwater and the oceans.",
        "A lake holds 1,000 units of water with an outflow of 50 units/year. Residence time? (1,000 / "
        "50 = 20 years.)",
    ),
    lesson(
        "Water Budgets & the Critical Zone",
        "Accounting for water inputs and outputs, and the thin layer where water, rock, soil, and life "
        "meet.",
        "WATER BUDGET -- inputs = outputs + change in storage. CRITICAL ZONE -- the layer from the tops "
        "of trees down to the bottom of groundwater. EVAPOTRANSPIRATION (ET).",
        "A water budget works like a bank account. Precipitation is the deposit; runoff, ET, and "
        "groundwater outflow are withdrawals; storage is the balance.",
        "Basin budget: P = Q + ET + change in S (P precipitation, Q streamflow, S storage of soil water "
        "and groundwater). Over long periods change in S is about 0, so Q is about P - ET. Potential ET "
        "is what would evaporate with unlimited water; actual ET is limited by supply. Soil moisture "
        "surplus feeds runoff and recharge; deficits stress plants. The critical zone controls "
        "weathering, soil formation, filtering, and how fast rain becomes streamflow. Its study uses "
        "observatories that measure all fluxes together.",
        "A basin gets 900 mm of rain per year and loses 600 mm to ET, with no storage change. Runoff? "
        "(300 mm.)",
    ),
    lesson(
        "Climatic Controls on Fresh Water",
        "Why some places are wet and others dry.",
        "HADLEY CELL -- rising air near the equator, sinking near 30 degrees. RAIN SHADOW -- the dry "
        "side of a mountain range. OROGRAPHIC LIFT -- air forced up over mountains.",
        "Rising air cools and drops rain; sinking air warms and dries. So the equator (rising air) is "
        "wet, about 30 degrees N and S (sinking air) is dry -- the great deserts -- and mountains make "
        "wet windward and dry leeward sides.",
        "Global circulation: Hadley, Ferrel, and polar cells; the ITCZ migrates with the seasons, "
        "creating wet and dry seasons and monsoons. Continentality: interiors are drier and more "
        "extreme. Cold ocean currents (e.g. off Chile, Namibia) stabilize air and make coastal "
        "deserts. Climate patterns such as El Nino/La Nina shift rainfall. Snowpack and glaciers act "
        "as seasonal water storage, releasing melt in spring and summer. Warming shifts precipitation "
        "from snow to rain and moves melt earlier.",
        "Why is the eastern side of the Sierra Nevada much drier than the western side? (Rain shadow "
        "-- moist Pacific air drops its rain on the windward west side.)",
    ),
    lesson(
        "Drainage Basins & Stream Networks",
        "How land is divided into watersheds and how streams branch.",
        "DRAINAGE BASIN (WATERSHED) -- all the land draining to one outlet. DIVIDE -- the high ground "
        "between basins. STREAM ORDER -- a ranking of stream size (Strahler).",
        "Every drop of rain falls in some watershed and flows to its outlet. Streams join like tree "
        "branches, getting bigger downstream.",
        "Strahler order: headwater streams are order 1; two order-1 streams joining make order 2; "
        "joining a lower-order stream doesn't raise the order. Drainage patterns reflect geology: "
        "dendritic (uniform rock), trellis (folded ridges), radial (from a peak such as a volcano), "
        "rectangular (jointed or faulted rock), centripetal (into a basin). Drainage density = total "
        "stream length / basin area (high on impermeable or sparsely vegetated ground). Continental "
        "divides send water to different oceans. Basin shape and size control how quickly floods "
        "peak.",
        "Two second-order streams join. What order is the new stream? (Third order.)",
    ),
    lesson(
        "Fluvial Sediment Properties & Transport",
        "Sediment sizes and how rivers move them.",
        "BED LOAD -- grains rolling, sliding, and bouncing (saltation) along the bed. SUSPENDED LOAD "
        "-- fine grains carried in the flow. DISSOLVED LOAD -- ions in solution. COMPETENCE -- the "
        "largest grain a stream can move. CAPACITY -- the total load it can carry.",
        "Faster water moves bigger grains. As a river slows, it drops the largest grains first -- so "
        "sediment sorts by size.",
        "Wentworth sizes: clay < 1/256 mm, silt 1/256-1/16, sand 1/16-2, gravel 2+ (granules, "
        "pebbles, cobbles, boulders). The Hjulstrom curve shows erosion, transport, and deposition "
        "velocities by grain size -- note that clay needs HIGH velocity to erode (cohesion) but "
        "settles only in nearly still water. Rounding and sorting increase with transport distance. "
        "Competence rises steeply with velocity (roughly velocity squared or more), which is why "
        "floods move boulders.",
        "On the Hjulstrom curve, which size is easiest to erode? (Medium sand, around 0.5 mm.)",
    ),
    lesson(
        "Channel Types, Sinuosity & Planform",
        "Straight, meandering, braided, and anastomosing channels.",
        "SINUOSITY -- channel length / straight-line valley length. MEANDER -- a looping bend. "
        "BRAIDED -- many shallow channels split by bars. THALWEG -- the line of deepest flow.",
        "Rivers take different shapes depending on slope, sediment load, and bank strength. Gentle "
        "slopes with fine sediment and firm banks tend to meander; steep slopes with lots of coarse "
        "sediment tend to braid.",
        "Sinuosity: about 1.0-1.3 straight to sinuous; above 1.5 meandering. Meanders erode on the "
        "outside of bends (cut banks) and deposit on the inside (point bars), migrating over time; "
        "cutoffs leave oxbow lakes. Braided channels form with abundant coarse load and variable flow "
        "(glacial outwash). Anastomosing channels are stable, multi-channel systems with vegetated "
        "islands on low slopes. Channel features: pools and riffles, the thalweg swinging to the "
        "outside of bends.",
        "A river is 15 km long in a valley 10 km long. Sinuosity? (1.5 -- meandering.)",
    ),
    lesson(
        "Fluvial Geomorphology & Landforms",
        "The landforms rivers carve and build.",
        "BASE LEVEL -- the lowest level a river can erode to (ultimately sea level). FLOODPLAIN -- flat "
        "land built by floods. TERRACE -- an old, abandoned floodplain. DELTA -- a sediment deposit "
        "where a river enters standing water.",
        "Rivers cut down in their upper reaches and build up in their lower reaches. Changes in base "
        "level or uplift make them cut down again.",
        "Erosional forms: V-shaped valleys, waterfalls and knickpoints (they migrate upstream), "
        "potholes, canyons, entrenched meanders. Depositional forms: floodplains, natural levees "
        "(coarse sediment dropped beside the channel in floods), backswamps, point bars, alluvial fans "
        "(at mountain fronts), deltas (arcuate like the Nile, bird's-foot like the Mississippi, "
        "cuspate). A graded stream balances erosion and deposition. Base-level fall (or uplift) -> "
        "incision -> terraces. Stream piracy (capture) diverts one stream's headwaters into another.",
        "What landform builds where a mountain stream suddenly reaches a flat valley floor? (An "
        "alluvial fan.)",
    ),
    lesson(
        "Streamflow, Discharge & Hydrographs",
        "Measuring how much water a river carries and how it responds to storms.",
        "DISCHARGE (Q) -- volume per time (m^3/s or cfs). Q = A x v (cross-sectional area x velocity). "
        "HYDROGRAPH -- discharge plotted over time. LAG TIME -- delay between peak rain and peak flow.",
        "After a storm, a river rises, peaks, and falls. How fast and how high depends on the basin: "
        "pavement and steep slopes make a sharp, fast peak; forests and soil make a gentle, delayed "
        "one.",
        "Measure Q by velocity-area (a flow meter at several verticals) or from a rating curve "
        "(stage vs discharge) at a USGS gauge. Hydrograph parts: baseflow (from groundwater), rising "
        "limb, peak, falling (recession) limb. Urbanization: more impervious surface -> less "
        "infiltration -> higher, earlier peaks and lower baseflow. Basin traits that shorten lag time: "
        "small size, steep slopes, high drainage density, saturated or frozen soil, little "
        "vegetation.",
        "A channel is 10 m wide and 2 m deep and flows at 1.5 m/s. Discharge? (10 x 2 x 1.5 = 30 "
        "m^3/s.)",
    ),
    lesson(
        "Floods, Recurrence Intervals & Frequency",
        "How likely a flood of a given size is.",
        "RECURRENCE INTERVAL (RETURN PERIOD) -- average years between floods of a given size. ANNUAL "
        "EXCEEDANCE PROBABILITY -- the chance in any year = 1 / recurrence interval.",
        "A \"100-year flood\" doesn't come once a century on schedule. It has a 1% chance of happening "
        "EVERY year -- you can get two in a row.",
        "Weibull formula: RI = (n + 1) / m, where n = years of record and m = the flood's rank "
        "(largest = 1). Probability = 1 / RI. Chance of at least one 100-year flood in N years = "
        "1 - (0.99)^N (about 26% in 30 years). Plot RI on a log scale to estimate rarer floods (a "
        "flood-frequency curve). Short records and land-use or climate change make estimates "
        "uncertain. Flood types: riverine, flash floods, coastal storm surge, ice jams, dam failure. "
        "FEMA maps the 100-year floodplain for insurance.",
        "With 49 years of record, the 2nd-largest flood has what recurrence interval? ((49 + 1) / 2 = "
        "25 years.)",
    ),
    lesson(
        "Groundwater Systems & Karst",
        "Aquifers, the water table, flow, and landscapes dissolved out of limestone.",
        "POROSITY -- the fraction of rock that is pore space. PERMEABILITY -- how easily water flows "
        "through it. AQUIFER -- rock that stores and transmits useful water. WATER TABLE -- the top of "
        "the saturated zone.",
        "Groundwater fills the spaces in rock and soil below the water table and slowly flows downhill "
        "toward rivers, springs, and wells.",
        "Unconfined aquifers are open to the surface; confined aquifers lie beneath an aquitard (clay) "
        "and can be artesian (water rises in a well above the aquifer top). Darcy's law: Q = K x A x "
        "(dh/dl) -- flow rises with conductivity and hydraulic gradient. Pumping creates a cone of "
        "depression; overpumping lowers the water table, causes subsidence, and draws in salt water "
        "near coasts. Gaining streams receive groundwater; losing streams leak to it. Karst: "
        "carbonic acid dissolves limestone -> caves, sinkholes, disappearing streams, springs, "
        "stalactites and stalagmites. Karst aquifers flow fast and are easily polluted.",
        "Clay has high porosity but makes a poor aquifer. Why? (Its pores are tiny and poorly "
        "connected -- very low permeability.)",
    ),
    lesson(
        "Lakes, Wetlands & Their Hydrology",
        "How lakes form and behave, and why wetlands matter.",
        "THERMAL STRATIFICATION -- layering by temperature (epilimnion, metalimnion/thermocline, "
        "hypolimnion). TURNOVER -- seasonal mixing. WETLAND -- land saturated long enough to support "
        "water-adapted plants and soils.",
        "Lakes layer in summer because warm water floats on cold. In fall (and spring) the layers mix. "
        "Wetlands act like sponges: they store floodwater, filter pollutants, and recharge groundwater.",
        "Lake origins: glacial (kettles, cirques, the Great Lakes), tectonic (rift lakes such as "
        "Baikal and Tanganyika), volcanic (crater lakes), fluvial (oxbows), human-made reservoirs. "
        "Water is densest at about 4 C, so ice floats and deep water stays near 4 C. Trophic state: "
        "oligotrophic (clear, low nutrients) to eutrophic (nutrient-rich, algae, low deep oxygen). "
        "Endorheic lakes have no outlet and become salty (Great Salt Lake). Wetland types: marshes "
        "(grasses), swamps (trees), bogs (acidic, peat, rain-fed), fens (groundwater-fed). Hydroperiod "
        "-- the seasonal pattern of flooding -- defines a wetland.",
        "Why does the Great Salt Lake become saltier over time? (It has no outlet; water leaves only "
        "by evaporation, leaving salts behind.)",
    ),
    lesson(
        "Human Impacts, Water Quality & Monitoring",
        "How people change fresh water and how it is measured and managed.",
        "IMPERVIOUS SURFACE -- pavement and roofs that block infiltration. NONPOINT POLLUTION -- diffuse "
        "runoff. USGS STREAMGAGE -- a station that records stage and discharge.",
        "Dams, cities, farms, and wells all change where water goes and how clean it is. Monitoring "
        "networks tell us what's changing so it can be managed.",
        "Dams trap sediment (starving downstream deltas and beaches), change temperature and flow "
        "timing, and block fish. Channelization speeds floods downstream. Urbanization raises flood "
        "peaks and lowers baseflow. Agriculture adds nitrogen and phosphorus (eutrophication) and "
        "pesticides; irrigation depletes aquifers (the Ogallala). Mining causes acid mine drainage. "
        "Measurements: discharge, temperature, DO, pH, conductivity, turbidity, nutrients, and "
        "biological indicators (macroinvertebrates such as mayflies and stoneflies signal clean "
        "water). Tools: USGS gauges, satellites (GRACE tracks groundwater storage from gravity), and "
        "the Clean Water and Safe Drinking Water Acts.",
        "Stoneflies and mayflies are common in a stream sample. What does that suggest? (Good water "
        "quality -- they are pollution-sensitive.)",
    ),
]

METEOROLOGY = [
    lesson(
        "Atmosphere Basics",
        "Layers, pressure, temperature, and moisture -- the foundation for everything else.",
        "TROPOSPHERE -- the lowest layer, where weather happens. AIR PRESSURE -- the weight of the air "
        "above (about 1013 mb at sea level). DEW POINT -- the temperature where air becomes "
        "saturated. RELATIVE HUMIDITY -- water vapor present vs the maximum possible.",
        "Air gets thinner and (in the troposphere) colder as you go up. Weather happens when air "
        "rises, cools, and its moisture condenses into clouds and rain.",
        "Layers: troposphere (temperature falls ~6.5 C/km), stratosphere (warms with height because "
        "of ozone absorbing UV), mesosphere, thermosphere. Pressure drops about by half every 5.5 km. "
        "Dry adiabatic lapse rate about 9.8 C/km; moist about 6 C/km (latent heat release). When "
        "temperature equals dew point, RH = 100% and clouds or fog form. A large dew point spread "
        "means dry air. Wind blows from high to low pressure, turned by the Coriolis effect (right in "
        "the Northern Hemisphere).",
        "Temperature 30 C, dew point 29 C. Humid or dry? (Very humid -- the dew point is close to the "
        "temperature.)",
    ),
    lesson(
        "Air Masses, Fronts & Large-Scale Circulation",
        "How air masses meet at fronts, and the jet streams that steer storms.",
        "AIR MASS -- a large body of air with similar temperature and moisture. FRONT -- the boundary "
        "between air masses. JET STREAM -- a fast river of wind near the top of the troposphere.",
        "Air masses take on the character of where they formed: cold or warm, dry or moist. When they "
        "collide, the warmer, lighter air is lifted -- that's where storms form.",
        "Types: cP (continental polar, cold and dry), mT (maritime tropical, warm and humid -- Gulf of "
        "Mexico), cT, mP, cA. Cold fronts: steep, fast, narrow bands of thunderstorms, sharp "
        "temperature drop, wind shift. Warm fronts: gentle slope, wide areas of stratus and steady "
        "rain ahead. Stationary and occluded fronts. Drylines separate moist from dry air (key for "
        "Plains tornadoes). Mid-latitude cyclones form along the polar front under jet-stream "
        "divergence. Wind shear, atmospheric rivers (long plumes of moisture), and Rossby waves are "
        "all part of the 2027 list.",
        "Which front usually brings a short burst of thunderstorms and a sharp temperature drop? "
        "(A cold front.)",
    ),
    lesson(
        "Station Models & Surface Maps",
        "Decoding the station-model symbol and reading a surface weather map.",
        "STATION MODEL -- a compact symbol of the weather at one site. ISOBAR -- a line of equal "
        "pressure. WIND BARB -- shows wind direction and speed.",
        "Each station model packs temperature, dew point, pressure, wind, cloud cover, and current "
        "weather around a small circle. Learn the positions once and you can read any of them.",
        "Upper left: temperature (F in the U.S.). Lower left: dew point. Upper right: pressure coded "
        "as the last three digits in tenths of a millibar: add a 10 or 9 in front -- 132 -> 1013.2 "
        "mb, 980 -> 998.0 mb (choose whichever gives a value nearest 1000). Circle fill: cloud cover "
        "in eighths. Wind barb: the shaft points to where wind comes FROM; a full barb = 10 knots, "
        "half = 5, a flag (pennant) = 50. Middle left: present weather symbol. Close isobars = strong "
        "winds. Fronts drawn with triangles (cold, blue) and half-circles (warm, red).",
        "Decode pressure \"045\". (1004.5 mb.)",
    ),
    lesson(
        "METAR Decoding",
        "Reading aviation weather reports.",
        "METAR -- routine hourly airport weather report. SPECI -- a special unscheduled report. "
        "Station ID -- four letters (e.g. KORD).",
        "A METAR is a coded line read left to right: where, when, wind, visibility, weather, clouds, "
        "temperature/dew point, pressure, remarks.",
        "Example: KDEN 121753Z 27015G25KT 10SM -TSRA BKN040CB 22/14 A2992 RMK... -> Denver, 12th day, "
        "1753 UTC; wind from 270 degrees at 15 knots gusting 25; 10 statute miles visibility; light "
        "thunderstorm with rain; broken clouds at 4,000 ft with cumulonimbus; temperature 22 C, dew "
        "point 14 C; altimeter 29.92 inHg. Codes: - light, + heavy, VC vicinity; RA rain, SN snow, "
        "TS thunderstorm, FG fog, BR mist, GR hail, FC funnel cloud. Clouds: FEW, SCT (scattered), "
        "BKN (broken), OVC (overcast), heights in hundreds of feet. M in temperatures means minus "
        "(M05 = -5 C).",
        "Decode \"OVC008\". (Overcast at 800 feet.)",
    ),
    lesson(
        "Doppler Radar Products",
        "Reflectivity, velocity, and correlation coefficient.",
        "REFLECTIVITY (dBZ) -- how much energy precipitation reflects. RADIAL VELOCITY -- motion toward "
        "or away from the radar. CORRELATION COEFFICIENT (CC) -- how similar the targets in a volume "
        "are.",
        "Reflectivity shows WHERE and HOW HARD it's raining. Velocity shows how the air is MOVING. CC "
        "helps tell rain from hail or tornado debris.",
        "Reflectivity: about 20 dBZ light rain, 40 moderate-heavy, 50+ very heavy, 60+ often hail. "
        "Base vs composite reflectivity (composite takes the maximum in each column). Velocity: by "
        "convention green = toward the radar, red = away. A tight pair of strong inbound and outbound "
        "velocities side by side = a rotation couplet (mesocyclone or tornado vortex signature, TVS). "
        "CC near 1 = uniform rain; a drop to under about 0.8 inside a rotation couplet = a debris ball "
        "(tornado lofting debris). Hook echo and bow echo shapes appear on reflectivity. Range folding "
        "and beam height limit what radar sees far away.",
        "On velocity, bright green right next to bright red at the tip of a hook echo suggests what? "
        "(Strong rotation -- a possible tornado.)",
    ),
    lesson(
        "Satellite Imagery",
        "Interpreting visible, infrared, and water vapor images.",
        "VISIBLE -- reflected sunlight (daytime only). INFRARED (IR) -- emitted heat; colder cloud tops "
        "look brighter. WATER VAPOR -- moisture in the mid and upper troposphere.",
        "Visible images look like photos and show texture. IR shows temperature, so it works at night "
        "and tells high, cold clouds from low, warm ones. Water vapor shows moist and dry air flows "
        "even where there are no clouds.",
        "Thick clouds are bright on visible; thin cirrus is faint on visible but bright on IR (cold). "
        "Low fog is bright on visible but gray on IR (similar temperature to the ground). Enhanced IR "
        "color tables highlight very cold tops (strong thunderstorms, overshooting tops). Water vapor "
        "imagery reveals jet streams, troughs, and dry slots. GOES satellites are geostationary "
        "(continuous view of one hemisphere); polar orbiters give higher resolution but pass "
        "periodically. Watch for lines of towering cumulus along fronts and the spiral of a "
        "hurricane with a clear eye.",
        "A cloud is bright on IR but barely visible on visible imagery. What is it likely to be? "
        "(Thin, high cirrus.)",
    ),
    lesson(
        "Stuve & Skew-T Diagrams",
        "Reading soundings for stability, wind shear, and cloud formation.",
        "SOUNDING -- a vertical profile from a weather balloon (radiosonde). LCL -- lifting "
        "condensation level, where rising air saturates (cloud base). CAPE -- convective available "
        "potential energy, the fuel for updrafts.",
        "A sounding plots temperature and dew point against height. Compare a rising air parcel to "
        "the surrounding air: if the parcel is warmer, it keeps rising -- unstable, stormy.",
        "Stuve diagrams use straight vertical temperature lines; Skew-T diagrams tilt them about 45 "
        "degrees so lapse rates are easier to read (Skew-T, LCL, and CAPE are State/Nationals only). "
        "Lift a parcel along the dry adiabat to the LCL, then the moist adiabat. Where the parcel "
        "becomes warmer than the environment: level of free convection; positive area above it = "
        "CAPE (over ~2,500 J/kg = strong instability); negative area below = CIN (a cap). Temperature "
        "and dew point lines close together = moist layer (clouds). Wind barbs on the side show shear "
        "-- veering winds with height suggest warm-air advection and favor rotating storms. "
        "Inversions (temperature rising with height) are stable.",
        "On a sounding, the temperature rises with height between 1 and 2 km. Stable or unstable "
        "layer? (Stable -- an inversion.)",
    ),
    lesson(
        "Thunderstorm Types & Life Cycles",
        "Single cells, multicells, squall lines, supercells, and MCCs.",
        "UPDRAFT -- rising air. DOWNDRAFT -- sinking air. SUPERCELL -- a storm with a rotating updraft "
        "(mesocyclone). SEVERE THUNDERSTORM (NWS) -- hail 1 inch or larger, winds 58 mph or more, or a "
        "tornado.",
        "Thunderstorms need moisture, instability, and lift. Wind shear decides how organized and "
        "long-lived they become.",
        "Single-cell life cycle: cumulus (updraft only), mature (updraft and downdraft, heaviest rain, "
        "lightning, hail), dissipating (downdraft only), about 30-60 minutes. Multicell clusters keep "
        "regenerating along the gust front. Squall lines and bow echoes produce straight-line winds; "
        "derechos are long-lived, widespread windstorms. Downbursts and microbursts (under 4 km) are "
        "dangerous for aircraft. Supercells form with strong shear: rotating updraft, hook echo, wall "
        "cloud, and most strong tornadoes and giant hail. Mesoscale convective complexes (MCCs) are "
        "huge overnight clusters. Lightning: charge separates as ice and graupel collide; thunder is "
        "the shock wave from rapidly heated air.",
        "Which storm type produces most violent tornadoes? (Supercells.)",
    ),
    lesson(
        "Tornadoes",
        "How tornadoes form, how they are rated, and how they're detected.",
        "TORNADO -- a rotating column of air in contact with the ground under a cumuliform cloud. EF "
        "SCALE -- Enhanced Fujita scale (EF0-EF5) rated from damage. WALL CLOUD -- a lowering under "
        "the rain-free base of a supercell.",
        "Most strong tornadoes come from supercells. Wind shear creates horizontal spin; the updraft "
        "tilts it upright; the storm's downdrafts help pull rotation down to the ground.",
        "EF scale (3-second gust estimates): EF0 65-85 mph, EF1 86-110, EF2 111-135, EF3 136-165, "
        "EF4 166-200, EF5 over 200. It's assigned AFTER the storm from damage surveys (damage "
        "indicators and degrees of damage). The older F scale is also on the list. Radar clues: hook "
        "echo, velocity couplet (TVS), debris ball on CC. Waterspouts: tornadic (from supercells) or "
        "fair-weather. Tornado Alley (Plains) and Dixie Alley (Southeast, more nighttime and "
        "rain-wrapped tornadoes). Historic cases for data interpretation: Xenia, Ohio 1974 and the "
        "April 2011 outbreaks.",
        "Can a tornado be rated EF4 while it is happening? (No -- ratings come from surveying the "
        "damage afterward.)",
    ),
    lesson(
        "Tropical Cyclones",
        "Hurricane formation, structure, the Saffir-Simpson scale, and impacts.",
        "TROPICAL CYCLONE -- a warm-core low over tropical oceans (depression < 39 mph, storm 39-73 "
        "mph, hurricane 74+). EYE -- calm center. EYEWALL -- the ring of strongest winds. STORM SURGE "
        "-- seawater pushed ashore.",
        "Hurricanes are heat engines. Warm ocean water (about 26.5 C/80 F or warmer) evaporates, the "
        "moisture condenses in thunderstorms, and that latent heat powers the storm.",
        "Needs: warm water, moist air, low vertical wind shear, a pre-existing disturbance, and enough "
        "Coriolis (usually 5+ degrees from the equator). Saffir-Simpson (sustained winds): Cat 1 "
        "74-95 mph, 2 96-110, 3 111-129 (major), 4 130-156, 5 157+. It rates wind only -- storm surge "
        "and inland flooding cause most deaths. The right-front quadrant (relative to motion) has the "
        "strongest winds and surge in the Northern Hemisphere. They weaken over land or cool water. "
        "ENSO affects seasons (El Nino tends to suppress Atlantic hurricanes). Historic cases: "
        "Galveston 1900, Andrew, Katrina, Sandy, Ida, Ian, Hilary, Helene, Erin, Melissa.",
        "A hurricane has sustained winds of 120 mph. Category? (Category 3 -- a major hurricane.)",
    ),
    lesson(
        "Winter Storms & Precipitation Types",
        "Snow, sleet, freezing rain, blizzards, nor'easters, and lake-effect snow.",
        "SLEET -- raindrops that refreeze into ice pellets before landing. FREEZING RAIN -- supercooled "
        "rain that freezes on contact. BLIZZARD -- winds 35 mph+ with visibility under 1/4 mile for 3+ "
        "hours.",
        "Precipitation type depends on the temperature profile the falling drop passes through. A warm "
        "layer aloft melts snow; what happens below decides sleet or freezing rain.",
        "Snow: below freezing all the way down. Sleet: a warm layer melts snow, then a DEEP cold layer "
        "near the ground refreezes it. Freezing rain: a warm layer, then only a SHALLOW cold layer at "
        "the surface (ice storms). Rain formation: collision-coalescence (warm clouds) and the "
        "Bergeron process (ice crystals grow at the expense of supercooled droplets). Hail grows in "
        "strong updrafts. Nor'easters: coastal lows with northeast winds along the U.S. East Coast "
        "(Storm of the Century 1993; Blizzard of 1888). Lake-effect snow: cold air over warm lakes "
        "picks up moisture and dumps it downwind, depending on fetch.",
        "A deep warm layer aloft and a thin sub-freezing layer at the ground produce what? (Freezing "
        "rain.)",
    ),
    lesson(
        "Watches, Warnings & Safety",
        "What NWS alerts mean and what to do.",
        "WATCH -- conditions are favorable; be prepared. WARNING -- the hazard is happening or "
        "imminent; take action now. ADVISORY -- a less serious hazard that's still inconvenient or "
        "risky.",
        "A watch means \"get ready\"; a warning means \"act now.\" The Storm Prediction Center issues "
        "watches over large areas; local NWS offices issue warnings for specific areas.",
        "Tornado warning: shelter in the lowest floor, interior room, away from windows; mobile homes "
        "are not safe. Severe thunderstorm warning: shelter indoors. Lightning: \"When thunder roars, "
        "go indoors\"; wait 30 minutes after the last thunder. Flash flood warning: \"Turn around, "
        "don't drown\" -- 6 inches of moving water can knock you down; about 1-2 feet can float a "
        "car. Hurricane: evacuate from surge zones when told. Heat: hydrate and check on vulnerable "
        "people. Winter storm: avoid travel, watch for carbon monoxide from generators. Know the "
        "SPC's convective outlook risk levels (marginal to high) and Wireless Emergency Alerts.",
        "Radar shows rotation near your town and the NWS issues an alert. Watch or warning, and what "
        "do you do? (Tornado warning -- go to an interior room on the lowest floor now.)",
    ),
]

REMOTE_SENSING = [
    lesson(
        "The Electromagnetic Spectrum",
        "Wavelength, frequency, and the parts of the spectrum satellites use.",
        "WAVELENGTH -- distance between wave crests. FREQUENCY -- waves per second (Hz). c = "
        "wavelength x frequency (c = 3.0 x 10^8 m/s). ATMOSPHERIC WINDOW -- a wavelength band the "
        "atmosphere lets through.",
        "Light is one small part of the electromagnetic spectrum. Satellites see in many bands -- "
        "visible, near-infrared, thermal infrared, microwave -- each revealing something different.",
        "Order (short to long wavelength): gamma, X-ray, UV, visible (about 0.4-0.7 micrometers), "
        "near-IR, shortwave IR, thermal IR (about 8-14 micrometers), microwave, radio. Shorter "
        "wavelength = higher frequency = more energy (E = hf). Windows: visible, near-IR, thermal IR, "
        "and microwave pass through well; much UV and IR is absorbed by ozone, water vapor, and CO2. "
        "Microwaves pass through clouds -- why radar works day or night in any weather. Interactions: "
        "reflection, absorption, transmission, scattering (Rayleigh scattering makes the sky blue), "
        "refraction (Snell's law -- qualitative only in 2027). This equation is one of three you may "
        "calculate.",
        "A wave has frequency 6 x 10^14 Hz. Wavelength? (3 x 10^8 / 6 x 10^14 = 5 x 10^-7 m = 500 nm, "
        "green light.)",
    ),
    lesson(
        "Wien's & Stefan-Boltzmann Laws",
        "How an object's temperature sets the light it gives off.",
        "BLACKBODY -- an ideal emitter and absorber. WIEN'S LAW -- peak wavelength = b / T, b = 2,898 "
        "micrometer-K. STEFAN-BOLTZMANN -- energy emitted per area = sigma x T^4.",
        "Hotter objects glow brighter and at shorter wavelengths. The Sun (about 5,800 K) peaks in "
        "visible light; Earth (about 288 K) peaks in thermal infrared -- that's why thermal sensors see "
        "Earth's heat.",
        "Wien: Sun peak = 2,898 / 5,800 = 0.50 micrometers (visible); Earth = 2,898 / 288 = about 10 "
        "micrometers (thermal IR). Wien's law may be calculated in 2027. Stefan-Boltzmann (E = sigma "
        "T^4, sigma = 5.67 x 10^-8 W/m^2/K^4) is qualitative only this season: doubling temperature "
        "multiplies emission by 16. Real surfaces have emissivity under 1. The inverse-square law "
        "(intensity falls with distance squared) is also qualitative. These laws explain why fires "
        "and lava stand out in shortwave IR and why ECOSTRESS measures plant temperature to detect "
        "water stress.",
        "A wildfire at about 1,000 K. Peak wavelength? (2,898 / 1,000 = about 2.9 micrometers -- "
        "shortwave/mid IR.)",
    ),
    lesson(
        "Active & Passive Sensors",
        "Sensors that record natural energy vs sensors that send their own.",
        "PASSIVE SENSOR -- records reflected sunlight or emitted heat (cameras, multispectral "
        "scanners). ACTIVE SENSOR -- sends its own signal and measures the return (radar, lidar). SAR "
        "-- synthetic aperture radar.",
        "Passive sensors are like your eyes -- they need light. Active sensors are like a flashlight "
        "or a bat's echolocation -- they work in the dark and, for radar, through clouds.",
        "Passive: Landsat OLI and TIRS, Sentinel-2 MSI, MODIS, ASTER, GOES ABI, ECOSTRESS. Active: "
        "Sentinel-1 C-band SAR (all-weather imaging; smooth water looks dark, rough or urban surfaces "
        "bright -- great for floods and oil slicks), SRTM (radar interferometry for a near-global "
        "elevation model), lidar (laser pulses for heights and forest structure), radar altimeters "
        "(sea level). Radar altimetry range = (c x time) / 2 -- divide by 2 because the pulse goes "
        "down and back; this is one of the three equations you may calculate.",
        "A radar altimeter pulse returns after 0.005 s. Range? ((3 x 10^8 x 0.005) / 2 = 750 km.)",
    ),
    lesson(
        "Satellite Orbits & Kepler's Laws",
        "Geostationary, polar, and sun-synchronous orbits, and why they're used.",
        "GEOSTATIONARY -- orbits once a day above the equator at about 35,786 km, staying over one "
        "spot. POLAR ORBIT -- passes near both poles. SUN-SYNCHRONOUS -- crosses each latitude at the "
        "same local time every day.",
        "Weather satellites like GOES sit far out in geostationary orbit to watch one region "
        "continuously. Earth-observing satellites like Landsat fly low polar orbits to see the whole "
        "planet in detail, a strip at a time.",
        "Low Earth orbit (about 400-900 km) gives high resolution and takes about 90-100 minutes per "
        "orbit. Landsat 8/9 at about 705 km revisit every 16 days each (8 days combined). "
        "Sun-synchronous orbits keep lighting consistent for comparing images over time. Kepler's "
        "laws: (1) orbits are ellipses, (2) equal areas in equal times (faster when closer), "
        "(3) T^2 is proportional to a^3 -- qualitative only in 2027. Higher orbits are slower and "
        "longer-period.",
        "Why can't a geostationary satellite see the poles well? (It sits over the equator, so the "
        "poles are at a very low, oblique angle at the edge of its view.)",
    ),
    lesson(
        "Image Resolution Types",
        "Spatial, spectral, temporal, and radiometric resolution.",
        "SPATIAL -- the ground size of a pixel. SPECTRAL -- the number and width of bands. TEMPORAL -- "
        "how often a place is imaged. RADIOMETRIC -- how many brightness levels (bits) each pixel can "
        "hold.",
        "No sensor is best at everything. Fine pixels usually mean less frequent coverage; frequent "
        "coverage usually means coarse pixels.",
        "Examples: Landsat OLI 30 m (15 m panchromatic, 100 m thermal), 16-day revisit, 12-bit. "
        "Sentinel-2 10-60 m, 13 bands, about 5-day revisit with two satellites. MODIS 250 m-1 km, 36 "
        "bands, near-daily. GOES ABI 0.5-2 km, every few minutes. Radiometric: 8-bit = 256 levels, "
        "12-bit = 4,096. Hyperspectral sensors have hundreds of narrow bands. Choose by task: daily "
        "fires or clouds -> MODIS or GOES; field-scale crops -> Landsat or Sentinel-2.",
        "An 8-bit image can record how many brightness values per pixel? (2^8 = 256.)",
    ),
    lesson(
        "Image Interpretation Fundamentals",
        "Reading true-color, false-color, and spectral signatures.",
        "SPECTRAL SIGNATURE -- how a surface's reflectance changes with wavelength. TRUE COLOR -- red, "
        "green, blue bands shown as red, green, blue. FALSE COLOR -- other bands shown as RGB (e.g. "
        "near-IR as red).",
        "Every surface has a spectral \"fingerprint.\" Healthy plants reflect lots of near-infrared, "
        "so in the classic false-color image (NIR as red) vegetation looks bright red.",
        "Signatures: vegetation -- low red (chlorophyll absorbs it), high near-IR (leaf structure); "
        "water -- dark in near-IR; snow -- bright in visible, dark in shortwave IR (separates it from "
        "clouds); bare soil -- rises steadily with wavelength. NDVI = (NIR - Red) / (NIR + Red): "
        "about 0.6-0.9 dense vegetation, near 0 bare ground, negative water. Interpretation cues: "
        "tone/color, size, shape, texture, pattern, shadow, association, site. Burn scars appear "
        "dark in NIR and bright in SWIR.",
        "In a NIR-red-green false-color image, a field appears bright red. What is it? (Healthy, "
        "growing vegetation.)",
    ),
    lesson(
        "Satellite Missions",
        "The missions whose imagery is allowed in 2027 and what each does.",
        "LANDSAT -- the longest continuous Earth-imaging record (since 1972). SENTINEL -- the European "
        "Copernicus program. TERRA -- a NASA satellite carrying MODIS and ASTER.",
        "2027 imagery comes only from Landsat 5-9, Sentinel-1 and -2, Terra (MODIS, ASTER), SRTM, "
        "ECOSTRESS, and GOES. Know what each is good for.",
        "Landsat 5 TM, 7 ETM+, 8/9 OLI and TIRS: 30 m multispectral plus thermal, land change over "
        "decades. Sentinel-1A/1B: C-band SAR, all-weather (floods, ice, ground deformation). "
        "Sentinel-2A/2B: 10 m multispectral with red-edge bands (crops, coasts). Terra MODIS: daily "
        "global coverage (fires, snow, ocean color, vegetation); ASTER: 15-90 m visible to thermal, "
        "plus stereo elevation. SRTM (2000, Space Shuttle): near-global radar elevation model. "
        "ECOSTRESS (on the ISS): thermal measurements of plant temperature and water use. GOES "
        "(geostationary): weather, fires, and lightning every few minutes.",
        "You need to map a flood under thick clouds. Which allowed mission? (Sentinel-1 SAR -- radar "
        "sees through clouds.)",
    ),
    lesson(
        "Land Cover Classification & NLCD",
        "Turning pixels into land-cover maps.",
        "CLASSIFICATION -- assigning each pixel a category. SUPERVISED -- the analyst provides training "
        "areas. UNSUPERVISED -- the computer groups pixels by similarity first. NLCD -- the U.S. "
        "National Land Cover Database.",
        "A classification map colors every pixel by what's on the ground: forest, water, cropland, "
        "city. It is built from spectral signatures.",
        "Supervised: pick training samples for each class, then a classifier (e.g. maximum "
        "likelihood) labels every pixel. Unsupervised: clustering (e.g. k-means) first, then the "
        "analyst names the clusters. Accuracy assessment with ground truth: an error (confusion) "
        "matrix gives overall, producer's, and user's accuracy. NLCD uses Landsat at 30 m with "
        "classes such as open water, developed (open space to high intensity), forest types, shrub, "
        "grassland, pasture, cultivated crops, and wetlands; its imperviousness layer tracks "
        "urbanization. Change detection compares classified images from different years.",
        "Out of 200 test pixels, 170 are classified correctly. Overall accuracy? (85%.)",
    ),
    lesson(
        "Climate Processes & Greenhouse Gases",
        "How greenhouse gases trap heat and how satellites monitor climate.",
        "GREENHOUSE EFFECT -- gases absorbing outgoing infrared and re-emitting part of it downward. "
        "GREENHOUSE GASES -- water vapor, CO2, methane, nitrous oxide, ozone. ALBEDO -- the fraction of "
        "sunlight reflected.",
        "Sunlight (mostly visible) passes through the air and warms the surface; the surface gives off "
        "infrared, which greenhouse gases absorb. Without them Earth would average about -18 C, not "
        "+15 C.",
        "CO2 has risen from about 280 ppm before industrialization to over 420 ppm. Methane is a much "
        "stronger absorber per molecule but shorter-lived. Water vapor is the largest greenhouse gas "
        "but acts as a feedback (warmer air holds more). Satellites track sea-surface temperature "
        "(MODIS), ice extent, snow cover, vegetation (NDVI), land-surface temperature, and sea level "
        "(altimetry). Aerosols (volcanic sulfate, pollution) cool by reflecting sunlight. Albedo: "
        "fresh snow ~0.8-0.9, ocean ~0.06, forest ~0.1-0.2.",
        "Why does replacing snow with open water raise local warming? (Water's albedo is much lower, "
        "so it absorbs much more sunlight.)",
    ),
    lesson(
        "Earth's Energy Balance & Feedbacks",
        "Incoming vs outgoing energy and the feedbacks that amplify or damp change.",
        "ENERGY BALANCE -- incoming solar = reflected + outgoing infrared (in equilibrium). POSITIVE "
        "FEEDBACK -- amplifies a change. NEGATIVE FEEDBACK -- counteracts it. RADIATIVE FORCING -- a "
        "change in the energy budget (W/m^2).",
        "Earth stays at a steady temperature when the energy it gets from the Sun equals the energy it "
        "sends back to space. Add greenhouse gases and less escapes, so Earth warms until balance "
        "returns at a higher temperature.",
        "About 30% of incoming sunlight is reflected (planetary albedo ~0.3). Positive feedbacks: "
        "ice-albedo (melting ice -> darker surface -> more warming), water vapor, permafrost thaw "
        "releasing methane. Negative feedbacks: more outgoing infrared from a warmer surface "
        "(Stefan-Boltzmann), some cloud effects. Low clouds mostly cool (reflect); high thin cirrus "
        "mostly warm (trap infrared). Urban heat islands show up on thermal imagery. Satellites such "
        "as CERES measure the budget from space.",
        "Melting Arctic sea ice exposing dark ocean is which kind of feedback? (Positive -- the "
        "ice-albedo feedback.)",
    ),
    lesson(
        "Math in Remote Sensing",
        "The calculations you may do in 2027, plus index and scale problems.",
        "WAVE EQUATION -- c = wavelength x frequency. WIEN'S LAW -- peak = 2,898 / T (micrometers). "
        "RADAR RANGE -- R = c t / 2. SCALE -- map distance : ground distance.",
        "Only three equations may be calculated this year: the wave equation, Wien's law, and radar "
        "altimetry range. Everything else is qualitative -- but simple scale and index calculations "
        "still appear.",
        "Practice: (1) 10 micrometer thermal IR -> frequency = 3 x 10^8 / 10^-5 = 3 x 10^13 Hz. "
        "(2) Peak at 0.5 micrometers -> T = 2,898 / 0.5 = 5,796 K. (3) Altimeter return 0.0048 s -> "
        "R = 3 x 10^8 x 0.0048 / 2 = 720 km. Pixels: a 30 m pixel covers 900 m^2; 1 km^2 = about 1,111 "
        "Landsat pixels. NDVI from reflectances: NIR 0.5, red 0.1 -> (0.5 - 0.1) / (0.5 + 0.1) = 0.67. "
        "Keep units consistent (micrometers vs meters) and use scientific notation.",
        "How many 10 m Sentinel-2 pixels fit in 1 km^2? (100 x 100 = 10,000.)",
    ),
    lesson(
        "Atmospheric & Map-Reading Skills",
        "The supporting skills: atmospheric effects on images, and reading maps and coordinates.",
        "LATITUDE/LONGITUDE -- angular position north-south / east-west. UTM -- a metric grid "
        "coordinate system used by Landsat. ATMOSPHERIC CORRECTION -- removing haze and scattering "
        "effects.",
        "Images are taken through the atmosphere, which adds haze and blocks some wavelengths. You "
        "also need to locate things: read coordinates, scale bars, and north arrows.",
        "Haze from Rayleigh scattering affects blue most, so atmospheric correction matters for blue "
        "bands; surface reflectance products have it removed. Clouds and their shadows must be masked. "
        "Map skills: latitude lines run east-west and measure north-south; one degree of latitude is "
        "about 111 km; longitude degrees shrink toward the poles. Read scale bars and representative "
        "fractions (1:24,000 means 1 cm = 240 m). Contour lines show elevation (close together = "
        "steep). Image orientation: check the north arrow; satellite paths are often tilted.",
        "On a 1:50,000 map, two points are 4 cm apart. Ground distance? (4 x 50,000 = 200,000 cm = "
        "2 km.)",
    ),
]

ROCKS_AND_MINERALS = [
    lesson(
        "Mineral Definition & Physical Properties",
        "What makes something a mineral, and the core tests for identifying one.",
        "MINERAL -- naturally occurring, inorganic (mostly), solid, with a definite chemical "
        "composition and an ordered crystal structure. HARDNESS -- resistance to scratching (Mohs "
        "scale 1-10). STREAK -- the color of a mineral's powder. LUSTER -- how it reflects light.",
        "Identifying a mineral is detective work: test hardness, streak, luster, cleavage, and "
        "density, then narrow the possibilities with a key or chart.",
        "Mohs: 1 talc, 2 gypsum, 3 calcite, 4 fluorite, 5 apatite, 6 orthoclase, 7 quartz, 8 topaz, "
        "9 corundum, 10 diamond. Tools: fingernail ~2.5, copper ~3.5, glass/steel ~5.5, streak plate "
        "~6.5. Streak is more reliable than color (hematite: red-brown streak even when the sample "
        "looks silver; pyrite: greenish-black). Luster: metallic, submetallic, nonmetallic (vitreous, "
        "pearly, silky, greasy, resinous, earthy, adamantine). Cleavage (breaks along flat planes -- "
        "micas in one direction, feldspars two at ~90 degrees, calcite three not at 90) vs fracture "
        "(conchoidal in quartz). Identification uses the 2027 National Rocks and Minerals List; "
        "asterisked specimens are State/Nationals only.",
        "A mineral scratches glass but not quartz. What's its hardness range? (Between about 5.5 "
        "and 7.)",
    ),
    lesson(
        "Habit & Other Diagnostic Properties",
        "Crystal habit, specific gravity, and special properties like magnetism and fizzing.",
        "HABIT -- the typical shape a mineral grows in. SPECIFIC GRAVITY (SG) -- density compared to "
        "water. TENACITY -- how it responds to stress (brittle, malleable, flexible, elastic).",
        "Some minerals give themselves away with one special test: magnetite sticks to a magnet, "
        "calcite fizzes in acid, halite tastes salty.",
        "Habits: cubic (halite, pyrite, galena), prismatic (quartz, tourmaline), bladed (kyanite), "
        "botryoidal (grape-like -- some hematite, malachite), acicular (needles), dendritic, massive, "
        "fibrous (asbestos-form serpentine), tabular, rhombohedral (calcite). SG: quartz 2.65, "
        "calcite 2.7, pyrite ~5.0, galena ~7.5 (feels heavy). Special properties: magnetism "
        "(magnetite; pyrrhotite weakly), effervescence in dilute HCl (calcite strongly, dolomite only "
        "as powder), double refraction (clear calcite -- Iceland spar), fluorescence (fluorite, some "
        "calcite under UV), taste (halite), striations (plagioclase, pyrite), elastic sheets "
        "(muscovite).",
        "A cube-shaped, silvery, very heavy mineral with a gray streak. Likely? (Galena.)",
    ),
    lesson(
        "Chemical Composition & Formulas",
        "Reading mineral formulas and connecting composition to properties.",
        "CHEMICAL FORMULA -- the elements and their ratio (quartz SiO2). ION -- a charged atom. SOLID "
        "SOLUTION -- one element substituting for another in a crystal.",
        "A mineral's formula tells you what it's made of. Minerals with the same chemical family "
        "often look and behave similarly.",
        "Examples: quartz SiO2; calcite CaCO3; dolomite CaMg(CO3)2; halite NaCl; fluorite CaF2; gypsum "
        "CaSO4 2H2O; pyrite FeS2; galena PbS; hematite Fe2O3; magnetite Fe3O4; orthoclase KAlSi3O8; "
        "olivine (Mg,Fe)2SiO4 -- the parentheses mean Mg and Fe substitute for each other. "
        "Polymorphs: same formula, different structure (diamond and graphite are both C; calcite and "
        "aragonite are both CaCO3). Water of hydration in gypsum makes it soft. Metal content gives "
        "ore minerals their high SG.",
        "Diamond and graphite are both pure carbon. What term describes them? (Polymorphs.)",
    ),
    lesson(
        "Mineral Families & Groups",
        "Silicates and the non-silicate classes.",
        "SILICATE -- built from SiO4 tetrahedra; over 90% of the crust. CARBONATE (CO3), SULFIDE (S), "
        "SULFATE (SO4), OXIDE (O), HALIDE (Cl, F), NATIVE ELEMENT.",
        "Most of Earth's crust is silicate minerals. The way the silicon-oxygen tetrahedra link "
        "together -- alone, in chains, sheets, or 3D frameworks -- controls how the mineral breaks "
        "and looks.",
        "Silicate structures: isolated (olivine, garnet), single chains (pyroxenes -- cleavage ~90 "
        "degrees), double chains (amphiboles like hornblende -- ~60/120 degrees), sheets (micas, "
        "clays, talc -- one perfect cleavage), frameworks (quartz, feldspars). Non-silicates: "
        "carbonates (calcite, dolomite, malachite, azurite -- many fizz), sulfides (pyrite, galena, "
        "sphalerite, chalcopyrite -- often metallic ores), sulfates (gypsum, barite), oxides "
        "(hematite, magnetite, corundum), halides (halite, fluorite), native elements (gold, copper, "
        "sulfur, graphite).",
        "A mineral splits into thin flexible sheets. Which silicate structure? (Sheet silicate -- a "
        "mica.)",
    ),
    lesson(
        "Mineral Formation & Bowen's Reaction Series",
        "Where minerals form, and the order they crystallize from magma.",
        "BOWEN'S REACTION SERIES -- the sequence in which minerals crystallize as magma cools. MAFIC -- "
        "rich in Mg and Fe (dark). FELSIC -- rich in feldspar and silica (light).",
        "As magma cools, different minerals crystallize at different temperatures. High-temperature "
        "minerals form first; quartz forms last.",
        "Discontinuous branch (high to low T): olivine -> pyroxene -> amphibole -> biotite. "
        "Continuous branch: Ca-rich plagioclase -> Na-rich plagioclase. Then K-feldspar, muscovite, "
        "and quartz last. Minerals that form first are least stable at Earth's surface and weather "
        "fastest (olivine); quartz is most stable (why sand is mostly quartz). Other formation paths: "
        "precipitation from water (halite, gypsum in evaporites; calcite), hydrothermal veins "
        "(quartz, sulfide ores), metamorphism (garnet, kyanite, staurolite), weathering (clays, "
        "bauxite -- now classed as a sedimentary rock on the 2027 list).",
        "Why is quartz the most common mineral in beach sand? (It crystallizes last, is hard, and "
        "resists weathering.)",
    ),
    lesson(
        "Rocks & the Rock Cycle",
        "What a rock is and how the three types turn into each other.",
        "ROCK -- a natural aggregate of one or more minerals (or glass or organic matter). IGNEOUS -- "
        "cooled from melt. SEDIMENTARY -- from sediment or precipitation. METAMORPHIC -- changed by "
        "heat and pressure without melting.",
        "Any rock can become any other type. Melt it and cool it: igneous. Weather it, move the "
        "pieces, and cement them: sedimentary. Bury it and squeeze or heat it: metamorphic.",
        "Processes: melting, crystallization, weathering, erosion, deposition, compaction and "
        "cementation (lithification), heat and pressure, and uplift. Plate tectonics drives the cycle: "
        "subduction makes magma; collisions make metamorphic belts; uplift exposes rock to weathering. "
        "Identification starts with texture (grain size, shape, arrangement) and then composition. "
        "List notes: Rock Salt = Halite and Rock Gypsum = Gypsum for ID purposes.",
        "Granite weathers into sand that becomes sandstone, which is buried and becomes quartzite. "
        "Name the rock types in order. (Igneous -> sedimentary -> metamorphic.)",
    ),
    lesson(
        "Igneous Rocks",
        "Textures, compositions, and the environments that make them.",
        "INTRUSIVE (PLUTONIC) -- cooled slowly underground, coarse-grained. EXTRUSIVE (VOLCANIC) -- "
        "cooled quickly at the surface, fine-grained or glassy. PORPHYRITIC -- big crystals in a finer "
        "matrix.",
        "Cooling speed sets crystal size. Slow underground cooling grows big crystals you can see; "
        "fast surface cooling makes tiny crystals or glass.",
        "Textures: phaneritic (coarse -- granite, diorite, gabbro), aphanitic (fine -- rhyolite, "
        "andesite, basalt), porphyritic (two cooling stages), glassy (obsidian), vesicular (gas "
        "holes -- pumice, scoria), pyroclastic (volcanic fragments -- tuff). Composition: felsic "
        "(granite/rhyolite, light, quartz and K-feldspar), intermediate (diorite/andesite), mafic "
        "(gabbro/basalt, dark, pyroxene and Ca-plagioclase), ultramafic (peridotite, mostly olivine). "
        "Environments: basalt at mid-ocean ridges and hot spots; andesite at subduction-zone volcanoes; "
        "granite batholiths in continental crust.",
        "A dark, fine-grained rock full of gas holes that sinks in water. (Scoria -- vesicular basalt; "
        "pumice would float.)",
    ),
    lesson(
        "Sedimentary Rocks",
        "Clastic, chemical, and organic sedimentary rocks and what they record.",
        "CLASTIC -- made of rock fragments (classified by grain size). CHEMICAL -- precipitated from "
        "water. BIOCHEMICAL/ORGANIC -- from shells or plant remains. SORTING -- how uniform grain "
        "sizes are.",
        "Sedimentary rocks are history books: grain size tells how fast the water was moving, fossils "
        "tell what lived there, and layers record the order of events.",
        "Clastic: conglomerate (rounded gravel), breccia (angular gravel -- little transport), "
        "sandstone (sand), siltstone, shale (clay, splits in layers). Chemical: rock salt, rock "
        "gypsum (evaporites), chert, some limestone (travertine, oolitic). Biochemical: fossiliferous "
        "limestone, coquina (shell hash), chalk (microscopic plankton), coal (plant matter: peat -> "
        "lignite -> bituminous; anthracite is metamorphic). Structures: bedding, cross-bedding (dunes, "
        "currents), ripple marks, mud cracks (drying), graded bedding. Well-rounded, well-sorted sand "
        "= long transport (beach or dune). Bauxite is classed as sedimentary on the 2027 list.",
        "A rock of angular pebbles cemented together. Conglomerate or breccia, and what does it say? "
        "(Breccia -- the fragments traveled only a short distance.)",
    ),
    lesson(
        "Metamorphic Rocks",
        "Foliation, protoliths, grade, and index minerals.",
        "PROTOLITH -- the parent rock. FOLIATED -- minerals aligned in layers by directed pressure. "
        "NONFOLIATED -- no alignment. METAMORPHIC GRADE -- the intensity of heat and pressure. INDEX "
        "MINERAL -- one that forms only in a certain grade range.",
        "Heat and pressure rearrange minerals without melting them. With directed pressure, platy "
        "minerals line up and the rock becomes layered (foliated).",
        "Foliated sequence from shale with rising grade: slate (fine, splits into sheets) -> phyllite "
        "(silky sheen) -> schist (visible mica flakes, often garnet) -> gneiss (light and dark "
        "banding). Nonfoliated: marble (from limestone, fizzes), quartzite (from sandstone, very "
        "hard), hornfels (contact metamorphism), anthracite (from coal). Index minerals with rising "
        "grade: chlorite -> biotite -> garnet -> staurolite -> kyanite -> sillimanite. Kyanite, "
        "andalusite, and sillimanite are polymorphs of Al2SiO5 used to read pressure and temperature. "
        "Types: regional (mountain belts) vs contact (next to an intrusion).",
        "A hard, sugary-textured rock that does not fizz and scratches glass. Protolith? (Quartz "
        "sandstone -- the rock is quartzite.)",
    ),
    lesson(
        "Solid Solution, Phase Diagrams & Crystal Systems",
        "Advanced mineral concepts for higher-level tests.",
        "SOLID SOLUTION -- a series where ions substitute in a range (forsterite Mg2SiO4 to fayalite "
        "Fe2SiO4). PHASE DIAGRAM -- shows which mineral is stable at each pressure and temperature. "
        "CRYSTAL SYSTEM -- one of six (or seven) symmetry groups.",
        "Many minerals aren't one fixed formula but a range between two end members. Phase diagrams "
        "show the conditions under which each form is stable.",
        "Solid solutions: olivine (Mg-Fe), plagioclase (albite NaAlSi3O8 to anorthite CaAl2Si2O8 -- "
        "coupled substitution), garnets. The Al2SiO5 phase diagram: kyanite (high pressure), "
        "andalusite (low pressure), sillimanite (high temperature), meeting at a triple point. Crystal "
        "systems: isometric/cubic (halite, garnet, pyrite), tetragonal (zircon), hexagonal and "
        "trigonal (quartz, calcite, beryl), orthorhombic (olivine, topaz, barite), monoclinic "
        "(gypsum, micas, orthoclase), triclinic (plagioclase, kyanite). Exsolution (e.g. perthite in "
        "feldspar) separates a solid solution on cooling.",
        "Which crystal system has three equal axes at right angles? (Isometric/cubic.)",
    ),
    lesson(
        "Magmatic Differentiation & Metamorphic Facies",
        "How one magma makes many rock types, and how metamorphic conditions are mapped.",
        "FRACTIONAL CRYSTALLIZATION -- early crystals separate from the melt, changing its "
        "composition. ASSIMILATION -- magma melting in surrounding rock. METAMORPHIC FACIES -- groups "
        "of mineral assemblages formed under similar P-T conditions.",
        "A single basaltic magma can evolve toward andesite and rhyolite as early mafic minerals crystallize "
        "out and sink, leaving the remaining melt richer in silica.",
        "Differentiation processes: fractional crystallization (Bowen), assimilation of crust, magma "
        "mixing, partial melting (melting the lowest-melting minerals first produces felsic melts). "
        "Layered intrusions (e.g. Bushveld, Stillwater) show crystal settling. Facies (low to high T "
        "and P): zeolite, prehnite-pumpellyite, greenschist (chlorite, actinolite), amphibolite "
        "(hornblende, plagioclase), granulite (very high T), blueschist (high P, low T -- subduction "
        "zones; glaucophane), eclogite (very high P -- garnet and pyroxene), and hornfels facies for "
        "contact metamorphism.",
        "Blueschist forms under high pressure but low temperature. Where? (Subduction zones, where "
        "cold slabs are pushed deep quickly.)",
    ),
    lesson(
        "Thin Sections & Incompatible Elements",
        "Reading rocks under the polarizing microscope, and how trace elements track melting.",
        "THIN SECTION -- a rock slice 30 micrometers thick. PPL/XPL -- plane- and cross-polarized "
        "light. BIREFRINGENCE -- interference colors in XPL. INCOMPATIBLE ELEMENT -- one that doesn't "
        "fit easily into common mineral structures and stays in the melt.",
        "At 30 micrometers, most minerals become transparent. Polarized light reveals each mineral's "
        "optical fingerprint.",
        "In XPL: quartz shows low first-order gray-white and no cleavage; plagioclase shows "
        "polysynthetic (striped) twinning; microcline shows tartan twinning; olivine shows high, "
        "bright colors and fractures; biotite is brown and pleochroic in PPL; isotropic minerals "
        "(garnet, glass) stay black in XPL. Textures show crystallization order. Incompatible elements "
        "(K, Rb, Ba, U, Th, rare earth elements, Zr) concentrate in the last melts and in continental "
        "crust, so felsic rocks and pegmatites are enriched in them. Compatible elements (Ni, Cr, Mg) "
        "go into early olivine and pyroxene.",
        "A grain stays black as the stage rotates in cross-polarized light. What could it be? (An "
        "isotropic mineral such as garnet, or volcanic glass.)",
    ),
]
