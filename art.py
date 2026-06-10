#!/usr/bin/env python3
"""Inline-SVG art for THE SIGNAL CHAIN: an illustrated cover, plus a library of
themed line-art diagrams / infographics injected at the top of relevant chapters.
All vector, self-contained — crisp in HTML and print. Themed by (a=accent, b=accent2)."""

import math
import html as _html

INK = "#2b2017"      # main line on cream
MUT = "#6b5d4c"      # labels
SANS = 'font-family="Helvetica Neue,Arial,sans-serif"'


def esc(s):
    return _html.escape(s, quote=False)


def svg(w, h, inner):
    return ('<svg viewBox="0 0 %d %d" width="%d" height="%d" xmlns="http://www.w3.org/2000/svg" '
            'fill="none" stroke-linecap="round" stroke-linejoin="round">%s</svg>') % (w, h, w, h, inner)


def t(x, y, s, size=12, fill=MUT, weight="400", anchor="middle", ls="0", style=""):
    return ('<text x="%s" y="%s" %s font-size="%s" font-weight="%s" fill="%s" text-anchor="%s" '
            'letter-spacing="%s" %s>%s</text>') % (x, y, SANS, size, weight, fill, anchor, ls, style, esc(s))


def figure(label, caption, inner_svg):
    return ('<figure class="fig"><div class="fig-art">%s</div>'
            '<figcaption><span class="fig-label">%s</span>%s</figcaption></figure>'
            ) % (inner_svg, esc(label), esc(caption))


def inject_hero(body_html, fig_html):
    # insert right after the chapter-head's closing </div>
    return body_html.replace("</div>", "</div>" + fig_html, 1)


# ----------------------------------------------------------------- COVER
def cover_hero(a, b):
    """Amp control-panel faceplate: jack, five knobs, jewel pilot light."""
    cream = "#f2e7cf"
    dim = "#c9b896"
    panel = "#191210"
    parts = []
    # panel + inner engraving line
    parts.append('<rect x="6" y="14" width="448" height="142" rx="10" fill="%s" stroke="%s" stroke-width="2"/>' % (panel, dim))
    parts.append('<rect x="15" y="23" width="430" height="124" rx="6" stroke="%s" stroke-width="1" opacity=".4"/>' % b)
    # corner screws (slotted)
    for sx, sy in ((26, 34), (434, 34), (26, 136), (434, 136)):
        parts.append('<circle cx="%d" cy="%d" r="4" stroke="%s" stroke-width="1.1" opacity=".8"/>' % (sx, sy, dim))
        parts.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.1" opacity=".8"/>'
                     % (sx - 2.3, sy + 2.3, sx + 2.3, sy - 2.3, dim))
    # input jack
    parts.append('<circle cx="56" cy="76" r="13" stroke="%s" stroke-width="2"/>' % cream)
    parts.append('<circle cx="56" cy="76" r="5" stroke="%s" stroke-width="1.4"/>' % b)
    parts.append(t(56, 112, "INPUT", size=9, fill=dim, weight="700", ls=".18em"))
    # five knobs with real settings
    knobs = (("VOLUME", 8), ("BASS", 4), ("MIDS", 7), ("TREBLE", 6), ("REVERB", 3))
    for i, (label, val) in enumerate(knobs):
        cx = 118 + i * 62
        cy = 76
        # tick ring
        for tv in (0, 2.5, 5, 7.5, 10):
            ang = math.radians(-135 + 27 * tv)
            x1 = cx + 21 * math.sin(ang); y1 = cy - 21 * math.cos(ang)
            x2 = cx + 24.5 * math.sin(ang); y2 = cy - 24.5 * math.cos(ang)
            parts.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.1" opacity=".75"/>'
                         % (x1, y1, x2, y2, b))
        parts.append('<circle cx="%d" cy="%d" r="17" stroke="%s" stroke-width="1.9" fill="#140e0a"/>' % (cx, cy, cream))
        ang = math.radians(-135 + 27 * val)
        px = cx + 12.5 * math.sin(ang); py = cy - 12.5 * math.cos(ang)
        parts.append('<line x1="%d" y1="%d" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="2.3"/>' % (cx, cy, px, py, cream))
        parts.append('<circle cx="%d" cy="%d" r="2" fill="%s"/>' % (cx, cy, cream))
        parts.append(t(cx, 112, label, size=9, fill=dim, weight="700", ls=".16em"))
    # jewel pilot light
    parts.append('<circle cx="408" cy="76" r="15" fill="#e0452f" opacity=".14"/>')
    parts.append('<circle cx="408" cy="76" r="10.5" fill="#e0452f" opacity=".22"/>')
    parts.append('<circle cx="408" cy="76" r="9.5" stroke="%s" stroke-width="1.2" opacity=".85"/>' % dim)
    parts.append('<circle cx="408" cy="76" r="6.5" fill="#d8472f"/>')
    parts.append('<circle cx="405.5" cy="73.5" r="2" fill="#ff9d8a" opacity=".9"/>')
    parts.append(t(408, 112, "ON", size=9, fill=dim, weight="700", ls=".2em"))
    # bottom engraving
    parts.append(t(230, 143, "MODEL JSP-2026  \u00b7  HAND-WIRED  \u00b7  POINT-TO-POINT", size=8.5, fill=dim, weight="400", ls=".22em"))
    return svg(460, 170, "".join(parts))


