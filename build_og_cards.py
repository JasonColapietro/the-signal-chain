"""Emit standalone SVG og:image cards for the free lessons."""
from html import escape
from pathlib import Path


WIDTH = 1200
HEIGHT = 630
OUT_DIR = Path(__file__).resolve().parent / "fragments" / "og"

COLORS = {
    "bg": "#120e0b",
    "bg2": "#19130d",
    "panel": "#1f1812",
    "panel2": "#261d14",
    "line": "#3b2f20",
    "line_soft": "#2b2218",
    "cream": "#f2e7cf",
    "cream_dim": "#d9c9a8",
    "amber": "#eb9a26",
    "amber_hot": "#ffb84d",
    "jewel": "#ff4b33",
}

FONT_UI = "Arial, Helvetica, sans-serif"
FONT_TITLE = "Arial Black, Impact, Arial, Helvetica, sans-serif"
FONT_MONO = "Courier New, Courier, monospace"


# (slug, title, artist, title lines, [(label, value 0-10, range_text)])
CARDS = [
    (
        "purple-haze",
        "Purple Haze",
        "The Jimi Hendrix Experience",
        ["Purple Haze"],
        [("FUZZ", 7.5, "7-8"), ("GTR VOL", 8.5, "8-9"), ("TREBLE", 7.0, "7")],
    ),
    (
        "comfortably-numb",
        "Comfortably Numb",
        "Pink Floyd",
        ["Comfortably", "Numb"],
        [("SUSTAIN", 7.0, "~7"), ("DELAY MIX", 3.5, "3-4"), ("TONE", 4.5, "4-5")],
    ),
    (
        "pride-and-joy",
        "Pride and Joy",
        "Stevie Ray Vaughan",
        ["Pride and Joy"],
        [("DRIVE", 3.5, "3-4"), ("LEVEL", 6.5, "6-7"), ("MIDS", 6.5, "6-7")],
    ),
    (
        "smells-like-teen-spirit",
        "Smells Like Teen Spirit",
        "Nirvana",
        ["Smells Like", "Teen Spirit"],
        [("DIST", 7.5, "7-8"), ("TONE", 5.5, "5-6"), ("AMP GAIN", 2.5, "2-3")],
    ),
]


def text(x, y, body, **attrs):
    attr = " ".join(f'{name.replace("_", "-")}="{escape(str(value), quote=True)}"' for name, value in attrs.items())
    return f'<text x="{x}" y="{y}" {attr}>{escape(body)}</text>'


def knob(cx, cy, value, label, rng):
    angle = -135 + value * 27.0
    label_text = f"{label} {rng}"
    return f"""
    <g aria-label="{escape(label_text, quote=True)}">
      <title>{escape(label_text)}</title>
      <circle cx="{cx}" cy="{cy}" r="48" fill="{COLORS["panel"]}" stroke="{COLORS["line"]}" stroke-width="3"/>
      <circle cx="{cx}" cy="{cy}" r="35" fill="none" stroke="{COLORS["line"]}" stroke-width="2" opacity=".7"/>
      <line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy - 32}" stroke="{COLORS["amber_hot"]}" stroke-width="6" stroke-linecap="round" transform="rotate({angle:.0f} {cx} {cy})"/>
      <circle cx="{cx}" cy="{cy}" r="6" fill="{COLORS["amber_hot"]}"/>
      {text(cx, cy + 78, label_text, text_anchor="middle", font_family=FONT_MONO, font_size="19", font_weight="700", letter_spacing="1.2", fill=COLORS["cream"])}
    </g>"""


