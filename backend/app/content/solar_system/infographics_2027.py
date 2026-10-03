"""Infographics for the chapters added to cover the rest of the 2027
Division B Solar System rules: microlensing, the three named extrasolar
systems, the no-calculator habitability math, water's many forms and
extremophiles, and the 2027 mission list. Same deterministic SVG helpers
as infographics.py; numbers are rounded published NASA/ESA values.
"""

from collections.abc import Callable

from app.content.solar_system.svg import (
    BLUE,
    GAS,
    GOLD,
    GREEN,
    ICE,
    MUTED,
    PANEL,
    PANEL_EDGE,
    PLANET_COLORS,
    PURPLE,
    RED,
    ROCK,
    SUN,
    TEXT,
    canvas,
    card,
    circle,
    line,
    para,
    path,
    rect,
    text,
)

SOURCE_2027 = "Topics: 2027 Div. B Solar System rules -- facts: NASA / ESA mission and exoplanet pages"


def microlensing() -> str:
    w, h = 1060, 640
    body = ""
    # Geometry: observer, lens star with planet, distant source star.
    body += circle(90, 230, 16, PLANET_COLORS["Earth"])
    body += text(90, 268, "us", 14, TEXT, "bold", "middle")
    body += circle(470, 230, 14, "#ff7a3d")
    body += text(470, 196, "LENS star", 14, "#ff7a3d", "bold", "middle")
    body += circle(520, 212, 5, PLANET_COLORS["Jupiter"])
    body += text(560, 206, "its planet", 13, GAS)
    body += circle(940, 230, 12, "#fff3b0")
    body += text(940, 196, "distant SOURCE star", 14, "#fff3b0", "bold", "middle")
    body += path("M 928 226 C 700 150, 300 150, 106 226", ICE, 2, arrow=True, dash="6 4")
    body += path("M 928 234 C 700 310, 300 310, 106 234", ICE, 2, arrow=True, dash="6 4")
    body += text(470, 330, "gravity bends and focuses the source's light (Einstein)", 14, ICE, anchor="middle")
    # Light curve.
    x0, y0, cw, ch = 60, 370, 600, 220
    body += rect(x0, y0, cw, ch, fill=PANEL, stroke=PANEL_EDGE)
    body += text(x0 + 16, y0 + 26, "Brightness of the source star", 14, MUTED)
    pts = []
    for i in range(0, 121):
        t = (i - 60) / 14
        b = 1 / (1 + t * t) ** 0.5
        pts.append((x0 + 20 + i * 4.6, y0 + ch - 24 - 150 * b * b))
    d = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pts)
    body += path(d, GOLD, 3)
    bx, by = pts[78]
    body += path(f"M {bx - 8:.1f} {by:.1f} L {bx:.1f} {by - 34:.1f} L {bx + 8:.1f} {by:.1f}", RED, 3)
    body += text(bx + 14, by - 30, "planet blip (hours)", 13, RED, "bold")
    body += text(x0 + cw / 2, y0 + ch - 4, "time (days to weeks)", 13, MUTED, anchor="middle")
    body += card(690, 370, 340, 104, "Strengths", "Finds small, cold planets 1-10 AU from their star, thousands of light-years away -- even rogue planets with no star.", GREEN, body_size=13)
    body += card(690, 486, 340, 104, "Weaknesses", "One-time event that never repeats; the host star is usually too faint to study again.", RED, body_size=13)
    return canvas(w, h, "Gravitational Microlensing", "A passing star acts like a magnifying glass -- and a planet adds a blip", body, SOURCE_2027)