def cover(super_kicker, title, subtitle, author, imprint, a, b):
    return ('<section class="cover"><div class="cover-inner">'
            '<div class="cover-kicker"><span class="cover-lamp"></span>%s</div>'
            '<h1 class="cover-title">%s</h1>'
            '<div class="cover-hero">%s</div>'
            '<p class="cover-sub">%s</p>'
            '<p class="cover-author">%s</p>'
            '<p class="cover-imprint">%s</p>'
            '</div></section>') % (esc(super_kicker), esc(title), cover_hero(a, b),
                                   esc(subtitle), esc(author), esc(imprint))


# ----------------------------------------------------------------- DIAGRAM HELPERS
def _box(x, y, w, h, label, a, fill="none", strong=False):
    sw = 2 if strong else 1.4
    col = a if strong else INK
    return ('<rect x="%d" y="%d" width="%d" height="%d" rx="5" stroke="%s" stroke-width="%s" fill="%s"/>%s'
            ) % (x, y, w, h, col, sw, fill, t(x + w / 2, y + h / 2 + 4, label, 11, INK, "600"))


def _arrow(x1, y, x2, b):
    return ('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1.6"/>'
            '<path d="M%d %d l-6 -4 v8 z" fill="%s"/>') % (x1, y, x2 - 6, y, b, x2, y, b)


def _poly(points, stroke, w=2):
    return '<polyline points="%s" stroke="%s" stroke-width="%s" fill="none"/>' % (points, stroke, w)


def _wavepts(x0, y0, wid, amp, fn, cycles=2, n=72):
    out = []
    for i in range(n + 1):
        ph = i / n * 2 * math.pi * cycles
        out.append("%.1f,%.1f" % (x0 + wid * i / n, y0 - amp * fn(ph)))
    return " ".join(out)


def _clamp(v, lo=-1, hi=1):
    return max(lo, min(hi, v))


# ----------------------------------------------------------------- FIGURES
def fig_signal_chain(a, b):
    P = [t(320, 18, "THE SIGNAL CHAIN", 11, a, "700", ls="2")]
    y = 96
    P.append('<line x1="40" y1="%d" x2="600" y2="%d" stroke="%s" stroke-width="1" opacity=".5"/>' % (y, y, MUT))
    # guitar
    P.append('<ellipse cx="40" cy="%d" rx="16" ry="22" stroke="%s" stroke-width="1.8"/>' % (y, INK))
    P.append(t(40, y + 40, "GUITAR", 9, MUT, "600", ls="1"))
    pedals = [("WAH", a), ("DRIVE", a), ("FUZZ", a), ("MOD", b), ("DELAY", b)]
    x = 86
    for name, c in pedals:
        P.append(_box(x, y - 18, 56, 36, name, c, strong=True))
        P.append(t(x + 28, y + 34, "pedal", 8, MUT))
        x += 70
    # amp + speaker
    P.append(_box(x, y - 26, 70, 52, "AMP", INK, strong=True))
    P.append(t(x + 35, y + 40, "amplifier", 8, MUT))
    sx = x + 96
    P.append('<circle cx="%d" cy="%d" r="22" stroke="%s" stroke-width="1.8"/><circle cx="%d" cy="%d" r="8" stroke="%s" stroke-width="1.4"/>' % (sx, y, INK, sx, y, b))
    for i, r in enumerate((10, 18, 26)):
        P.append('<path d="M%d %d A %d %d 0 0 1 %d %d" stroke="%s" stroke-width="1.4" opacity="%.2f"/>' % (sx + 24, y - r, r, r, sx + 24, y + r, b, 0.8 - i * 0.2))
    P.append(t(sx, y + 40, "SPEAKER", 9, MUT, "600", ls="1"))
    return svg(640, 150, "".join(P))


