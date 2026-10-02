"""Hand-built infographics for the Solar System learning chapters.

Each function returns a complete SVG document. Every number drawn here is
taken from the coach-supplied Solar System source reader (OpenStax
Astronomy 2e excerpts), the same facts the chapter flashcards and stories
teach -- so a student sees one consistent set of values everywhere.
`INFOGRAPHICS` maps a stable key to (caption, builder); seed.py stores the
rendered SVG as a Diagram data URL on the chapter that lists that key.
"""

import math
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
    mtext,
    para,
    path,
    rect,
    text,
    wrap,
)


# ---------------------------------------------------------------- chapter 1


def mass_budget() -> str:
    w, h = 960, 620
    body = ""
    # Whole-system bar: the Sun is essentially the entire bar.
    body += text(40, 128, "The whole Solar System's mass, as one bar:", 18, TEXT, "bold")
    body += rect(40, 142, 880, 56, fill="#2a1d05", stroke=GOLD, rx=10)
    body += rect(40, 142, 878.2, 56, fill=SUN, stroke="none", rx=10)
    body += text(470, 178, "THE SUN  99.80%", 24, "#3a2200", "bold", "middle")
    body += line(918, 200, 918, 236, GOLD, 2)
    body += text(918, 254, "everything else = 0.20%", 15, GOLD, "bold", "end")

    body += text(40, 300, "Zooming into that tiny 0.20% sliver:", 18, TEXT, "bold")
    rows = [
        ("Jupiter", "0.10", 1.0, PLANET_COLORS["Jupiter"]),
        ("All other planets + dwarf planets", "0.04", 0.4, PLANET_COLORS["Earth"]),
        ("Comets (estimate)", "0.0005 - 0.03", 0.3, ICE),
        ("Moons and rings", "0.00005", 0.02, MUTED),
        ("Asteroids (estimate)", "0.000002", 0.012, ROCK),
        ("Cosmic dust (estimate)", "0.0000001", 0.008, "#dddddd"),
    ]
    for i, (name, pct, frac, color) in enumerate(rows):
        y = 322 + i * 38
        body += text(40, y + 20, name, 15, TEXT)
        body += rect(330, y + 4, 420, 22, fill=PANEL, stroke=PANEL_EDGE, rx=6)
        body += rect(330, y + 4, max(4, 420 * frac), 22, fill=color, stroke="none", rx=6)
        body += text(765, y + 21, pct + " %", 15, GOLD, "bold")
    body += para(40, 568, "Jupiter alone is more massive than all the other planets put together -- about 1,300 Earths could fit inside it.", 130, 14, MUTED)
    return canvas(w, h, "Who Owns the Solar System's Mass?", "Table 7.1 -- percentage of the total mass of the Solar System", body)


def planet_lineup() -> str:
    w, h = 1040, 680
    planets = [
        # name, AU, period (y), diameter (km), density (g/cm^3), mass (10^23 kg)
        ("Mercury", "0.39", "0.24", 4878, "5.4", "3.3", "58.6 d"),
        ("Venus", "0.72", "0.62", 12120, "5.2", "48.7", "243 d (back)"),
        ("Earth", "1.00", "1.00", 12756, "5.5", "59.8", "1 d"),
        ("Mars", "1.52", "1.88", 6787, "3.9", "6.4", "1.03 d"),
        ("Jupiter", "5.20", "11.86", 142984, "1.3", "18,991", "0.41 d"),
        ("Saturn", "9.54", "29.46", 120536, "0.7", "5,686", "0.42 d"),
        ("Uranus", "19.18", "84.07", 51118, "1.3", "866", "0.72 d"),
        ("Neptune", "30.06", "164.82", 49660, "1.6", "1,030", "0.67 d"),
    ]
    body = ""
    body += rect(20, 96, 470, 490, fill="#1d1a12", stroke=ROCK, rx=14, opacity=0.9)
    body += rect(530, 96, 490, 490, fill="#0f1f3a", stroke=ICE, rx=14, opacity=0.9)
    body += text(255, 124, "TERRESTRIAL (inner) planets", 17, ROCK, "bold", "middle")
    body += text(775, 124, "JOVIAN / GIANT (outer) planets", 17, ICE, "bold", "middle")
    body += text(510, 330, "asteroid", 12, MUTED, "middle")
    body += text(510, 345, "belt", 12, MUTED, "middle")
    for k in range(9):
        body += circle(503 + (k % 3) * 7, 260 + k * 7, 1.6, ROCK)
    xs = [75, 190, 305, 420, 600, 728, 852, 960]
    for (name, au, period, diam, dens, mass, day), x in zip(planets, xs):
        r = 5 + 45 * (diam / 142984) ** 0.75
        cy = 230
        body += circle(x, cy, r, PLANET_COLORS[name])
        if name == "Saturn":
            body += f'<ellipse cx="{x}" cy="{cy}" rx="{r * 1.5}" ry="{r * 0.4}" fill="none" stroke="#f3e2b0" stroke-width="3" opacity="0.8"/>'
        body += text(x, 320, name, 16, TEXT, "bold", "middle")
        body += text(x, 348, f"{au} AU", 14, GOLD, "bold", "middle")
        body += text(x, 370, f"year {period} y", 13, TEXT, anchor="middle")
        body += text(x, 392, f"{diam:,} km", 13, TEXT, anchor="middle")
        body += text(x, 414, f"{dens} g/cm3", 13, TEXT, anchor="middle")
        body += text(x, 436, f"day {day}", 13, TEXT, anchor="middle")
        body += text(x, 456, f"{mass}e23 kg", 12, MUTED, anchor="middle")
    body += para(36, 486, "Small, rocky and metal-rich, with solid surfaces scarred by craters, mountains and volcanoes. Dense: 3.9 to 5.5 g/cm3 (water = 1). Earth is the densest planet.", 60, 14, TEXT)
    body += para(546, 486, "Huge worlds of light gases, liquids and ices with no solid surface to land on -- like giant spherical oceans around small dense cores. Saturn (0.7) would float in water!", 62, 14, TEXT)
    body += para(30, 606, "Every planet orbits the Sun in the same direction and in nearly the same flat plane. Sizes of the small planets are enlarged so you can see them; the numbers are real (Table 7.2). 1 AU = Earth-Sun distance.", 140, 13, MUTED)
    return canvas(w, h, "Meet the Eight Planets", "Distance from the Sun, year, diameter, density, day and mass", body)


# ---------------------------------------------------------------- chapter 2


