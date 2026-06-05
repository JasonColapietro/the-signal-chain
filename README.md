# THE SIGNAL CHAIN

**A Player's History of Amplifiers, Effects, and the Pursuit of Electric Guitar Tone**
by **Jason Colapietro** · *Johnny Suede Press*

### 📖 [Read the full book free online → **guitar.solutions**](https://guitar.solutions)

![Cover](preview-9-cover.png)

An illustrated, ~480-page history of electric guitar tone — the amplifiers, the effects pedals,
and the players who defined the sound — woven with mid-level music theory, hundreds of properly
formatted tablature examples, and original vector diagrams. It ships in three editions, plus a
50-lesson hands-on companion.

## Editions

| Edition | Pages | Files |
|---|---|---|
| **The Signal Chain** — the history | ~485 | [PDF](THE-SIGNAL-CHAIN.pdf) · [HTML](THE-SIGNAL-CHAIN.html) · [Markdown](THE-SIGNAL-CHAIN.md) |
| **The Tone Workbook** — 50 song-lessons | ~338 | [PDF](THE-SIGNAL-CHAIN-WORKBOOK.pdf) · [HTML](THE-SIGNAL-CHAIN-WORKBOOK.html) · [Markdown](THE-SIGNAL-CHAIN-WORKBOOK.md) |
| **Deluxe Edition** — book + lessons interleaved | ~827 | [PDF](THE-SIGNAL-CHAIN-DELUXE.pdf) · [HTML](THE-SIGNAL-CHAIN-DELUXE.html) · [Markdown](THE-SIGNAL-CHAIN-DELUXE.md) |

## What's inside

- **8 parts, 46 chapters + 4 appendices** — from the Rickenbacker Frying Pan to digital modeling,
  with deep dives on Hendrix, Clapton, Page, Gilmour, Van Halen, SRV, The Edge, and more.
- **50 analytical song-lessons** (the Workbook) — each with the real rig, an accessible tone recipe,
  the theory, short fair-use excerpts, and original tablature drills.
- **12 hand-built inline-SVG diagrams & infographics** — the signal chain, tube-amp anatomy, the EQ
  spectrum, clipping waveforms, the harmonic series, gain staging, a pedalboard, and a century timeline.
- **Hundreds of properly formatted ASCII tablature examples** throughout.

## Build it yourself

Everything is generated from the Markdown sources by self-contained Python (no third-party
dependencies):

```bash
python3 assemble.py                     # The Signal Chain (book)
python3 workbook/assemble_workbook.py   # The Tone Workbook
python3 build_deluxe.py                 # The Deluxe Edition
```

Each writes a master `.md` and a typeset `.html`. To produce the PDFs, print the HTML with
headless Chrome, e.g.:

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless=new --print-to-pdf="THE-SIGNAL-CHAIN.pdf" \
  --no-pdf-header-footer "file://$PWD/THE-SIGNAL-CHAIN.html"
```

## Repository layout

```
chapters/             51 source Markdown files (front matter + 46 chapters + 4 appendices)
workbook/lessons/     50 lesson Markdown files
bookkit.py            shared typesetting engine (Markdown → themed HTML)
art.py                inline-SVG cover art + diagrams/infographics
assemble.py           builds the book
workbook/assemble_workbook.py   builds the workbook
build_deluxe.py       builds the interleaved deluxe edition
```

## Credits

Written and designed by **Jason Colapietro** (*Johnny Suede*).
Typeset and illustrated as self-contained HTML/SVG — no external assets.

© 2026 Jason Colapietro. All rights reserved.