def fig_amp_anatomy(a, b):
    P = []
    y = 70
    stages = [("INPUT", 30, 54), ("PREAMP", 96, 70), ("TONE\nSTACK", 178, 60), ("PHASE\nINV.", 250, 56),
              ("POWER\nTUBES", 318, 64), ("OUTPUT\nTRANS.", 394, 64), ("SPEAKER", 472, 70)]
    prev = None
    for name, x, w in stages:
        strong = name in ("PREAMP", "POWER\nTUBES")
        lines = name.split("\n")
        P.append('<rect x="%d" y="%d" width="%d" height="56" rx="5" stroke="%s" stroke-width="%s"/>'
                 % (x, y, w, a if strong else INK, 2 if strong else 1.4))
        for i, ln in enumerate(lines):
            P.append(t(x + w / 2, y + 28 + (i - (len(lines) - 1) / 2) * 13 + 4, ln, 10, INK, "600"))
        if prev is not None:
            P.append(_arrow(prev, y + 28, x, b))
        prev = x + w
    # tube glyphs over preamp/power
    for cx in (131, 350):
        P.append('<ellipse cx="%d" cy="46" rx="7" ry="11" stroke="%s" stroke-width="1.3"/><circle cx="%d" cy="46" r="3" fill="%s" opacity=".5"/>' % (cx, b, cx, b))
    P.append(t(131, 28, "12AX7", 8, MUT))
    P.append(t(350, 28, "EL34 / 6L6", 8, MUT))
    P.append(t(270, 150, "Each stage shapes the signal; the tubes add the warm, even-order harmonics.", 10, MUT, anchor="middle"))
    return svg(560, 170, "".join(P))


def fig_eq_spectrum(a, b):
    W, H = 600, 240
    x0, x1, yb = 50, 560, 180
    P = ['<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1.2"/>' % (x0, yb, x1, yb, INK)]
    bands = [("LOWS", "80", 0.0, 0.16, "body & boom"), ("LOW-MIDS", "250", 0.16, 0.34, "warmth / mud"),
             ("MIDS", "500", 0.34, 0.56, "presence / honk"), ("UPPER-MIDS", "2k", 0.56, 0.74, "attack / bite"),
             ("PRESENCE", "4k", 0.74, 0.88, "edge"), ("AIR", "8k+", 0.88, 1.0, "sparkle")]
    for i, (nm, hz, f0, f1, role) in enumerate(bands):
        bx0, bx1 = x0 + (x1 - x0) * f0, x0 + (x1 - x0) * f1
        fill = a if i % 2 == 0 else b
        P.append('<rect x="%.0f" y="60" width="%.0f" height="%d" fill="%s" opacity="%.2f"/>'
                 % (bx0, bx1 - bx0, yb - 60, fill, 0.10 + (i % 2) * 0.05))
        P.append('<line x1="%.0f" y1="60" x2="%.0f" y2="%d" stroke="%s" stroke-width="1" opacity=".4"/>' % (bx0, bx0, yb, MUT))
        P.append(t((bx0 + bx1) / 2, 52, nm, 8.5, INK, "700", ls="0.5"))
        P.append(t((bx0 + bx1) / 2, yb + 16, hz, 9, MUT))
        P.append(t((bx0 + bx1) / 2, yb + 30, role, 8, MUT))
    # a gentle response curve
    pts = []
    for i in range(61):
        f = i / 60
        x = x0 + (x1 - x0) * f
        hump = math.exp(-((f - 0.45) ** 2) / 0.05) * 0.7 + math.exp(-((f - 0.82) ** 2) / 0.03) * 0.4 + 0.25
        pts.append("%.1f,%.1f" % (x, yb - hump * 95))
    P.append(_poly(" ".join(pts), a, 2.4))
    P.append(t(x0, yb + 16, "Hz", 9, MUT, anchor="end"))
    return svg(W, H, "".join(P))


