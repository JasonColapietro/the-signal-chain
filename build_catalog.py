#!/usr/bin/env python3
"""Build the guitar.solutions catalog page (catalog.html) — a hub linking to
everything Jason Colapietro / Johnny Suede makes: books, the essay series, the
pedal list, the apps, and the Suede Labs platform.

Reads articles/catalog.json (verified offering data + agent-written copy) and
renders catalog.html in the same cream reading style as the book/essay pages."""

import os
import json
import html as _html
import bookkit as bk

BASE = os.path.dirname(os.path.abspath(__file__))
SITE = "https://guitar.solutions"
OG = SITE + "/og-card.png"
AUTHOR = "Jason Colapietro"
IMPRINT = "Johnny Suede Press"

THEME = {"paper": "#f7f2e8", "ink": "#2a2118", "inksoft": "#6b5d4c", "accent": "#8c2f22",
         "accent2": "#b06a24", "rule": "#d9c9a9", "tabbg": "#efe6d2", "quote": "#efe6d2"}

PERSON = {"@type": "Person", "name": AUTHOR, "alternateName": "Johnny Suede", "url": "https://suedeai.ai"}
ORG = {"@type": "Organization", "name": IMPRINT}


def esc(s):
    return _html.escape(s, quote=False)


def escq(s):
    return _html.escape(s, quote=True)


