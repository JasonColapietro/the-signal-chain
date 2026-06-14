#!/usr/bin/env python3
"""Assemble THE TONE WORKBOOK (50 lessons) -> master Markdown + typeset HTML.
Uses the shared bookkit engine. Indigo + antique-gold companion theme."""

import os
import re
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
import bookkit as bk
import art

LES = os.path.join(BASE, "workbook", "lessons")
SUPER = "The Signal Chain · Companion"
TITLE = "THE TONE WORKBOOK"
SUBTITLE = "Fifty Iconic Tones — How to Hear Them, Dial Them In, and Play Them"
EPIGRAPH = "You do not learn a tone by buying it. You learn it by chasing the sound in your own hands."
AUTHOR = "Jason Colapietro"

THEME = {"paper": "#f6f3ec", "ink": "#211f24", "inksoft": "#5f5a52", "accent": "#2b2f77",
         "accent2": "#9a7b2e", "rule": "#d6cdb6", "tabbg": "#ece7da", "quote": "#eae8f2"}

PARTS = [
    ("0 · Theory: The Self-Taught Curriculum", ["THEORY-curriculum"]),
    ("A · Foundations & Tweed", ["L01-solo-flight", "L02-johnny-b-goode", "L03-peggy-sue", "L04-rumble", "L05-mannish-boy"]),
    ("B · British Invasion & 60s Amps", ["L06-ticket-to-ride", "L07-you-really-got-me", "L08-pinball-wizard", "L09-misirlou", "L10-apache"]),
    ("C · Fuzz, Wah & First Effects", ["L11-satisfaction", "L12-voodoo-child", "L13-white-room", "L14-purple-haze", "L15-paranoid"]),
    ("D · Classic Rock: Marshall & Les Paul", ["L16-whole-lotta-love", "L17-stairway-to-heaven", "L18-smoke-on-the-water", "L19-sweet-home-alabama", "L20-back-in-black", "L21-boys-are-back-in-town"]),
    ("E · 70s Pedals, Modulation & Sustain", ["L22-comfortably-numb", "L23-shine-on-you-crazy-diamond", "L24-bridge-of-sighs", "L25-more-than-a-feeling", "L26-walking-on-the-moon", "L27-sultans-of-swing"]),
    ("F · Blues & the Tube Screamer", ["L28-pride-and-joy", "L29-texas-flood", "L30-the-thrill-is-gone", "L31-still-got-the-blues"]),
    ("G · High Gain, the 80s & Shred", ["L32-eruption", "L33-aint-talkin-bout-love", "L34-crazy-train", "L35-master-of-puppets", "L36-cliffs-of-dover", "L37-surfing-with-the-alien"]),
    ("H · Alt, Grunge & Modern Rock", ["L38-smells-like-teen-spirit", "L39-come-as-you-are", "L40-cherub-rock", "L41-black-hole-sun", "L42-killing-in-the-name", "L43-under-the-bridge"]),
    ("I · Atmosphere & Delay", ["L44-where-the-streets-have-no-name", "L45-with-or-without-you", "L46-paranoid-android", "L47-gravity"]),
    ("J · Tone Showcases", ["L48-bohemian-rhapsody", "L49-hotel-california", "L50-black-magic-woman"]),
]


def csec(fn):
    return "sec-" + fn


def pid(part):
    return re.sub(r"[^a-z0-9]+", "-", part.lower()).strip("-")


def part_meta(part):
    letter, name = part.split("·", 1)
    return "PART " + letter.strip(), name.strip(), letter.strip()


heads = {}
for _, fns in PARTS:
    for fn in fns:
        heads[fn] = bk.heading_of(bk.read_text(os.path.join(LES, fn + ".md")))

# master markdown
md = ["# %s — %s\n" % (SUPER, TITLE), "*%s*\n" % SUBTITLE, "\n**by %s**\n" % AUTHOR, "_Johnny Suede Press_\n", "> %s\n" % EPIGRAPH, "\n---\n", "## Contents\n"]
for part, fns in PARTS:
    md.append("- **%s**" % part)
    for fn in fns:
        md.append("  - %s" % heads[fn])
for part, fns in PARTS:
    md.append("\n\n---\n\n# %s\n\n---\n" % part)
    for fn in fns:
        md.append("\n\n" + bk.read_text(os.path.join(LES, fn + ".md")).strip() + "\n")
master = "\n".join(md)
open(os.path.join(BASE, "THE-SIGNAL-CHAIN-WORKBOOK.md"), "w", encoding="utf-8").write(master)

# html
A, A2 = THEME["accent"], THEME["accent2"]
META_TITLE = "THE TONE WORKBOOK — Fifty Iconic Guitar Tones, Decoded with Tablature"
DESC = ("THE TONE WORKBOOK by Jason Colapietro (Johnny Suede): fifty iconic guitar tones broken down "
        "with the real gear, accessible tone recipes, music theory, and original tablature drills.")
KEYWORDS = ("guitar lessons, guitar tone, how to sound like, guitar tablature, gear and settings, fuzz, "
            "overdrive, Tube Screamer, Big Muff, Stevie Ray Vaughan, Hendrix, Gilmour, "
            "Jason Colapietro, Johnny Suede")
B = [art.cover(SUPER, TITLE, SUBTITLE, AUTHOR, "Johnny Suede Press", A, A2),
     bk.title_page(SUPER, TITLE, SUBTITLE, AUTHOR, EPIGRAPH, "Fifty Lessons &middot; With Tablature", A, A2, "Johnny Suede Press")]
B.append('<nav class="toc"><h2>Contents</h2>')
for part, fns in PARTS:
    B.append('<div class="toc-part"><a href="#%s">Part %s</a></div>' % (pid(part), bk.esc(part)))
    B.append("<ul>")
    for fn in fns:
        B.append('<li><a href="#%s">%s</a></li>' % (csec(fn), bk.esc(heads[fn])))
    B.append("</ul>")
B.append("</nav>")
for part, fns in PARTS:
    k, nm, g = part_meta(part)
    B.append(bk.part_divider(pid(part), g, k, nm, A, A2))
    for fn in fns:
        B.append('<section class="chapter" id="%s">%s</section>'
                 % (csec(fn), bk.render_blocks(bk.read_text(os.path.join(LES, fn + ".md")).splitlines())))
free_B, locked_html = bk.split_gated(B, "sec-L02-johnny-b-goode")
free_B.append(bk.gate_block("workbook", "https://buy.stripe.com/eVqcN774Xajzb3mgMraZi0i"))
html = bk.doc(META_TITLE + " | Jason Colapietro (Johnny Suede)", bk.build_css(THEME),
              "\n".join(B), bk.seo_head(META_TITLE, DESC, KEYWORDS, AUTHOR, "Johnny Suede Press"))
gated = bk.doc(META_TITLE + " | Jason Colapietro (Johnny Suede)", bk.build_css(THEME),
               "\n".join(free_B), bk.seo_head(META_TITLE, DESC, KEYWORDS, AUTHOR, "Johnny Suede Press"))
open(os.path.join(BASE, "THE-SIGNAL-CHAIN-WORKBOOK.html"), "w", encoding="utf-8").write(gated)
open(os.path.join(BASE, "THE-SIGNAL-CHAIN-WORKBOOK-FULL.html"), "w", encoding="utf-8").write(html)
bk.write_locked_fragment("workbook", locked_html)

print("workbook: %d lessons, %d tab blocks, %d words" %
      (sum(len(f) for _, f in PARTS), html.count('<pre class="tab">'), len(re.findall(r"\S+", master))))