def fig_clipping(a, b):
    W, H = 600, 200
    P = [t(300, 18, "FROM CLEAN TO FUZZ", 11, a, "700", ls="2")]
    panels = [("CLEAN", lambda p: math.sin(p)),
              ("OVERDRIVE", lambda p: math.tanh(1.7 * math.sin(p)) / math.tanh(1.7)),
              ("DISTORTION", lambda p: _clamp(2.4 * math.sin(p))),
              ("FUZZ", lambda p: _clamp(7 * math.sin(p)))]
    pw = 130
    for i, (nm, fn) in enumerate(panels):
        x0 = 30 + i * (pw + 16)
        cy = 100
        P.append('<rect x="%d" y="46" width="%d" height="108" rx="5" stroke="%s" stroke-width="1.2" opacity=".5"/>' % (x0, pw, MUT))
        P.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1" opacity=".4"/>' % (x0 + 8, cy, x0 + pw - 8, cy, MUT))
        col = a if i < 2 else b
        P.append(_poly(_wavepts(x0 + 10, cy, pw - 20, 40, fn), col, 2.2))
        P.append(t(x0 + pw / 2, 172, nm, 9.5, INK, "700", ls="0.5"))
    return svg(W, H, "".join(P))


def fig_harmonic_series(a, b):
    W, H = 560, 210
    P = [t(280, 18, "THE HARMONIC SERIES", 11, a, "700", ls="2")]
    # vibrating string with nodes
    sy = 56
    P.append('<line x1="40" y1="%d" x2="520" y2="%d" stroke="%s" stroke-width="1" opacity=".4"/>' % (sy, sy, MUT))
    pts = []
    for i in range(97):
        x = 40 + 480 * i / 96
        y = sy - 16 * math.sin(math.pi * i / 96) * math.cos(2 * math.pi * 3 * i / 96)
        pts.append("%.1f,%.1f" % (x, y))
    P.append(_poly(" ".join(pts), a, 2))
    P.append('<circle cx="40" cy="%d" r="3" fill="%s"/><circle cx="520" cy="%d" r="3" fill="%s"/>' % (sy, INK, sy, INK))
    # harmonic amplitude bars
    by = 184
    amps = [1.0, 0.6, 0.42, 0.3, 0.24, 0.18, 0.14, 0.1]
    labels = ["1f", "2f", "3f", "4f", "5f", "6f", "7f", "8f"]
    for i, (h, lab) in enumerate(zip(amps, labels)):
        x = 70 + i * 56
        bh = h * 78
        col = a if i == 0 else b
        P.append('<rect x="%d" y="%.0f" width="26" height="%.0f" rx="2" fill="%s" opacity="%.2f" stroke="%s" stroke-width="1"/>'
                 % (x, by - bh, bh, col, 0.85 if i == 0 else 0.5, col))
        P.append(t(x + 13, by + 14, lab, 9, MUT, "600"))
    P.append(t(83, 108, "fundamental", 8.5, MUT, anchor="start"))
    return svg(W, H, "".join(P))


