"""Tiny, dependency-free SVG drawing helpers for the Solar System
infographics and flashcard badges.

Everything here is pure string building, so the rendered images are fully
deterministic -- the same code always produces byte-identical SVG, which
is what lets the seed store them as data URLs without any image service or
LLM call. Images are rendered through an <img> tag (flashcards, diagram
grid), which can't load web fonts, so text sticks to a system font stack.
"""

import base64
from xml.sax.saxutils import escape

FONT = "'Segoe UI', 'Helvetica Neue', Helvetica, Arial, sans-serif"

# Shared palette -- a dark "space" canvas reads well in both the app's light
# and dark surroundings, so infographics don't need a per-theme variant.
BG = "#0b1530"
PANEL = "#16244a"
PANEL_EDGE = "#2c3f74"
TEXT = "#eef2ff"
MUTED = "#a9b8e0"
GOLD = "#f5c542"
SUN = "#ffb347"
ROCK = "#c98a5a"
ICE = "#8fd3ff"
GAS = "#e8b878"
GREEN = "#6fdc8c"
RED = "#ff6b6b"
BLUE = "#4da3ff"
PURPLE = "#b48cff"

PLANET_COLORS = {
    "Mercury": "#b5b5b5",
    "Venus": "#e8c27a",
    "Earth": "#4da3ff",
    "Mars": "#e0603a",
    "Jupiter": "#d9a066",
    "Saturn": "#e9d08f",
    "Uranus": "#8fe3e8",
    "Neptune": "#4f74ff",
}


def esc(value: object) -> str:
    return escape(str(value))


def wrap(text: str, width: int) -> list[str]:
    """Greedy word-wrap by character count -- good enough for a fixed
    sans-serif font at a known size, and keeps output deterministic."""
    lines: list[str] = []
    for paragraph in text.split("\n"):
        current = ""
        for word in paragraph.split():
            candidate = f"{current} {word}".strip()
            if len(candidate) > width and current:
                lines.append(current)
                current = word
            else:
                current = candidate
        lines.append(current)
    return lines


def text(x: float, y: float, value: str, size: int = 16, fill: str = TEXT, weight: str = "normal", anchor: str = "start", italic: bool = False) -> str:
    style = ' font-style="italic"' if italic else ""
    return (
        f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" fill="{fill}" '
        f'font-weight="{weight}" text-anchor="{anchor}"{style}>{esc(value)}</text>'
    )


def mtext(x: float, y: float, lines: list[str], size: int = 15, fill: str = TEXT, weight: str = "normal", anchor: str = "start", line_height: float | None = None) -> str:
    lh = line_height or size * 1.3
    return "".join(text(x, y + i * lh, line, size, fill, weight, anchor) for i, line in enumerate(lines))


def para(x: float, y: float, value: str, width_chars: int, size: int = 15, fill: str = TEXT, weight: str = "normal", anchor: str = "start") -> str:
    return mtext(x, y, wrap(value, width_chars), size, fill, weight, anchor)


def rect(x: float, y: float, w: float, h: float, fill: str = PANEL, stroke: str = PANEL_EDGE, rx: float = 12, stroke_width: float = 1.5, opacity: float = 1.0) -> str:
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" '
        f'stroke="{stroke}" stroke-width="{stroke_width}" opacity="{opacity}"/>'
    )


def circle(cx: float, cy: float, r: float, fill: str, stroke: str = "none", stroke_width: float = 0, opacity: float = 1.0) -> str:
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}" opacity="{opacity}"/>'


def line(x1: float, y1: float, x2: float, y2: float, stroke: str = MUTED, width: float = 2, dash: str = "", arrow: bool = False) -> str:
    dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
    marker = ' marker-end="url(#arrow)"' if arrow else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{width}"{dash_attr}{marker}/>'


def path(d: str, stroke: str = MUTED, width: float = 2, fill: str = "none", arrow: bool = False, dash: str = "") -> str:
    dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
    marker = ' marker-end="url(#arrow)"' if arrow else ""
    return f'<path d="{d}" stroke="{stroke}" stroke-width="{width}" fill="{fill}"{dash_attr}{marker}/>'


def card(x: float, y: float, w: float, h: float, heading: str, body: str, accent: str = GOLD, width_chars: int | None = None, body_size: int = 14) -> str:
    """A rounded panel with a colored heading and a wrapped body paragraph."""
    chars = width_chars or max(10, int((w - 30) / (body_size * 0.47)))
    return (
        rect(x, y, w, h)
        + f'<rect x="{x}" y="{y}" width="6" height="{h}" rx="3" fill="{accent}"/>'
        + text(x + 18, y + 28, heading, 17, accent, "bold")
        + para(x + 18, y + 52, body, chars, body_size, TEXT)
    )


def canvas(width: int, height: int, title: str, subtitle: str, body: str, source: str = "Source: OpenStax Astronomy 2e (CC BY 4.0) -- Solar System source reader") -> str:
    stars = "".join(
        circle((i * 137) % width, (i * 89) % height, 0.9 + (i % 3) * 0.4, "#ffffff", opacity=0.18 + (i % 4) * 0.08)
        for i in range(1, 70)
    )
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">'
        '<defs><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
        f'<path d="M 0 0 L 10 5 L 0 10 z" fill="{MUTED}"/></marker>'
        f'<radialGradient id="sunglow"><stop offset="0%" stop-color="#fff3b0"/><stop offset="55%" stop-color="{SUN}"/><stop offset="100%" stop-color="#ff7b2e"/></radialGradient>'
        "</defs>"
        f'<rect width="{width}" height="{height}" fill="{BG}"/>'
        + stars
        + text(32, 48, title, 30, GOLD, "bold")
        + text(32, 76, subtitle, 16, MUTED)
        + body
        + text(width - 20, height - 14, source, 11, MUTED, anchor="end")
        + "</svg>"
    )


def badge_svg(label: str, sub: str, color: str) -> str:
    """Square flashcard badge, designed to survive the front-of-card circle
    crop (StudentPractice renders the image at 96px with border-radius 50%)."""
    size = 240
    big = 54 if len(label) <= 4 else 42 if len(label) <= 6 else 32 if len(label) <= 9 else 26
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 {size} {size}">'
        f'<defs><radialGradient id="g" cx="35%" cy="30%" r="80%"><stop offset="0%" stop-color="#ffffff" stop-opacity="0.35"/>'
        f'<stop offset="45%" stop-color="{color}"/><stop offset="100%" stop-color="{BG}"/></radialGradient></defs>'
        f'<rect width="{size}" height="{size}" fill="{BG}"/>'
        + circle(120, 120, 112, "url(#g)")
        + circle(120, 120, 112, "none", stroke="#ffffff", stroke_width=3, opacity=0.35)
        + f'<ellipse cx="120" cy="120" rx="118" ry="30" fill="none" stroke="{GOLD}" stroke-width="2" opacity="0.35" transform="rotate(-18 120 120)"/>'
        + text(120, 120 + big * 0.35, label, big, "#ffffff", "bold", "middle")
        + text(120, 178, sub, 17, "#ffffff", "bold", "middle")
        + "</svg>"
    )


def data_url(svg: str) -> str:
    return "data:image/svg+xml;base64," + base64.b64encode(svg.encode("utf-8")).decode("ascii")
