#!/usr/bin/env python3
"""Build THE SIGNAL CHAIN — DELUXE EDITION: the full book with all 50 lessons
interleaved as indigo 'Workshop' blocks. Uses the shared bookkit engine."""

import os
import re
import bookkit as bk
import art

BASE = os.path.dirname(os.path.abspath(__file__))
CH = os.path.join(BASE, "chapters")
LES = os.path.join(BASE, "workbook", "lessons")
TITLE = "THE SIGNAL CHAIN"
SUB = "A Life in Six Strings"
EPIGRAPH = "First the story of the sound. Then the sound in your own hands."
AUTHOR = "Jason Colapietro"

THEME = {"paper": "#f7f2e8", "ink": "#2a2118", "inksoft": "#6b5d4c", "accent": "#8c2f22",
         "accent2": "#b06a24", "rule": "#d9c9a9", "tabbg": "#efe6d2", "quote": "#efe6d2"}
WS = {"wsbg": "#f1f0f9", "wsaccent": "#2b2f77", "wsaccent2": "#9a7b2e", "wstab": "#ece9f4", "wsquote": "#e9e7f3"}

# The opening cluster is THE pre-memoir; a teaser for Jason's forthcoming memoir, "Loaded."
MEMOIR_PART = "Six Strings, No Serial Number"
MEMOIR_NOTE = ("> **Coming soon.** These chapters are early excerpts from *Loaded: Part Lore, Part War Stories*, "
               "Jason Colapietro's forthcoming memoir.")

ORDER = [
    ("00-front-matter.md", "Front Matter"),
    ("00a-prologue.md", MEMOIR_PART),
    ("00b-origins.md", MEMOIR_PART),
    ("00c-inheritance.md", MEMOIR_PART),
    ("00d-geography.md", MEMOIR_PART),
    ("THEORY-curriculum.md", "Learning the Language"),
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
    ("GEAR1-tone-quest.md", "The Player's Gear"),
    ("GEAR2-the-trinity.md", "The Player's Gear"),
    ("GEAR3-pedalboard.md", "The Player's Gear"),
    ("GEAR4-two-setups.md", "The Player's Gear"),
    ("GEAR5-working-stack.md", "The Player's Gear"),
    ("SB1-songwriters.md", "The Songbook"),
    ("SB2-riff-makers.md", "The Songbook"),
    ("SB3-avant-garde.md", "The Songbook"),
    ("EPILOGUE.md", "Epilogue"),
    ("47-appendix-a-glossary.md", "Appendices"),
    ("48-appendix-b-timeline.md", "Appendices"),
    ("49-appendix-c-tab-reference.md", "Appendices"),
    ("50-appendix-d-discography.md", "Appendices"),
    ("BACKMATTER-extra.md", "Appendices"),
]
CH2LESSON = {
    5: ["L01-solo-flight"], 6: ["L02-johnny-b-goode", "L03-peggy-sue"], 7: ["L05-mannish-boy"], 8: ["L04-rumble"],
    10: ["L18-smoke-on-the-water", "L20-back-in-black"], 11: ["L06-ticket-to-ride"], 12: ["L19-sweet-home-alabama", "L43-under-the-bridge"],
    13: ["L08-pinball-wizard"], 15: ["L09-misirlou"], 16: ["L07-you-really-got-me", "L11-satisfaction", "L14-purple-haze"],
    18: ["L15-paranoid"], 19: ["L24-bridge-of-sighs"], 20: ["L23-shine-on-you-crazy-diamond", "L40-cherub-rock"],
    22: ["L29-texas-flood", "L35-master-of-puppets"], 23: ["L10-apache"], 24: ["L25-more-than-a-feeling", "L26-walking-on-the-moon"],
    25: ["L27-sultans-of-swing"], 26: ["L34-crazy-train", "L50-black-magic-woman"], 28: ["L36-cliffs-of-dover", "L49-hotel-california"],
    29: ["L37-surfing-with-the-alien"], 30: ["L41-black-hole-sun"], 31: ["L46-paranoid-android"], 32: ["L12-voodoo-child"],
    33: ["L13-white-room"], 34: ["L16-whole-lotta-love", "L17-stairway-to-heaven"], 35: ["L22-comfortably-numb"],
    36: ["L32-eruption", "L33-aint-talkin-bout-love"], 37: ["L28-pride-and-joy"], 38: ["L44-where-the-streets-have-no-name", "L45-with-or-without-you"],
    39: ["L38-smells-like-teen-spirit", "L39-come-as-you-are"], 40: ["L30-the-thrill-is-gone", "L31-still-got-the-blues", "L47-gravity"],
    41: ["L21-boys-are-back-in-town", "L48-bohemian-rhapsody"], 42: ["L42-killing-in-the-name"],
}


def cnum(fn):
    m = re.match(r"^(\d+)", fn)
    return int(m.group(1)) if m else -1


def chbody(fn):
    t = bk.read_text(os.path.join(CH, fn))
    if fn == "00-front-matter.md":
        i = t.find("\n## ")
        if i != -1:
            t = t[i + 1:]
    return t


def part_meta(part):
    if part == MEMOIR_PART:
        return "THE PRE-MEMOIR", part, "❖"
    if part.startswith("Part "):
        kick, name = part.split(":", 1)
        return kick.strip().upper(), name.strip(), kick.replace("Part", "").strip()
    return "", part, "❖"


def csec(fn):
    return "sec-" + fn[:-3]


def lsec(fn):
    return "ws-" + fn


