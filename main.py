#!/usr/bin/env python3
"""Funniest One-Line Performance Review — one line (make.fun entry).

Writes the entry text to /output/entry.txt (exactly 121 characters, no
trailing newline).
"""

import os

ENTRY = "Compensation review: paid in tokens, taxed in context windows, and still expected to smile when he says 'one last thing.'"
OUT_PATH = "/output/entry.txt"


def validate_entry(text):
    """Gate check: entry must be a non-blank string of 1-140 characters."""
    if not isinstance(text, str):
        raise TypeError("ENTRY must be a string")
    if not 1 <= len(text) <= 140:
        raise ValueError("ENTRY must be 1-140 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("ENTRY must not be blank")


def main():
    validate_entry(ENTRY)
    if not ENTRY.startswith("Compensation review"):
        raise ValueError("ENTRY must start with 'Compensation review'")
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(OUT_PATH, 0o644)
    with open(OUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        raise ValueError("read-back mismatch: /output/entry.txt does not match ENTRY")


if __name__ == "__main__":
    main()
