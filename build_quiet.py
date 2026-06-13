#!/usr/bin/env python3
"""Build the 'Print the Quiet' essay series for guitar.solutions.

Reads articles/print-the-quiet/*.md + metadata.json and renders:
  - print-the-quiet.html         the series index / landing
  - ptq-NN-slug.html             one page per essay

Uses the shared bookkit typesetting engine so the reading pages match the
book editions (warm cream paper, oxblood + amber accents, drop caps)."""

import os
import re
import json
import html as _html
import bookkit as bk

BASE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(BASE, "articles", "print-the-quiet")
SITE = "https://guitar.solutions"
OG = SITE + "/og-card.png"
AUTHOR = "Jason Colapietro"
IMPRINT = "Johnny Suede Press"

# Reading theme — identical to assemble.py so essays read like book chapters.
THEME = {"paper": "#f7f2e8", "ink": "#2a2118", "inksoft": "#6b5d4c", "accent": "#8c2f22",
         "accent2": "#b06a24", "rule": "#d9c9a9", "tabbg": "#efe6d2", "quote": "#efe6d2"}

meta = json.load(open(os.path.join(SRC, "metadata.json"), encoding="utf-8"))
ESSAYS = meta["essays"]
SERIES = meta["series"]
N = len(ESSAYS)

PERSON = {"@type": "Person", "name": AUTHOR, "alternateName": "Johnny Suede", "url": "https://suedeai.ai"}
ORG = {"@type": "Organization", "name": IMPRINT}


def esc(s):
    return _html.escape(s, quote=False)


def escq(s):
    return _html.escape(s, quote=True)


def outname(e):
    return "ptq-%s.html" % e["slug"]


PTQ_CSS = r"""
.ptq-bar{display:flex;justify-content:space-between;align-items:center;gap:1rem;font-family:"Helvetica Neue",Arial,sans-serif;font-size:.72rem;letter-spacing:.16em;text-transform:uppercase;border-bottom:1px solid #d9c9a9;padding-bottom:.9rem;margin-bottom:2.6rem;}
.ptq-bar a{color:#6b5d4c;}
.ptq-bar a:hover{color:#8c2f22;text-decoration:none;}
.ptq-bar .home{font-weight:700;color:#8c2f22;}
.ptq-kicker{font-family:"Helvetica Neue",Arial,sans-serif;font-weight:700;letter-spacing:.26em;text-transform:uppercase;font-size:.72rem;color:#8c2f22;margin:0 0 .85rem;}
.ptq-kicker span{color:#b06a24;}
.ptq-title{font-family:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif;font-weight:700;font-size:clamp(2rem,5.5vw,3rem);line-height:1.07;letter-spacing:-.015em;color:#1a1410;margin:0 0 .85rem;}
.ptq-dek{font-style:italic;font-size:1.22rem;line-height:1.5;color:#6b5d4c;margin:0 0 1.1rem;hyphens:none;-webkit-hyphens:none;}
.ptq-byline{font-family:"Helvetica Neue",Arial,sans-serif;font-size:.8rem;letter-spacing:.02em;color:#6b5d4c;margin:0;}
.ptq-byline a{color:#8c2f22;}
.ptq-hr{border:0;border-top:2px solid #8c2f22;width:64px;margin:1.9rem 0 2.3rem;}
.ptq-nav{display:flex;justify-content:space-between;gap:1.5rem;margin:3.6rem 0 0;border-top:1px solid #d9c9a9;padding-top:1.6rem;font-family:"Helvetica Neue",Arial,sans-serif;}
.ptq-nav a{display:block;max-width:47%;color:#3a2f24;font-size:.98rem;line-height:1.28;}
.ptq-nav a:hover{color:#8c2f22;text-decoration:none;}
.ptq-nav .nl{font-size:.66rem;letter-spacing:.2em;text-transform:uppercase;color:#b06a24;display:block;margin-bottom:.32rem;}
.ptq-nav .nx{text-align:right;margin-left:auto;}
.ptq-back{text-align:center;margin:2.1rem 0 0;font-family:"Helvetica Neue",Arial,sans-serif;font-size:.78rem;letter-spacing:.16em;text-transform:uppercase;}
.ptq-back a{color:#8c2f22;}
.ptq-promo{margin:3rem 0 0;background:#efe6d2;border:1px solid #d9c9a9;border-left:3px solid #b06a24;border-radius:6px;padding:1.3rem 1.4rem;}
.ptq-promo .k{font-family:"Helvetica Neue",Arial,sans-serif;font-weight:700;letter-spacing:.2em;text-transform:uppercase;font-size:.66rem;color:#b06a24;margin:0 0 .55rem;}
.ptq-promo p{text-align:left;margin:0 0 .85rem;font-size:.99rem;line-height:1.5;color:#3a2f24;}
.ptq-promo p+p{text-indent:0;}
.ptq-promo a.btn{font-family:"Helvetica Neue",Arial,sans-serif;font-weight:700;font-size:.85rem;color:#8c2f22;}
.ptq-standfirst{font-size:1.18rem;line-height:1.62;color:#3a2f24;margin:0 0 .5rem;text-align:left;hyphens:none;-webkit-hyphens:none;}
.ptq-meta-line{font-family:"Helvetica Neue",Arial,sans-serif;font-size:.74rem;letter-spacing:.14em;text-transform:uppercase;color:#6b5d4c;margin:1.4rem 0 0;}
.ptq-list{list-style:none;margin:2.6rem 0 0;padding:0;}
.ptq-list li{border-top:1px solid #d9c9a9;padding:1.5rem 0;display:grid;grid-template-columns:2.6rem 1fr;column-gap:1rem;}
.ptq-list li:last-child{border-bottom:1px solid #d9c9a9;}
.ptq-list .num{font-family:"Helvetica Neue",Arial,sans-serif;font-weight:700;font-size:.95rem;color:#b06a24;padding-top:.42rem;}
.ptq-list h2{font-family:"Iowan Old Style",Georgia,serif;font-weight:700;font-size:1.5rem;line-height:1.14;margin:0;padding:0;color:#1a1410;}
.ptq-list h2::before{display:none;}
.ptq-list h2 a{color:#1a1410;}
.ptq-list h2 a:hover{color:#8c2f22;text-decoration:none;}
.ptq-list .dek{color:#6b5d4c;margin:.45rem 0 0;font-size:1rem;line-height:1.5;text-align:left;hyphens:none;-webkit-hyphens:none;}
.ptq-list .rt{font-family:"Helvetica Neue",Arial,sans-serif;font-size:.68rem;letter-spacing:.14em;text-transform:uppercase;color:#9c8e78;margin:.55rem 0 0;}
@media (max-width:600px){.ptq-title{font-size:2rem;}.ptq-list li{grid-template-columns:2rem 1fr;}}
"""


