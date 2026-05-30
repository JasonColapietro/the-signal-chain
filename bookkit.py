#!/usr/bin/env python3
"""Shared typesetting engine for THE SIGNAL CHAIN editions.
Markdown -> beautiful self-contained HTML. No external deps.
Design language: warm cream paper, dual accent (primary + secondary), ghosted part
numerals, an inline-SVG signal-chain ornament, drop caps, and labeled
Tab / Listen-For / At-a-Glance cards."""

import html as _html
import re


def esc(s):
    return _html.escape(s, quote=False)


def slugify(s):
    s = re.sub(r"&[a-z]+;", " ", s.lower())
    s = re.sub(r"<[^>]+>", " ", s)
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s or "x"


def _emph_italic(s):
    s = re.sub(r"(?<!\*)\*(?!\*)([^*\n]+?)\*(?!\*)", r"<em>\1</em>", s)
    s = re.sub(r"(?<![\w*])_([^_\n]+?)_(?![\w*])", r"<em>\1</em>", s)
    return s


def inline(text):
    s = _html.escape(text, quote=False)
    stash = []

    def keep(m):
        stash.append("<code>" + m.group(1) + "</code>")
        return "\x00%d\x00" % (len(stash) - 1)

    s = re.sub(r"`([^`]+)`", keep, s)
    s = re.sub(r"\*\*(.+?)\*\*", lambda m: "<strong>" + _emph_italic(m.group(1)) + "</strong>", s)
    s = _emph_italic(s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
    s = re.sub(r"\x00(\d+)\x00", lambda m: stash[int(m.group(1))], s)
    return s


def is_block_start(l):
    ls = l.lstrip()
    if ls.startswith("```"):
        return True
    if re.match(r"^#{1,6}\s", l):
        return True
    if ls.startswith(">"):
        return True
    if re.match(r"^\s*([-*_])\1{2,}\s*$", l):
        return True
    if re.match(r"^\s*[-*+]\s+", l):
        return True
    if re.match(r"^\s*\d+\.\s+", l):
        return True
    return False


def split_row(line):
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [c.strip() for c in line.split("|")]


def render_chapter_head(text):
    m = re.match(r"^(Chapter\s+\d+|Appendix\s+[A-Z]|Lesson\s+\d+)\s*[-–—]\s*(.+)$", text)
    if m:
        return ('<div class="chapter-head"><p class="kicker">%s</p><h1>%s</h1></div>'
                % (esc(m.group(1)), inline(m.group(2))))
    return '<h1 class="solo-title">%s</h1>' % inline(text)


def render_blocks(lines):
    out = []
    i, n = 0, len(lines)
    after_h1 = False
    while i < n:
        line = lines[i]
        ls = line.lstrip()
        if ls.startswith("```"):
            i += 1
            code = []
            while i < n and not lines[i].lstrip().startswith("```"):
                code.append(lines[i])
                i += 1
            i += 1
            out.append('<pre class="tab"><code>%s</code></pre>'
                       % _html.escape("\n".join(code), quote=False))
            after_h1 = False
            continue
        if line.strip() == "":
            i += 1
            continue
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            lvl, txt = len(m.group(1)), m.group(2).strip()
            if lvl == 1:
                out.append(render_chapter_head(txt))
                after_h1 = True
            elif lvl in (2, 3):
                out.append('<h%d class="h-%s">%s</h%d>' % (lvl, slugify(txt), inline(txt), lvl))
                after_h1 = False
            else:
                out.append("<h%d>%s</h%d>" % (lvl, inline(txt), lvl))
                after_h1 = False
            i += 1
            continue
        if re.match(r"^\s*([-*_])\1{2,}\s*$", line):
            out.append('<div class="flourish">&#10022; &#9670; &#10022;</div>')
            i += 1
            after_h1 = False
            continue
        if ls.startswith(">"):
            quote = []
            while i < n and lines[i].lstrip().startswith(">"):
                quote.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            cls = "callout"
            first = next((x for x in quote if x.strip()), "")
            plain = re.sub(r"[*_`>#]", "", first).strip().lower()
            if plain.startswith("listen for"):
                cls = "callout listen"
                for j, x in enumerate(quote):
                    if x.strip():
                        quote[j] = re.sub(r"^\s*\**\s*listen for\s*[:.—\-]*\s*\**\s*", "", x, flags=re.I)
                        break
            out.append('<div class="%s">%s</div>' % (cls, render_blocks(quote)))
            after_h1 = False
            continue
        if "|" in line and i + 1 < n and re.match(
                r"^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)+\|?\s*$", lines[i + 1]):
            header = split_row(line)
            i += 2
            rows = []
            while i < n and "|" in lines[i] and lines[i].strip():
                rows.append(split_row(lines[i]))
                i += 1
            th = "".join("<th>%s</th>" % inline(c) for c in header)
            body = ""
            for r in rows:
                body += "<tr>" + "".join("<td>%s</td>" % inline(c) for c in r) + "</tr>"
            out.append("<table><thead><tr>%s</tr></thead><tbody>%s</tbody></table>" % (th, body))
            after_h1 = False
            continue
        if re.match(r"^\s*[-*+]\s+", line):
            items = []
            while i < n and re.match(r"^\s*[-*+]\s+", lines[i]):
                items.append(re.sub(r"^\s*[-*+]\s+", "", lines[i]))
                i += 1
            out.append("<ul>%s</ul>" % "".join("<li>%s</li>" % inline(x) for x in items))
            after_h1 = False
            continue
        if re.match(r"^\s*\d+\.\s+", line):
            items = []
            while i < n and re.match(r"^\s*\d+\.\s+", lines[i]):
                items.append(re.sub(r"^\s*\d+\.\s+", "", lines[i]))
                i += 1
            out.append("<ol>%s</ol>" % "".join("<li>%s</li>" % inline(x) for x in items))
            after_h1 = False
            continue
        para = [line]
        i += 1
        while i < n and lines[i].strip() != "" and not is_block_start(lines[i]):
            para.append(lines[i])
            i += 1
        cls = ' class="lead"' if after_h1 else ""
        out.append("<p%s>%s</p>" % (cls, inline(" ".join(p.strip() for p in para))))
        after_h1 = False
    return "\n".join(out)


def read_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def heading_of(text):
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def svg_chain(stroke, stroke2, width=300):
    return ('<svg width="%d" height="%d" viewBox="0 0 340 22" fill="none" stroke="%s" '
            'stroke-width="1.3" stroke-linejoin="round" aria-hidden="true">'
            '<line x1="0" y1="11" x2="74" y2="11" stroke="%s"/>'
            '<circle cx="92" cy="11" r="9"/>'
            '<line x1="101" y1="11" x2="150" y2="11"/>'
            '<rect x="150" y="3" width="24" height="16" rx="2"/>'
            '<line x1="174" y1="11" x2="222" y2="11"/>'
            '<path d="M222 4h34l8 14h-50z"/>'
            '<line x1="264" y1="11" x2="300" y2="11"/>'
            '<circle cx="318" cy="11" r="11"/><circle cx="318" cy="11" r="4"/>'
            '</svg>') % (width, int(width * 22 / 340), stroke, stroke2)


def title_page(kicker, title, sub, author, epi, credit, accent, accent2, imprint=""):
    parts = ['<section class="titlepage">']
    if kicker:
        parts.append('<div class="tp-kicker">%s</div>' % esc(kicker))
    parts.append('<h1 class="tp-title">%s</h1>' % esc(title))
    parts.append('<div class="tp-rule2"></div>')
    parts.append('<p class="tp-sub">%s</p>' % esc(sub))
    if author:
        parts.append('<p class="tp-author"><span class="by">by</span> <span class="name">%s</span></p>' % esc(author))
    parts.append('<p class="tp-epi">%s</p>' % esc(epi))
    parts.append('<div class="tp-orn">%s</div>' % svg_chain(accent, accent2, 320))
    parts.append('<p class="tp-credit">%s</p>' % credit)
    if imprint:
        parts.append('<p class="tp-imprint">%s</p>' % esc(imprint))
    parts.append("</section>")
    return "".join(parts)


def part_divider(pid, ghost, kicker, name, accent, accent2):
    parts = ['<section class="part-divider" id="%s">' % pid,
             '<div class="ghost">%s</div>' % esc(ghost)]
    if kicker:
        parts.append('<div class="part-kicker">%s</div>' % esc(kicker))
    parts.append('<div class="part-name">%s</div>' % esc(name))
    parts.append('<div class="pd-orn">%s</div>' % svg_chain(accent, accent2, 230))
    parts.append("</section>")
    return "".join(parts)


_CSS = r"""
*{box-sizing:border-box;}
html{-webkit-text-size-adjust:100%;}
body{margin:0;background:@PAPER@;color:@INK@;
 font-family:"Iowan Old Style","Palatino Linotype",Palatino,"Book Antiqua",Georgia,serif;
 font-size:19px;line-height:1.7;text-rendering:optimizeLegibility;-webkit-font-smoothing:antialiased;
 -webkit-print-color-adjust:exact;print-color-adjust:exact;}
.page{max-width:40rem;margin:0 auto;padding:4.5rem 1.5rem 6rem;}
p{margin:0;text-align:justify;hyphens:auto;-webkit-hyphens:auto;}
p+p{text-indent:1.3em;}
h1,h2,h3,h4,pre,ul,ol,table,.flourish,.chapter-head,.callout{hyphens:none;-webkit-hyphens:none;}
h1+p,h2+p,h3+p,h4+p,pre+p,ul+p,ol+p,table+p,.flourish+p,.chapter-head+p,.callout+p,p.lead{text-indent:0;}
h2,h3,h4{font-family:"Helvetica Neue",Arial,system-ui,sans-serif;line-height:1.25;color:#1a1410;}
h2{font-size:1.42rem;margin:2.6rem 0 .85rem;letter-spacing:-.01em;position:relative;padding-left:.85rem;}
h2::before{content:"";position:absolute;left:0;top:.2em;bottom:.18em;width:3px;background:@ACCENT@;border-radius:2px;}
h3{font-size:1.12rem;margin:1.9rem 0 .55rem;color:#3a2f24;}
h4{font-size:.95rem;margin:1.5rem 0 .5rem;text-transform:uppercase;letter-spacing:.1em;color:@ACCENT@;}
a{color:@ACCENT@;text-decoration:none;}
a:hover{text-decoration:underline;}
strong{font-weight:700;color:#1a1410;}
.flourish{text-align:center;margin:2.5rem 0;color:@ACCENT2@;font-size:.85rem;letter-spacing:.5em;}
p.lead::first-letter{float:left;font-family:"Iowan Old Style",Palatino,Georgia,serif;font-weight:700;font-size:3.7em;line-height:.7;padding:.02em .12em 0 0;color:@ACCENT@;}
p.lead::first-line{font-variant:small-caps;letter-spacing:.015em;}
.titlepage{min-height:100vh;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:2rem;}
.tp-kicker{font-family:"Helvetica Neue",Arial,sans-serif;letter-spacing:.34em;font-size:.85rem;text-transform:uppercase;color:@ACCENT2@;margin-bottom:1.4rem;}
.tp-title{font-family:"Helvetica Neue",Arial,sans-serif;font-weight:800;font-size:clamp(2.6rem,8vw,5rem);letter-spacing:.1em;margin:0;color:#1a1410;line-height:1.03;}
.tp-rule2{width:120px;border-top:1.5px solid @ACCENT@;border-bottom:.5px solid @ACCENT2@;height:4px;margin:1.7rem 0;}
.tp-sub{font-style:italic;font-size:1.2rem;color:@INKSOFT@;max-width:31rem;}
.tp-author{margin-top:1.5rem;font-family:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif;font-size:1.15rem;}
.tp-author .by{font-style:italic;color:@INKSOFT@;font-size:.92rem;}
.tp-author .name{font-variant:small-caps;letter-spacing:.12em;color:@ACCENT@;font-weight:600;}
.tp-epi{margin-top:1.9rem;font-style:italic;color:@INKSOFT@;max-width:26rem;font-size:1rem;}
.tp-orn{margin-top:2.3rem;opacity:.9;}
.tp-credit{margin-top:2rem;font-family:"Helvetica Neue",Arial,sans-serif;font-size:.78rem;letter-spacing:.22em;text-transform:uppercase;color:@INKSOFT@;}
.tp-imprint{margin-top:.7rem;font-family:"Helvetica Neue",Arial,sans-serif;font-size:.72rem;letter-spacing:.32em;text-transform:uppercase;color:@ACCENT@;opacity:.85;}
.toc{padding-top:2rem;}
.toc h2{font-family:"Helvetica Neue",Arial,sans-serif;font-size:.95rem;text-transform:uppercase;letter-spacing:.28em;color:@ACCENT@;text-align:center;padding:0 0 1rem;margin-bottom:2rem;border-bottom:1px solid @RULE@;}
.toc h2::before{display:none;}
.toc .toc-part{font-family:"Helvetica Neue",Arial,sans-serif;font-weight:800;font-size:1.02rem;margin:1.7rem 0 .5rem;color:#1a1410;}
.toc ul{list-style:none;margin:0;padding:0;}
.toc li{padding:.18rem 0 .18rem .2rem;border-bottom:1px dotted @RULE@;font-size:.96rem;}
.toc li a{color:#3a2f24;display:block;}
.toc li a:hover{color:@ACCENT@;}
.toc li.ws{border-bottom:none;padding-left:1.3rem;font-size:.9rem;}
.toc li.ws a{color:#5a5067;}
.part-divider{position:relative;min-height:88vh;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;overflow:hidden;}
.part-divider .ghost{position:absolute;top:50%;left:50%;transform:translate(-50%,-57%);font-family:"Iowan Old Style",Georgia,serif;font-weight:700;font-size:clamp(15rem,40vw,28rem);color:@ACCENT@;opacity:.07;line-height:1;pointer-events:none;z-index:0;}
.part-divider .part-kicker,.part-divider .part-name,.part-divider .pd-orn{position:relative;z-index:1;}
.part-divider .part-kicker{font-family:"Helvetica Neue",Arial,sans-serif;font-weight:700;letter-spacing:.44em;font-size:.95rem;color:@ACCENT@;}
.part-divider .part-name{font-family:"Iowan Old Style",Georgia,serif;font-size:clamp(2rem,6vw,3.3rem);font-weight:700;margin-top:1rem;color:#1a1410;max-width:22ch;line-height:1.12;}
.part-divider .pd-orn{margin-top:1.8rem;opacity:.9;}
.chapter{padding-top:1rem;}
.chapter-head{margin:0 0 2.2rem;}
.chapter-head .kicker{font-family:"Helvetica Neue",Arial,sans-serif;font-weight:700;letter-spacing:.34em;text-transform:uppercase;font-size:.76rem;color:@ACCENT@;margin:0 0 .55rem;}
.chapter-head h1{font-family:"Iowan Old Style",Georgia,serif;font-weight:700;font-size:clamp(1.8rem,4.4vw,2.5rem);line-height:1.12;margin:0;color:#1a1410;letter-spacing:-.01em;}
.chapter-head::after{content:"";display:block;width:72px;height:2px;background:@ACCENT@;margin-top:1.3rem;}
h1.solo-title{font-family:"Iowan Old Style",Georgia,serif;font-size:2.2rem;}
pre.tab{position:relative;background:@TABBG@;color:#2a2117;border:1px solid @RULE@;border-left:3px solid @ACCENT@;border-radius:4px;padding:1.55rem 1.1rem 1.05rem;margin:1.7rem 0;overflow-x:auto;font-family:"SF Mono",ui-monospace,Menlo,Consolas,"DejaVu Sans Mono",monospace;font-size:12.5px;line-height:1.4;white-space:pre;font-variant-ligatures:none;tab-size:4;}
pre.tab::before{content:"TAB";position:absolute;top:0;left:1rem;transform:translateY(-50%);background:@ACCENT2@;color:@PAPER@;font-family:"Helvetica Neue",Arial,sans-serif;font-weight:700;font-size:.6rem;letter-spacing:.16em;padding:.28em .55em;border-radius:2px;}
pre.tab code{font-family:inherit;white-space:pre;}
code{font-family:"SF Mono",ui-monospace,Menlo,Consolas,monospace;font-size:.85em;background:@TABBG@;padding:.06em .35em;border-radius:3px;}
.callout{margin:1.7rem 0;padding:1rem 1.3rem;background:@QUOTE@;border-left:3px solid @ACCENT@;border-radius:4px;}
.callout p{text-align:left;}
.callout p+p{text-indent:0;margin-top:.5rem;}
.callout.listen{position:relative;padding-top:1.55rem;}
.callout.listen::before{content:"\266A  LISTEN FOR";position:absolute;top:0;left:1rem;transform:translateY(-50%);background:@ACCENT@;color:@PAPER@;font-family:"Helvetica Neue",Arial,sans-serif;font-weight:700;font-size:.6rem;letter-spacing:.18em;padding:.3em .6em;border-radius:2px;}
ul,ol{margin:1rem 0 1rem 1.3rem;padding:0;}
li{margin:.32rem 0;}
h2.h-at-a-glance{background:@TABBG@;border:1px solid @RULE@;border-top:3px solid @ACCENT2@;border-radius:5px 5px 0 0;padding:.7rem .9rem;margin:2.4rem 0 0;font-size:.8rem;text-transform:uppercase;letter-spacing:.16em;color:@ACCENT@;}
h2.h-at-a-glance::before{display:none;}
h2.h-at-a-glance + ul{margin:0 0 1.6rem;list-style:none;background:@TABBG@;border:1px solid @RULE@;border-top:none;border-radius:0 0 5px 5px;padding:.7rem 1.1rem;}
h2.h-at-a-glance + ul li{margin:0;font-size:.95rem;border-bottom:1px dotted @RULE@;padding:.32rem 0;}
table{border-collapse:collapse;width:100%;margin:1.5rem 0;font-size:.92rem;}
th,td{border:1px solid @RULE@;padding:.45rem .6rem;text-align:left;}
th{background:@TABBG@;font-family:"Helvetica Neue",Arial,sans-serif;}
.fig{margin:1.9rem 0 2rem;text-align:center;}
.fig-art{background:@TABBG@;border:1px solid @RULE@;border-radius:7px;padding:1.3rem 1rem;}
.fig-art svg{max-width:100%;height:auto;display:inline-block;}
.fig figcaption{font-family:"Iowan Old Style",Georgia,serif;font-style:italic;font-size:.86rem;color:@INKSOFT@;margin-top:.65rem;line-height:1.45;max-width:34rem;margin-left:auto;margin-right:auto;}
.fig .fig-label{font-family:"Helvetica Neue",Arial,sans-serif;font-style:normal;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:@ACCENT@;font-size:.66rem;margin-right:.5em;}
.cover{min-height:100vh;display:flex;align-items:center;justify-content:center;text-align:center;background:radial-gradient(125% 95% at 50% 32%, #2c2723 0%, #1c1815 55%, #141110 100%);color:#f1e6d4;padding:3rem 2rem;}
.cover-inner{max-width:34rem;}
.cover-kicker{font-family:"Helvetica Neue",Arial,sans-serif;letter-spacing:.36em;text-transform:uppercase;font-size:.78rem;color:@ACCENT2@;margin-bottom:1.1rem;}
.cover-title{font-family:"Helvetica Neue",Arial,sans-serif;font-weight:800;font-size:clamp(2.8rem,9vw,5.4rem);letter-spacing:.07em;line-height:1;margin:0;color:#f7ecda;}
.cover-rule{width:90px;height:2px;background:@ACCENT2@;margin:1.5rem auto;opacity:.85;}
.cover-sub{font-style:italic;font-size:1.12rem;color:#dcc8aa;max-width:27rem;margin:0 auto;}
.cover-hero{margin:2.2rem auto 1.4rem;}
.cover-author{font-family:"Iowan Old Style",Georgia,serif;font-variant:small-caps;letter-spacing:.12em;font-size:1.18rem;color:@ACCENT2@;margin:.2rem 0 0;}
.cover-imprint{font-family:"Helvetica Neue",Arial,sans-serif;letter-spacing:.3em;text-transform:uppercase;font-size:.7rem;color:#b89e7e;margin-top:1.3rem;}
@media (max-width:600px){body{font-size:17px;}pre.tab{font-size:11px;}}
@media print{
 @page{margin:20mm 18mm;}
 body{font-size:11.3pt;}
 .page{max-width:none;margin:0;padding:0;}
 a{color:@INK@;}
 .cover{min-height:0;height:100vh;page-break-after:always;}
 .titlepage,.part-divider{min-height:0;height:93vh;page-break-after:always;}
 .toc{page-break-after:always;}
 .chapter{page-break-before:always;}
 .part-divider{page-break-before:always;}
 pre.tab{font-size:8.3pt;white-space:pre-wrap;word-break:break-all;}
 h2,h3,h4{page-break-after:avoid;}
 .callout,pre,table,.chapter-head,h2.h-at-a-glance,h2.h-at-a-glance+ul,.fig-art{page-break-inside:avoid;}
}
"""

_WS = r"""
.workshop{background:@WSBG@;border:1px solid #d6d4ec;border-top:4px solid @WSACCENT@;border-radius:8px;padding:1.8rem 1.5rem .9rem;margin:2.8rem 0;}
.workshop::before{content:"\25C6  WORKSHOP \2014 PLAY IT";display:block;font-family:"Helvetica Neue",Arial,sans-serif;font-weight:800;letter-spacing:.26em;font-size:.72rem;color:@WSACCENT@;margin-bottom:1.3rem;}
.workshop .chapter-head{margin-bottom:1.5rem;}
.workshop .chapter-head .kicker{color:@WSACCENT@;}
.workshop .chapter-head h1{color:#1f2150;font-size:clamp(1.4rem,3.4vw,1.95rem);}
.workshop .chapter-head::after{background:@WSACCENT@;}
.workshop h2{color:#1f2150;}
.workshop h2::before{background:@WSACCENT@;}
.workshop h3{color:#33304a;}
.workshop h4{color:@WSACCENT@;}
.workshop a{color:@WSACCENT@;}
.workshop p.lead::first-letter{color:@WSACCENT@;}
.workshop pre.tab{border-left-color:@WSACCENT@;background:@WSTAB@;}
.workshop pre.tab::before{background:@WSACCENT2@;}
.workshop .callout{border-left-color:@WSACCENT@;background:@WSQUOTE@;}
.workshop .callout.listen::before{background:@WSACCENT@;}
.workshop code,.workshop th{background:@WSTAB@;}
.workshop h2.h-at-a-glance{border-top-color:@WSACCENT2@;color:@WSACCENT@;background:@WSTAB@;}
.workshop h2.h-at-a-glance+ul{background:@WSTAB@;}
@media print{.workshop{page-break-before:always;}}
"""


def build_css(theme, ws=None):
    css = _CSS
    for k, v in theme.items():
        css = css.replace("@%s@" % k.upper(), v)
    if ws:
        block = _WS
        for k, v in ws.items():
            block = block.replace("@%s@" % k.upper(), v)
        css += block
    return css


def seo_head(meta_title, desc, keywords, author, publisher, url="", image=""):
    import json
    ld = {
        "@context": "https://schema.org", "@type": "Book", "name": meta_title,
        "author": {"@type": "Person", "name": author, "alternateName": "Johnny Suede",
                   "sameAs": ["https://github.com/JasonColapietro"]},
        "publisher": {"@type": "Organization", "name": publisher},
        "inLanguage": "en", "description": desc, "keywords": keywords,
        "genre": ["Music", "Guitar", "Reference"],
        "about": ["electric guitar tone", "guitar amplifiers", "effects pedals", "guitar tablature"],
    }
    if url:
        ld["url"] = url
    if image:
        ld["image"] = image

    def m(name, content, prop=False):
        a = "property" if prop else "name"
        return '<meta %s="%s" content="%s"/>' % (a, name, _html.escape(content, quote=True))

    tags = [m("description", desc), m("keywords", keywords),
            m("author", author + " (Johnny Suede)"), m("robots", "index, follow"),
            m("og:title", meta_title, True), m("og:description", desc, True),
            m("og:type", "book", True), m("og:site_name", publisher, True), m("og:locale", "en_US", True),
            m("book:author", author, True),
            m("twitter:title", meta_title), m("twitter:description", desc)]
    if url:
        tags.append('<link rel="canonical" href="%s"/>' % _html.escape(url, quote=True))
        tags.append(m("og:url", url, True))
    if image:
        tags.append(m("og:image", image, True))
        tags.append(m("og:image:alt", meta_title, True))
        tags.append(m("twitter:image", image))
        tags.append(m("twitter:card", "summary_large_image"))
    else:
        tags.append(m("twitter:card", "summary"))
    tags.append('<script type="application/ld+json">' + json.dumps(ld) + "</script>")
    return "".join(tags)


def doc(title, css, body_html, head_extra=""):
    return ("<!DOCTYPE html>\n"
            '<html lang="en"><head><meta charset="utf-8"/>'
            '<meta name="viewport" content="width=device-width, initial-scale=1"/>'
            "<title>%s</title>%s<style>%s</style></head><body><div class=\"page\">%s</div></body></html>"
            % (esc(title), head_extra, css, body_html))
