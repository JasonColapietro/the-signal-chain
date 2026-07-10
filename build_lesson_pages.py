#!/usr/bin/env python3
"""Emit standalone pages for the free lessons -> lesson-<slug>.html

Each page is extracted live from lessons.html (single source of truth for the
article content) and wrapped in its own chrome: canonical URL, per-song
metadata, JSON-LD, the shared nav/footer, the same locked-sibling teaser, and
the shared player/counter script. Rerun after any edit to lessons.html.
Self-contained, no third-party dependencies, same as every builder here.
"""
import io
import re

SITE = "https://www.guitar.solutions"

LESSONS = [
    {
        "slug": "purple-haze",
        "song": "Purple Haze",
        "artist": "The Jimi Hendrix Experience",
        "title": "Purple Haze Guitar Lesson — Hendrix Tone, Rig, and Tab | THE SIGNAL CHAIN",
        "desc": "How Purple Haze actually sounds the way it does: the Fuzz Face, the Octavia, the Strat, and a loud Marshall — plus an honest budget recipe, the theory, and original tab drills. A complete free lesson from The Tone Workbook.",
        "keywords": "Purple Haze tone, Purple Haze guitar lesson, Hendrix fuzz face settings, Octavia, Purple Haze tab, Hendrix guitar tone",
    },
    {
        "slug": "comfortably-numb",
        "song": "Comfortably Numb",
        "artist": "Pink Floyd",
        "title": "Comfortably Numb Guitar Lesson — Gilmour Tone, Rig, and Tab | THE SIGNAL CHAIN",
        "desc": "The Comfortably Numb solo tone decoded: Big Muff bloom, long delay, a clean Fender-style platform — plus an honest budget recipe, the theory, and original tab drills. A complete free lesson from The Tone Workbook.",
        "keywords": "Comfortably Numb tone, Comfortably Numb guitar lesson, Gilmour Big Muff settings, Comfortably Numb solo tab, David Gilmour tone",
    },
    {
        "slug": "pride-and-joy",
        "song": "Pride and Joy",
        "artist": "Stevie Ray Vaughan",
        "title": "Pride and Joy Guitar Lesson — SRV Tone, Rig, and Tab | THE SIGNAL CHAIN",
        "desc": "The Pride and Joy shuffle decoded: Tube Screamer into a pushed Fender amp, heavy strings, and the right hand — plus an honest budget recipe, the theory, and original tab drills. A complete free lesson from The Tone Workbook.",
        "keywords": "Pride and Joy tone, Pride and Joy guitar lesson, SRV Tube Screamer settings, Pride and Joy tab, Stevie Ray Vaughan tone",
    },
    {
        "slug": "smells-like-teen-spirit",
        "song": "Smells Like Teen Spirit",
        "artist": "Nirvana",
        "title": "Smells Like Teen Spirit Guitar Lesson — Nirvana Tone, Rig, and Tab | THE SIGNAL CHAIN",
        "desc": "The quiet-loud detonation decoded: a cheap offset, a Boss DS-1, and a clean amp doing the contrast — plus an honest budget recipe, the theory, and original tab drills. A complete free lesson from The Tone Workbook.",
        "keywords": "Smells Like Teen Spirit guitar lesson, Nirvana DS-1 settings, Teen Spirit tab, Kurt Cobain tone, Nirvana guitar tone",
    },
]


def slice_between(t, start, end, from_idx=0):
    s = t.index(start, from_idx)
    e = t.index(end, s) + len(end)
    return t[s:e], s, e


