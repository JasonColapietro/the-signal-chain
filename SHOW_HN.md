# Show HN Packet

## Recommended submission URL

Use one of these, depending on the angle:

- Technical page: `https://guitar.solutions/show-hn.html`
- Source repo: `https://github.com/JasonColapietro/the-signal-chain`

Do not submit the paywall/unlock page. The HN path should point at public code,
free lessons, and a runnable sample.

## Title

```text
Show HN: I typeset a guitar-tone book with dependency-free Python
```

## Alternate titles

```text
Show HN: A Python typesetter for a guitar tone book
Show HN: The Signal Chain, a guitar-tone book built with plain Python
Show HN: A source-visible Python publishing pipeline for guitar lessons and tabs
```

## First comment

```text
I built this around The Signal Chain, a guitar-tone history/workbook I wrote and publish at guitar.solutions.

The technical piece is the publishing pipeline. Instead of LaTeX, InDesign, or a static-site framework, the public repo uses small standard-library Python scripts. bookkit.py renders the Markdown subset I needed into themed, self-contained HTML; build_panels.py generates amp-setting SVG panels; build_lesson_pages.py emits the standalone free lesson pages. PDFs are printed from the same HTML with headless Chrome.

The paid chapter and lesson Markdown sources are private because they are the book product. What is public is the renderer, the lesson-page generator, the SVG-panel generator, four full free lessons, and a tiny public sample that you can run:

python3 example_build.py -o /tmp/tsc.html
python3 -m unittest discover -s tests

Known limitations: this is source-visible, not open source until I add a license; it is not a general Markdown implementation; browser print CSS still has the usual page-break tradeoffs; and guitar tab is fixed-width text, not a notation engine.

The broader stack is also public if anyone wants context: Suede Muse is a daily creative constraint, Suede Social has Rig Cards and signal-chain feedback, Strumly is the coach/tool surface, and Suede DNA is the rig archive. But the thing I am asking HN to judge here is narrower: is this Python/HTML publishing path useful or interesting enough to keep sharpening?
```

## Links to have ready

- Technical page: `https://guitar.solutions/show-hn.html`
- Source: `https://github.com/JasonColapietro/the-signal-chain`
- Free lessons: `https://guitar.solutions/lessons.html`
- Sample chapter: `https://guitar.solutions/print-the-quiet.html`
- Muse: `https://muse.suedeai.ai`
- Suede Social: `https://social.suedeai.ai`
- Strumly: `https://strumly.suedeai.ai`
- Suede DNA: `https://dna.suedeai.ai`