def trappist1() -> str:
    w, h = 1060, 640
    body = ""
    planets = [
        ("b", 1.51, 1.12, RED),
        ("c", 2.42, 1.10, "#ff9a5a"),
        ("d", 4.05, 0.79, GOLD),
        ("e", 6.10, 0.92, GREEN),
        ("f", 9.21, 1.05, GREEN),
        ("g", 12.35, 1.13, GREEN),
        ("h", 18.77, 0.76, ICE),
    ]
    body += circle(80, 250, 46, "#ff5a3a")
    body += text(80, 320, "TRAPPIST-1", 15, "#ff8a6a", "bold", "middle")
    body += text(80, 340, "red dwarf", 13, MUTED, anchor="middle")
    body += rect(500, 140, 330, 220, fill=GREEN, stroke="none", rx=12, opacity=0.18)
    body += text(665, 162, "HABITABLE ZONE (e, f, g)", 14, "#d9ffe3", "bold", "middle")
    for i, (name, days, radius, color) in enumerate(planets):
        x = 170 + i * 108
        body += circle(x, 250, 14 * radius, color)
        body += text(x, 302, name, 18, TEXT, "bold", "middle")
        body += text(x, 324, f"{days} d", 13, MUTED, anchor="middle")
        body += text(x, 342, f"{radius} R⊕", 13, MUTED, anchor="middle")
    body += text(530, 116, "All seven orbit closer than Mercury -- years of 1.5 to 19 days", 15, TEXT, "bold", "middle")
    body += card(30, 390, 320, 220, "The star", "About 40 light-years away in Aquarius. Only ~9% of the Sun's mass and barely bigger than Jupiter, ~2,550 K, very dim. It flares often -- risky for atmospheres -- but will shine for trillions of years.", "#ff8a6a", body_size=13)
    body += card(370, 390, 320, 220, "The planets", "Seven Earth-sized rocky worlds (2016-2017, TRAPPIST telescope + Spitzer). Masses come from transit timing. Locked in a resonant chain and probably tidally locked: one side always day.", GOLD, body_size=13)
    body += card(710, 390, 320, 220, "JWST says", "2023: TRAPPIST-1 b (~500 K dayside) and c show no thick CO2 atmosphere. The big question for e, f and g: can planets this close to an active red dwarf keep any air?", ICE, body_size=13)
    return canvas(w, h, "TRAPPIST-1: Seven Earth-Sized Worlds", "Orbital period and size of each planet (R⊕ = Earth radii)", body, SOURCE_2027)


def three_systems() -> str:
    w, h = 1060, 670
    body = ""
    cols = ["", "TRAPPIST-1", "Kepler-452", "LHS 1140", "Sun / Earth"]
    colors = [TEXT, "#ff8a6a", SUN, "#ff9a5a", PLANET_COLORS["Earth"]]
    rows = [
        ("Distance", "~40 ly", "~1,800 ly", "~49 ly", "--"),
        ("Star type", "M8 red dwarf", "G2, Sun-like", "M4.5 red dwarf", "G2"),
        ("Star temp.", "~2,550 K", "~5,750 K", "~3,100 K", "~5,770 K"),
        ("Key planet", "e, f, g", "452 b", "1140 b", "Earth"),
        ("Planet size", "~0.9-1.1 R⊕", "~1.6 R⊕", "~1.7 R⊕", "1 R⊕"),
        ("Planet mass", "~0.7-1.3 M⊕", "unknown", "~5.6 M⊕", "1 M⊕"),
        ("Year", "6-12 days", "385 days", "24.7 days", "365 days"),
        ("Sunlight vs. Earth", "~1/4 to 2/3", "~1.1x", "~0.4x", "1x"),
        ("Found by", "transits", "transits (Kepler)", "transits (MEarth)", "--"),
    ]
    x_cols = [40, 250, 450, 650, 850]
    for x, label, color in zip(x_cols, cols, colors):
        body += text(x, 120, label, 17, color, "bold")
    for r, row in enumerate(rows):
        y = 150 + r * 34
        if r % 2 == 0:
            body += rect(30, y - 22, 1000, 32, fill=PANEL, stroke="none", rx=6)
        for x, value in zip(x_cols, row):
            body += text(x, y, value, 14, MUTED if x == 40 else TEXT, "bold" if x == 40 else "normal")
    body += card(30, 470, 320, 160, "TRAPPIST-1 e-g", "Rocky, Earth-sized, in the habitable zone of a tiny, flaring star. Best place to test whether red-dwarf planets keep atmospheres.", "#ff8a6a", body_size=13)
    body += card(370, 470, 320, 160, "Kepler-452 b", "'Earth's older cousin' (2015): Sun-like star 1.5 billion years older than ours. Too far to weigh -- and later studies doubt the signal is even a planet.", SUN, body_size=13)
    body += card(710, 470, 320, 160, "LHS 1140 b", "Too light to be pure rock: a water world (maybe icy with a liquid 'bullseye' ocean) or a mini-Neptune. Close and bright -- a top JWST target.", "#ff9a5a", body_size=13)
    return canvas(w, h, "The Three 2027 Extrasolar Systems", "Rounded values; ly = light-years", body, SOURCE_2027)