def title_block(lines, artist):
    if len(lines) == 1:
        title_size = 86 if len(lines[0]) < 16 else 76
        y0 = 226
        artist_y = 286
    else:
        title_size = 76
        y0 = 184
        artist_y = 318

    parts = []
    for index, line in enumerate(lines):
        parts.append(
            text(
                70,
                y0 + index * 78,
                line.upper(),
                font_family=FONT_TITLE,
                font_size=title_size,
                font_weight="900",
                letter_spacing="1.5",
                fill=COLORS["cream"],
            )
        )
    parts.append(
        text(
            74,
            artist_y,
            artist.upper(),
            font_family=FONT_UI,
            font_size="27",
            font_weight="700",
            letter_spacing="4.2",
            fill=COLORS["cream_dim"],
        )
    )
    return "\n      ".join(parts)


def knob_panel(settings):
    knob_xs = [795, 945, 1095]
    knobs = [knob(x, 374, value, label, rng) for x, (label, value, rng) in zip(knob_xs, settings)]
    signal_points = "735,374 745,374 745,374 795,374 945,374 1095,374 1150,374"
    return f"""
    <g>
      <rect x="718" y="224" width="412" height="282" rx="8" fill="{COLORS["panel"]}" stroke="{COLORS["line"]}" stroke-width="2"/>
      <rect x="736" y="244" width="376" height="70" rx="5" fill="{COLORS["panel2"]}" stroke="{COLORS["line_soft"]}" stroke-width="1"/>
      {text(924, 288, "STARTING POINTS, OUT OF 10", text_anchor="middle", font_family=FONT_MONO, font_size="16", font_weight="700", letter_spacing="2.7", fill=COLORS["amber"])}
      <polyline points="{signal_points}" fill="none" stroke="{COLORS["amber"]}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" opacity=".55"/>
      {''.join(knobs)}
    </g>"""


def card(slug, song, artist, lines, settings):
    aria = f"The Signal Chain free lesson card for {song} by {artist}"
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-label="{escape(aria, quote=True)}" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="panelGlow-{slug}" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{COLORS["amber"]}" stop-opacity=".18"/>
      <stop offset=".55" stop-color="{COLORS["jewel"]}" stop-opacity=".08"/>
      <stop offset="1" stop-color="{COLORS["bg"]}" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <rect width="{WIDTH}" height="{HEIGHT}" fill="{COLORS["bg"]}"/>
  <circle cx="1082" cy="72" r="250" fill="url(#panelGlow-{slug})"/>
  <rect x="42" y="40" width="1116" height="550" rx="10" fill="none" stroke="{COLORS["line"]}" stroke-width="2"/>
  <rect x="42" y="40" width="1116" height="74" rx="10" fill="{COLORS["panel"]}"/>
  <rect x="42" y="556" width="1116" height="34" fill="{COLORS["panel"]}"/>
  <g>
    {text(70, 86, "THE SIGNAL CHAIN · FREE LESSON", font_family=FONT_MONO, font_size="20", font_weight="700", letter_spacing="4.5", fill=COLORS["amber"])}
    {title_block(lines, artist)}
    <line x1="70" y1="348" x2="630" y2="348" stroke="{COLORS["line"]}" stroke-width="2"/>
    {text(70, 394, "REAL RIGS. AFFORDABLE PATHS.", font_family=FONT_UI, font_size="23", font_weight="700", letter_spacing="3.4", fill=COLORS["cream_dim"])}
    {knob_panel(settings)}
    {text(70, 580, "guitar.solutions", font_family=FONT_UI, font_size="26", font_weight="700", letter_spacing="1.2", fill=COLORS["cream"])}
    {text(1130, 580, "RANGES, NOT GOSPEL", text_anchor="end", font_family=FONT_MONO, font_size="18", font_weight="700", letter_spacing="3.0", fill=COLORS["cream_dim"])}
  </g>
</svg>
"""


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for slug, song, artist, lines, settings in CARDS:
        path = OUT_DIR / f"og-{slug}.svg"
        path.write_text(card(slug, song, artist, lines, settings), encoding="utf-8")
        print(f"wrote {path.relative_to(Path(__file__).resolve().parent)}")


if __name__ == "__main__":
    main()