CATALOG_CSS = r"""
.cat-bar{display:flex;justify-content:space-between;align-items:center;gap:1rem;font-family:"Helvetica Neue",Arial,sans-serif;font-size:.72rem;letter-spacing:.16em;text-transform:uppercase;border-bottom:1px solid #d9c9a9;padding-bottom:.9rem;margin-bottom:2.6rem;}
.cat-bar a{color:#6b5d4c;}
.cat-bar a:hover{color:#8c2f22;text-decoration:none;}
.cat-bar .home{font-weight:700;color:#8c2f22;}
.cat-kicker{font-family:"Helvetica Neue",Arial,sans-serif;font-weight:700;letter-spacing:.26em;text-transform:uppercase;font-size:.72rem;color:#8c2f22;margin:0 0 .85rem;}
.cat-kicker span{color:#b06a24;}
.cat-title{font-family:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif;font-weight:700;font-size:clamp(2.4rem,7vw,3.6rem);line-height:1.05;letter-spacing:-.015em;color:#1a1410;margin:0 0 .85rem;}
.cat-dek{font-style:italic;font-size:1.22rem;line-height:1.5;color:#6b5d4c;margin:0 0 1.1rem;hyphens:none;-webkit-hyphens:none;}
.cat-hr{border:0;border-top:2px solid #8c2f22;width:64px;margin:1.9rem 0 2.2rem;}
.cat-standfirst{font-size:1.18rem;line-height:1.62;color:#3a2f24;margin:0 0 .5rem;text-align:left;hyphens:none;-webkit-hyphens:none;}
.cat-sec{margin:3.2rem 0 0;}
.cat-sec-head{display:flex;align-items:baseline;gap:.8rem;border-top:2px solid #8c2f22;padding-top:1rem;}
.cat-sec-num{font-family:"Helvetica Neue",Arial,sans-serif;font-weight:700;font-size:.8rem;letter-spacing:.16em;color:#b06a24;}
.cat-sec-head h2{font-family:"Helvetica Neue",Arial,sans-serif;font-weight:800;font-size:1.02rem;letter-spacing:.04em;text-transform:uppercase;color:#1a1410;margin:0;padding:0;}
.cat-sec-head h2::before{display:none;}
.cat-sec-intro{color:#6b5d4c;font-size:1rem;line-height:1.55;margin:.7rem 0 0;text-align:left;hyphens:none;-webkit-hyphens:none;}
.cat-list{list-style:none;margin:1.4rem 0 0;padding:0;}
.cat-list li{border-top:1px solid #d9c9a9;padding:1.3rem 0;}
.cat-list li:last-child{border-bottom:1px solid #d9c9a9;}
.cat-item-title{font-family:"Iowan Old Style",Georgia,serif;font-weight:700;font-size:1.38rem;line-height:1.16;margin:0;color:#1a1410;}
.cat-item-title a{color:#1a1410;}
.cat-item-title a:hover{color:#8c2f22;text-decoration:none;}
.cat-item-title .ext{font-family:"Helvetica Neue",Arial,sans-serif;font-size:.7rem;letter-spacing:.04em;color:#9c8e78;vertical-align:.15em;margin-left:.25rem;}
.cat-blurb{color:#3a2f24;margin:.4rem 0 0;font-size:1rem;line-height:1.5;text-align:left;hyphens:none;-webkit-hyphens:none;}
.cat-cta{display:inline-block;margin:.7rem 0 0;font-family:"Helvetica Neue",Arial,sans-serif;font-weight:700;font-size:.85rem;color:#8c2f22;}
.cat-cta:hover{text-decoration:none;color:#b06a24;}
.cat-promo{margin:3rem 0 0;background:#efe6d2;border:1px solid #d9c9a9;border-left:3px solid #b06a24;border-radius:6px;padding:1.3rem 1.4rem;}
.cat-promo .k{font-family:"Helvetica Neue",Arial,sans-serif;font-weight:700;letter-spacing:.2em;text-transform:uppercase;font-size:.66rem;color:#b06a24;margin:0 0 .55rem;}
.cat-promo p{text-align:left;margin:0 0 .85rem;font-size:.99rem;line-height:1.5;color:#3a2f24;}
.cat-promo a.btn{font-family:"Helvetica Neue",Arial,sans-serif;font-weight:700;font-size:.85rem;color:#8c2f22;}
.cat-map{margin:3.6rem 0 0;border-top:2px solid #8c2f22;padding-top:1.4rem;}
.cat-map-h{font-family:"Helvetica Neue",Arial,sans-serif;font-weight:800;font-size:1.02rem;letter-spacing:.04em;text-transform:uppercase;color:#1a1410;margin:0;padding-left:0;}
.cat-map-h::before{display:none;}
.cat-map-intro{color:#6b5d4c;font-size:1rem;line-height:1.55;margin:.7rem 0 0;text-align:left;hyphens:none;-webkit-hyphens:none;}
.cat-map-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(13.5rem,1fr));gap:1.9rem 1.6rem;margin-top:1.9rem;}
.cat-map-col h3{font-family:"Helvetica Neue",Arial,sans-serif;font-weight:700;font-size:.72rem;letter-spacing:.18em;text-transform:uppercase;color:#8c2f22;margin:0 0 .15rem;}
.cat-map-col .note{display:block;font-family:"Helvetica Neue",Arial,sans-serif;font-size:.66rem;letter-spacing:.01em;color:#9c8e78;margin:0 0 .65rem;text-transform:none;line-height:1.35;}
.cat-map-col ul{list-style:none;margin:0;padding:0;}
.cat-map-col li{margin:.1rem 0;}
.cat-map-col li a{font-family:"Iowan Old Style",Georgia,serif;font-size:1.02rem;color:#3a2f24;display:inline-flex;align-items:center;gap:.4rem;}
.cat-map-col li a:hover{color:#8c2f22;text-decoration:none;}
.cat-tag{font-family:"Helvetica Neue",Arial,sans-serif;font-weight:700;font-size:.55rem;letter-spacing:.1em;text-transform:uppercase;padding:.12em .42em;border-radius:3px;border:1px solid currentColor;}
.cat-tag.new{color:#8c2f22;}
.cat-tag.hot{color:#b06a24;}
.cat-tag.soon{color:#9c8e78;}
@media (max-width:600px){.cat-title{font-size:2.2rem;}.cat-map-grid{grid-template-columns:1fr 1fr;}}
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
        '<meta property="og:type" content="website"/>',
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


def is_external(url):
    return url.startswith("http") and "guitar.solutions" not in url


def link_attrs(url):
    return ' target="_blank" rel="noopener"' if is_external(url) else ""


def build():
    data = json.load(open(os.path.join(BASE, "articles", "catalog.json"), encoding="utf-8"))
    m = data["masthead"]
    canonical = SITE + "/catalog.html"

    bar = ('<header class="cat-bar"><a class="home" href="index.html">guitar.solutions</a>'
           '<a href="index.html#editions">The book</a></header>')
    head_blk = (
        '<p class="cat-kicker"><span>●</span> Johnny Suede · The catalog</p>'
        + '<h1 class="cat-title">%s</h1>' % esc(m["title"])
        + '<p class="cat-dek">%s</p>' % esc(m["dek"])
        + '<hr class="cat-hr"/>'
        + '<p class="cat-standfirst">%s</p>' % esc(m["standfirst"]))

    body = [bar, head_blk]
    all_items = []
    for idx, sec in enumerate(data["sections"], 1):
        body.append('<section class="cat-sec"><div class="cat-sec-head">'
                    '<span class="cat-sec-num">%02d</span><h2>%s</h2></div>'
                    % (idx, esc(sec["title"])))
        if sec.get("intro"):
            body.append('<p class="cat-sec-intro">%s</p>' % esc(sec["intro"]))
        body.append('<ul class="cat-list">')
        for it in sec["items"]:
            url = it["url"]
            ext = '<span class="ext">↗</span>' if is_external(url) else ''
            body.append(
                '<li>'
                '<p class="cat-item-title"><a href="%s"%s>%s%s</a></p>'
                '<p class="cat-blurb">%s</p>'
                '<a class="cat-cta" href="%s"%s>%s →</a>'
                '</li>' % (escq(url), link_attrs(url), esc(it["name"]), ext,
                           esc(it["blurb"]), escq(url), link_attrs(url), esc(it["cta"])))
            all_items.append({"@type": "CreativeWork", "name": it["name"], "url": url})
        body.append('</ul></section>')

    mp = data.get("map")
    if mp:
        body.append('<section class="cat-map"><h2 class="cat-map-h">Everything else — the full map</h2>')
        body.append('<p class="cat-map-intro">%s</p>' % esc(mp["intro"]))
        body.append('<div class="cat-map-grid">')
        for g in mp["groups"]:
            body.append('<div class="cat-map-col"><h3>%s</h3>' % esc(g["title"]))
            if g.get("note"):
                body.append('<span class="note">%s</span>' % esc(g["note"]))
            body.append('<ul>')
            for it in g["items"]:
                tag = ('<span class="cat-tag %s">%s</span>' % (it["tag"].lower(), esc(it["tag"]))) if it.get("tag") else ''
                body.append('<li><a href="%s"%s>%s%s</a></li>'
                            % (escq(it["url"]), link_attrs(it["url"]), esc(it["label"]), tag))
            body.append('</ul></div>')
            for it in g["items"]:
                all_items.append({"@type": "WebPage", "name": it["label"], "url": it["url"]})
        body.append('</div></section>')

    body.append('<aside class="cat-promo"><p class="k">Start here</p>'
                '<p>New to the desk? Begin with <b>THE SIGNAL CHAIN</b> — chapter one and three '
                'song lessons are free — or read the <b>Print the Quiet</b> essays.</p>'
                '<a class="btn" href="index.html">The book →</a></aside>')

    jsonld = {
        "@context": "https://schema.org", "@type": "CollectionPage", "name": m["title"],
        "description": m["seo_description"], "url": canonical, "inLanguage": "en",
        "author": PERSON, "publisher": ORG, "image": OG, "hasPart": all_items,
    }
    kw = ("Jason Colapietro, Johnny Suede, The Signal Chain, Print the Quiet, Suede 100, "
          "Strumly, Suede Studio Guitar, guitar books, guitar apps, Suede Labs")
    head = head_html(m["seo_title"], m["seo_description"], kw, canonical, jsonld)
    htmlpage = bk.doc(m["seo_title"] + " | Jason Colapietro (Johnny Suede)",
                      bk.build_css(THEME) + CATALOG_CSS, "\n".join(body), head)
    open(os.path.join(BASE, "catalog.html"), "w", encoding="utf-8").write(htmlpage)
    print("catalog: wrote catalog.html (%d sections, %d items)"
          % (len(data["sections"]), len(all_items)))


if __name__ == "__main__":
    build()
