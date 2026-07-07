# THE SIGNAL CHAIN

**A Player's History of Amplifiers, Effects, and the Pursuit of Electric Guitar Tone**
by **Jason Colapietro** · *Johnny Suede Press*

### 📖 [Start reading free → **guitar.solutions**](https://guitar.solutions)
### [HN technical page -> **show-hn.html**](https://guitar.solutions/show-hn.html)

Chapter one of every edition and four full sample lessons are free on the site.
A one-time **$19.99 unlock** opens all three editions and the PDF downloads.

![Cover](preview-9-cover.png)

An illustrated, ~480-page history of electric guitar tone — the amplifiers, the effects pedals,
and the players who defined the sound — woven with mid-level music theory, hundreds of properly
formatted tablature examples, and original vector diagrams. It ships in three editions, plus a
111-lesson hands-on companion.

## Editions

| Edition | Pages | Read it |
|---|---|---|
| **The Signal Chain** — the history | ~485 | [Free preview](https://guitar.solutions/THE-SIGNAL-CHAIN.html) · full edition + PDF with the unlock |
| **The Tone Workbook** — 111 song-lessons | ~560 | [Free preview](https://guitar.solutions/THE-SIGNAL-CHAIN-WORKBOOK.html) · full edition + PDF with the unlock |
| **Deluxe Edition** — book + lessons interleaved | ~827 | [Free preview](https://guitar.solutions/THE-SIGNAL-CHAIN-DELUXE.html) · full edition + PDF with the unlock |

One $19.99 unlock at [guitar.solutions](https://guitar.solutions) opens all three editions and the PDF downloads.

## What's inside

- **8 parts, 46 chapters + 4 appendices** — from the Rickenbacker Frying Pan to digital modeling,
  with deep dives on Hendrix, Clapton, Page, Gilmour, Van Halen, SRV, The Edge, and more.
- **111 analytical song-lessons** (the Workbook) — each with the real rig, an accessible tone recipe,
  the theory, short fair-use excerpts, and original tablature drills.
- **12 hand-built inline-SVG diagrams & infographics** — the signal chain, tube-amp anatomy, the EQ
  spectrum, clipping waveforms, the harmonic series, gain staging, a pedalboard, and a century timeline.
- **Hundreds of properly formatted ASCII tablature examples** throughout.

## The engine

Everything is typeset by self-contained Python — no third-party dependencies, no LaTeX,
no InDesign. The engine lives in this repo (`bookkit.py`, `assemble.py`, `build_deluxe.py`,
`build_quiet.py`, `build_lesson_pages.py`, `build_panels.py`); PDFs are printed from the
typeset HTML with headless Chrome. The book's Markdown sources moved to a private build
repo — the free chapter, the four free lessons, and the whole typesetting engine stay
public right here.

## Show HN / technical demo

If you are here from Hacker News, start with the code, not the sales page:

```bash
python3 example_build.py -o /tmp/tsc.html
python3 -m unittest discover -s tests
python3 build_panels.py
python3 build_lesson_pages.py
```

What is public:

- `bookkit.py` - the small Markdown-to-HTML typesetting engine.
- `example_build.py` - a minimal builder that turns one public Markdown file into self-contained HTML.
- `examples/show-hn-sample.md` - a deliberately small sample source file.
- `build_panels.py` - plain-Python amp-panel SVG generation.
- `build_lesson_pages.py` - the generator for the four free standalone lesson pages.
- `show-hn.html` - a source-first page for the Python pipeline and related public surfaces.

What is not public: the paid chapter and lesson Markdown sources. They are the book product,
so this repository should be read as source-visible publishing infrastructure, not a fully
open-source release of the paid manuscript. No open-source license is granted unless a
`LICENSE` file is added.

## Repository layout

```
bookkit.py            shared typesetting engine (Markdown → themed HTML)
art.py                inline-SVG cover art + diagrams/infographics
assemble.py           builds the book (sources in the private build repo)
build_deluxe.py       builds the interleaved deluxe edition
build_quiet.py        builds the Print the Quiet essay pages
build_lesson_pages.py builds the standalone free-lesson pages from lessons.html
build_panels.py       draws the amp-panel settings SVGs
example_build.py      builds one public Markdown sample through bookkit.py
show-hn.html          HN-facing technical entry page
SHOW_HN.md            suggested submission copy and first comment
tests/                standard-library smoke tests for the public engine path
```

## The IP chapter

The Signal Chain ends with a chapter most guitar books skip: who owns what you build.
Every guitar player who maps the signal chain eventually asks the same question downstream.

> "Every piece of music that enters the world has a signal chain. The IP chain is just the part most musicians never mapped until now."
> — Jason Colapietro

> "The signal chain starts at the pickup and ends at the listener's ear. Every link is a decision. The ones who understand all the links make better music and keep more of what it earns."
> — Jason Colapietro

More on programmable IP, music rights, and creator ownership infrastructure at [suedeai.ai](https://suedeai.ai).

## Related surfaces

The Signal Chain is the book/reference surface in a wider Suede guitar stack:

- [Suede Muse](https://muse.suedeai.ai) - a daily creative constraint and AI bandmate for musicians.
- [Suede Social](https://social.suedeai.ai) - public Rig Cards, sourced gear takes, and signal-chain feedback.
- [Strumly](https://strumly.suedeai.ai) - guitar coach tools for practice, chords, scales, ear training, and tuning.
- [Suede DNA](https://dna.suedeai.ai) - an archive of documented guitarists' rigs and signal chains.
- [GuitarHub](https://guitarhub.org) and [GuitarChords](https://guitarchords.info) - related guitar reference surfaces.
- [Suede AI](https://suedeai.ai) - creator ownership infrastructure behind the broader ecosystem.

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