def habitability_math() -> str:
    w, h = 1060, 680
    body = ""
    cards = [
        ("Stefan-Boltzmann", "Power per m² = sigma x T^4. Double the temperature -> 16x the power. A star's luminosity L = 4 pi R² sigma T^4.", GOLD),
        ("Wien's law", "Peak wavelength = 2,900 µm·K / T. Sun (5,800 K): 0.5 µm, visible. TRAPPIST-1 (2,550 K): ~1.1 µm, infrared. Earth (290 K): 10 µm.", RED),
        ("Albedo A", "Fraction of light reflected: 0 = black, 1 = mirror. Moon ~0.1, Earth ~0.3, Venus ~0.75, fresh ice (Enceladus) ~0.8-0.9.", ICE),
        ("Equilibrium temp.", "T_eq = T_star x sqrt(R_star / 2d) x (1 - A)^(1/4). Same star: T_eq ~ 1/sqrt(d). 4x farther -> half the temperature.", GREEN),
        ("Doppler shift", "Delta lambda / lambda = v / c. A 30 m/s wobble: 30 / (3 x 10^8) = 10^-7 of a shift.", BLUE),
        ("Tides", "Tidal force ~ M / r^3. Twice as far -> 1/8 the tidal stretch. Close-in planets and moons get squeezed (tidal heating).", PURPLE),
        ("Ideal gas law", "PV = nRT. Fixed volume: double T -> double P. Molecule speed ~ sqrt(T / m): hot, light gases (H2) escape first.", GAS),
        ("Arrhenius", "Rate k = A e^(-Ea / RT). Colder = much slower chemistry. Rule of thumb: ~2x faster per +10 C near room temperature.", ROCK),
    ]
    for i, (head, desc, color) in enumerate(cards):
        col, row = i % 2, i // 2
        body += card(30 + col * 505, 100 + row * 124, 490, 112, head, desc, color, body_size=13)
    body += para(40, 620, "Worked example: Earth's T_eq is ~255 K. A planet with the same albedo 4 AU from the Sun: 255 / sqrt(4) = ~128 K.", 140, 14, GOLD)
    return canvas(w, h, "Habitability Math -- No Calculator", "The 2027 formulas, and how to scale them in your head", body, SOURCE_2027)


def water_forms() -> str:
    w, h = 1060, 640
    body = ""
    forms = [
        ("Liquid water", "The solvent life needs. Only liquid between certain temperatures AND pressures (triple point: 0.01 C at 611 Pa -- about Mars' surface pressure).", BLUE),
        ("Crystalline ice", "Molecules in a neat hexagonal lattice (ordinary ice, Ih). Huge pressures inside Ganymede and Titan make denser ices (like ice VI) below their oceans.", ICE),
        ("Amorphous ice", "Frozen so cold and fast (below ~130 K) that the molecules never line up -- no crystal. Common on interstellar dust and in comets; traps gases.", PURPLE),
        ("Brines", "Salty water stays liquid far below 0 C. Perchlorate brines on Mars, salty oceans in Europa and Enceladus, salt deposits at Ceres' bright spots.", GREEN),
        ("Clathrates", "Ice 'cages' that trap gas molecules like methane or CO2 ('fire ice' on Earth's seafloor). May store methane inside Titan and gases on Mars.", GOLD),
    ]
    for i, (head, desc, color) in enumerate(forms):
        col, row = i % 3, i // 3
        body += card(30 + col * 338, 100 + row * 250, 326, 236, head, desc, color, body_size=14)
    body += card(706, 350, 326, 236, "Why it matters", "Every form changes where liquid water can hide: salt lowers the freezing point, pressure changes which ice forms, and clathrates and amorphous ice lock away gases.", RED, body_size=14)
    return canvas(w, h, "Water's Many Forms", "Liquid, two kinds of ice, brines and clathrates", body, SOURCE_2027)