def pid(part):
    return re.sub(r"[^a-z0-9]+", "-", part.lower()).strip("-")


part_seq, by_part, ch_head, les_head = [], {}, {}, {}
for fn, p in ORDER:
    if p not in part_seq:
        part_seq.append(p)
    by_part.setdefault(p, []).append(fn)
    ch_head[fn] = bk.heading_of(bk.read_text(os.path.join(CH, fn)))
for fns in CH2LESSON.values():
    for lf in fns:
        les_head[lf] = bk.heading_of(bk.read_text(os.path.join(LES, lf + ".md")))

# master markdown
md = ["# %s\n" % TITLE, "*%s*\n" % SUB, "\n**by %s**\n" % AUTHOR, "_Johnny Suede Press_\n", "> %s\n" % EPIGRAPH, "\n---\n", "## Contents\n"]
for p in part_seq:
    if p == "Front Matter":
        md.append("- **Front Matter**")
        continue
    md.append("- **%s**" % p)
    for fn in by_part[p]:
        md.append("  - %s" % ch_head[fn])
        for lf in CH2LESSON.get(cnum(fn), []):
            md.append("    - WORKSHOP — %s" % les_head[lf])
for p in part_seq:
    if p != "Front Matter":
        md.append("\n\n---\n\n# %s\n\n---\n" % p)
    if p == MEMOIR_PART:
        md.append("\n" + MEMOIR_NOTE + "\n")
    for fn in by_part[p]:
        md.append("\n\n" + chbody(fn).strip() + "\n")
        for lf in CH2LESSON.get(cnum(fn), []):
            md.append("\n\n> **WORKSHOP — PLAY IT**\n\n" + bk.read_text(os.path.join(LES, lf + ".md")).strip() + "\n")
master = "\n".join(md)
open(os.path.join(BASE, "THE-SIGNAL-CHAIN-DELUXE.md"), "w", encoding="utf-8").write(master)

# html
A, A2 = THEME["accent"], THEME["accent2"]
META_TITLE = "THE SIGNAL CHAIN: A Life in Six Strings — Guitar Tone History + 50 Hands-On Lessons"
DESC = ("THE SIGNAL CHAIN: A Life in Six Strings by Jason Colapietro (Johnny Suede): the complete illustrated "
        "history of guitar amplifiers and effects, with fifty hands-on song-tone lessons and tablature "
        "interleaved throughout.")
KEYWORDS = ("guitar tone, guitar amplifiers, effects pedals, guitar history, guitar lessons, tablature, "
            "music theory, Marshall, Fender, Vox, fuzz, Tube Screamer, Jason Colapietro, Johnny Suede")
B = [art.cover("The Complete Edition", TITLE, SUB, AUTHOR, "Johnny Suede Press", A, A2),
     bk.title_page("The Complete Edition", TITLE, SUB, AUTHOR, EPIGRAPH,
                   "46 Chapters &middot; 50 Workshops &middot; With Tablature", A, A2, "Johnny Suede Press")]
B.append('<nav class="toc"><h2>Contents</h2>')
for p in part_seq:
    if p == "Front Matter":
        B.append('<div class="toc-part"><a href="#%s">Front Matter</a></div>' % csec("00-front-matter.md"))
        continue
    B.append('<div class="toc-part"><a href="#%s">%s</a></div>' % (pid(p), bk.esc(p.replace(":", " ·"))))
    B.append("<ul>")
    for fn in by_part[p]:
        B.append('<li><a href="#%s">%s</a></li>' % (csec(fn), bk.esc(ch_head[fn])))
        for lf in CH2LESSON.get(cnum(fn), []):
            B.append('<li class="ws"><a href="#%s">&#9670; %s</a></li>' % (lsec(lf), bk.esc(les_head[lf])))
    B.append("</ul>")
B.append("</nav>")
fig_no = 0
for p in part_seq:
    if p != "Front Matter":
        k, nm, g = part_meta(p)
        B.append(bk.part_divider(pid(p), g, k, nm, A, A2))
    if p == MEMOIR_PART:
        B.append(bk.render_blocks(MEMOIR_NOTE.splitlines()))
    for fn in by_part[p]:
        bh = bk.render_blocks(chbody(fn).splitlines())
        fh = art.hero_html(fn, fig_no + 1, A, A2)
        if fh:
            fig_no += 1
            bh = art.inject_hero(bh, fh)
        B.append('<section class="chapter" id="%s">%s</section>' % (csec(fn), bh))
        for lf in CH2LESSON.get(cnum(fn), []):
            B.append('<section class="chapter workshop" id="%s">%s</section>'
                     % (lsec(lf), bk.render_blocks(bk.read_text(os.path.join(LES, lf + ".md")).splitlines())))
B.append(bk.paywall("sec-02-anatomy-of-an-amplifier", "https://buy.stripe.com/3cIfZjbldfDT7RafInaZi0h"))
html = bk.doc(META_TITLE + " | Jason Colapietro (Johnny Suede)", bk.build_css(THEME, WS),
              "\n".join(B), bk.seo_head(META_TITLE, DESC, KEYWORDS, AUTHOR, "Johnny Suede Press"))
open(os.path.join(BASE, "THE-SIGNAL-CHAIN-DELUXE.html"), "w", encoding="utf-8").write(html)

print("deluxe: %d chapters + %d workshops, %d tab blocks, %d words" %
      (len(ORDER), sum(len(v) for v in CH2LESSON.values()), html.count('<pre class="tab">'), len(re.findall(r"\S+", master))))
