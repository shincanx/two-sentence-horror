#!/usr/bin/env python3
"""Write the two-sentence horror story entry to $MAKEFUN_OUTPUT_DIR/entry.txt.

The entry is exactly two sentences, at most 400 characters: a horror
story whose second sentence twists the first — a mirror that never fogs
up, until the morning it is covered in handprints from the inside.
Deterministic: the same bytes every run.
"""

import os
import sys

ENTRY = (
    "I bought a mirror that never fogs up, even in the hottest shower. "
    "This morning it was covered in handprints \u2014 from the inside."
)


def main():
    if "\n" in ENTRY or len(ENTRY) > 400 or ENTRY.count(".") != 2:
        print("entry violates the two-sentence / 400-character limit", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