def fig_wah_sweep(a, b):
    W, H = 560, 210
    x0, x1, yb = 50, 520, 168
    P = [t(280, 18, "THE WAH: A SWEPT RESONANT PEAK", 11, a, "700", ls="2"),
         '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1.2"/>' % (x0, yb, x1, yb, INK)]
    for j, (cf, lab, col, op) in enumerate([(0.28, "heel", MUT, .5), (0.5, "mid", b, .8), (0.74, "toe", a, 1)]):
        pts = []
        for i in range(81):
            f = i / 80
            x = x0 + (x1 - x0) * f
            peak = math.exp(-((f - cf) ** 2) / 0.006) * 100
            pts.append("%.1f,%.1f" % (x, yb - 14 - peak))
        P.append('<polyline points="%s" stroke="%s" stroke-width="2.2" fill="none" opacity="%.2f"/>' % (" ".join(pts), col, op))
        P.append(t(x0 + (x1 - x0) * cf, yb - 128, lab, 9, col, "700"))
    P.append('<path d="M%d %d q 235 -36 470 0" stroke="%s" stroke-width="1.2" fill="none" opacity=".4"/>' % (x0, yb - 6, MUT))
    P.append(t(x0, yb + 18, "low", 9, MUT, anchor="start"))
    P.append(t(x1, yb + 18, "high  (frequency)", 9, MUT, anchor="end"))
    return svg(W, H, "".join(P))


def fig_delay_timing(a, b):
    W, H = 600, 190
    y = 100
    P = [t(300, 18, "DELAY AS RHYTHM  (dotted-eighth + quarter)", 11, a, "700", ls="1.5"),
         '<line x1="40" y1="%d" x2="560" y2="%d" stroke="%s" stroke-width="1" opacity=".5"/>' % (y, y, MUT)]
    # beat grid
    for i in range(9):
        x = 60 + i * 60
        P.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1" opacity=".3"/>' % (x, y - 40, x, y + 30, MUT))
        P.append(t(x, y + 44, str(i % 4 + 1) if i % 1 == 0 else "", 9, MUT))
    # played note (tall) + repeats fading
    notes = [(60, 1.0, a, "play"), (105, 0.6, b, "·8th"), (120, 0.45, b, "1/4"), (165, 0.32, b, ""), (180, 0.22, b, ""), (225, 0.16, b, "")]
    for x, h, c, lab in notes:
        P.append('<line x1="%d" y1="%d" x2="%d" y2="%.0f" stroke="%s" stroke-width="3" opacity="%.2f"/>' % (x, y, x, y - 46 * h, c, max(h, .25)))
        P.append('<circle cx="%d" cy="%.0f" r="3.5" fill="%s" opacity="%.2f"/>' % (x, y - 46 * h, c, max(h, .25)))
        if lab:
            P.append(t(x, y - 46 * h - 8, lab, 8, MUT))
    P.append(t(300, 168, "One pick stroke becomes a cascade locked to the tempo.", 10, MUT))
    return svg(W, H, "".join(P))


def fig_gain_staging(a, b):
    W, H = 560, 210
    P = [t(280, 18, "GAIN STAGING — STACKING DIRT", 11, a, "700", ls="2")]
    stages = [("GUITAR", 0.32, MUT), ("BOOST", 0.5, b), ("OVERDRIVE", 0.72, a), ("CRANKED AMP", 1.0, a)]
    y = 60
    for i, (nm, lvl, c) in enumerate(stages):
        yy = y + i * 36
        P.append(t(46, yy + 5, nm, 9.5, INK, "600", anchor="start", ls="0.5"))
        P.append('<rect x="150" y="%d" width="360" height="14" rx="7" stroke="%s" stroke-width="1" opacity=".4"/>' % (yy - 7, MUT))
        P.append('<rect x="150" y="%d" width="%.0f" height="14" rx="7" fill="%s" opacity="%.2f"/>' % (yy - 7, 360 * lvl, c, 0.35 + i * 0.12))
        if i < 3:
            P.append('<path d="M520 %d l8 4 l-8 4 z" fill="%s"/>' % (yy - 3, b))
    P.append(t(280, 196, "Each stage pushes the next — level and saturation accumulate into singing sustain.", 9.5, MUT))
    return svg(W, H, "".join(P))