def extremophiles() -> str:
    w, h = 1060, 640
    body = ""
    kinds = [
        ("Heat lovers", "Thermophiles; 'Strain 121' grows at 121 C near deep-sea vents.", RED),
        ("Cold lovers", "Psychrophiles grow below 0 C in sea ice and salty brines.", ICE),
        ("Salt lovers", "Halophiles live in water 10x saltier than the ocean.", GOLD),
        ("Acid / base", "Acidophiles at pH ~0; alkaliphiles at pH 11+.", GREEN),
        ("Pressure", "Piezophiles thrive at the bottom of the Mariana Trench.", BLUE),
        ("Radiation", "Deinococcus radiodurans survives ~1,000x a lethal human dose.", PURPLE),
    ]
    for i, (head, desc, color) in enumerate(kinds):
        col, row = i % 3, i // 3
        body += card(30 + col * 338, 100 + row * 130, 326, 118, head, desc, color, body_size=14)
    body += card(30, 370, 490, 230, "Chemolithoautotrophs", "CHEMO (energy from chemical reactions) + LITHO (from rock / inorganic chemicals) + AUTOTROPH (builds its own food from CO2). No sunlight needed! Example: methanogens make methane from H2 + CO2 -- exactly the kind of life the H2 in Enceladus' plume could feed.", GAS, body_size=14)
    body += card(540, 370, 490, 230, "Tardigrades (water bears)", "Half-millimeter animals that dry out into a 'tun' and survive freezing near absolute zero, crushing pressure, radiation -- even 10 days exposed to space (2007). They SURVIVE extremes but don't grow in them, so they're 'extremotolerant'.", SUN, body_size=14)
    return canvas(w, h, "Life at the Extremes", "Extremophiles stretch where life could survive -- on Earth and beyond", body, SOURCE_2027)


def mission_design() -> str:
    w, h = 1060, 660
    body = ""
    kinds = [
        ("Flyby", "Quick pass; cheap, one look"),
        ("Orbiter", "Maps a world for years"),
        ("Lander / rover", "Touches the ground"),
        ("Probe", "Falls through the air"),
        ("Sample return", "Brings pieces home"),
        ("Space telescope", "Watches from afar"),
    ]
    for i, (head, desc) in enumerate(kinds):
        x = 30 + i * 168
        body += rect(x, 100, 158, 84)
        body += text(x + 79, 132, head, 15, GOLD, "bold", "middle")
        body += text(x + 79, 160, desc, 13, MUTED, anchor="middle")
    body += text(30, 214, "<-- cheaper, less detail", 14, MUTED)
    body += text(1030, 214, "more detail, more cost and risk -->", 14, MUTED, anchor="end")
    cards = [
        ("Power", "Solar panels lose power as 1/d²: Jupiter gets ~1/27 of Earth's sunlight, so JUICE and Europa Clipper need giant arrays. Far away or in the dark -> nuclear RTGs (Cassini, Perseverance, Dragonfly).", SUN),
        ("Radiation & heat", "Jupiter's radiation fries electronics: Europa Clipper hides them in a thick vault and only flies by Europa. Venus' 465 C surface killed Soviet landers within ~2 hours.", RED),
        ("Getting there", "Gravity assists from planets save fuel but add years. Every kilogram of instruments needs more fuel and a bigger rocket.", BLUE),
        ("Instruments", "Cameras (shape), spectrometers (what it's made of), radar (through clouds and ice), magnetometers (hidden oceans), gravity science (insides), mass spectrometers (sniff gases).", GREEN),
        ("Talking home", "Signals take minutes to hours and get weaker with distance, so data rates fall and spacecraft must make some decisions on their own.", ICE),
        ("Planetary protection", "Don't contaminate a world that might have life: Galileo and Cassini were crashed into their planets on purpose to keep them from hitting Europa or Enceladus.", PURPLE),
    ]
    for i, (head, desc, color) in enumerate(cards):
        col, row = i % 3, i // 3
        body += card(30 + col * 338, 236 + row * 198, 326, 184, head, desc, color, body_size=13)
    return canvas(w, h, "How Missions Are Designed", "Every choice is a tradeoff between science, risk, mass and money", body, SOURCE_2027)


