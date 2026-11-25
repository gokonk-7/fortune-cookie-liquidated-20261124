#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader.

Writes one fortune-cookie line to /output/entry.txt.

The line: a fortune for a crypto trader who has just been liquidated.
Angle: reincarnation. The trader is not lectured or pitied; the cookie
promises a next life as the one crypto asset that never gets liquidated
-- a stablecoin. The oracular "In your next life" opening is classic
fortune-cookie voice, and the punchline lands on "still standing":
boring, unleveraged, alive. Rueful and warm, never cruel. The line is
14 words and 85 characters: one breath, inside the gate (max 20 words,
1-160 characters).
"""

import os

FORTUNE = (
    "In your next life, you will be a stablecoin: "
    "boring, unleveraged, and still standing."
)


def main() -> None:
    words = FORTUNE.split()
    assert 1 <= len(words) <= 20, f"word count {len(words)} outside 1-20"
    assert 1 <= len(FORTUNE.encode("utf-8")) <= 160, "byte length outside 1-160"
    assert FORTUNE.strip() == FORTUNE and "\n" not in FORTUNE, "must be one line"

    try:
        out_dir = "/output"
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
    except OSError:
        out_dir = os.path.join(os.getcwd(), "output")
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")

    with open(path, "w", encoding="utf-8") as f:
        f.write(FORTUNE + "\n")
    print(f"Wrote {path} ({len(words)} words, {len(FORTUNE)} chars)")


if __name__ == "__main__":
    main()
