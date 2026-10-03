"""Infographics added with the restructured Solar System lessons: the
distance scale, spin vs. orbit, the moon census, the asteroid alphabet,
dwarf planets, the resonance/shepherd/Trojan tables, and the hot/cold
Jupiter family. Same deterministic SVG helpers as infographics.py; the
numbers come from the scioly.org Solar System wiki and the source reader.
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
)

WIKI_SOURCE = "Sources: scioly.org Solar System wiki + OpenStax Astronomy 2e (CC BY 4.0)"


def scale_ruler() -> str:
    w, h = 1080, 660
    body = ""
    # --- the whole planet zone to scale: 1 AU = 30 px
    body += rect(24, 96, 1032, 250)
    body += text(44, 126, "Distance from the Sun, drawn to scale (1 AU = one tick)", 17, GOLD, "bold")
    x0, y = 70, 230
    scale = 30
    body += circle(x0 - 18, y, 22, "url(#sunglow)")
    body += line(x0, y, x0 + 31 * scale, y, MUTED, 2)
    for au in range(0, 32):
        tick = 12 if au % 5 == 0 else 6
        body += line(x0 + au * scale, y - tick, x0 + au * scale, y + tick, MUTED, 1.5)
        if au % 5 == 0 and au:
            body += text(x0 + au * scale, y + 32, f"{au} AU", 13, MUTED, anchor="middle")
    # asteroid belt band (about 2.2-3.2 AU)
    body += rect(x0 + 2.2 * scale, y - 26, 1.0 * scale, 52, fill=ROCK, stroke="none", rx=4, opacity=0.35)
    body += text(x0 + 2.7 * scale, y - 34, "asteroid belt", 13, ROCK, anchor="middle")
    for name, au in [("Mercury", 0.39), ("Venus", 0.72), ("Earth", 1.0), ("Mars", 1.52)]:
        body += circle(x0 + au * scale, y, 4.5, PLANET_COLORS[name])
    body += path(f"M {x0} {y + 46} L {x0} {y + 56} L {x0 + 1.52 * scale} {y + 56} L {x0 + 1.52 * scale} {y + 46}", GOLD, 1.5)
    body += text(x0 + 6, y + 78, "all 4 rocky planets fit inside 1.5 AU!", 14, GOLD, "bold")
    for name, au, r in [("Jupiter", 5.2, 13), ("Saturn", 9.54, 11), ("Uranus", 19.18, 8), ("Neptune", 30.06, 8)]:
        x = x0 + au * scale
        body += circle(x, y, r, PLANET_COLORS[name])
        body += text(x, y - 40, name, 14, TEXT, "bold", "middle")
        body += text(x, y + 56, f"{au} AU", 13, GOLD, "bold", "middle")
    body += text(1040, y + 104, "Kuiper Belt: 30-50 AU, Oort Cloud: thousands of AU -->", 13, ICE, anchor="end")

    # --- light travel times
    body += rect(24, 362, 1032, 140)
    body += text(44, 392, "How long sunlight takes to get there (light: 300,000 km every second)", 17, GOLD, "bold")
    trips = [("Earth", "8.3 minutes", BLUE), ("Jupiter", "~43 minutes", GAS), ("Neptune", "~4.2 hours", ICE), ("Proxima Centauri", "4.2 YEARS", RED)]
    for i, (where, how, color) in enumerate(trips):
        x = 44 + i * 252
        body += rect(x, 408, 236, 78, fill="#101b38", stroke=color, rx=10)
        body += text(x + 118, 438, f"Sun -> {where}", 14, TEXT, "bold", "middle")
        body += text(x + 118, 470, how, 20, color, "bold", "middle")

    # --- the three rulers
    rulers = [
        ("KILOMETER (km)", "Fine on Earth: about a 12-minute walk. Earth is 12,756 km across.", MUTED),
        ("ASTRONOMICAL UNIT (AU)", "Earth-Sun distance = 150 million km = 1.5 x 10^8 km. For distances inside the Solar System.", GOLD),
        ("LIGHT-YEAR (ly)", "Distance light goes in a year = 9.46 trillion km = about 63,000 AU. A distance, NOT a time!", PURPLE),
    ]
    for i, (head, desc, color) in enumerate(rulers):
        body += card(24 + i * 348, 518, 336, 112, head, desc, color, body_size=14)
    return canvas(w, h, "How Far Is Far?", "Kilometers, astronomical units and light-years", body, WIKI_SOURCE)


def orbit_vs_spin() -> str:
    w, h = 1080, 700
    body = ""
    # rotation panel
    body += rect(24, 96, 508, 320)
    body += text(278, 128, "ROTATION = spinning = one DAY", 18, GOLD, "bold", "middle")
    cx, cy = 278, 262
    body += circle(cx, cy, 70, PLANET_COLORS["Earth"])
    tilt = math.radians(23.5)
    dx, dy = 105 * math.sin(tilt), 105 * math.cos(tilt)
    body += line(cx - dx, cy + dy, cx + dx, cy - dy, TEXT, 3, dash="8 5")
    body += text(cx + dx + 8, cy - dy - 6, "axis", 14, TEXT, "bold")
    body += path(f"M {cx - 92} {cy + 34} A 96 30 0 0 0 {cx + 92} {cy + 34}", GOLD, 3, arrow=True)
    body += text(cx, 376, "Earth spins once in about 24 hours (23 h 56 min)", 14, TEXT, anchor="middle")
    body += text(cx, 398, "Jupiter: ~10 h (fastest)  |  Venus: 243 days, backward", 14, MUTED, anchor="middle")
    # revolution panel
    body += rect(548, 96, 508, 320)
    body += text(802, 128, "REVOLUTION = orbiting = one YEAR", 18, GOLD, "bold", "middle")
    ox, oy = 802, 262
    body += f'<ellipse cx="{ox}" cy="{oy}" rx="190" ry="92" fill="none" stroke="{MUTED}" stroke-width="2" stroke-dasharray="6 6"/>'
    body += circle(ox, oy, 30, "url(#sunglow)")
    body += circle(ox + 190, oy, 16, PLANET_COLORS["Earth"])
    body += path(f"M {ox + 180} {oy - 48} A 190 92 0 0 0 {ox + 70} {oy - 86}", GOLD, 3, arrow=True)
    body += text(ox, 376, "Earth goes around the Sun once in 365.25 days", 14, TEXT, anchor="middle")
    body += text(ox, 398, "Mercury: 88 days (fastest)  |  Neptune: 164.8 years", 14, MUTED, anchor="middle")
    # seasons panel
    body += rect(24, 432, 1032, 246)
    body += text(44, 462, "SEASONS come from the TILT, not from distance", 18, GOLD, "bold")
    sx, sy = 540, 562
    body += circle(sx, sy, 34, "url(#sunglow)")
    for ex, label, sub in [(250, "June: the north half leans TOWARD the Sun", "= northern summer (direct light, long days)"), (830, "December: the north half leans AWAY", "= northern winter (slanted light, short days)")]:
        body += circle(ex, sy, 38, PLANET_COLORS["Earth"])
        body += line(ex - 30 * math.sin(tilt) * 1.6, sy + 30 * math.cos(tilt) * 1.6, ex + 30 * math.sin(tilt) * 1.6, sy - 30 * math.cos(tilt) * 1.6, TEXT, 3, dash="6 4")
        body += text(ex + 30 * math.sin(tilt) * 1.6 + 6, sy - 30 * math.cos(tilt) * 1.6 - 8, "N", 14, TEXT, "bold", "middle")
        body += text(ex, sy + 66, label, 14, TEXT, "bold", "middle")
        body += text(ex, sy + 86, sub, 13, MUTED, anchor="middle")
    body += line(300, sy, 496, sy, GOLD, 2, dash="4 6", arrow=False)
    body += line(584, sy, 780, sy, GOLD, 2, dash="4 6")
    body += text(sx, 500, "Earth's axis always points the same way in space (tilted 23.5 degrees)", 14, TEXT, anchor="middle")
    return canvas(w, h, "Days, Years and Seasons", "Rotation vs. revolution, and why Earth has seasons", body, WIKI_SOURCE)


def moon_census() -> str:
    w, h = 1120, 720
    body = ""
    cards = [
        ("Mercury & Venus", "0 moons", ["No moons at all -- the only", "planets without any."], PLANET_COLORS["Venus"]),
        ("Earth", "1 moon", ["The Moon: 384,400 km away,", "3,476 km across,", "orbits in 27.322 days.", "Tidally locked."], PLANET_COLORS["Earth"]),
        ("Mars", "2 moons", ["Phobos and Deimos,", "found 1877 by Asaph Hall.", "Tiny, lumpy -- probably", "captured asteroids."], PLANET_COLORS["Mars"]),
        ("Jupiter", "115 known in 2026 (wiki: 79)", ["Galilean moons, found by", "Galileo in 1610:", "Io, Europa, Ganymede,", "Callisto. Most others are", "small captured asteroids."], PLANET_COLORS["Jupiter"]),
        ("Saturn", "293 known in 2026 (wiki: 60+)", ["Titan -- Huygens, 1655", "Iapetus, Rhea, Tethys,", "Dione -- G. Cassini 1671-84", "Mimas, Enceladus --", "Herschel, 1789", "Phoebe orbits backward"], PLANET_COLORS["Saturn"]),
        ("Uranus", "29 known (wiki: 27)", ["Titania, Oberon --", "Herschel, 1787", "Ariel, Umbriel --", "Lassell, 1851", "Miranda -- Kuiper, 1948"], PLANET_COLORS["Uranus"]),
        ("Neptune", "16 known", ["Triton -- Lassell, 1846", "(orbits BACKWARD)", "Nereid -- Kuiper, 1949", "6 more found by", "Voyager 2 in 1989"], PLANET_COLORS["Neptune"]),
        ("Pluto (dwarf)", "5 moons", ["Charon -- Christy, 1978", "(Pluto and Charon are", "tidally locked together)", "Nix, Hydra 2005;", "Kerberos 2011; Styx 2012"], "#c9b79c"),
    ]
    for i, (name, count, lines, color) in enumerate(cards):
        col, row = i % 4, i // 4
        x, y = 24 + col * 272, 100 + row * 276
        body += rect(x, y, 258, 262)
        body += f'<rect x="{x}" y="{y}" width="258" height="8" rx="4" fill="{color}"/>'
        body += circle(x + 34, y + 50, 18, color)
        body += text(x + 62, y + 46, name, 17, TEXT, "bold")
        body += text(x + 62, y + 68, count, 14, GOLD, "bold")
        body += mtext(x + 18, y + 108, lines, 14, TEXT, line_height=24)
    body += text(24, 672, "Moon counts keep rising as telescopes find tiny moons (newest counts: source reader; older: wiki). About 430 known in all.", 14, MUTED)
    return canvas(w, h, "Moon Roll Call", "How many moons each world has, and who discovered the famous ones", body, WIKI_SOURCE)


def asteroid_types() -> str:
    w, h = 1120, 720
    body = ""
    big = [
        ("C-TYPE", "Dark, carbon-rich, primitive. The MOST COMMON type.", "#4a4740"),
        ("S-TYPE", "Silicate (stony) minerals. Brighter.", "#c9a46a"),
        ("M-TYPE", "Metal-rich, like iron-nickel.", "#b8c2cc"),
    ]
    for i, (head, desc, color) in enumerate(big):
        x = 24 + i * 362
        body += rect(x, 96, 348, 150)
        body += circle(x + 60, 171, 42, color, stroke="#ffffff", stroke_width=1.5, opacity=0.95)
        body += text(x + 60, 178, head[0], 26, "#ffffff", "bold", "middle")
        body += text(x + 120, 140, head, 20, GOLD, "bold")
        body += para(x + 120, 168, desc, 26, 15, TEXT)
    rare = [
        ("E", "Very bright; enstatite (iron-free silicates)"),
        ("P", "Dark, primitive"),
        ("D", "Very dark, organic-rich"),
        ("V", "Basaltic (volcanic), like Vesta"),
        ("Q", "Fresh silicate surfaces"),
        ("A", "Olivine-rich"),
        ("B", "Blue, hydrated (water in minerals)"),
        ("G", "C-type WITH ultraviolet features"),
        ("F", "C-type WITHOUT ultraviolet features"),
        ("R", "Rare: olivine + pyroxene"),
        ("T", "Dark, featureless"),
        ("L", "Moderately red"),
        ("K", "Silicate-rich, subtle features"),
        ("X", "Featureless -- needs albedo to sort"),
        ("I", "In-between S/M mixture"),
    ]
    body += text(24, 280, "The rarer types (from the wiki's table)", 18, TEXT, "bold")
    for i, (letter, desc) in enumerate(rare):
        col, row = i % 3, i // 3
        x, y = 24 + col * 362, 296 + row * 72
        body += rect(x, y, 348, 62, rx=10)
        body += circle(x + 32, y + 31, 20, PURPLE, opacity=0.85)
        body += text(x + 32, y + 38, letter, 20, "#ffffff", "bold", "middle")
        body += para(x + 64, y + (36 if len(desc) <= 34 else 27), desc, 34, 14, TEXT)
    body += text(24, 674, "Types are sorted by color, brightness (albedo) and spectrum, which reveal what the surface is made of.", 14, MUTED)
    return canvas(w, h, "The Asteroid Alphabet", "Asteroid types: the big three and the rare classes", body, WIKI_SOURCE)


def dwarf_planets() -> str:
    w, h = 1120, 700
    body = ""
    # rules table
    body += rect(24, 96, 520, 300)
    body += text(44, 128, "Planet or dwarf planet? Check the rules", 17, GOLD, "bold")
    rules = ["Orbits the Sun", "Round because of its own gravity", "Has cleared its neighborhood", "Is not a moon of something else"]
    body += text(352, 162, "PLANET", 14, BLUE, "bold", "middle")
    body += text(468, 162, "DWARF", 14, PURPLE, "bold", "middle")
    for i, rule in enumerate(rules):
        y = 200 + i * 48
        body += line(44, y - 26, 524, y - 26, PANEL_EDGE, 1)
        body += text(44, y, rule, 15, TEXT)
        body += text(352, y, "YES", 15, GREEN, "bold", "middle")
        dwarf = "NO" if i == 2 else "YES"
        body += text(468, y, dwarf, 15, RED if dwarf == "NO" else GREEN, "bold", "middle")
    body += para(44, 384, "PLUTOID = a dwarf planet that orbits beyond Neptune.", 60, 14, GOLD)

    # the five dwarf planets
    body += rect(560, 96, 536, 300)
    body += text(580, 128, "The five dwarf planets", 17, GOLD, "bold")
    dwarfs = [
        ("Ceres", "asteroid belt -- nearly 1,000 km; visited by Dawn", False),
        ("Pluto", "Kuiper Belt -- 5 moons; New Horizons 2015", True),
        ("Eris", "beyond the Kuiper Belt -- about Pluto's size", True),
        ("Haumea", "Kuiper Belt", True),
        ("Makemake", "Kuiper Belt", True),
    ]
    for i, (name, where, plutoid) in enumerate(dwarfs):
        y = 168 + i * 46
        body += circle(594, y - 5, 12, "#c9b79c" if plutoid else ROCK)
        body += text(616, y, name, 16, TEXT, "bold")
        body += text(716, y, where, 14, MUTED)
        if plutoid:
            body += rect(1004, y - 19, 80, 24, fill=PURPLE, stroke="none", rx=8, opacity=0.85)
            body += text(1044, y - 2, "PLUTOID", 12, "#ffffff", "bold", "middle")

    # Sedna orbit sketch
    body += rect(24, 412, 1072, 268)
    body += text(44, 444, "Sedna: a Plutoid CANDIDATE with an extremely stretched orbit (sketch, not to scale)", 17, GOLD, "bold")
    sx, sy = 80, 556
    body += circle(sx, sy, 9, "url(#sunglow)")
    body += circle(sx, sy, 30, "none", PLANET_COLORS["Neptune"], 2)
    body += text(sx, sy + 52, "Neptune's orbit", 13, PLANET_COLORS["Neptune"], anchor="middle")
    body += f'<ellipse cx="600" cy="{sy}" rx="450" ry="70" fill="none" stroke="{ICE}" stroke-width="2.5" stroke-dasharray="8 5"/>'
    body += circle(150, sy, 7, "#d98b6a")
    body += line(150, sy + 10, 150, sy + 78, MUTED, 1)
    body += text(156, sy + 98, "perihelion: outer Kuiper Belt", 13, TEXT, "bold")
    body += line(1050, sy + 10, 1050, sy + 78, MUTED, 1)
    body += text(1044, sy + 98, "aphelion: maybe the inner Oort Cloud", 13, TEXT, "bold", "end")
    body += para(330, sy - 10, "One orbit takes roughly 11,000 years. About 1,000 km (~600 miles) across, no known moons -- found by luck near perihelion.", 64, 15, TEXT)
    return canvas(w, h, "Dwarf Planets and Plutoids", "The 2006 rules, the five dwarf planets, and Sedna", body, WIKI_SOURCE)


def resonance_table() -> str:
    w, h = 1120, 720
    body = ""
    body += rect(24, 96, 540, 420)
    body += text(44, 128, "ORBITAL RESONANCES", 18, GAS, "bold")
    body += text(44, 152, "orbit times in a simple whole-number ratio", 14, MUTED)
    rows = [
        ("2:3", "Neptune and Pluto", "Neptune's year is 2/3 of Pluto's"),
        ("1:2", "Mimas and Tethys", "Saturn's moons"),
        ("1:2", "Enceladus and Dione", "Saturn's moons"),
        ("3:4", "Titan and Hyperion", "Saturn's moons"),
        ("1:2:4", "Io, Europa, Ganymede", "Jupiter -- a LAPLACE resonance"),
    ]
    for i, (ratio, who, note) in enumerate(rows):
        y = 196 + i * 62
        body += rect(44, y - 28, 92, 44, fill="#2b2412", stroke=GAS, rx=8)
        body += text(90, y + 1, ratio, 19, GAS, "bold", "middle")
        body += text(152, y - 6, who, 16, TEXT, "bold")
        body += text(152, y + 14, note, 13, MUTED)
    body += para(44, 494, "Someday Callisto may join: 1:2:4:8.", 60, 14, GOLD)

    body += rect(580, 96, 516, 236)
    body += text(600, 128, "SHEPHERD MOONS", 18, PURPLE, "bold")
    body += text(600, 152, "keep ring particles in tight bands", 14, MUTED)
    shepherds = [
        ("Jupiter", "Metis, Adrastea, Amalthea, Thebe"),
        ("Saturn", "Pan, Daphnis, Atlas, Prometheus, Pandora, Aegaeon + moonlets"),
        ("Uranus", "Cordelia and Ophelia"),
    ]
    for i, (planet, moons) in enumerate(shepherds):
        y = 188 + i * 48
        body += circle(612, y - 5, 10, PLANET_COLORS[planet])
        body += text(632, y, planet, 15, TEXT, "bold")
        body += para(712, y, moons, 46, 14, TEXT)

    body += rect(580, 348, 516, 168)
    body += text(600, 380, "TROJANS (1:1, at L4 and L5)", 18, ROCK, "bold")
    body += para(600, 408, "Share an orbit 60 degrees ahead of or behind a bigger body. Planets: Mars, Jupiter (thousands!) and Neptune. Moons: Telesto + Calypso share Tethys' orbit; Helene + Polydeuces share Dione's.", 60, 14, TEXT)

    # small Laplace dial
    body += rect(24, 532, 1072, 160)
    body += text(44, 562, "Why resonance matters", 17, GOLD, "bold")
    cx, cy = 140, 622
    body += circle(cx, cy, 10, PLANET_COLORS["Jupiter"])
    for r, name, c in [(24, "Io", "#f4d35e"), (40, "Europa", "#e8e2d0"), (56, "Ganymede", "#a39e93")]:
        body += circle(cx, cy, r, "none", c, 2)
        body += circle(cx + r, cy, 5, c)
    body += para(230, 598, "Regular tugs add up, like pushing a swing at the right moment. The 1:2:4 tugs keep Io's orbit oval, so Jupiter keeps flexing it -- that powers Io's volcanoes and helps keep Europa's ocean liquid. The 2:3 resonance keeps Pluto from ever hitting Neptune, even though their orbits cross.", 118, 15, TEXT)
    return canvas(w, h, "Resonances, Shepherds and Trojans", "The wiki's tables of orbital relationships", body, WIKI_SOURCE)


def jupiter_types() -> str:
    w, h = 1120, 640
    body = ""
    body += rect(24, 96, 1072, 290)
    body += text(44, 128, "Where they orbit", 17, GOLD, "bold")
    sx, sy = 90, 240
    body += circle(sx, sy, 46, "url(#sunglow)")
    frost_x = 600
    body += rect(140, 146, 460, 226, fill=RED, stroke="none", rx=12, opacity=0.08)
    body += line(frost_x, 146, frost_x, 372, ICE, 3, dash="10 6")
    body += text(frost_x, 140, "FROST LINE", 15, ICE, "bold", "middle")
    body += text(152, 362, "too warm for ice", 13, RED)
    body += text(612, 362, "beyond: water, ammonia and methane freeze", 13, ICE)
    body += circle(200, sy, 30, "#ff7a3d")
    body += text(200, sy - 44, "HOT JUPITER", 14, "#ff7a3d", "bold", "middle")
    body += circle(330, sy, 18, "#7fb8d8")
    body += text(330, sy - 32, "HOT NEPTUNE", 14, "#7fb8d8", "bold", "middle")
    body += circle(850, sy, 30, PLANET_COLORS["Jupiter"])
    body += text(850, sy - 44, "COLD JUPITER", 14, GAS, "bold", "middle")
    body += text(850, sy + 52, "(our Jupiter is one)", 13, MUTED, anchor="middle")
    body += path(f"M 812 {sy + 18} C 640 {sy + 80}, 420 {sy + 80}, 236 {sy + 34}", GOLD, 2, arrow=True, dash="6 5")
    body += text(590, sy + 96, "hot Jupiters formed out here, then MIGRATED in", 13, GOLD, anchor="end")

    cards = [
        ("HOT JUPITER", "Gas giant on a super-close orbit of just a few days. Often over 1,000 K and tidally locked. Mass 0.36 to 13.6 Jupiter masses (a favorite test fact!). Mostly hydrogen + helium. Easiest to find with the Doppler wobble -- 51 Pegasi b was first.", "#ff7a3d"),
        ("HOT NEPTUNE", "Smaller, Neptune/Uranus-like ice giant close to its star (often within ~1 AU). Less atmosphere and a denser core, because starlight strips its gas. Contains heavier stuff: water, ammonia, methane.", "#7fb8d8"),
        ("COLD JUPITER", "A gas giant like a hot Jupiter, but orbiting far out, BEYOND the frost line, where volatile compounds freeze into ice grains. Not inflated unless very young.", GAS),
    ]
    for i, (head, desc, color) in enumerate(cards):
        body += card(24 + i * 362, 402, 348, 208, head, desc, color, body_size=15)
    return canvas(w, h, "Hot Jupiters, Hot Neptunes and Cold Jupiters", "Three exoplanet types every Solar System test asks about", body, WIKI_SOURCE)


EXTRA_INFOGRAPHICS: dict[str, tuple[str, Callable[[], str]]] = {
    "scale_ruler": ("How far is far? Planet distances to scale, light travel times, and km vs. AU vs. light-years.", scale_ruler),
    "orbit_vs_spin": ("Rotation (a day) vs. revolution (a year), and how Earth's tilt causes the seasons.", orbit_vs_spin),
    "moon_census": ("Moon roll call: how many moons each world has and who discovered the famous ones.", moon_census),
    "asteroid_types": ("The asteroid alphabet: C, S and M types plus all the rarer classes.", asteroid_types),
    "dwarf_planets": ("Planet vs. dwarf planet rules, the five dwarf planets and Plutoids, and Sedna's stretched orbit.", dwarf_planets),
    "resonance_table": ("Orbital resonances, shepherd moons and Trojans -- the wiki's tables.", resonance_table),
    "jupiter_types": ("Hot Jupiters, hot Neptunes and cold Jupiters, and the frost line that separates them.", jupiter_types),
}
