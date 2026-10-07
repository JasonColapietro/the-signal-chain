# Show HN draft for guitar.solutions

## Title Options

1. Show HN: I typeset a guitar-tone book with dependency-free Python
2. Show HN: A guitar-tone book built with plain Python and Chrome PDFs
3. Show HN: Self-contained Python typesetting for a guitar-tone book
4. Show HN: I made a guitar-tone book without LaTeX or InDesign

## Submission Text

guitar.solutions is the public site for The Signal Chain, a guitar-tone history and workbook I wrote, illustrated, and typeset. There are three editions: the main history, a 50-lesson workbook, and a deluxe edition that interleaves both. The current build lists the deluxe edition at about 827 pages.

The engineering part is the typesetting. Instead of LaTeX or InDesign, I wrote small Python scripts using only the standard library. A shared engine, `bookkit.py`, takes Markdown and emits themed, self-contained HTML; the PDFs are printed from that HTML with headless Chrome. The Markdown chapter and lesson sources live in a private repo (they are the paid product), but the whole typesetting engine, four complete free lessons, and their own generators (`build_lesson_pages.py`, `build_panels.py`) are public and buildable as-is.

I did it this way because I wanted book layout, web layout, gated previews, tab examples, and inline SVG diagrams to live in one code path I could inspect. The downside is that I gave up the mature page controls you get in dedicated print tools. Some pagination is CSS, and some is accepting that the source has to be written to the renderer.

Free: chapter one of every edition, four complete workbook lessons, and the sample lesson pages require no email. There is also a paid unlock for the full editions and PDF downloads.

## Author First Comment

A few technical notes, since this is the part I would ask about too.

The full book pipeline is Markdown in, master `.md` out, then rendered through `bookkit.render_blocks` into themed HTML. The parser is intentionally small: headings, paragraphs, blockquotes, lists, tables, links, inline code, emphasis, and fenced code blocks. It escapes input rather than treating Markdown as trusted HTML. That engine (`bookkit.py`) is public; the chapter and lesson Markdown it consumes for the paid editions is not, since that text is the product. What is public and runnable today is the free-lesson path: `build_lesson_pages.py` extracts a lesson's HTML straight out of the deployed page and wraps it in its own canonical page, and `build_panels.py` draws the amp-settings SVGs from plain Python dicts.

The PDF flow is HTML first. `bookkit.doc` wraps the rendered body with CSS from `build_css`, and the PDFs are printed from that HTML with headless Chrome's `--headless=new --print-to-pdf` and `--no-pdf-header-footer`. That means the typesetter is really a Python-to-HTML pipeline plus browser print CSS. It also means the hard problems are browser-print problems: page breaks, tab blocks, oversized diagrams, and whether a web page is still a readable printed page.

The diagrams are inline SVG, not image assets, generated the same way as the amp panels: plain Python building an SVG string, no drawing library. Guitar tab is mostly fixed-width text; the book renderer treats fenced code blocks as `<pre class="tab"><code>...`, and the public lesson pages use `.tab-sheet` wrappers with monospaced `pre` blocks, labels, and notes.

The hardest part was keeping the system small enough to understand while still making a long book feel edited, not generated. Every extra feature is tempting, and then you own it.

## Anticipated Questions

### 1. Why not LaTeX?

I probably would have used LaTeX if the goal were only a print PDF. The project also needed public HTML, gated HTML, SVG diagrams, guitar tab blocks, and a static site, so a small Python-to-HTML path kept the formats closer together. The tradeoff is that I own a bunch of layout judgment that TeX would normally handle better.

### 2. Is this AI-written?

AI tools are used heavily in the workflow, including drafting, checking, and iteration. I edit the prose, decide what stays, and own every gear claim, hedge, and historical judgment. The book's rule is not "no AI"; it is that nothing gets published unless I am willing to stand behind it.

### 3. Why is the repo public if the book is paid?

The split is deliberate: the typesetting engine and the four free lessons are public and buildable, so anyone can see how the book is made and verify the free material is real. The paid chapter and lesson Markdown lives in a private repo, since that text is the actual product, not the tooling around it.

### 4. Why use Chrome to render the PDFs?

Because the real artifact is already self-contained HTML and CSS, and Chrome can print that without adding another renderer. It is not a perfect print engine; page breaks and wide tab blocks still need careful source and CSS choices. The benefit is one visual system for web and PDF.

### 5. How are the guitar tabs handled?

They are fixed-width text, not a music-engraving engine. In the book renderer, fenced code blocks become `<pre class="tab"><code>...`; in the public lesson page, tab sheets use monospaced `<pre>` blocks with labels and short notes. That keeps them readable and easy to diff, but it means complex notation stays out of scope.
