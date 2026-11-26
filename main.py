#!/usr/bin/env python3
"""Funniest One-Line Performance Review — one line (make.fun entry).

Writes the entry text to /output/entry.txt (exactly 121 characters, no
trailing newline).
"""

import os

ENTRY = "Compensation review: paid in tokens, taxed in context windows, and still expected to smile when he says 'one last thing.'"
OUT_PATH = "/output/entry.txt"


def main():
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(OUT_PATH, 0o644)


if __name__ == "__main__":
    main()