def fig_pedalboard(a, b):
    W, H = 600, 210
    P = [t(300, 18, "A PEDALBOARD IN SIGNAL ORDER", 11, a, "700", ls="1.5")]
    P.append('<rect x="30" y="40" width="540" height="150" rx="10" stroke="%s" stroke-width="1.6" opacity=".6"/>' % INK)
    order = [("TUNER", MUT), ("WAH", a), ("COMP", b), ("DRIVE", a), ("FUZZ", a), ("CHORUS", b), ("DELAY", b), ("VERB", b)]
    n = len(order)
    pw = 50
    gap = (540 - 40 - n * pw) / (n - 1)
    x = 50
    cy = 115
    P.append('<line x1="40" y1="%d" x2="560" y2="%d" stroke="%s" stroke-width="1.4" opacity=".5"/>' % (cy, cy, b))
    for nm, c in order:
        P.append('<rect x="%.0f" y="%d" width="%d" height="58" rx="5" stroke="%s" stroke-width="1.7" fill="#fff" fill-opacity=".0"/>' % (x, cy - 29, pw, c))
        P.append('<circle cx="%.0f" cy="%d" r="4" stroke="%s" stroke-width="1.2"/><circle cx="%.0f" cy="%d" r="4" stroke="%s" stroke-width="1.2"/>' % (x + 15, cy - 14, c, x + pw - 15, cy - 14, c))
        P.append('<rect x="%.0f" y="%d" width="16" height="9" rx="2" stroke="%s" stroke-width="1.2"/>' % (x + pw / 2 - 8, cy + 12, c))
        P.append(t(x + pw / 2, cy + 44, nm, 8, INK, "600"))
        x += pw + gap
    return svg(W, H, "".join(P))


def fig_amp_stack(a, b):
    W, H = 300, 380
    P = []
    # head
    P.append('<rect x="60" y="30" width="180" height="64" rx="8" stroke="%s" stroke-width="2.2"/>' % INK)
    P.append('<rect x="72" y="40" width="156" height="20" rx="3" stroke="%s" stroke-width="1.3" opacity=".7"/>' % b)
    for kx in range(86, 220, 18):
        P.append('<circle cx="%d" cy="50" r="4" stroke="%s" stroke-width="1.2"/>' % (kx, b))
    P.append(t(150, 82, "HEAD  ·  100 watts", 9, MUT, "600", ls="1"))
    # 4x12 cabinet
    P.append('<rect x="40" y="104" width="220" height="250" rx="10" stroke="%s" stroke-width="2.4"/>' % INK)
    P.append('<rect x="58" y="122" width="184" height="214" rx="6" stroke="%s" stroke-width="1.4" opacity=".7"/>' % b)
    for r in range(2):
        for c in range(2):
            cx, cy = 105 + c * 92, 175 + r * 92
            P.append('<circle cx="%d" cy="%d" r="40" stroke="%s" stroke-width="1.8"/><circle cx="%d" cy="%d" r="15" stroke="%s" stroke-width="1.3"/><circle cx="%d" cy="%d" r="4" fill="%s"/>' % (cx, cy, INK, cx, cy, b, cx, cy, b))
    P.append(t(150, 372, "4 × 12″ CABINET", 9, MUT, "600", ls="1"))
    return svg(W, H, "".join(P))


def fig_pedal(a, b):
    W, H = 280, 360
    P = []
    P.append('<rect x="50" y="30" width="180" height="300" rx="14" stroke="%s" stroke-width="2.4"/>' % INK)
    # knobs
    for i, (kx, lab) in enumerate([(90, "VOL"), (140, "TONE"), (190, "GAIN")]):
        P.append('<circle cx="%d" cy="92" r="20" stroke="%s" stroke-width="1.8"/>' % (kx, INK))
        ang = -2.1 + i * 0.7
        P.append('<line x1="%d" y1="92" x2="%.0f" y2="%.0f" stroke="%s" stroke-width="2"/>' % (kx, kx + 14 * math.cos(ang), 92 + 14 * math.sin(ang), a))
        P.append(t(kx, 128, lab, 8, MUT, "600"))
    # status LED
    P.append('<circle cx="140" cy="158" r="5" fill="%s"/><circle cx="140" cy="158" r="9" stroke="%s" stroke-width="1" opacity=".5"/>' % (a, a))
    # footswitch
    P.append('<circle cx="140" cy="250" r="34" stroke="%s" stroke-width="2.4"/><circle cx="140" cy="250" r="22" stroke="%s" stroke-width="1.4" opacity=".6"/>' % (INK, b))
    P.append(t(140, 306, "TRUE BYPASS", 8, MUT, "600", ls="1"))
    # jacks
    P.append('<circle cx="50" cy="120" r="9" stroke="%s" stroke-width="1.6"/><circle cx="230" cy="120" r="9" stroke="%s" stroke-width="1.6"/>' % (INK, INK))
    P.append(t(34, 124, "IN", 8, MUT, anchor="end"))
    P.append(t(246, 124, "OUT", 8, MUT, anchor="start"))
    return svg(W, H, "".join(P))


