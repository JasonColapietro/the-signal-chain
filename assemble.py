#!/usr/bin/env python3
"""Assemble THE SIGNAL CHAIN (main book) -> master Markdown + typeset HTML.
Uses the shared bookkit engine. Oxblood + amber theme on warm cream."""

import os
import re
import bookkit as bk
import art

BASE = os.path.dirname(os.path.abspath(__file__))
CH = os.path.join(BASE, "chapters")
TITLE = "THE SIGNAL CHAIN"
SUBTITLE = "A Player's History of Amplifiers, Effects, and the Pursuit of Electric Guitar Tone"
EPIGRAPH = "Tone is not a thing you buy. It is the whole journey of a string's voice, from steel to speaker."
AUTHOR = "Jason Colapietro"

THEME = {"paper": "#f7f2e8", "ink": "#2a2118", "inksoft": "#6b5d4c", "accent": "#8c2f22",
         "accent2": "#b06a24", "rule": "#d9c9a9", "tabbg": "#efe6d2", "quote": "#efe6d2"}

ORDER = [
    ("00-front-matter.md", "Front Matter"),
    ("01-the-electric-signal.md", "Part I: Foundations"),
    ("02-anatomy-of-an-amplifier.md", "Part I: Foundations"),
    ("03-the-language-of-tone.md", "Part I: Foundations"),
    ("04-pickups-wood-and-truth.md", "Part I: Foundations"),
    ("05-frying-pan-to-charlie-christian.md", "Part II: Birth of Amplification"),
    ("06-leo-fender-and-the-tweed-era.md", "Part II: Birth of Amplification"),
    ("07-the-tweed-bassman.md", "Part II: Birth of Amplification"),
    ("08-gibson-valco-american-combo.md", "Part II: Birth of Amplification"),
    ("09-danelectro-supro-cheap-genius.md", "Part II: Birth of Amplification"),
    ("10-marshall-birth-of-the-stack.md", "Part III: The British Invasion"),
    ("11-vox-ac30-chime-and-jangle.md", "Part III: The British Invasion"),
    ("12-fender-blackface-brownface.md", "Part III: The British Invasion"),
    ("13-hiwatt-and-the-command-sound.md", "Part III: The British Invasion"),
    ("14-tremolo-and-vibrato.md", "Part IV: The First Effects"),
    ("15-spring-reverb-surf-and-space.md", "Part IV: The First Effects"),
    ("16-the-fuzz-explosion.md", "Part IV: The First Effects"),
    ("17-the-wah-wah.md", "Part IV: The First Effects"),
    ("18-treble-booster-british-lead.md", "Part IV: The First Effects"),
    ("19-the-univibe.md", "Part V: The Pedal Revolution"),
    ("20-the-big-muff.md", "Part V: The Pedal Revolution"),
    ("21-mxr-and-the-phase-90.md", "Part V: The Pedal Revolution"),
    ("22-the-tube-screamer.md", "Part V: The Pedal Revolution"),
    ("23-echo-and-delay.md", "Part V: The Pedal Revolution"),
    ("24-chorus-flange-modulation-boom.md", "Part V: The Pedal Revolution"),
    ("25-the-compressor.md", "Part V: The Pedal Revolution"),
    ("26-mesa-boogie-high-gain.md", "Part VI: High Gain & the Modern Era"),
    ("27-hot-rodded-marshall-brown-sound.md", "Part VI: High Gain & the Modern Era"),
    ("28-rack-systems-big-80s-rig.md", "Part VI: High Gain & the Modern Era"),
    ("29-soldano-bogner-boutique.md", "Part VI: High Gain & the Modern Era"),
    ("30-grunge-and-the-return-of-fuzz.md", "Part VI: High Gain & the Modern Era"),
    ("31-digital-modeling.md", "Part VI: High Gain & the Modern Era"),
    ("32-jimi-hendrix.md", "Part VII: Tone in Practice — The Players"),
    ("33-eric-clapton.md", "Part VII: Tone in Practice — The Players"),
    ("34-jimmy-page.md", "Part VII: Tone in Practice — The Players"),
    ("35-david-gilmour.md", "Part VII: Tone in Practice — The Players"),
    ("36-eddie-van-halen.md", "Part VII: Tone in Practice — The Players"),
    ("37-stevie-ray-vaughan.md", "Part VII: Tone in Practice — The Players"),
    ("38-the-edge.md", "Part VII: Tone in Practice — The Players"),
    ("39-kurt-cobain.md", "Part VII: Tone in Practice — The Players"),
    ("40-modern-blues-torchbearers.md", "Part VII: Tone in Practice — The Players"),
    ("41-brian-may.md", "Part VII: Tone in Practice — The Players"),
    ("42-tom-morello.md", "Part VII: Tone in Practice — The Players"),
    ("43-signal-chain-order.md", "Part VIII: Building Your Rig"),
    ("44-gain-staging.md", "Part VIII: Building Your Rig"),
    ("45-building-the-pedalboard.md", "Part VIII: Building Your Rig"),
    ("46-matching-tone-to-music.md", "Part VIII: Building Your Rig"),
    ("47-appendix-a-glossary.md", "Appendices"),
    ("48-appendix-b-timeline.md", "Appendices"),
    ("49-appendix-c-tab-reference.md", "Appendices"),
    ("50-appendix-d-discography.md", "Appendices"),
]