def mission_list() -> str:
    w, h = 1060, 700
    body = ""
    groups = [
        ("VENUS", PLANET_COLORS["Venus"], [
            ("Venus Express", "ESA orbiter 2006-2014"),
            ("DAVINCI", "NASA descent probe, 2030s"),
            ("VERITAS", "NASA radar orbiter, 2030s"),
        ]),
        ("MARS", PLANET_COLORS["Mars"], [
            ("Mars Recon. Orbiter", "NASA, orbiting since 2006"),
            ("MAVEN", "NASA, atmosphere loss, 2014-"),
            ("Perseverance", "NASA rover, Jezero, 2021-"),
        ]),
        ("JUPITER SYSTEM", PLANET_COLORS["Jupiter"], [
            ("Galileo", "NASA orbiter 1995-2003"),
            ("Europa Clipper", "NASA, arrives 2030"),
            ("JUICE", "ESA, arrives 2031"),
        ]),
        ("SATURN SYSTEM", PLANET_COLORS["Saturn"], [
            ("Cassini-Huygens", "NASA/ESA 2004-2017"),
            ("Dragonfly", "NASA Titan drone, launch 2028"),
        ]),
        ("SMALL BODIES", ROCK, [
            ("OSIRIS-REx", "Bennu sample, home 2023"),
            ("Rosetta", "ESA, comet 67P 2014-2016"),
        ]),
        ("TELESCOPES", BLUE, [
            ("Kepler", "Transit survey 2009-2018"),
            ("JWST", "Infrared, L2, 2021-"),
            ("Roman", "Wide-field + microlensing"),
        ]),
    ]
    for i, (head, color, missions) in enumerate(groups):
        col, row = i % 3, i // 3
        x, y = 30 + col * 338, 100 + row * 290
        body += rect(x, y, 326, 274)
        body += f'<rect x="{x}" y="{y}" width="326" height="40" rx="12" fill="{color}" opacity="0.85"/>'
        body += text(x + 18, y + 27, head, 17, "#14182b", "bold")
        for j, (name, note) in enumerate(missions):
            yy = y + 78 + j * 70
            body += text(x + 18, yy, name, 17, TEXT, "bold")
            body += text(x + 18, yy + 24, note, 14, MUTED)
    return canvas(w, h, "The 16 Missions on the 2027 List", "Only these get specific questions -- know the target, agency, dates and main result", body, SOURCE_2027)


INFOGRAPHICS_2027: dict[str, tuple[str, Callable[[], str]]] = {
    "microlensing": ("Gravitational microlensing: a passing star magnifies a background star, and its planet adds a blip.", microlensing),
    "trappist1": ("TRAPPIST-1's seven Earth-sized planets, their years, sizes and the habitable zone.", trappist1),
    "three_systems": ("Comparing the three 2027 extrasolar systems: TRAPPIST-1, Kepler-452 and LHS 1140.", three_systems),
    "habitability_math": ("The 2027 habitability formulas: Stefan-Boltzmann, Wien, albedo, equilibrium temperature, Doppler, tides, gases and Arrhenius.", habitability_math),
    "water_forms": ("Water's many forms: liquid, crystalline and amorphous ice, brines and clathrates.", water_forms),
    "extremophiles": ("Extremophiles, chemolithoautotrophs and tardigrades.", extremophiles),
    "mission_design": ("How missions are designed: mission types, power, radiation, instruments and planetary protection.", mission_design),
    "mission_list": ("The 16 missions on the 2027 Solar System list, grouped by target.", mission_list),
}