def nebula_steps() -> str:
    w, h = 1040, 640
    body = ""
    titles = ["1. A cloud collapses", "2. It spins and flattens", "3. Dust clumps together", "4. Planets + leftovers"]
    for i, t in enumerate(titles):
        x = 24 + i * 254
        body += rect(x, 100, 236, 300)
        body += text(x + 118, 128, t, 15, GOLD, "bold", "middle")
        if i < 3:
            body += line(x + 238, 250, x + 252, 250, GOLD, 3, arrow=True)
    # panel 1: lumpy cloud
    for k, (dx, dy, r) in enumerate([(0, 0, 60), (-40, 20, 40), (45, 25, 38), (10, -40, 36), (-30, -30, 30)]):
        body += circle(142 + dx, 260 + dy, r, "#6c5a8f", opacity=0.45)
    body += text(142, 380, "gravity pulls gas + dust inward", 12, MUTED, anchor="middle")
    # panel 2: spinning disk with protosun
    body += '<ellipse cx="396" cy="260" rx="100" ry="26" fill="#8a6fbf" opacity="0.55"/>'
    body += circle(396, 260, 20, "url(#sunglow)")
    body += path("M 330 220 A 80 30 0 0 1 470 222", GOLD, 2, arrow=True)
    body += text(396, 380, "the protosun forms in the middle", 12, MUTED, anchor="middle")
    # panel 3: inner rock / frost line / outer ice
    body += circle(560, 260, 16, "url(#sunglow)")
    for k in range(10):
        body += circle(590 + (k % 5) * 10, 236 + (k // 5) * 48, 4, ROCK)
    body += line(655, 160, 655, 360, ICE, 2, dash="6 5")
    body += text(655, 154, "frost line", 12, ICE, "bold", "middle")
    for k in range(12):
        body += circle(675 + (k % 4) * 14, 226 + (k // 4) * 24, 5, ICE)
    body += text(605, 360, "hot: rock", 12, ROCK, "bold", "middle")
    body += text(700, 360, "cold: ice", 12, ICE, "bold", "middle")
    body += text(651, 380, "+ rock", 12, MUTED, anchor="middle")
    # panel 4: final system
    sx, sy = 904, 256
    body += circle(sx, sy, 12, "url(#sunglow)")
    for r, color, size in [(24, PLANET_COLORS["Mercury"], 3), (36, PLANET_COLORS["Earth"], 4), (47, PLANET_COLORS["Mars"], 3)]:
        body += circle(sx, sy, r, "none", PANEL_EDGE, 1)
        body += circle(sx + r, sy, size, color)
    for k in range(16):
        body += circle(sx + 58 * math.cos(k * 0.39), sy + 58 * math.sin(k * 0.39), 1.6, ROCK)
    body += circle(sx, sy, 72, "none", PANEL_EDGE, 1)
    body += circle(sx - 72, sy, 9, PLANET_COLORS["Jupiter"])
    body += circle(sx, sy, 92, "none", PANEL_EDGE, 1, opacity=0.6)
    body += circle(sx, sy - 92, 7, PLANET_COLORS["Saturn"])
    for k in range(28):
        body += circle(sx + 108 * math.cos(k * 0.2245), sy + 108 * math.sin(k * 0.2245) * 0.55 + 0, 1.4, ICE, opacity=0.7)
    body += text(sx, 380, "leftovers: asteroid + Kuiper belts", 12, MUTED, anchor="middle")
    clues = [
        ("Motion clue", "All planets orbit in nearly the same plane and the same direction -- and the Sun spins that way too. They formed together from one spinning cloud: the solar nebula.", GOLD),
        ("Chemistry clue", "The Sun, Jupiter and Saturn share the same hydrogen-rich recipe. The inner planets are mostly heavy iron and silicon -- the light gases and ices were lost there.", ICE),
        ("Why was the inside hot?", "Not mainly sunlight (the dense disk blocked it). Inner material moved faster (Kepler's laws), so more friction heated it -- too warm for water ice.", RED),
        ("Violent finish", "Planetesimals (up to ~100 km) crashed together. Impacts + radioactive heat melted young planets so they differentiated into layers.", PURPLE),
    ]
    for i, (head, bodytxt, color) in enumerate(clues):
        body += card(24 + i * 254, 418, 236, 190, head, bodytxt, color, body_size=13)
    return canvas(w, h, "How the Solar System Was Born", "The solar nebula model -- about 4.5 billion years ago", body)


# ---------------------------------------------------------------- chapter 3


def earth_interior() -> str:
    w, h = 1000, 620
    cx, cy = 300, 560
    body = ""
    layers = [
        (420, "#3c6e3a", "Crust"),
        (406, "#c0582b", "Mantle"),
        (220, "#f2a33a", "Outer core"),
        (95, "#ffe27a", "Inner core"),
    ]
    for r, color, _ in layers:
        body += f'<path d="M {cx - r} {cy} A {r} {r} 0 0 1 {cx + r} {cy} Z" fill="{color}"/>'
    body += text(cx, cy - 430, "Crust (thin skin!)", 15, GREEN, "bold", "middle")
    body += text(cx, cy - 300, "MANTLE", 22, "#fff", "bold", "middle")
    body += text(cx, cy - 276, "mostly solid rock, to 2,900 km deep", 14, "#fff", anchor="middle")
    body += text(cx, cy - 160, "OUTER CORE", 18, "#3a1b00", "bold", "middle")
    body += text(cx, cy - 140, "liquid metal", 14, "#3a1b00", anchor="middle")
    body += text(cx, cy - 40, "INNER CORE", 15, "#3a2a00", "bold", "middle")
    body += text(cx, cy - 22, "solid metal", 13, "#3a2a00", anchor="middle")
    body += text(cx, cy + 0, "center: 6,378 km down", 12, "#3a2a00", anchor="middle")

    x = 640
    body += card(x, 100, 340, 150, "Two kinds of crust", "Oceanic crust: covers 55% of Earth, ~6 km thick, dark volcanic basalt. Continental crust: 45%, 20-70 km thick, mostly granite. Both ~3 g/cm3. The crust is only 0.3% of Earth's mass.", GREEN, body_size=13)
    body += card(x, 262, 340, 150, "How do we know?", "Nobody can dig there! Seismic waves from earthquakes ring through Earth like sound through a struck bell. They bend (refract) between layers, leaving 'shadow' zones that reveal liquid vs solid layers -- like an ultrasound of the planet.", BLUE, body_size=13)
    body += card(x, 424, 340, 160, "Earth by the numbers", "Diameter 12,756 km - radius 6,378 km - density 5.514 g/cm3 (densest planet) - escape velocity 11.2 km/s - day 23 h 56 m 4 s - air pressure 1.00 bar - 1.00 AU from the Sun.", GOLD, body_size=13)
    return canvas(w, h, "Inside Planet Earth", "Layers found by listening to earthquakes (Figure 8.3)", body)


def atmosphere_layers() -> str:
    w, h = 1000, 620
    body = ""
    bands = [
        (100, 190, "#1b1450", "IONOSPHERE (above 100 km)", "So thin satellites glide through. Solar UV strips electrons off atoms. Light atoms like hydrogen and helium leak away into space."),
        (190, 280, "#24206b", "MESOSPHERE", "Very thin, very cold air."),
        (280, 420, "#203f88", "STRATOSPHERE + OZONE LAYER", "Ozone (O3) near the top absorbs dangerous ultraviolet light and warms this layer. CFCs were banned -- the Antarctic ozone hole is slowly healing."),
        (420, 560, "#2f6fb5", "TROPOSPHERE (where we live)", "Weather happens here. Temperature drops as you go up."),
    ]
    for y1, y2, color, name, desc in bands:
        body += rect(40, y1, 560, y2 - y1, fill=color, stroke="none", rx=0)
        body += text(56, y1 + 26, name, 16, GOLD, "bold")
        body += para(56, y1 + 50, desc, 70, 13, TEXT)
    body += rect(40, 398, 560, 14, fill="#7fdcff", stroke="none", rx=4, opacity=0.6)
    body += text(590, 409, "ozone", 12, "#062a3a", "bold", "end")
    body += rect(40, 560, 560, 20, fill="#3d7a3a", stroke="none", rx=0)
    body += text(320, 575, "ground", 12, "#fff", anchor="middle")
    body += line(24, 580, 24, 104, MUTED, 2, arrow=True)
    body += text(18, 96, "height", 12, MUTED)

    x = 630
    body += text(x, 120, "What is air made of?", 18, TEXT, "bold")
    for i, (gas, pct, color) in enumerate([("Nitrogen N2", 78, BLUE), ("Oxygen O2", 21, GREEN), ("Argon Ar", 1, PURPLE)]):
        y = 150 + i * 42
        body += text(x, y - 6, f"{gas}  {pct}%", 14, TEXT, "bold")
        body += rect(x, y, 340, 18, fill=PANEL, stroke=PANEL_EDGE, rx=6)
        body += rect(x, y, max(6, 340 * pct / 100), 18, fill=color, stroke="none", rx=6)
    body += para(x, 278, "+ traces of water vapor, CO2 and other gases, plus dust and droplets.", 44, 13, MUTED)
    body += card(x, 320, 340, 250, "If Earth got hotter...", "Boil the oceans (100 C) and they'd add ~300 bars of water vapor (10 m of water presses like 1 bar; the oceans average ~300 m deep spread over Earth). Bake the carbonate rocks and they'd release ~70 bars of CO2. A hot Earth's air would be ~400 bars of steam + CO2 -- like Venus! Today's CO2 is only 0.0005 bar.", RED, body_size=13)
    return canvas(w, h, "Earth's Atmosphere, Layer by Layer", "Structure and composition (Figure 8.12)", body)


def greenhouse() -> str:
    w, h = 1000, 600
    body = ""
    body += circle(110, 150, 50, "url(#sunglow)")
    body += rect(0, 470, 640, 90, fill="#2f5a2d", stroke="none", rx=0)
    body += text(320, 520, "GROUND absorbs sunlight and warms up", 16, "#e8ffe0", "bold", "middle")
    body += '<rect x="0" y="230" width="640" height="150" fill="#5b8bd6" opacity="0.18"/>'
    body += text(620, 252, "greenhouse gases: CO2, methane, water vapor", 13, ICE, "bold", "end")
    for k in range(3):
        x = 170 + k * 70
        body += line(x, 206, x + 116, 460, GOLD, 4, arrow=True)
    body += text(170, 196, "visible sunlight passes through", 13, GOLD, "bold")
    for k in range(3):
        x0 = 400 + k * 70
        body += path(f"M {x0} 465 q 10 -20 0 -40 q -10 -20 0 -40 q 10 -20 0 -40 q -10 -20 0 -30", RED, 3, arrow=True)
    body += path("M 470 330 q 30 -10 60 30 q 20 30 0 70", RED, 2, arrow=True, dash="5 4")
    body += text(470, 220, "infrared (heat) tries to escape...", 13, RED, "bold")
    body += text(520, 425, "...but is trapped", 13, RED, "bold")
    x = 660
    body += card(x, 100, 320, 170, "Like a car in the sun", "Glass lets sunlight in but slows heat getting out, so the car gets much hotter than sunlight alone would make it. Greenhouse gases are the 'glass' of a planet.", GOLD, body_size=13)
    body += card(x, 282, 320, 140, "Good news", "Earth's natural greenhouse effect keeps us warm. Without it Earth would be well below freezing -- a global ice age. (The text gives ~23 C in one chapter and ~33 C in another.)", GREEN, body_size=13)
    body += card(x, 434, 320, 140, "Bad news", "Burning fossil fuels adds CO2: up ~30% in a century, rising >0.5%/yr, heading for double pre-industrial levels this century. That is global warming.", RED, body_size=13)
    return canvas(w, h, "The Greenhouse Effect", "Why gases like CO2 make a planet warmer (Figure 8.17)", body)


# ---------------------------------------------------------------- chapter 4


def earth_life_timeline() -> str:
    w, h = 1100, 580
    body = ""
    x0, x1, y = 60, 1040, 300
    body += line(x0, y, x1, y, GOLD, 4)

    def xpos(gya: float) -> float:
        return x0 + (4.6 - gya) / 4.6 * (x1 - x0)

    events = [
        (4.5, "Earth + Sun form", "4.5 billion yrs ago", True),
        (4.0, "Heavy bombardment", "4.1 - 3.8 bya; impacts could sterilize the surface", False),
        (3.9, "Oldest surviving rocks", "life already existed (chemical evidence)", True),
        (3.5, "Stromatolites + microbe fossils", "oldest stromatolite 3.47 bya", False),
        (3.4, "Photosynthesis at work", "strong fossil evidence", True),
        (2.4, "Oxygen builds up in the air", "~2.4 bya (some data say ~2 bya); ozone forms", False),
        (0.6, "Abundant fossils", "last 600 million yrs (<15% of history)", True),
        (0.065, "Dinosaur-killing impact", "65 million yrs ago", False),
    ]
    # Markers sit at their true dates; labels are spread evenly and joined by
    # leader lines, alternating above/below, so crowded early events stay readable.
    for i, (gya, title, sub, up) in enumerate(events):
        x = xpos(gya)
        lx = 120 + i * 122
        body += circle(x, y, 8, GOLD)
        if up:
            body += path(f"M {x:.1f} {y - 8} L {lx:.1f} {y - 70}", MUTED, 1.5)
            body += text(lx, y - 110, title, 14, TEXT, "bold", "middle")
            body += mtext(lx, y - 92, wrap(sub, 32), 12, MUTED, anchor="middle")
        else:
            body += path(f"M {x:.1f} {y + 8} L {lx:.1f} {y + 62}", MUTED, 1.5)
            body += text(lx, y + 82, title, 14, TEXT, "bold", "middle")
            body += mtext(lx, y + 100, wrap(sub, 32), 12, MUTED, anchor="middle")
    for gya in [4, 3, 2, 1, 0]:
        body += text(xpos(gya), y + 26, f"{gya} bya" if gya else "today", 11, MUTED, anchor="middle")
    body += para(60, 490, "Plants (from blue-green algae) release oxygen. Once oxygen built up, the ozone layer blocked deadly UV, life could move onto land, and animals could breathe oxygen -- the 'waste product' of plants. Life also pulled most CO2 out of our air.", 150, 14, TEXT)
    return canvas(w, h, "Life's Timeline on Earth", "bya = billion years ago", body)


# ---------------------------------------------------------------- chapter 5


def three_planets() -> str:
    w, h = 1000, 640
    rows = [
        ("Distance from Sun (AU)", "1.00", "0.72", "1.52"),
        ("Year (Earth years)", "1.00", "0.61", "1.88"),
        ("Mass (Earth = 1)", "1.00", "0.82", "0.11"),
        ("Diameter (km)", "12,756", "12,102", "6,790"),
        ("Density (g/cm3)", "5.5", "5.3", "3.9"),
        ("Surface gravity (Earth = 1)", "1.00", "0.91", "0.38"),
        ("Escape velocity (km/s)", "11.2", "10.4", "5.0"),
        ("Rotation (day)", "23.9 h", "243 d (backward!)", "24.6 h"),
        ("Surface area (Earth = 1)", "1.00", "0.90", "0.28"),
        ("Air pressure (bar)", "1.00", "90", "0.007"),
    ]
    body = ""
    cols = [(40, 300, "Property", MUTED), (360, 190, "EARTH", PLANET_COLORS["Earth"]), (560, 210, "VENUS", PLANET_COLORS["Venus"]), (780, 190, "MARS", PLANET_COLORS["Mars"])]
    for x, cw, name, color in cols:
        body += text(x + (0 if name == "Property" else cw / 2), 120, name, 18, color, "bold", "start" if name == "Property" else "middle")
    for i, row in enumerate(rows):
        y = 136 + i * 40
        body += rect(30, y, 940, 36, fill=PANEL if i % 2 == 0 else "#122042", stroke="none", rx=6)
        for (x, cw, _, color), value in zip(cols, row):
            if x == 40:
                body += text(x, y + 24, value, 15, TEXT)
            else:
                body += text(x + cw / 2, y + 24, value, 15, TEXT, "bold", "middle")
    body += para(40, 556, "Venus is Earth's near-twin in size, mass and density -- but its air is ~90 times thicker and its surface is ~730 K (over 850 F). Mars is small (0.11 Earth masses) with air less than 1% as thick as ours.", 140, 14, MUTED)
    return canvas(w, h, "Earth vs. Venus vs. Mars", "Three neighbors that turned out very differently (Table 10.1)", body)


def venus_geology() -> str:
    w, h = 1000, 600
    body = ""
    cards = [
        ("Lava plains", "About 75% of Venus is lowland lava plains, made by huge eruptions -- like the Moon's maria. No subduction zones: Venus never had plate tectonics.", ROCK),
        ("Two 'continents'", "Aphrodite (size of Africa, along the equator) and Ishtar (size of Australia, in the north). Ishtar holds the Maxwell Mountains, 11 km high -- the only feature named after a man.", GOLD),
        ("Volcanoes", "Sif Mons: ~500 km wide, 3 km high (broader but lower than Mauna Loa). 'Pancake domes': ~25 km wide, ~2 km tall, from thick sludgy lava.", RED),
        ("Coronae + tectonics", "Rising lava that never reaches the surface pushes up round bulges called coronae (like the 'Miss Piggy' Fotla Corona). Mantle convection cracks the crust into ridges and rift valleys.", PURPLE),
        ("Craters tell the age", "Few craters < 10 km: the thick air stops rocks smaller than ~1 km. Big craters say the surface is only 300-600 million years old. Largest crater: Mead, 275 km.", BLUE),
        ("Hidden world", "Clouds reflect ~70% of sunlight, so we map Venus by radar (Magellan). Venera 7 (1970) was the first probe to land and send data. Mariner 2 (1962) flew by first.", GREEN),
    ]
    for i, (head, desc, color) in enumerate(cards):
        x = 30 + (i % 3) * 318
        y = 100 + (i // 3) * 240
        body += card(x, y, 300, 222, head, desc, color, body_size=14)
    return canvas(w, h, "The Geology of Venus", "A young, volcanic surface with no plate tectonics (Section 10.2)", body)


def runaway_greenhouse() -> str:
    w, h = 1000, 620
    body = ""
    cx, cy, r = 330, 350, 170
    steps = [
        (-90, "A little extra heat", "(the young Sun slowly brightens)"),
        (0, "Oceans evaporate", "and rocks release CO2"),
        (90, "More CO2 + water vapor", "in the air"),
        (180, "Stronger greenhouse", "traps even more heat"),
    ]
    for angle, title, sub in steps:
        a = math.radians(angle)
        x, y = cx + r * math.cos(a), cy + r * math.sin(a)
        body += rect(x - 105, y - 36, 210, 72, fill=PANEL, stroke=RED, rx=14)
        body += text(x, y - 6, title, 15, TEXT, "bold", "middle")
        body += text(x, y + 16, sub, 12, MUTED, anchor="middle")
    for a1 in [-60, 30, 120, 210]:
        s, e = math.radians(a1), math.radians(a1 + 40)
        x1, y1 = cx + r * 0.78 * math.cos(s), cy + r * 0.78 * math.sin(s)
        x2, y2 = cx + r * 0.78 * math.cos(e), cy + r * 0.78 * math.sin(e)
        body += path(f"M {x1:.1f} {y1:.1f} A {r * 0.78} {r * 0.78} 0 0 1 {x2:.1f} {y2:.1f}", RED, 3, arrow=True)
    body += text(cx, cy - 4, "RUNAWAY", 22, RED, "bold", "middle")
    body += text(cx, cy + 20, "loop", 16, RED, anchor="middle")
    x = 640
    body += card(x, 100, 330, 170, "The point of no return", "Sunlight's UV splits water vapor. Light hydrogen escapes to space; oxygen bonds with rocks. Once the water is gone it can't come back -- the loss is irreversible.", GOLD, body_size=13)
    body += card(x, 282, 330, 150, "Venus today", "~1 million times more CO2 than Earth -> surface over 700 K, hotter than an oven's self-clean cycle. Strong greenhouse warming of about 510 C.", RED, body_size=13)
    body += card(x, 444, 330, 140, "Lesson for Earth", "Earth's CO2 is safely locked in rocks and oceans. A runaway effect is an evolution, not just a big greenhouse -- and nobody knows exactly where the tipping point is.", GREEN, body_size=13)
    return canvas(w, h, "The Runaway Greenhouse Effect", "How Venus may have turned from Earthlike to scorching (Section 10.3)", body)


# ---------------------------------------------------------------- chapter 6


def mars_water() -> str:
    w, h = 1040, 640
    body = ""
    body += text(30, 116, "Three kinds of water-carved features", 19, TEXT, "bold")
    feats = [
        ("Runoff channels", "Small, twisting valleys in the old highlands: a few m deep, tens of m wide, 10-20 km long. Look like rain runoff. ~4 billion years old (crater counts).", BLUE),
        ("Outflow channels", "Huge: 10+ km wide, hundreds of km long. Carved by catastrophic floods when frozen ground (permafrost) was suddenly melted -- maybe by volcanic heat.", PURPLE),
        ("Gullies + 'RSL' streaks", "Very young (no craters on them). Dark streaks grow each season ('recurring slope lineae'). 2015 spectra found hydrated salts -- salty water may flow briefly today.", GREEN),
    ]
    for i, (head, desc, color) in enumerate(feats):
        body += card(30 + i * 336, 130, 316, 190, head, desc, color, body_size=14)
    body += text(30, 360, "Rovers that followed the water", 19, TEXT, "bold")
    rovers = [
        ("Spirit (2004-2010)", "Gusev crater lake bed -- but lava covered it."),
        ("Opportunity", "Layered salty-lake rock + hematite 'blueberries'."),
        ("Curiosity (2012)", "Gale crater: ancient lake mudstones; proved a habitable past."),
        ("Perseverance", "Jezero crater river delta (45 km); collecting samples."),
    ]
    for i, (name, desc) in enumerate(rovers):
        x = 30 + i * 252
        body += rect(x, 374, 236, 130, fill=PANEL, stroke=ROCK)
        body += text(x + 14, 400, name, 15, ROCK, "bold")
        body += para(x + 14, 424, desc, 30, 13, TEXT)
    body += para(30, 540, "Lowell's 'canals' were NOT these channels -- the channels are too small to see from Earth and aren't straight. The canals were an optical illusion. The guiding rule for finding life is 'follow the water'.", 150, 14, MUTED)
    return canvas(w, h, "Mars: Following the Water", "Evidence that rivers, lakes and floods once shaped the red planet (Section 10.5)", body)


def mars_ice() -> str:
    w, h = 1000, 600
    body = ""
    body += card(30, 100, 460, 200, "Why no lakes on Mars today?", "Air pressure is only 0.007 bar (<1% of Earth's -- like 30 km up on Earth). Below ~0.006 bar, liquid water can't exist: ice turns straight into vapor, like dry ice. Salt lowers the freezing point, so salty water can sometimes stay liquid briefly.", BLUE, body_size=14)
    body += card(30, 316, 460, 250, "Martian air + clouds", "95% CO2, ~3% nitrogen, ~2% argon. Wind is fast but weak (thin air) -- though it lifts fine red dust (iron oxides) into planet-wide storms and carves yardangs. Three cloud types: dust, water-ice, and CO2 'dry ice' hazes (need ~150 K, never happens on Earth).", GOLD, body_size=14)
    x = 520
    body += card(x, 100, 450, 140, "Seasonal caps = dry ice", "Thin frozen CO2 that condenses from the air below ~150 K each winter and spreads down to ~50 degrees latitude by spring.", ICE, body_size=14)
    body += card(x, 252, 450, 140, "South permanent cap", "350 km across; frozen CO2 mixed with lots of water ice. Stays at 150 K all summer.", ICE, body_size=14)
    body += card(x, 404, 450, 162, "North permanent cap", "Water ice, never smaller than 1,000 km across, ~3 km thick, ~10 million km3 (like the Mediterranean Sea). Sits in a basin as big as the Arctic Ocean -- maybe an old sea. Phoenix (2008) dug up ice that sublimated.", ICE, body_size=14)
    return canvas(w, h, "Mars: Air, Ice and Polar Caps", "Where the water on Mars is hiding today (Section 10.5)", body)


# ---------------------------------------------------------------- chapter 7


def galilean_moons() -> str:
    w, h = 1060, 640
    body = ""
    body += circle(-40, 270, 150, PLANET_COLORS["Jupiter"])
    for k, dy in enumerate([-80, -30, 20, 70]):
        body += f'<rect x="-190" y="{270 + dy}" width="300" height="12" fill="#b07a46" opacity="0.5"/>'
    body += text(30, 450, "JUPITER", 16, GAS, "bold")
    moons = [
        ("Io", 3640, "3.5", "60%", "#f4d35e", "Most volcanic world in the Solar System. Sulfur 'snow'. Interior fully melted."),
        ("Europa", 3130, "3.0", "70%", "#e8e2d0", "Smooth young ice over a salty ocean. Surface only a few million years old."),
        ("Ganymede", 5270, "1.9", "40%", "#a39e93", "LARGEST moon. Layered, has a magnetic field, likely hidden water."),
        ("Callisto", 4820, "1.8", "20%", "#6d6459", "Ancient, cratered, never fully layered. Geologically dead 4+ billion yrs."),
    ]
    xs = [250, 450, 660, 890]
    for (name, diam, dens, refl, color, note), x in zip(moons, xs):
        r = diam / 5270 * 46
        body += circle(x, 200, r, color)
        body += text(x, 280, name, 20, TEXT, "bold", "middle")
        body += text(x, 304, f"{diam:,} km", 14, GOLD, "bold", "middle")
        body += text(x, 324, f"density {dens} g/cm3", 13, TEXT, anchor="middle")
        body += text(x, 344, f"reflects {refl}", 13, TEXT, anchor="middle")
        body += mtext(x, 372, wrap(note, 24), 13, MUTED, anchor="middle")
    body += f'<defs><linearGradient id="tide" x1="0" x2="1"><stop offset="0%" stop-color="{RED}"/><stop offset="100%" stop-color="{BLUE}"/></linearGradient></defs>'
    body += rect(200, 480, 760, 22, fill="url(#tide)", stroke="none", rx=11)
    body += text(200, 524, "closest to Jupiter: strongest tidal heating, most active, rockiest", 13, RED, "bold")
    body += text(960, 524, "farthest: weakest heating, coldest, iciest", 13, BLUE, "bold", "end")
    body += para(30, 562, "Compare: our Moon is 3,476 km, density 3.3, reflects 12%. Saturn's Titan is 5,150 km, density 1.9. Discovered by Galileo in 1610; Ganymede and Callisto are about the size of Mercury; Io and Europa about the size of our Moon.", 160, 13, MUTED)
    return canvas(w, h, "The Galilean Moons of Jupiter", "A mini solar system: rocky and hot inside, icy and cold outside (Table 12.1)", body)


def tidal_heating() -> str:
    w, h = 1000, 600
    body = ""
    body += circle(260, 330, 110, PLANET_COLORS["Jupiter"])
    body += text(260, 336, "JUPITER", 18, "#3a2200", "bold", "middle")
    body += f'<ellipse cx="300" cy="330" rx="230" ry="190" fill="none" stroke="{MUTED}" stroke-width="2" stroke-dasharray="6 6"/>'
    body += '<ellipse cx="530" cy="330" rx="30" ry="22" fill="#f4d35e"/>'
    body += text(530, 300, "Io (stretched)", 13, TEXT, "bold", "middle")
    body += '<ellipse cx="300" cy="140" rx="20" ry="18" fill="#f4d35e"/>'
    body += text(300, 118, "Io farther: bulge relaxes", 12, MUTED, anchor="middle")
    body += line(500, 330, 380, 330, GOLD, 2, arrow=True)
    body += text(430, 350, "pull", 12, GOLD, anchor="middle")
    x = 600
    body += card(x, 100, 370, 150, "The squeeze", "Io is about as far from Jupiter as our Moon is from Earth, but Jupiter is 300+ times more massive than Earth. Its gravity pulls Io into a stretched shape with a bulge kilometers high.", GOLD, body_size=13)
    body += card(x, 262, 370, 150, "The wobble", "Tugs from Europa and Ganymede keep Io's orbit slightly oval (eccentric). So Io moves nearer and farther and twists back and forth every orbit -- its bulge keeps flexing.", PURPLE, body_size=13)
    body += card(x, 424, 370, 150, "The heat", "Bend a wire coat hanger back and forth and it gets hot. Flexing heats Io the same way: it melted Io's interior and drove off water and CO2. Tidal force = unequal pull on the near and far sides.", RED, body_size=13)
    return canvas(w, h, "Tidal Heating", "How gravity can melt a moon (Section 12.2)", body)


# ---------------------------------------------------------------- chapter 8


def ocean_worlds() -> str:
    w, h = 1060, 640
    body = ""

    def section(cx: float, label: str) -> str:
        s = circle(cx, 260, 120, "#dfe9f5")
        s += circle(cx, 260, 104, "#2a6fd6")
        s += circle(cx, 260, 70, "#8a6a4a")
        s += text(cx, 266, "rock", 14, "#fff", "bold", "middle")
        s += text(cx, 175, "ocean", 13, "#fff", "bold", "middle")
        s += text(cx, 410, label, 22, GOLD, "bold", "middle")
        return s

    body += section(180, "EUROPA (Jupiter)")
    body += section(530, "ENCELADUS (Saturn)")
    body += section(880, "GANYMEDE (Jupiter)")
    for k in range(6):
        body += path(f"M {500 + k * 12} 150 q {-8 + k * 3} -40 {-4 + k * 6} -60", ICE, 2)
    body += text(530, 96, "plumes!", 13, ICE, "bold", "middle")
    body += para(40, 440, "Thin cracked ice shell (about 1 to 20+ km; Juno data in 2024 hint it may be twice as thick). Very few craters: surface a few million years old at most. Its magnetic 'signature' matches a salty liquid ocean. Europa Clipper launched Oct 2024, arrives 2030.", 46, 13, TEXT)
    body += para(390, 440, "Only ~500 km across. Cassini (2005) found geysers at the south pole venting ~250 kg of ice + gas per second, with salts -- ocean samples free for the taking by a passing spacecraft!", 46, 13, TEXT)
    body += para(740, 440, "The largest moon has a magnetic field (a partly molten interior) and very likely liquid water deep inside. Tidal heating from Jupiter keeps it partly active.", 44, 13, TEXT)
    return canvas(w, h, "Ocean Worlds of the Outer Solar System", "Liquid water hidden under ice, kept warm by tidal heating", body)


def titan_cycle() -> str:
    w, h = 1040, 620
    body = ""
    for i, (x, title, liquid, color, temp) in enumerate([(30, "EARTH: water cycle", "water", BLUE, "~15 C average"), (530, "TITAN: methane cycle", "methane + ethane", GAS, "94 K (-179 C)")]):
        body += rect(x, 100, 480, 300, fill=PANEL, stroke=color)
        body += text(x + 240, 130, title, 19, color, "bold", "middle")
        body += rect(x + 30, 330, 200, 40, fill=color, stroke="none", rx=8, opacity=0.8)
        body += text(x + 130, 356, f"lakes of {liquid}", 13, "#0b1530", "bold", "middle")
        body += path(f"M {x + 130} 320 C {x + 130} 240, {x + 240} 200, {x + 300} 190", MUTED, 2, arrow=True)
        body += text(x + 150, 260, "evaporates", 12, MUTED)
        body += f'<ellipse cx="{x + 350}" cy="180" rx="70" ry="28" fill="#c9d3e8" opacity="0.8"/>'
        body += text(x + 350, 186, "clouds", 13, "#0b1530", "bold", "middle")
        for k in range(5):
            body += line(x + 320 + k * 14, 214, x + 312 + k * 14, 250, color, 2)
        body += text(x + 350, 274, "rain", 13, color, "bold", "middle")
        body += path(f"M {x + 400} 300 C {x + 360} 340, {x + 300} 350, {x + 240} 350", MUTED, 2, arrow=True)
        body += text(x + 330, 384, f"flows down valleys -- {temp}", 12, MUTED, anchor="middle")
    body += card(30, 420, 320, 170, "Thick orange air", "The only moon with a substantial atmosphere: mostly nitrogen + ~5% methane. Sunlight builds organic molecules (tholins, HCN...) that make an orange haze.", GOLD, body_size=13)
    body += card(366, 420, 320, 170, "Huygens landed!", "Jan 14, 2005: the only landing in the outer Solar System. Found ice 'boulders' hard as rock, an orange sky, sunlight 1,000x dimmer than on Earth. Lasted ~90 minutes.", ICE, body_size=13)
    body += card(702, 420, 308, 170, "Life as we don't know it?", "Too cold for liquid water, but liquid hydrocarbons might play water's role. NASA's Dragonfly drone launches in 2027 to study pre-biotic chemistry.", GREEN, body_size=13)
    return canvas(w, h, "Titan: A Weird Twin of Earth", "Saturn's giant moon has rain, rivers and lakes -- of methane (Section 12.3)", body)


# ---------------------------------------------------------------- chapter 9


def mountain_heights() -> str:
    w, h = 1000, 600
    body = ""
    base = 480
    scale = 15  # px per km
    peaks = [
        ("Mauna Loa", "Earth", 9, 140, PLANET_COLORS["Earth"], "volcano"),
        ("Mt. Everest", "Earth", 9, 300, "#9fb4c8", "crust squeezed up"),
        ("Maxwell Mts", "Venus", 11, 460, PLANET_COLORS["Venus"], "crust squeezed up"),
        ("Olympus Mons", "Mars", 21, 700, PLANET_COLORS["Mars"], "volcano, 500 km wide"),
    ]
    for name, planet, km, x, color, kind in peaks:
        top = base - km * scale
        half = 70 if name != "Olympus Mons" else 200
        body += f'<path d="M {x - half} {base} L {x} {top} L {x + half} {base} Z" fill="{color}" opacity="0.85"/>'
        body += text(x, top - 30, name, 15, TEXT, "bold", "middle")
        body += text(x, top - 12, f"{planet}: ~{km} km" if name != "Olympus Mons" else "Mars: 20+ km", 13, GOLD, "bold", "middle")
        body += text(x, base + 22, kind, 12, MUTED, anchor="middle")
    body += line(40, base, 960, base, MUTED, 2)
    body += line(40, base - 10 * scale, 960, base - 10 * scale, RED, 1.5, dash="6 6")
    body += text(955, base - 10 * scale - 8, "~10 km: limit with Earth/Venus gravity", 12, RED, "bold", "end")
    body += para(40, 540, "Why so tall on Mars? (1) Gravity is only ~1/3 of Earth's, so rock can hold up a taller pile. (2) Mars has no moving plates, so one volcano sits over the same hot spot for hundreds of millions of years. On Earth the plate slides on, making a chain like Hawaii.", 150, 13, TEXT)
    return canvas(w, h, "Tallest Mountains: Earth, Venus, Mars", "Heights above the surroundings (vertical scale exaggerated; Figure 14.19)", body)


def baked_potato() -> str:
    w, h = 1040, 640
    body = ""
    worlds = [
        ("Moon", 3476, "#bdbdbd", "Volcanism stopped ~3.3 billion yrs ago. Geologically dead."),
        ("Mercury", 4878, PLANET_COLORS["Mercury"], "Probably went quiet about when the Moon did."),
        ("Mars", 6787, PLANET_COLORS["Mars"], "In between: Tharsis volcanoes active on and off to the present era."),
        ("Venus", 12120, PLANET_COLORS["Venus"], "Very active, but no plate tectonics. 'Blob tectonics'; surface <= ~500 million yrs."),
        ("Earth", 12756, PLANET_COLORS["Earth"], "Plate tectonics recycles the crust: most of it < 200 million yrs old."),
    ]
    for i, (name, diam, color, note) in enumerate(worlds):
        x = 110 + i * 200
        r = 14 + diam / 12756 * 52
        body += circle(x, 220, r, color)
        body += text(x, 310, name, 18, TEXT, "bold", "middle")
        body += mtext(x, 336, wrap(note, 24), 13, MUTED, anchor="middle")
    body += line(60, 440, 980, 440, GOLD, 3, arrow=True)
    body += text(520, 466, "BIGGER WORLD = holds heat longer = stays geologically active longer", 15, GOLD, "bold", "middle")
    body += card(60, 490, 440, 110, "The 'baked potato effect'", "A big potato stays hot inside far longer than a small one. Heat comes from leftover formation heat + radioactive decay.", GOLD, body_size=13)
    body += card(530, 490, 450, 110, "The exceptions: tidal heating", "Io, Europa (Jupiter) and maybe Enceladus (Saturn) are small but kept warm by tides. Icy moons erupt water and ice instead of rock lava.", RED, body_size=13)
    return canvas(w, h, "Why Some Worlds Are Still Active", "Size controls geological life span (Section 14.5)", body)


# ---------------------------------------------------------------- chapter 10


def planet_growth() -> str:
    w, h = 1080, 640
    body = ""
    steps = [
        ("dust grains", "microscopic", 4, "#d9cbb0"),
        ("clumps ~10 cm", "DANGER: gas drag", 8, ROCK),
        ("> 100 m quickly", "escape the drag", 12, ROCK),
        ("planetesimal ~1 km", "safe building block", 17, "#a0703f"),
        ("protoplanet", "sweeps up more", 26, PLANET_COLORS["Mars"]),
        ("> 10 Earth masses", "grabs hydrogen gas", 40, PLANET_COLORS["Jupiter"]),
    ]
    for i, (label, sub, r, color) in enumerate(steps):
        x = 80 + i * 180
        body += circle(x, 210, r, color)
        if i == 1:
            body += circle(x, 210, r + 10, "none", RED, 2)
        body += text(x, 290, label, 15, TEXT, "bold", "middle")
        body += text(x, 310, sub, 12, RED if i == 1 else MUTED, anchor="middle")
        if i < len(steps) - 1:
            body += line(x + r + 8, 210, x + 180 - steps[i + 1][2] - 10, 210, GOLD, 2, arrow=True)
    body += text(40, 360, "The clock is ticking (star ages):", 18, TEXT, "bold")
    tl = [
        ("< 1-3 Myr", "Disk reaches from the star out to tens-hundreds of AU"),
        ("older", "Inner dust cleared: a 'donut' around the star"),
        ("~10 Myr", "Dense inner disk gone; stellar wind can blow gas away -> giants must form fast"),
        ("3-30 Myr", "Planets form (if planets carve the holes)"),
        ("~30 Myr", "Leftover dust gone unless collisions resupply it"),
        ("400-500 Myr", "Debris disks fade (our heavy bombardment ended at ~500 Myr)"),
    ]
    for i, (t, d) in enumerate(tl):
        y = 384 + i * 36
        body += rect(40, y, 140, 28, fill=PANEL, stroke=GOLD, rx=8)
        body += text(110, y + 19, t, 13, GOLD, "bold", "middle")
        body += text(196, y + 19, d, 14, TEXT)
    body += card(720, 360, 330, 230, "Disk facts", "Nearly all very young stars have disks, 10 to 1,000 AU across, holding 1-10% of the Sun's mass (more than all our planets combined). For scale: Pluto's orbit is ~80 AU across, the Kuiper belt ~100 AU. Warm dust glows in infrared, so we hunt disks in infrared light.", ICE, body_size=13)
    return canvas(w, h, "Growing a Planet from Dust", "Accretion in a protoplanetary disk (Section 21.3)", body)


# ---------------------------------------------------------------- chapter 11


def doppler_method() -> str:
    w, h = 1040, 620
    body = ""
    body += circle(260, 250, 6, MUTED)
    body += text(260, 300, "center of mass (dot)", 12, MUTED, anchor="middle")
    body += circle(260, 250, 30, "none", GOLD, 1.5)
    body += circle(230, 250, 26, "url(#sunglow)")
    body += circle(260, 250, 170, "none", PANEL_EDGE, 1.5)
    body += circle(430, 250, 10, PLANET_COLORS["Jupiter"])
    body += text(430, 280, "planet", 13, TEXT, anchor="middle")
    body += text(100, 120, "toward us = BLUESHIFT", 15, BLUE, "bold")
    body += text(100, 400, "away from us = REDSHIFT", 15, RED, "bold")
    body += line(60, 250, 60, 170, BLUE, 3, arrow=True)
    body += line(60, 250, 60, 330, RED, 3, arrow=True)
    # velocity curve
    x0, y0 = 520, 250
    body += rect(500, 120, 510, 260, fill=PANEL, stroke=PANEL_EDGE)
    body += line(520, y0, 990, y0, MUTED, 1.5)
    pts = " ".join(f"{x0 + t * 4.7:.1f},{y0 - 90 * math.sin(t / 100 * 2 * 3.14159 * 2):.1f}" for t in range(0, 101))
    body += f'<polyline points="{pts}" fill="none" stroke="{GOLD}" stroke-width="3"/>'
    body += text(520, 140, "star's speed toward/away from us", 13, MUTED)
    body += text(990, 372, "time", 13, MUTED, anchor="end")
    body += text(760, 400, "one wiggle = one orbit (the planet's year)", 13, GOLD, "bold", "middle")
    body += card(30, 430, 320, 170, "What it tells us", "The planet's orbital period (-> distance, with Kepler's laws) and its MINIMUM mass (we usually can't tell the orbit's tilt). Works at any distance if the star is bright enough.", GOLD, body_size=13)
    body += card(366, 430, 320, 170, "Tiny wobbles", "Jupiter makes the Sun wobble ~13 m/s (about 30 mph) every 12 years. 51 Pegasi b (1995, Mayor + Queloz, Nobel 2019): a 'hot Jupiter' circling every 4.2 days, ~7 million km out.", ICE, body_size=13)
    body += card(702, 430, 308, 170, "Selection effect", "Easiest finds: BIG planets CLOSE to their stars (biggest, fastest wobbles). So early discoveries were mostly hot Jupiters -- a bias, not the true mix.", RED, body_size=13)
    return canvas(w, h, "Finding Planets by the Wobble", "The Doppler (radial velocity) method (Section 21.4)", body)


def transit_method() -> str:
    w, h = 1040, 620
    body = ""
    body += circle(200, 230, 110, "url(#sunglow)")
    body += circle(200, 230, 14, "#101010")
    body += line(40, 230, 360, 230, MUTED, 1, dash="4 6")
    body += text(200, 370, "the planet blocks a little starlight", 14, TEXT, "bold", "middle")
    body += rect(420, 110, 590, 260, fill=PANEL, stroke=PANEL_EDGE)
    body += text(440, 136, "brightness of the star (light curve)", 13, MUTED)
    body += path("M 440 180 L 640 180 L 670 260 L 780 260 L 810 180 L 990 180", GOLD, 3)
    body += text(540, 172, "1", 14, GOLD, "bold", "middle")
    body += text(655, 236, "2", 14, GOLD, "bold", "middle")
    body += text(725, 286, "3", 14, GOLD, "bold", "middle")
    body += line(1000, 180, 1000, 260, RED, 2)
    body += text(995, 300, "transit depth", 12, RED, "bold", "end")
    body += text(716, 350, "time between dips = the planet's year", 13, GOLD, "bold", "middle")
    body += rect(30, 400, 470, 190, fill="#1d1a12", stroke=GOLD)
    body += text(50, 432, "Transit depth = (R planet / R star)²", 20, GOLD, "bold")
    body += mtext(50, 466, [
        "Jupiter (71,400 km) in front of the Sun (695,700 km):",
        "(71,400 / 695,700)² = 0.0105  ->  about 1%",
        "Earth (6,371 km) in front of a star half the Sun's size:",
        "(6,371 / 347,850)² = 0.0003  ->  about 0.03%",
    ], 14, TEXT, line_height=26)
    body += card(520, 400, 490, 190, "Rules + results", "Need 3 evenly spaced dips of the same depth to call it a discovery, so Kepler (2009-2018, 150,000+ stars near Cygnus) only found Earth-like 1-year orbits late. Doppler mass + transit size = density! HD 209458 b (1999): 70% of Jupiter's mass but 35% wider -- a gas giant with sodium in its air. Now TESS surveys bright nearby stars.", ICE, body_size=13)
    return canvas(w, h, "Finding Planets by the Shadow", "The transit method (Section 21.4)", body)


def detection_compare() -> str:
    w, h = 1060, 630
    body = ""
    headers = ["Method", "What we watch", "What we learn", "Best at finding", "Famous example"]
    xs = [30, 210, 420, 640, 850]
    widths = [170, 200, 210, 200, 190]
    rows = [
        ("Doppler / radial velocity", "Star's spectrum shifts blue, then red", "Period + minimum mass", "Massive planets close in", "51 Pegasi b (1995); a planet around Proxima Centauri"),
        ("Transit", "Star dims slightly, repeatedly", "Size (radius) + period; air composition", "Big planets, short orbits", "HD 209458 b; Kepler's thousands; TESS"),
        ("Direct imaging", "The planet's own light, star blocked", "Temperature, clouds, gases", "Young, hot giants far from the star (infrared)", "HR 8799: 4 planets (2008, +1 in 2010)"),
        ("Astrometry", "Star's tiny side-to-side wiggle", "Mass + orbit", "(Too hard so far -- no confirmed finds)", "Sun seen from Alpha Centauri moves just 0.010 arcsec"),
    ]
    for x, cw, head in zip(xs, widths, headers):
        body += text(x + 6, 122, head, 15, GOLD, "bold")
    for i, row in enumerate(rows):
        y = 136 + i * 108
        body += rect(24, y, 1012, 100, fill=PANEL if i % 2 == 0 else "#122042", stroke="none", rx=8)
        for j, (x, cw, cell) in enumerate(zip(xs, widths, row)):
            body += mtext(x + 6, y + 26, wrap(cell, int(cw / 7.6)), 14 if j else 15, TEXT if j else ICE, "bold" if j == 0 else "normal")
    body += para(30, 582, "Indirect methods spot the planet's effect on its star. Earth reflects less than one billionth of the Sun's light, so imaging an Earth-like planet directly is incredibly hard.", 150, 13, MUTED)
    return canvas(w, h, "Exoplanet Detection Cheat Sheet", "Four ways to find planets around other stars", body)


# ---------------------------------------------------------------- chapter 12


def exoplanet_zoo() -> str:
    w, h = 1060, 620
    body = ""
    zoo = [
        ("Earth", 10, PLANET_COLORS["Earth"], "rock + metal"),
        ("Super-Earth", 16, "#6fb07a", "2-10 Earth masses; we have none!"),
        ("Mini-Neptune", 22, "#7fb8d8", "likely mostly gas (e.g. Kepler-62d)"),
        ("Neptune", 30, PLANET_COLORS["Neptune"], "ice giant"),
        ("Jupiter", 70, PLANET_COLORS["Jupiter"], "gas giant"),
        ("Hot Jupiter", 74, "#ff7a3d", "closer than Mercury; puffed up by heat"),
    ]
    for (name, r, color, note), cx in zip(zoo, [90, 250, 410, 570, 740, 930]):
        body += circle(cx, 240, r, color)
        body += text(cx, 340, name, 15, TEXT, "bold", "middle")
        body += mtext(cx, 362, wrap(note, 20), 13, MUTED, anchor="middle", line_height=17)
    body += card(30, 430, 330, 160, "Most common sizes", "Kepler found the most planets in sizes we DON'T have: between Earth and Neptune. Small planets are actually more common than giants once detection bias is corrected.", GOLD, body_size=13)
    body += card(376, 430, 330, 160, "How common?", "About half (or more) of stars have planets: at least 100 billion planets in our Galaxy. Over 1,000 multi-planet systems known by 2025 -- one has 8 planets.", ICE, body_size=13)
    body += card(722, 430, 308, 160, "Mass vs size", "More mass usually means bigger, but above ~1,000 Earth masses gravity squeezes planets SMALLER. Some hot Jupiters are puffier than pure hydrogen should be.", RED, body_size=13)
    return canvas(w, h, "The Exoplanet Zoo", "Kinds of planets found around other stars (Section 21.5)", body)


def hot_jupiter_migration() -> str:
    w, h = 1040, 600
    body = ""
    body += circle(110, 250, 40, "url(#sunglow)")
    body += line(330, 120, 330, 380, ICE, 2, dash="6 6")
    body += text(330, 110, "frost line", 13, ICE, "bold", "middle")
    body += circle(560, 250, 26, PLANET_COLORS["Jupiter"])
    body += text(560, 300, "giant forms out here", 13, TEXT, "bold", "middle")
    body += text(560, 318, "(~5-10 AU, ice available)", 12, MUTED, anchor="middle")
    body += path("M 530 240 C 430 180, 300 190, 200 236", GOLD, 3, arrow=True)
    body += text(370, 176, "A: disk drag -- spirals inward", 14, GOLD, "bold", "middle")
    body += path("M 540 270 C 460 400, 250 380, 180 280", RED, 3, arrow=True, dash="8 5")
    body += text(370, 410, "B: kicked by a sibling planet, then circularized", 14, RED, "bold", "middle")
    body += circle(175, 250, 12, "#ff7a3d")
    body += text(175, 222, "hot Jupiter", 12, "#ff7a3d", "bold", "middle")
    body += card(640, 100, 370, 160, "The puzzle", "Giant planets need ice to build their cores, but ice can't exist that close to a star. So hot Jupiters must form far out, then MIGRATE inward.", GOLD, body_size=13)
    body += card(640, 272, 370, 150, "Weird orbits too", "Many exoplanets have very oval orbits, and some even orbit sideways or backwards relative to their star's spin -- signs of planets shoving each other.", PURPLE, body_size=13)
    body += card(30, 450, 980, 120, "Our Solar System moved too", "Jupiter may have drifted inward long ago, perhaps knocking close-in rocky planets into the Sun. Uranus and Neptune probably formed nearer Jupiter and Saturn and were thrown outward -- the outer disk was too thin to build them in a few million years. Old picture: polite skaters on a rink. New picture: a roller derby!", ICE, body_size=14)
    return canvas(w, h, "How to Make a Hot Jupiter", "Planet migration (Section 21.6)", body)


# ---------------------------------------------------------------- chapter 13


def habitable_zone() -> str:
    w, h = 1060, 640
    body = ""
    stars = [
        ("Hot, bright star", "#9fc5ff", 34, 330, 560, "zone far out"),
        ("Sun-like (G) star", SUN, 26, 190, 300, "Venus too hot, Mars too cold, Earth just right"),
        ("M-dwarf (red dwarf)", "#ff6b4a", 16, 80, 120, "zone 3-30x closer; most common stars"),
    ]
    for i, (name, color, r, z1, z2, note) in enumerate(stars):
        y = 176 + i * 122
        body += rect(z1 + 120, y - 34, z2 - z1, 68, fill=GREEN, stroke="none", rx=10, opacity=0.35)
        body += circle(110, y, r, color)
        body += text(160, y - 44, name, 15, TEXT, "bold")
        body += text(z1 + 120 + (z2 - z1) / 2, y + 6, "HABITABLE ZONE" if z2 - z1 > 120 else "HZ", 13, "#d9ffe3", "bold", "middle")
        body += text(z2 + 132, y + 6, note, 13, MUTED)
    body += text(160, 112, "<-- too hot (closer to the star)", 13, RED, "bold")
    body += text(1030, 112, "too cold (farther away) -->", 13, BLUE, "bold", "end")
    body += card(30, 460, 330, 160, "Inverse-square law", "Light per square meter drops with distance squared. 2x farther = 1/4 the light; 10x = 1/100. Venus (0.72 AU) gets ~1.92x Earth's sunlight; Mars (1.52 AU) ~0.43x.", GOLD, body_size=13)
    body += card(376, 460, 330, 160, "Stars brighten", "The Sun is 30%+ brighter than 4 billion years ago, so the zone creeps outward. The 'continuously habitable zone' (in the zone the star's whole life) is much narrower.", ICE, body_size=13)
    body += card(722, 460, 308, 160, "Zone isn't a guarantee", "Habitability also needs an atmosphere, a greenhouse effect and actual water. Venus moved into the zone today would still have no water.", RED, body_size=13)
    return canvas(w, h, "The Habitable Zone", "The 'Goldilocks' distances where liquid surface water is possible", body)


def greenhouse_numbers() -> str:
    w, h = 1000, 600
    body = ""
    rows = [
        ("Mars", 2, PLANET_COLORS["Mars"], "~0.5x Earth's sunlight, reflects ~half as much; thin air: ~2 C of warming"),
        ("Earth", 33, PLANET_COLORS["Earth"], "water vapor + CO2: ~33 C of warming keeps oceans liquid"),
        ("Venus", 510, PLANET_COLORS["Venus"], "~2x sunlight but clouds reflect ~2x as much; thick CO2: ~510 C!"),
    ]
    for i, (name, warm, color, note) in enumerate(rows):
        y = 130 + i * 120
        body += text(40, y + 34, name, 22, TEXT, "bold")
        body += rect(160, y + 10, 780, 40, fill=PANEL, stroke=PANEL_EDGE, rx=8)
        body += rect(160, y + 10, max(8, 780 * warm / 510), 40, fill=color, stroke="none", rx=8)
        bar = max(8, 780 * warm / 510)
        if bar > 700:
            body += text(160 + bar - 12, y + 38, f"+{warm} C", 18, "#3a2200", "bold", "end")
        else:
            body += text(170 + bar, y + 38, f"+{warm} C", 18, GOLD, "bold")
        body += text(160, y + 76, note, 14, MUTED)
    body += para(40, 500, "Surprise: Venus, Earth and Mars absorb roughly the SAME amount of sunlight energy. Their atmospheres make the difference -- so judging habitability needs both the distance from the star and the atmosphere.", 120, 15, TEXT)
    return canvas(w, h, "Greenhouse Warming on Three Planets", "Extra warming from each planet's atmosphere (Section 30.3)", body)


# ---------------------------------------------------------------- chapter 14


def life_recipe() -> str:
    w, h = 1040, 600
    body = ""
    items = [
        ("LIQUID WATER", "The solvent: chemicals dissolve and react in it. Must be liquid -- the right temperature AND pressure. Strategy: 'follow the water'.", BLUE, "H2O"),
        ("THE RIGHT ELEMENTS", "C, H, N, O, P, S. Carbon is the star: it makes 4 bonds, so it builds endless big molecules (hydrocarbons, amino acids, sugars).", GREEN, "CHNOPS"),
        ("ENERGY", "Sunlight (photosynthesis) or chemical energy -- like a battery with a reducing side (rock + water) and an oxidizing side.", GOLD, "E"),
    ]
    for i, (head, desc, color, glyph) in enumerate(items):
        x = 30 + i * 336
        body += rect(x, 100, 316, 330)
        body += circle(x + 158, 180, 56, color, opacity=0.9)
        body += text(x + 158, 192, glyph, 30 if len(glyph) < 4 else 22, "#0b1530", "bold", "middle")
        body += text(x + 158, 270, head, 18, color, "bold", "middle")
        body += mtext(x + 158, 298, wrap(desc, 36), 13, TEXT, anchor="middle")
    body += para(30, 470, "Also needed by even the simplest life: a way to get energy from its surroundings AND a way to store information and copy itself (DNA + proteins today; maybe RNA first -- the 'RNA world'). Habitable = water + energy + raw materials, not just water.", 150, 14, TEXT)
    return canvas(w, h, "The Recipe for Life (as We Know It)", "What astrobiologists look for in a habitable environment (Section 30.2)", body)


def biomarkers() -> str:
    w, h = 1040, 600
    body = ""
    body += circle(150, 250, 6, "#9cc8ff")
    body += text(150, 280, "Earth from 6 billion km:", 13, MUTED, anchor="middle")
    body += text(150, 298, "the 'Pale Blue Dot'", 13, MUTED, anchor="middle")
    body += text(150, 316, "(less than 1 pixel)", 13, MUTED, anchor="middle")
    signs = [
        ("Lots of oxygen", "Over 20% of Earth's air is O2 from photosynthesis -- very hard to explain without life.", GREEN),
        ("Gas combos", "Methane or nitrous oxide found TOGETHER with oxygen are strong hints of biology.", GOLD),
        ("Color", "Plants make Earth look greener and reflect extra near-infrared light.", BLUE),
        ("Where to look", "Earth-size planets in the habitable zone with surface water -- life there can change a whole planet in ways telescopes can see.", PURPLE),
    ]
    for i, (head, desc, color) in enumerate(signs):
        x = 320 + (i % 2) * 350
        y = 100 + (i // 2) * 200
        body += card(x, y, 330, 180, head, desc, color, body_size=14)
    body += para(40, 520, "A biomarker (biosignature) is a sign in a planet's light that is hard to explain without life. Life hidden under ice (Europa) or underground (Mars) probably can't be seen from light-years away -- which is why the search focuses on planets with life on the surface.", 150, 14, TEXT)
    return canvas(w, h, "Biomarkers: Spotting Life from Afar", "Reading a planet's light for signs of a biosphere (Section 30.3)", body)


# ---------------------------------------------------------------- chapter 1 (merged)


def sun_layers() -> str:
    w, h = 1040, 640
    cx, cy = 300, 360
    body = ""
    layers = [
        (250, "#ffe7a8", 0.35, "Corona ~1,000,000 C"),
        (215, "#ffcf6b", 0.6, "Chromosphere + transition region"),
        (198, "#ffb347", 1, "Photosphere (surface) ~6,000 C"),
        (180, "#ff9a3c", 1, "Convection zone"),
        (130, "#ff7b2e", 1, "Radiative zone ~2,000,000 C"),
        (62, "#fff1a8", 1, "Core ~15,000,000 C"),
    ]
    for r, color, op, _ in layers:
        body += circle(cx, cy, r, color, opacity=op)
    for k in range(10):
        a = math.radians(200 + k * 14)
        body += path(f"M {cx + 140 * math.cos(a):.0f} {cy + 140 * math.sin(a):.0f} q 12 -10 22 0 q 10 10 22 0", "#c75c1e", 2)
    body += text(cx, cy + 6, "CORE", 16, "#5a2a00", "bold", "middle")
    labels = [
        (cy - 236, "CORONA", "thin outer atmosphere, ~1,000,000 C (hotter than the surface!)"),
        (cy - 196, "CHROMOSPHERE + TRANSITION REGION", "thin layers above the surface"),
        (cy - 150, "PHOTOSPHERE", "the visible surface, ~6,000 C"),
        (cy - 104, "CONVECTION ZONE", "hot gas rises and sinks like boiling soup"),
        (cy - 50, "RADIATIVE ZONE", "energy creeps out as light, ~2,000,000 C"),
        (cy + 4, "CORE", "hydrogen fuses into helium, ~15,000,000 C"),
    ]
    for y, name, desc in labels:
        body += line(cx + 40, y + 4, 600, y + 4, MUTED, 1, dash="3 4")
        body += text(610, y, name, 15, GOLD, "bold")
        body += text(610, y + 20, desc, 14, TEXT)
    body += card(610, 430, 400, 170, "Sun by the numbers", "Diameter 1,392,000 km (about 109 Earths) - mass 1.989 x 10^30 kg (99.8% of the Solar System) - power 3.846 x 10^26 W - about 74% hydrogen, 25% helium - halfway through its life.", SUN, body_size=15)
    return canvas(w, h, "Inside the Sun", "Layers from the core out (temperatures from the scioly.org Solar System wiki)", body)


def small_bodies() -> str:
    w, h = 1060, 660
    body = ""
    y = 300
    body += circle(50, y, 30, "url(#sunglow)")
    body += line(84, y, 600, y, PANEL_EDGE, 1.5, dash="4 6")
    zones = [
        (120, 170, PLANET_COLORS["Earth"], "inner planets", "rocky"),
        (205, 240, ROCK, "asteroid belt", "Mars-Jupiter"),
        (275, 380, PLANET_COLORS["Jupiter"], "giant planets", "5-30 AU"),
        (420, 480, ICE, "Kuiper Belt", "30-50 AU"),
        (520, 600, "#c9d3e8", "Oort Cloud", "far, far out"),
    ]
    for i, (x1, x2, color, name, sub) in enumerate(zones):
        body += rect(x1, y - 120, x2 - x1, 240, fill=color, stroke="none", rx=10, opacity=0.13)
        body += text((x1 + x2) / 2, y + 150 + (i % 2) * 44, name, 15, color, "bold", "middle")
        body += text((x1 + x2) / 2, y + 168 + (i % 2) * 44, sub, 13, MUTED, anchor="middle")
    for k, x in enumerate([130, 148, 162]):
        body += circle(x, y, 6 + k, [PLANET_COLORS["Mercury"], PLANET_COLORS["Earth"], PLANET_COLORS["Mars"]][k])
    for k in range(26):
        body += circle(208 + (k * 13) % 30, y - 100 + (k * 37) % 200, 2.4, ROCK)
    for x, r, c in [(296, 22, PLANET_COLORS["Jupiter"]), (330, 18, PLANET_COLORS["Saturn"]), (354, 11, PLANET_COLORS["Uranus"]), (372, 10, PLANET_COLORS["Neptune"])]:
        body += circle(x, y, r, c)
    for k in range(34):
        body += circle(424 + (k * 17) % 54, y - 104 + (k * 41) % 208, 2.2, ICE)
    for k in range(40):
        body += circle(524 + (k * 23) % 74, y - 112 + (k * 53) % 224, 1.8, "#c9d3e8", opacity=0.7)
    body += text(326, y - 140, "not to scale -- the Oort Cloud is thousands of times farther out", 13, MUTED, anchor="middle")
    cards = [
        ("ASTEROIDS", "Rocky leftovers, mostly between Mars and Jupiter. Types: C (dark, carbon-rich, most common), S (stony silicate), M (metal-rich).", ROCK),
        ("COMETS", "'Dirty snowballs' of ice + dust. Nucleus -> coma -> tails pointing away from the Sun. Periodic: < ~200 yrs; long-period: thousands to millions.", ICE),
        ("DWARF PLANETS", "Round, but haven't cleared their orbits: Ceres, Pluto, Eris, Haumea, Makemake. Plutoids = the ones beyond Neptune. Candidate: Sedna (11,518-yr orbit).", PURPLE),
        ("METEORS + METEORITES", "Dust burning up in our air = meteor. A piece that lands = meteorite (irons, stony-irons, stones).", GOLD),
    ]
    for i, (head, desc, color) in enumerate(cards):
        body += card(640, 100 + i * 134, 400, 122, head, desc, color, body_size=14)
    return canvas(w, h, "Small Bodies of the Solar System", "Where the leftovers live -- not to scale", body)


# ---------------------------------------------------------------- chapter 2 (merged)


def star_lifecycle() -> str:
    w, h = 1060, 650
    body = ""
    body += '<ellipse cx="110" cy="300" rx="80" ry="56" fill="#6c5a8f" opacity="0.6"/>'
    body += text(110, 380, "NEBULA", 16, TEXT, "bold", "middle")
    body += text(110, 400, "cold gas + dust", 14, MUTED, anchor="middle")
    body += line(196, 300, 246, 300, GOLD, 3, arrow=True)
    body += circle(290, 300, 30, "#ff9a5a")
    body += text(290, 380, "PROTOSTAR", 16, TEXT, "bold", "middle")
    body += text(290, 400, "shrinks + heats", 14, MUTED, anchor="middle")
    body += line(326, 300, 376, 300, GOLD, 3, arrow=True)
    body += circle(420, 300, 34, "url(#sunglow)")
    body += text(420, 380, "MAIN SEQUENCE", 16, TEXT, "bold", "middle")
    body += text(420, 400, "fuses hydrogen", 14, MUTED, anchor="middle")
    body += text(420, 440, "(the Sun: halfway)", 14, MUTED, anchor="middle")
    body += path("M 460 280 C 520 200, 560 170, 600 170", GOLD, 3, arrow=True)
    body += path("M 460 320 C 520 400, 560 430, 600 430", RED, 3, arrow=True)
    body += text(500, 200, "Sun-like star", 14, GOLD, "bold", "end")
    body += text(560, 470, "massive star", 14, RED, "bold", "middle")
    for x, r, color, name, sub, y in [
        (660, 46, "#ff6b4a", "RED GIANT", "swells up", 170),
        (820, 30, "#cfe3ff", "planetary nebula", "outer layers drift off", 170),
        (960, 12, "#ffffff", "WHITE DWARF", "small hot leftover", 170),
        (660, 58, "#ff4a3a", "RED SUPERGIANT", "huge", 430),
        (820, 44, "#ffe27a", "SUPERNOVA", "explodes!", 430),
        (960, 14, "#9fb4ff", "NEUTRON STAR", "or BLACK HOLE", 430),
    ]:
        body += circle(x, y, r, color, opacity=0.95)
        body += text(x, y + r + 26, name, 15, TEXT, "bold", "middle")
        body += text(x, y + r + 46, sub, 14, MUTED, anchor="middle")
    body += line(712, 170, 770, 170, MUTED, 2, arrow=True)
    body += line(856, 170, 930, 170, MUTED, 2, arrow=True)
    body += line(724, 430, 768, 430, MUTED, 2, arrow=True)
    body += line(870, 430, 930, 430, MUTED, 2, arrow=True)
    body += para(40, 588, "Supernovas scatter heavy elements (iron, carbon, oxygen) into space, where they become part of new stars, planets -- and you.", 120, 15, TEXT)
    return canvas(w, h, "The Life Cycle of a Star", "What happens depends on how massive the star is", body)


# ---------------------------------------------------------------- chapter 15


def kepler_laws() -> str:
    w, h = 1080, 640
    body = ""
    # law 1
    body += rect(24, 100, 336, 330)
    body += text(192, 128, "1. Orbits are ellipses", 17, GOLD, "bold", "middle")
    body += f'<ellipse cx="192" cy="270" rx="140" ry="90" fill="none" stroke="{ICE}" stroke-width="2.5"/>'
    body += circle(85, 270, 14, "url(#sunglow)")
    body += circle(299, 270, 4, MUTED)
    body += text(105, 304, "Sun at a focus", 14, TEXT, anchor="middle")
    body += text(290, 292, "empty focus", 13, MUTED, anchor="middle")
    body += circle(192, 180, 8, PLANET_COLORS["Earth"])
    body += para(40, 384, "Not the center! a = semi-major axis (average distance).", 40, 14, TEXT)
    # law 2
    body += rect(372, 100, 336, 330)
    body += text(540, 128, "2. Equal areas, equal times", 17, GOLD, "bold", "middle")
    body += f'<ellipse cx="540" cy="270" rx="140" ry="90" fill="none" stroke="{ICE}" stroke-width="2.5"/>'
    body += f'<path d="M 433 270 L 418.8 225 A 140 90 0 0 0 418.8 315 Z" fill="{GOLD}" opacity="0.55"/>'
    body += f'<path d="M 433 270 L 677.9 254.4 A 140 90 0 0 1 677.9 285.6 Z" fill="{GOLD}" opacity="0.55"/>'
    body += circle(433, 270, 14, "url(#sunglow)")
    body += text(450, 372, "FAST near the Sun", 14, RED, "bold", "middle")
    body += text(600, 172, "SLOW far away", 14, BLUE, "bold", "middle")
    body += para(388, 384, "Both shaded slices = same time and same area.", 40, 14, TEXT)
    # law 3
    body += rect(720, 100, 336, 330)
    body += text(888, 128, "3.  p² = a³", 20, GOLD, "bold", "middle")
    body += text(888, 152, "p in years, a in AU", 14, MUTED, anchor="middle")
    rows = [("Earth", "1.00", "1.00", "1.00"), ("Mars", "1.52", "3.51", "1.87"), ("Jupiter", "5.20", "140.6", "11.86"), ("Neptune", "30.06", "27,162", "164.8")]
    body += text(740, 186, "planet      a        a³       p = √a³", 14, ICE, "bold")
    for i, (n, a, a3, p) in enumerate(rows):
        y = 214 + i * 30
        body += text(740, y, n, 14, TEXT, "bold")
        body += text(830, y, a, 14, TEXT)
        body += text(898, y, a3, 14, TEXT)
        body += text(980, y, p, 14, GOLD, "bold")
    body += para(736, 352, "Farther out = much longer year. Mars check: table says 1.88 y.", 40, 14, TEXT)
    body += card(24, 446, 520, 160, "Newton's gravity", "F = G m1 m2 / r^2 with G = 6.67 x 10^-11 N m^2/kg^2. More mass = more pull; double the distance = 1/4 the pull. Gravity is mutual: star and planet both orbit their center of mass.", PURPLE, body_size=15)
    body += card(560, 446, 496, 160, "Escape velocity", "Ev = sqrt(2GM/R) -- radius in METERS. Earth 11.2 km/s, Venus 10.4, Mars 5.0. Low escape velocity lets light gas atoms leak away.", RED, body_size=15)
    return canvas(w, h, "Kepler's Laws and Gravity", "How planets move -- and how to calculate it", body)


def orbit_tricks() -> str:
    w, h = 1060, 600
    body = ""
    panels = [
        ("TIDAL LOCKING", ICE), ("SHEPHERD MOONS", PURPLE), ("RESONANCE", GAS), ("TROJANS", ROCK),
    ]
    for i, (head, color) in enumerate(panels):
        x = 24 + i * 258
        body += rect(x, 100, 244, 300)
        body += text(x + 122, 130, head, 17, color, "bold", "middle")
    # tidal locking
    body += circle(146, 270, 40, PLANET_COLORS["Earth"])
    body += circle(146, 270, 92, "none", PANEL_EDGE, 1.5, opacity=0.8)
    for ang in (0, 90, 180, 270):
        a = math.radians(ang)
        mx, my = 146 + 92 * math.cos(a), 270 + 92 * math.sin(a)
        body += circle(mx, my, 12, "#bdbdbd")
        body += circle(mx - 9 * math.cos(a), my - 9 * math.sin(a), 4, RED)
    body += text(146, 388, "red dot always faces Earth", 13, TEXT, anchor="middle")
    # shepherd
    cx2 = 404
    body += circle(cx2, 270, 30, PLANET_COLORS["Saturn"])
    body += f'<ellipse cx="{cx2}" cy="270" rx="96" ry="34" fill="none" stroke="#f3e2b0" stroke-width="10" opacity="0.7"/>'
    body += circle(cx2 + 104, 262, 6, "#bdbdbd")
    body += circle(cx2 - 88, 290, 6, "#bdbdbd")
    body += text(cx2, 388, "Pan, Prometheus keep edges sharp", 13, TEXT, anchor="middle")
    # resonance
    cx3 = 662
    body += circle(cx3, 260, 16, PLANET_COLORS["Jupiter"])
    for r, n, c in [(36, "Io", "#f4d35e"), (60, "Europa", "#e8e2d0"), (86, "Ganymede", "#a39e93")]:
        body += circle(cx3, 260, r, "none", c, 2)
        body += circle(cx3 + r, 260, 5, c)
    body += text(cx3, 160, "Io  /  Europa  /  Ganymede", 13, TEXT, "bold", "middle")
    body += text(cx3, 370, "Io : Europa : Ganymede = 1:2:4", 13, TEXT, anchor="middle")
    body += text(cx3, 388, "Neptune : Pluto periods = 2:3", 13, TEXT, anchor="middle")
    # trojans
    cx4 = 920
    body += circle(cx4, 270, 14, "url(#sunglow)")
    body += circle(cx4, 270, 90, "none", PANEL_EDGE, 1.5)
    body += circle(cx4 + 90, 270, 12, PLANET_COLORS["Jupiter"])
    for ang in (-60, 60):
        a = math.radians(ang)
        for k in range(6):
            body += circle(cx4 + 90 * math.cos(a) + (k % 3 - 1) * 7, 270 + 90 * math.sin(a) + (k // 3) * 7, 2.6, ROCK)
    body += text(cx4, 388, "60 deg ahead + behind Jupiter", 13, TEXT, anchor="middle")
    body += card(24, 420, 1012, 150, "Why it matters", "Tidal locking gives close-in planets a permanent day side and night side. Shepherding is how young planets carve gaps in dusty disks. Resonance keeps Io's orbit oval, which powers its volcanoes -- and keeps Pluto safe from Neptune even though their paths cross.", GOLD, body_size=15)
    return canvas(w, h, "Orbit Tricks", "Tidal locking, shepherd moons, orbital resonance and Trojans", body)


def eclipses() -> str:
    w, h = 1060, 640
    body = ""
    for i, (title, y, order, phase) in enumerate([("SOLAR ECLIPSE -- only at NEW moon", 120, ["Sun", "Moon", "Earth"], "Moon's shadow falls on Earth"), ("LUNAR ECLIPSE -- only at FULL moon", 330, ["Sun", "Earth", "Moon"], "Earth's shadow falls on the Moon")]):
        body += rect(24, y, 1012, 190)
        body += text(44, y + 30, title, 18, GOLD, "bold")
        body += text(44, y + 52, phase, 14, MUTED)
        xs = {"Sun": 130, "Earth": 560 if order[1] == "Earth" else 820, "Moon": 560 if order[1] == "Moon" else 820}
        sizes = {"Sun": 56, "Earth": 30, "Moon": 12}
        mid = order[1]
        body += f'<path d="M {xs[mid]} {y + 115 - sizes[mid]} L 1000 {y + 105} L 1000 {y + 125} L {xs[mid]} {y + 115 + sizes[mid]} Z" fill="#000" opacity="0.55"/>'
        body += f'<path d="M {xs[mid]} {y + 115 - sizes[mid]} L 1000 {y + 60} L 1000 {y + 170} L {xs[mid]} {y + 115 + sizes[mid]} Z" fill="#000" opacity="0.25"/>'
        for name in order:
            fill = "url(#sunglow)" if name == "Sun" else (PLANET_COLORS["Earth"] if name == "Earth" else "#bdbdbd")
            body += circle(xs[name], y + 115, sizes[name], fill)
            body += text(xs[name], y + 115 + sizes[name] + 20, name, 14, TEXT, "bold", "middle")
        body += text(960, y + 92, "umbra", 13, TEXT, "bold", "end")
        body += text(960, y + 160, "penumbra", 13, MUTED, anchor="end")
    body += para(44, 552, "SOLAR types: total, annular (Moon looks smaller -- 'ring of fire'), hybrid, partial. Never look without eclipse glasses!", 140, 15, TEXT)
    body += para(44, 584, "LUNAR types: penumbral, total penumbral, partial, total (Moon turns coppery red; totality up to ~107 minutes).", 140, 15, TEXT)
    return canvas(w, h, "Solar and Lunar Eclipses", "Shadow play between the Sun, Earth and Moon -- not to scale", body)


# ---------------------------------------------------------------- chapter 16


def _timeline(events: list[tuple[str, str, str]], start: int, end: int, width: int = 1100) -> str:
    x0, x1, y = 60, width - 60, 330
    body = line(x0, y, x1, y, GOLD, 4)

    def xpos(year: int) -> float:
        return x0 + (year - start) / (end - start) * (x1 - x0)

    for i, (yr, title, sub) in enumerate(events):
        x = xpos(int(yr[:4]))
        lx = x0 + 40 + i * ((x1 - x0 - 80) / max(1, len(events) - 1))
        up = i % 2 == 0
        body += circle(x, y, 7, GOLD)
        if up:
            body += path(f"M {x:.1f} {y - 7} L {lx:.1f} {y - 80}", MUTED, 1.5)
            body += text(lx, y - 150, yr, 14, GOLD, "bold", "middle")
            body += text(lx, y - 130, title, 15, TEXT, "bold", "middle")
            body += mtext(lx, y - 112, wrap(sub, 22)[:2], 13, MUTED, anchor="middle", line_height=16)
        else:
            body += path(f"M {x:.1f} {y + 7} L {lx:.1f} {y + 60}", MUTED, 1.5)
            body += text(lx, y + 80, yr, 14, GOLD, "bold", "middle")
            body += text(lx, y + 100, title, 15, TEXT, "bold", "middle")
            body += mtext(lx, y + 118, wrap(sub, 22)[:2], 13, MUTED, anchor="middle")
    return body


def astronomer_timeline() -> str:
    w, h = 1100, 560
    events = [
        ("1543", "Copernicus", "Sun-centered model"),
        ("1572", "Tycho Brahe", "precise data; supernova"),
        ("1609", "Kepler", "laws of planetary motion"),
        ("1610", "Galileo", "Jupiter's moons, Venus phases"),
        ("1655", "Huygens", "discovers Titan"),
        ("1705", "Halley", "first comet orbit"),
        ("1781", "Uranus", "found (Herschel)"),
        ("1846", "Neptune", "predicted + found"),
        ("1877", "Schiaparelli", "'canali'; Phobos + Deimos"),
        ("1930", "Tombaugh", "discovers Pluto"),
        ("1980", "Carl Sagan", "Cosmos; Venus greenhouse"),
        ("1995", "Mayor + Queloz", "first Sun-like exoplanet"),
    ]
    body = _timeline(events, 1520, 2010, w)
    body += para(60, 500, "Aristarchus (ancient Greece) first proposed a Sun-centered system, almost 2,000 years before Copernicus. Dates mark each person's key work.", 150, 14, TEXT)
    return canvas(w, h, "Astronomers Who Mapped the Solar System", "From the Sun-centered model to the first exoplanet", body)


def mission_timeline() -> str:
    w, h = 1100, 560
    events = [
        ("1962", "Mariner 2", "first Venus flyby"),
        ("1970", "Venera 7", "first Venus landing data"),
        ("1977", "Voyager 1 + 2", "outer planet flybys"),
        ("1990", "Hubble", "space telescope"),
        ("1995", "Galileo", "Jupiter orbiter"),
        ("2004", "Cassini", "Saturn; Huygens lands on Titan 2005"),
        ("2004", "Spirit + Opp.", "Mars rovers"),
        ("2009", "Kepler", "thousands of exoplanets"),
        ("2012", "Curiosity", "Mars: habitable past"),
        ("2015", "New Horizons", "Pluto flyby"),
        ("2021", "JWST", "infrared telescope"),
        ("2024", "Europa Clipper", "launched; arrives 2030"),
    ]
    body = _timeline(events, 1958, 2030, w)
    body += para(60, 500, "Also: Magellan (Venus radar), Dawn (Vesta + Ceres), Juno (Jupiter), Rosetta (comet 67P), NEAR (Eros), BepiColombo (Mercury), TESS, Perseverance, Dragonfly (Titan, launch 2027).", 150, 14, TEXT)
    return canvas(w, h, "Missions That Explored the Solar System", "Year each mission launched or reached its target", body)


INFOGRAPHICS: dict[str, tuple[str, Callable[[], str]]] = {
    "mass_budget": ("Who owns the Solar System's mass? The Sun has 99.8% -- Jupiter has most of the rest.", mass_budget),
    "planet_lineup": ("Meet the eight planets: terrestrial vs. jovian, with distance, year, size, density and mass.", planet_lineup),
    "nebula_steps": ("How the Solar System formed from the solar nebula, plus the four big clues.", nebula_steps),
    "earth_interior": ("Inside Earth: crust, mantle, liquid outer core and solid inner core.", earth_interior),
    "atmosphere_layers": ("Earth's atmosphere layers, the ozone layer and what air is made of.", atmosphere_layers),
    "greenhouse": ("How the greenhouse effect traps heat -- the good news and the bad news.", greenhouse),
    "earth_life_timeline": ("Timeline of life on Earth, from 4.5 billion years ago to the dinosaur impact.", earth_life_timeline),
    "three_planets": ("Earth vs. Venus vs. Mars property table.", three_planets),
    "venus_geology": ("The geology of Venus: plains, continents, volcanoes, coronae and craters.", venus_geology),
    "runaway_greenhouse": ("The runaway greenhouse loop that dried out Venus.", runaway_greenhouse),
    "mars_water": ("Mars water evidence: runoff channels, outflow channels, gullies and the rovers.", mars_water),
    "mars_ice": ("Mars air, clouds and polar caps.", mars_ice),
    "galilean_moons": ("Jupiter's Galilean moons and the tidal-heating gradient.", galilean_moons),
    "tidal_heating": ("How tidal heating melts Io.", tidal_heating),
    "ocean_worlds": ("Ocean worlds: Europa, Enceladus and Ganymede.", ocean_worlds),
    "titan_cycle": ("Titan's methane cycle compared with Earth's water cycle.", titan_cycle),
    "mountain_heights": ("Tallest mountains on Earth, Venus and Mars -- and why Olympus Mons wins.", mountain_heights),
    "baked_potato": ("Bigger worlds stay geologically active longer (the baked potato effect).", baked_potato),
    "planet_growth": ("Growing a planet from dust, and the disk timeline.", planet_growth),
    "doppler_method": ("The Doppler wobble method for finding exoplanets.", doppler_method),
    "transit_method": ("The transit method and the transit depth formula.", transit_method),
    "detection_compare": ("Cheat sheet comparing four exoplanet detection methods.", detection_compare),
    "exoplanet_zoo": ("The exoplanet zoo: super-Earths, mini-Neptunes and hot Jupiters.", exoplanet_zoo),
    "hot_jupiter_migration": ("How hot Jupiters migrate inward.", hot_jupiter_migration),
    "habitable_zone": ("The habitable zone around different kinds of stars.", habitable_zone),
    "greenhouse_numbers": ("Greenhouse warming on Mars, Earth and Venus.", greenhouse_numbers),
    "life_recipe": ("The recipe for life: liquid water, the right elements and energy.", life_recipe),
    "biomarkers": ("Biomarkers: how we could spot life on a distant planet.", biomarkers),
    "sun_layers": ("Inside the Sun: core, radiative and convection zones, photosphere, chromosphere and corona.", sun_layers),
    "small_bodies": ("Small bodies: asteroids, comets, dwarf planets, the Kuiper Belt and the Oort Cloud.", small_bodies),
    "star_lifecycle": ("The life cycle of a star: Sun-like stars vs. massive stars.", star_lifecycle),
    "kepler_laws": ("Kepler's three laws with p squared = a cubed practice, Newton's gravity and escape velocity.", kepler_laws),
    "orbit_tricks": ("Orbit tricks: tidal locking, shepherd moons, orbital resonance and Trojans.", orbit_tricks),
    "eclipses": ("Solar and lunar eclipses: when they happen and all the types.", eclipses),
    "astronomer_timeline": ("Timeline of the astronomers who mapped the solar system.", astronomer_timeline),
    "mission_timeline": ("Timeline of the space missions that explored the solar system.", mission_timeline),
}


# Infographics added with the restructured lessons (kept in their own module).
from app.content.solar_system.infographics_extra import EXTRA_INFOGRAPHICS  # noqa: E402

INFOGRAPHICS.update(EXTRA_INFOGRAPHICS)