def body_of(fn):
    t = bk.read_text(os.path.join(CH, fn))
    if fn == "00-front-matter.md":
        idx = t.find("\n## ")
        if idx != -1:
            t = t[idx + 1:]
    return t


def part_meta(part):
    if part.startswith("Part "):
        kick, name = part.split(":", 1)
        ghost = kick.replace("Part", "").strip()
        return kick.strip().upper(), name.strip(), ghost
    return "", part, "❖"


def csec(fn):
    return "sec-" + fn[:-3]


def pid(part):
    return re.sub(r"[^a-z0-9]+", "-", part.lower()).strip("-")


part_seq, by_part, heads = [], {}, {}
for fn, p in ORDER:
    if p not in part_seq:
        part_seq.append(p)
    by_part.setdefault(p, []).append(fn)
    heads[fn] = bk.heading_of(bk.read_text(os.path.join(CH, fn)))

# master markdown
md = ["# %s\n" % TITLE, "*%s*\n" % SUBTITLE, "\n**by %s**\n" % AUTHOR, "_Johnny Suede Press_\n", "> %s\n" % EPIGRAPH, "\n---\n", "## Contents\n"]
for p in part_seq:
    if p == "Front Matter":
        md.append("- **Front Matter** — Preface & How to Read This Book")
        continue
    md.append("- **%s**" % p)
    for fn in by_part[p]:
        md.append("  - %s" % heads[fn])
for p in part_seq:
    if p != "Front Matter":
        md.append("\n\n---\n\n# %s\n\n---\n" % p)
    for fn in by_part[p]:
        md.append("\n\n" + body_of(fn).strip() + "\n")
master = "\n".join(md)
open(os.path.join(BASE, "THE-SIGNAL-CHAIN.md"), "w", encoding="utf-8").write(master)

# html
A, A2 = THEME["accent"], THEME["accent2"]
META_TITLE = "THE SIGNAL CHAIN — A Player's History of Guitar Tone, Amps & Effects"
DESC = ("THE SIGNAL CHAIN by Jason Colapietro (Johnny Suede): an illustrated history of guitar "
        "amplifiers, effects pedals, and tone, with rich gear history, mid-level music theory, and "
        "hundreds of properly formatted guitar tablature examples.")
KEYWORDS = ("guitar tone, guitar amplifier history, effects pedals, fuzz, overdrive, Tube Screamer, "
            "Big Muff, Marshall, Fender, Vox, Uni-Vibe, guitar tablature, music theory, "
            "Jason Colapietro, Johnny Suede")
B = [art.cover("A History of Guitar Tone", TITLE, SUBTITLE, AUTHOR, "Johnny Suede Press", A, A2),
     bk.title_page("A History of Guitar Tone", TITLE, SUBTITLE, AUTHOR, EPIGRAPH,
                   "An Illustrated History &middot; With Tablature", A, A2, "Johnny Suede Press")]
B.append('<nav class="toc"><h2>Contents</h2>')
for p in part_seq:
    if p == "Front Matter":
        B.append('<div class="toc-part"><a href="#%s">Front Matter</a></div>' % csec("00-front-matter.md"))
        B.append('<ul><li><a href="#%s">Preface &amp; How to Read This Book</a></li></ul>' % csec("00-front-matter.md"))
        continue
    B.append('<div class="toc-part"><a href="#%s">%s</a></div>' % (pid(p), bk.esc(p.replace(":", " &middot;"))))
    B.append("<ul>")
    for fn in by_part[p]:
        B.append('<li><a href="#%s">%s</a></li>' % (csec(fn), bk.esc(heads[fn])))
    B.append("</ul>")
B.append("</nav>")
fig_no = 0
for p in part_seq:
    if p != "Front Matter":
        k, nm, g = part_meta(p)
        B.append(bk.part_divider(pid(p), g, k, nm, A, A2))
    for fn in by_part[p]:
        bh = bk.render_blocks(body_of(fn).splitlines())
        fh = art.hero_html(fn, fig_no + 1, A, A2)
        if fh:
            fig_no += 1
            bh = art.inject_hero(bh, fh)
        B.append('<section class="chapter" id="%s">%s</section>' % (csec(fn), bh))
SITE = "https://guitar.solutions"
html = bk.doc(META_TITLE + " | Jason Colapietro (Johnny Suede)", bk.build_css(THEME),
              "\n".join(B), bk.seo_head(META_TITLE, DESC, KEYWORDS, AUTHOR, "Johnny Suede Press",
                                        SITE + "/THE-SIGNAL-CHAIN.html", SITE + "/og-card.png"))
open(os.path.join(BASE, "THE-SIGNAL-CHAIN.html"), "w", encoding="utf-8").write(html)

print("book: %d sections, %d tab blocks, %d words" %
      (len(ORDER), html.count('<pre class="tab">'), len(re.findall(r"\S+", master))))