def main():
    t = io.open("lessons.html", encoding="utf-8").read()

    style, _, _ = slice_between(t, "<style>", "</style>")
    navbar, _, _ = slice_between(t, '<a class="skip"', "</header>")
    endcta, _, _ = slice_between(t, '<section class="end-cta">', "</section>")
    footer, _, _ = slice_between(t, "<footer>", "</footer>")
    script = t[t.rindex("<script>"):t.rindex("</script>") + len("</script>")]
    fonts = "\n".join(re.findall(r'<link rel="preconnect"[^>]*/>|<link href="https://fonts[^>]*/>', t))
    icons = "\n".join(re.findall(r'<link rel="icon"[^>]*/>|<link rel="apple-touch-icon"[^>]*/>', t))

    for L in LESSONS:
        art, s, e = slice_between(t, '<article class="lesson" id="%s"' % L["slug"], "</article>")
        teaser, _, _ = slice_between(t, '<div class="wrap">\n<section class="locked-teaser"', "</section>\n</div>", e)
        url = "%s/lesson-%s.html" % (SITE, L["slug"])
        jsonld = (
            '{"@context":"https://schema.org","@type":"Article",'
            '"headline":"%s \\u2014 the tone, the rig, and the lesson",'
            '"author":{"@type":"Person","@id":"https://suedeai.ai/founder#person",'
            '"name":"Jason Colapietro","alternateName":"Johnny Suede","url":"https://suedeai.ai/founder"},'
            '"publisher":{"@type":"Organization","name":"Johnny Suede Press"},'
            '"mainEntityOfPage":"%s",'
            '"about":{"@type":"MusicRecording","name":"%s","byArtist":{"@type":"MusicGroup","name":"%s"}},'
            '"isPartOf":{"@type":"Book","name":"The Signal Chain: The Tone Workbook"}}'
            % (L["song"], url, L["song"], L["artist"])
        )
        page = """<!DOCTYPE html>
<html lang="en" data-gc="">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>%(title)s</title>
<meta name="description" content="%(desc)s"/>
<meta name="author" content="Jason Colapietro (Johnny Suede)"/>
<meta name="keywords" content="%(keywords)s"/>
<meta name="robots" content="index, follow"/>
<link rel="canonical" href="%(url)s"/>
<meta property="og:type" content="article"/>
<meta property="og:site_name" content="Johnny Suede Press"/>
<meta property="og:locale" content="en_US"/>
<meta property="og:title" content="%(song)s — the tone, the rig, and the lesson"/>
<meta property="og:description" content="%(desc)s"/>
<meta property="og:url" content="%(url)s"/>
<meta property="og:image" content="%(site)s/og/og-%(slug)s.png"/>
<meta property="og:image:width" content="1200"/>
<meta property="og:image:height" content="630"/>
<meta property="og:image:alt" content="THE SIGNAL CHAIN — free guitar lesson: %(song)s"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:site" content="@suedeai"/>
<meta name="twitter:creator" content="@johnnysuede"/>
<meta name="twitter:title" content="%(song)s — the tone, the rig, and the lesson"/>
<meta name="twitter:description" content="%(desc)s"/>
<meta name="twitter:image" content="%(site)s/og/og-%(slug)s.png"/>
<meta name="theme-color" content="#120e0b"/>
%(icons)s
%(fonts)s
<script type="application/ld+json">
%(jsonld)s
</script>
%(style)s
</head>
<body>
%(navbar)s
<main id="main">
<div class="wrap" style="padding-top:1.4rem">
  <p class="lesson-permalink"><a href="lessons.html">&larr; All four free lessons</a></p>
</div>
%(article)s

<div class="wrap">
%(teaser)s
</div>

%(endcta)s
</main>
%(footer)s
%(script)s
</body>
</html>
""" % {
            "title": L["title"], "desc": L["desc"], "keywords": L["keywords"],
            "url": url, "song": L["song"], "slug": L["slug"], "site": SITE, "icons": icons,
            "fonts": fonts, "jsonld": jsonld, "style": style, "navbar": navbar,
            "article": art, "teaser": teaser, "endcta": endcta,
            "footer": footer, "script": script,
        }
        # the page's own permalink line would self-link; keep it but point home
        page = page.replace(
            '<p class="lesson-permalink"><a href="lesson-%s.html">This lesson has its own page — link it, share it →</a></p>' % L["slug"],
            '<p class="lesson-permalink"><a href="%s">%s</a> is this page&#8217;s permanent address — link it, share it.</p>' % ("lesson-%s.html" % L["slug"], url.replace("https://", "")),
        )
        out = "lesson-%s.html" % L["slug"]
        io.open(out, "w", encoding="utf-8").write(page)
        print("wrote", out, len(page), "bytes")


if __name__ == "__main__":
    main()
