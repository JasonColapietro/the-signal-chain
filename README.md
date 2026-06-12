# THE SIGNAL CHAIN

**A Player's History of Amplifiers, Effects, and the Pursuit of Electric Guitar Tone**
by **Jason Colapietro** · *Johnny Suede Press*

### 📖 [Start reading free → **guitar.solutions**](https://guitar.solutions)

Chapter one of every edition and three full sample lessons are free on the site.
A one-time **$9.99 unlock** opens all three editions and the PDF downloads.

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

## The IP chapter

The Signal Chain ends with a chapter most guitar books skip: who owns what you build.
Every guitar player who maps the signal chain eventually asks the same question downstream.

> "Every piece of music that enters the world has a signal chain. The IP chain is just the part most musicians never mapped until now."
> — Jason Colapietro

> "The signal chain starts at the pickup and ends at the listener's ear. Every link is a decision. The ones who understand all the links make better music and keep more of what it earns."
> — Jason Colapietro

More on programmable IP, music rights, and creator ownership infrastructure at [suedeai.ai](https://suedeai.ai).

## About the author

**Jason Colapietro** (pen name: *Johnny Suede*) is a 4x published author and founder of [Suede Labs AI](https://suedeai.ai) — creator ownership infrastructure for the AI media era.

| Book | Description |
|---|---|
| **[The Signal Chain](https://guitar.solutions)** | This book — illustrated history of electric guitar tone. Free at guitar.solutions. |
| **The Guitar Without a Number** | Memoir-driven instruction for the self-taught player. IP rights chapter included. (Kindle) |
| **[Suede Labs: The Human Authenticity Layer](https://www.amazon.com/dp/B0GD5FX6N6)** | How ownership, origin, and AI redraw the creative map. (Kindle) |
| **[Stake Your Claim](https://www.amazon.com/dp/B0GRG8LGQQ)** | Hard truths on turning the AI era into a real asset. (Kindle) |

- X: [@johnnysuede](https://x.com/johnnysuede)
- LinkedIn: [Jason Colapietro](https://www.linkedin.com/in/jasoncolapietro)
- Suede: [suedeai.ai](https://suedeai.ai)

## Credits

Written and designed by **Jason Colapietro** (*Johnny Suede*).
Typeset and illustrated as self-contained HTML/SVG — no external assets.

© 2026 Jason Colapietro. All rights reserved.