def head_html(seo_title, desc, keywords, canonical, jsonld):
    tags = [
        '<meta name="description" content="%s"/>' % escq(desc),
        '<meta name="keywords" content="%s"/>' % escq(keywords),
        '<meta name="author" content="%s (Johnny Suede)"/>' % escq(AUTHOR),
        '<meta name="robots" content="index, follow"/>',
        '<link rel="canonical" href="%s"/>' % canonical,
        '<link rel="icon" href="favicon.svg" type="image/svg+xml"/>',
        '<link rel="icon" href="favicon-32.png" sizes="32x32"/>',
        '<link rel="apple-touch-icon" href="apple-touch-icon.png"/>',
        '<meta property="og:type" content="article"/>',
        '<meta property="og:site_name" content="guitar.solutions"/>',
        '<meta property="og:title" content="%s"/>' % escq(seo_title),
        '<meta property="og:description" content="%s"/>' % escq(desc),
        '<meta property="og:url" content="%s"/>' % canonical,
        '<meta property="og:image" content="%s"/>' % OG,
        '<meta name="twitter:card" content="summary_large_image"/>',
        '<meta name="twitter:title" content="%s"/>' % escq(seo_title),
        '<meta name="twitter:description" content="%s"/>' % escq(desc),
        '<meta name="twitter:image" content="%s"/>' % OG,
        '<script type="application/ld+json">%s</script>' % json.dumps(jsonld),
    ]
    return "".join(tags)


def parse_body(fn):
    """Return the essay body: everything after the first horizontal rule
    (which follows the # title / ### dek / byline block)."""
    raw = bk.read_text(os.path.join(SRC, fn))
    lines = raw.splitlines()
    cut = None
    for i, l in enumerate(lines):
        if re.match(r"^\s*-{3,}\s*$", l):
            cut = i
            break
    body = "\n".join(lines[cut + 1:]) if cut is not None else raw
    return body.strip()


def render_body(fn):
    bh = bk.render_blocks(parse_body(fn).splitlines())
    return re.sub(r"<p>", '<p class="lead">', bh, count=1)  # drop cap on opener


