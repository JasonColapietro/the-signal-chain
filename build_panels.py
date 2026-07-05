#!/usr/bin/env python3
"""Emit the amp-panel SVGs for the free lessons -> fragments/panel-<slug>.svg

Each panel is a screenshot-able summary of a lesson's Tone Recipe starting
points. Knob angles sit at the midpoint of the printed range; the range text
stays visible because the numbers are honest ranges, not gospel.
Self-contained, no third-party dependencies, same as every builder here.
"""
import os

# (slug, song, artist, groups) — group = (label, [(knob, value 0-10, range_text)])
PANELS = [
    ("purple-haze", "Purple Haze", "The Jimi Hendrix Experience", [
        ("FUZZ FACE", [("FUZZ", 7.5, "7–8"), ("VOLUME", 5, "UNITY")]),
        ("GUITAR", [("VOLUME", 8.5, "8–9"), ("TONE", 7.5, "7–8")]),
        ("AMP · CLEAN-ISH, LOUD", [("BASS", 5, "5"), ("MIDS", 6, "6"), ("TREBLE", 7, "7")]),
    ]),
    ("comfortably-numb", "Comfortably Numb", "Pink Floyd", [
        ("BIG MUFF", [("SUSTAIN", 7, "~7"), ("TONE", 4.5, "4–5"), ("VOLUME", 5, "UNITY")]),
        ("DELAY", [("TIME", 6, "~450MS"), ("REPEATS", 3.5, "3–4"), ("MIX", 3.5, "3–4")]),
        ("AMP · CLEAN, BRIGHT", [("BASS", 5, "5"), ("MIDS", 5.5, "5–6"), ("TREBLE", 6, "6")]),
    ]),
    ("pride-and-joy", "Pride and Joy", "Stevie Ray Vaughan", [
        ("TUBE SCREAMER", [("DRIVE", 3.5, "3–4"), ("TONE", 5.5, "5–6"), ("LEVEL", 6.5, "6–7")]),
        ("AMP · EDGE OF BREAKUP", [("BASS", 5, "5"), ("MIDS", 6.5, "6–7"), ("TREBLE", 6, "6"), ("REVERB", 3, "3")]),
    ]),
    ("smells-like-teen-spirit", "Smells Like Teen Spirit", "Nirvana", [
        ("DS-1 · THE CLIPPING", [("DIST", 7.5, "7–8"), ("TONE", 5.5, "5–6"), ("LEVEL", 5, "TO TASTE")]),
        ("AMP · CLEAN-TO-EDGE", [("GAIN", 2.5, "2–3"), ("BASS", 5, "NOON"), ("MIDS", 5, "NOON"), ("TREBLE", 5, "NOON")]),
    ]),
]

KNOB_W = 78          # horizontal pitch per knob
GROUP_PAD = 26       # padding inside a group box
GROUP_GAP = 18       # gap between group boxes
ROW_H = 132          # group box height
TOP = 64             # title strip height


def knob(cx, cy, value, label, rng):
    ang = -135 + value * 27.0
    return (
        f'<g transform="translate({cx},{cy})">'
        f'<circle r="24" fill="var(--panel,#1c1611)" stroke="var(--line,#3a2f24)" stroke-width="1.5"/>'
        f'<circle r="18" fill="none" stroke="var(--line,#3a2f24)" stroke-width="1" opacity=".55"/>'
        f'<line x1="0" y1="0" x2="0" y2="-16" stroke="var(--amber-hot,#f0a83c)" stroke-width="3" '
        f'stroke-linecap="round" transform="rotate({ang:.0f})"/>'
        f'<circle r="3" fill="var(--amber-hot,#f0a83c)"/>'
        f'<text y="-32" text-anchor="middle" font-size="9.5" letter-spacing="1.4" '
        f'fill="var(--cream-dim,#d9c9a8)">{label}</text>'
        f'<text y="42" text-anchor="middle" font-size="11" font-weight="700" '
        f'fill="var(--amber,#d8952f)">{rng}</text>'
        f'</g>'
    )


def panel(slug, song, artist, groups):
    boxes = []
    x = 0
    for glabel, knobs in groups:
        w = GROUP_PAD * 2 + KNOB_W * len(knobs)
        kx = x + GROUP_PAD + KNOB_W / 2
        ks = []
        for klabel, val, rng in knobs:
            ks.append(knob(kx, TOP + 62, val, klabel, rng))
            kx += KNOB_W
        boxes.append(
            f'<g><rect x="{x}" y="{TOP + 8}" width="{w}" height="{ROW_H}" rx="10" '
            f'fill="var(--paper,#f4ead8)" fill-opacity=".045" stroke="var(--line,#3a2f24)"/>'
            f'<text x="{x + w / 2}" y="{TOP + 28}" text-anchor="middle" font-size="10" '
            f'letter-spacing="2" font-weight="700" fill="var(--cream-dim,#d9c9a8)">{glabel}</text>'
            + "".join(ks) + "</g>"
        )
        x += w + GROUP_GAP
    width = x - GROUP_GAP
    h = TOP + ROW_H + 20
    return (
        f'<svg class="amp-panel-svg" viewBox="0 0 {width} {h}" role="img" '
        f'aria-label="Starting-point settings for {song}" xmlns="http://www.w3.org/2000/svg" '
        f'font-family="Jost,sans-serif">'
        f'<text x="0" y="22" font-size="13" font-weight="800" letter-spacing="2.5" '
        f'fill="var(--cream,#f2e7cf)">{song.upper()}</text>'
        f'<text x="0" y="42" font-size="10.5" letter-spacing="2" '
        f'fill="var(--cream-dim,#d9c9a8)">{artist.upper()} · STARTING POINTS, OUT OF 10 · RANGES, NOT GOSPEL</text>'
        + "".join(boxes) + "</svg>"
    )


def main():
    os.makedirs("fragments", exist_ok=True)
    for slug, song, artist, groups in PANELS:
        out = os.path.join("fragments", "panel-%s.svg" % slug)
        with open(out, "w", encoding="utf-8") as f:
            f.write(panel(slug, song, artist, groups))
        print("wrote", out)


if __name__ == "__main__":
    main()
