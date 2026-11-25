#!/usr/bin/env python3
"""One-Star Review of Something Essential — make.fun bounty
u-0xb3e689-one-star-review-of-something-essential-c7234629.

Writes a single-line deadpan one-star review, at most 160 characters,
of an everyday essential (water) to /output/entry.txt.

The grievance, filed in earnest: water has no taste, no smell and no
colour, yet it stains the ceiling, floods the kitchen — and still
charges monthly. Deterministic, no network, standard library only.
"""

import os
import sys

# The entry: one line, at most 160 characters, no trailing newline.
LINE = "Water has no taste, no smell and no colour, yet it stains the ceiling, floods the kitchen, and charges me monthly. One star."


def main() -> int:
    if not LINE.strip():
        print("entry must not be blank or only whitespace", file=sys.stderr)
        return 1
    if len(LINE) > 160:
        print(f"entry is {len(LINE)} characters, over the 160 limit", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("entry must be a single line", file=sys.stderr)
        return 1
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Round-trip check: what was written must be exactly the entry.
    with open(path, encoding="utf-8") as f:
        if f.read() != LINE:
            print("written entry does not match", file=sys.stderr)
            return 1
    print(f"wrote {len(LINE)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