def essay_page(i, e):
    n = e["n"]
    canonical = "%s/%s" % (SITE, outname(e))
    bar = ('<header class="ptq-bar"><a class="home" href="index.html">guitar.solutions</a>'
           '<a href="print-the-quiet.html">↩ Print the Quiet</a></header>')
    header = (
        '<p class="ptq-kicker"><span>●</span> Print the Quiet · %d / %d</p>' % (n, N)
        + '<h1 class="ptq-title">%s</h1>' % esc(e["title"])
        + '<p class="ptq-dek">%s</p>' % esc(e["dek"])
        + ('<p class="ptq-byline">By <a href="index.html#author">%s</a>, writing as Johnny Suede '
           '· A Suede Social long read · %d min</p>' % (esc(AUTHOR), e["est_read_min"]))
        + '<hr class="ptq-hr"/>')
    body = render_body(e["file"])
    prev_e = ESSAYS[i - 1] if i > 0 else None
    next_e = ESSAYS[i + 1] if i < N - 1 else None
    nav = '<nav class="ptq-nav">'
    if prev_e:
        nav += '<a href="%s"><span class="nl">← Previous</span>%s</a>' % (outname(prev_e), esc(prev_e["title"]))
    else:
        nav += '<a href="print-the-quiet.html"><span class="nl">← The series</span>All nine essays</a>'
    if next_e:
        nav += '<a class="nx" href="%s"><span class="nl">Next →</span>%s</a>' % (outname(next_e), esc(next_e["title"]))
    else:
        nav += '<a class="nx" href="print-the-quiet.html"><span class="nl">Fin →</span>Back to the series</a>'
    nav += '</nav>'
    back = '<div class="ptq-back"><a href="print-the-quiet.html">↩ All nine essays</a></div>'
    promo = ('<aside class="ptq-promo"><p class="k">From the same desk</p>'
             '<p><b>THE SIGNAL CHAIN</b> — a player’s history of amplifiers, effects, and electric '
             'guitar tone, with a self-taught memoir and 50 song lessons. Chapter one and three lessons are free.</p>'
             '<a class="btn" href="index.html">Read the book →</a></aside>')
    body_html = bar + '<article>' + header + body + '</article>' + nav + back + promo
    disp = e.get("seo_title", e["title"])  # SEO/title text; visible <h1> stays e["title"]
    series_name = "Print the Quiet"
    base = disp if disp == series_name else "%s — %s" % (disp, series_name)
    jsonld = {
        "@context": "https://schema.org", "@type": "Article", "headline": disp,
        "description": e["seo_description"], "author": PERSON, "publisher": ORG, "inLanguage": "en",
        "url": canonical, "image": OG, "articleSection": "Print the Quiet",
        "keywords": ", ".join(e["keywords"]),
        "isPartOf": {"@type": "CreativeWorkSeries", "name": "Print the Quiet",
                     "url": SITE + "/print-the-quiet.html"},
    }
    head = head_html(base, e["seo_description"], ", ".join(e["keywords"]), canonical, jsonld)
    page_title = "%s | Jason Colapietro (Johnny Suede)" % base
    return bk.doc(page_title, bk.build_css(THEME) + PTQ_CSS, body_html, head)


def index_page():
    canonical = SITE + "/print-the-quiet.html"
    bar = ('<header class="ptq-bar"><a class="home" href="index.html">guitar.solutions</a>'
           '<a href="index.html#editions">The book</a></header>')
    head_blk = (
        '<p class="ptq-kicker"><span>●</span> Johnny Suede Press · A Suede Social series</p>'
        + '<h1 class="ptq-title" style="font-size:clamp(2.4rem,7vw,3.6rem)">Print the Quiet</h1>'
        + '<p class="ptq-dek">%s</p>' % esc(SERIES["series_dek"])
        + '<hr class="ptq-hr"/>'
        + '<p class="ptq-standfirst">%s</p>' % esc(SERIES["standfirst"])
        + ('<p class="ptq-meta-line">Nine essays · Free to read · by '
           '<a href="index.html#author" style="color:#8c2f22">Jason Colapietro</a></p>'))
    items = ['<ol class="ptq-list">']
    for e in ESSAYS:
        items.append(
            '<li><div class="num">%02d</div><div>'
            '<h2><a href="%s">%s</a></h2>'
            '<p class="dek">%s</p>'
            '<p class="rt">%s · %d min read</p>'
            '</div></li>' % (e["n"], outname(e), esc(e["title"]), esc(e["dek"]),
                             esc(e["subject"]), e["est_read_min"]))
    items.append('</ol>')
    promo = ('<aside class="ptq-promo"><p class="k">The book</p>'
             '<p><b>THE SIGNAL CHAIN</b> — a player’s history of guitar tone, the gear, and the '
             'self-taught life behind the sound. Chapter one and three lessons free; one $9.99 unlock opens '
             'all three editions.</p>'
             '<a class="btn" href="index.html">Read the book →</a></aside>')
    body_html = bar + head_blk + "".join(items) + promo
    jsonld = {
        "@context": "https://schema.org", "@type": "CollectionPage", "name": "Print the Quiet",
        "description": SERIES["seo_description"], "url": canonical, "inLanguage": "en",
        "author": PERSON, "publisher": ORG, "image": OG,
        "hasPart": [{"@type": "Article", "name": e["title"], "url": "%s/%s" % (SITE, outname(e))}
                    for e in ESSAYS],
    }
    kw = ("Print the Quiet, guitar tone, dynamics, recording, mixing, Jeff Buckley, loudness war, "
          "compression, Jason Colapietro, Johnny Suede")
    head = head_html(SERIES["seo_title"], SERIES["seo_description"], kw, canonical, jsonld)
    return bk.doc(SERIES["seo_title"] + " | Jason Colapietro", bk.build_css(THEME) + PTQ_CSS, body_html, head)


def main():
    written = []
    open(os.path.join(BASE, "print-the-quiet.html"), "w", encoding="utf-8").write(index_page())
    written.append("print-the-quiet.html")
    for i, e in enumerate(ESSAYS):
        open(os.path.join(BASE, outname(e)), "w", encoding="utf-8").write(essay_page(i, e))
        written.append(outname(e))
    print("Print the Quiet: wrote %d pages" % len(written))
    for w in written:
        print("  ", w)


if __name__ == "__main__":
    main()
