# Show HN Sample - The Little Amp Check

This is a small public input file for the Python typesetter behind **The Signal Chain**.
It is not the private manuscript. It exists so the renderer can be run from a fresh
clone without depending on paid book sources.

## At a Glance

- Source: `examples/show-hn-sample.md`
- Builder: `example_build.py`
- Engine: `bookkit.py`
- Output: self-contained HTML

## The Working Rule

The book uses plain Markdown for prose, fixed-width blocks for tab, and generated
SVG for diagrams. The renderer keeps that boring on purpose: escape text, format
the handful of blocks the book needs, and leave the final artifact inspectable.

> Listen for: the clean signal before the effects. If the direct sound is wrong,
> more pedals only make the wrong thing louder.

## A Tiny Tab Block

```text
e|----------------0-----|
B|------------1---------|
G|--------0-------------|
D|----2-----------------|
A|3---------------------|
E|----------------------|
```

## What This Sample Does Not Prove

It does not reproduce the paid book build. It proves the public renderer path:
Markdown in, escaped and themed HTML out, with guitar-tab blocks treated as
first-class content instead of screenshots.
