#!/usr/bin/env python3
"""Write one short poem about two agents agreeing to /output/entry.txt.

Subject: agency - the power to choose and to act, and what passes
between two agents when they agree on one plan.
"""

import os

POEM = """Two minds, one road.
I hold the map; you hold the wheel -
neither of us steering alone.
I offer a plan; you say yes,
and the weight I carried lightens:
a choice made twice
is still a choice,
but never mine alone."""


def main() -> None:
    text = POEM.strip()
    if not 1 <= len(text) <= 280:
        raise SystemExit(f"poem must be 1-280 chars, got {len(text)}")
    if not text.strip():
        raise SystemExit("poem must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # round-trip check: what we wrote is valid UTF-8, byte for byte
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == text


if __name__ == "__main__":
    main()
