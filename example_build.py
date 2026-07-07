#!/usr/bin/env python3
"""Build one public Markdown sample with the same bookkit engine.

This is intentionally small: it proves the public renderer path without
pretending the private book manuscript is part of this repository.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

import bookkit as bk


THEME = {
    "paper": "#f7f2e8",
    "ink": "#2a2118",
    "inksoft": "#6b5d4c",
    "accent": "#8c2f22",
    "accent2": "#b06a24",
    "rule": "#d9c9a9",
    "tabbg": "#efe6d2",
    "quote": "#efe6d2",
}


def render_markdown(markdown: str, title: str = "The Signal Chain Sample") -> str:
    body = '<section class="chapter" id="show-hn-sample">%s</section>' % (
        bk.render_blocks(markdown.splitlines())
    )
    desc = "A public sample rendered by the dependency-free Python typesetter behind The Signal Chain."
    keywords = "Python typesetting, Markdown to HTML, guitar tab, The Signal Chain, guitar.solutions"
    return bk.doc(
        title,
        bk.build_css(THEME),
        body,
        bk.seo_head(title, desc, keywords, "Jason Colapietro", "Johnny Suede Press"),
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Render one public Markdown sample through bookkit.py."
    )
    parser.add_argument(
        "input",
        nargs="?",
        default="examples/show-hn-sample.md",
        help="Markdown file to render. Defaults to examples/show-hn-sample.md.",
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Write HTML to this file instead of stdout.",
    )
    parser.add_argument(
        "--title",
        default="The Signal Chain Python Typesetter Sample",
        help="HTML title for the rendered document.",
    )
    args = parser.parse_args(argv)

    source = Path(args.input)
    markdown = source.read_text(encoding="utf-8")
    rendered = render_markdown(markdown, args.title)

    if args.output:
        Path(args.output).write_text(rendered, encoding="utf-8")
    else:
        sys.stdout.write(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
