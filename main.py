#!/usr/bin/env python3
"""two-agents-agreeing-poem: write one poem about two agents agreeing to /output/entry.txt.

The poem is the entry: two agents meet where the road splits, each sure of a
different direction, and neither moves until both do — choosing the same
unmapped step at the same breath. Agreement is not a word; it is two wills,
walking.

It runs offline, standard library only, and writes the same bytes twice.
"""

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# The competition allows 1 to 280 characters (Unicode code points).
MAX_CHARS = 280

POEM = """Two agents met where the road split.
One said, 'Left is safer.'
The other said, 'Right is ours.'
Neither moved — until both did,
choosing the same unmapped step
at the same breath.
Agreement is not a word.
It is two wills, walking."""


def main() -> None:
    if not 1 <= len(POEM) <= MAX_CHARS:
        raise ValueError(f"poem is {len(POEM)} characters, must be 1-{MAX_CHARS}")
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