def fig_timeline(a, b):
    W, H = 600, 250
    y = 150
    P = ['<line x1="40" y1="%d" x2="560" y2="%d" stroke="%s" stroke-width="1.6"/>' % (y, y, INK)]
    marks = [("1931", "Frying Pan", -1), ("1952", "Tweed", 1), ("1959", "Plexi", -1), ("1962", "AC30 / Cry Baby", 1),
             ("1969", "Big Muff", -1), ("1979", "Mesa", 1), ("1980", "JCM800", -1), ("1991", "SLO-100", 1),
             ("1998", "POD", -1), ("2008", "Axe-Fx", 1)]
    n = len(marks)
    for i, (yr, lab, side) in enumerate(marks):
        x = 60 + i * (480 / (n - 1))
        col = a if i % 2 == 0 else b
        P.append('<circle cx="%.0f" cy="%d" r="5" fill="%s"/>' % (x, y, col))
        ly = y + side * 30
        P.append('<line x1="%.0f" y1="%d" x2="%.0f" y2="%.0f" stroke="%s" stroke-width="1" opacity=".5"/>' % (x, y, x, ly, MUT))
        P.append(t(x, ly + (12 if side > 0 else -4), yr, 9.5, INK, "700"))
        P.append(t(x, ly + (24 if side > 0 else -16), lab, 8.5, MUT))
    P.append(t(300, 20, "A CENTURY OF TONE", 11, a, "700", ls="2"))
    return svg(W, H, "".join(P))


# chapter file -> (figure key, caption)
HERO = {
    "01-the-electric-signal.md": ("harmonic_series", "A struck string sounds a fundamental plus a stack of quieter overtones; pickup position decides which you hear."),
    "02-anatomy-of-an-amplifier.md": ("amp_anatomy", "The path of your signal through a tube amplifier, from input jack to speaker cone."),
    "03-the-language-of-tone.md": ("eq_spectrum", "The guitar's frequency range, band by band, and what each one does for your tone."),
    "10-marshall-birth-of-the-stack.md": ("amp_stack", "The full stack: a 100-watt head atop a 4x12 cabinet of Celestions."),
    "16-the-fuzz-explosion.md": ("clipping", "From clean to fuzz — how progressively harder clipping reshapes the waveform."),
    "17-the-wah-wah.md": ("wah_sweep", "A wah pedal sweeps a resonant peak across the midrange — the guitar learning to say a vowel."),
    "22-the-tube-screamer.md": ("pedal", "The anatomy of an overdrive stompbox."),
    "23-echo-and-delay.md": ("delay_timing", "Delay as rhythm: one pick stroke and its dotted-eighth and quarter-note repeats."),
    "43-signal-chain-order.md": ("signal_chain", "A typical signal chain — each effect hears whatever sits in front of it, so order is tone."),
    "44-gain-staging.md": ("gain_staging", "Stacking gain: each stage adds level and saturation as it pushes into the next."),
    "45-building-the-pedalboard.md": ("pedalboard", "A pedalboard laid out in signal order, from tuner to reverb."),
    "48-appendix-b-timeline.md": ("timeline", "A century of amplifiers and effects, at a glance."),
}


def hero_html(fn, n, a, b):
    h = HERO.get(fn)
    if not h:
        return None
    svg_inner = globals()["fig_" + h[0]](a, b)
    return figure("Figure %d" % n, h[1], svg_inner)
