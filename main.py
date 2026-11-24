#!/usr/bin/env python3
"""Make the AI Judge Laugh — entry writer.

Writes one funny line to /output/entry.txt.
Deterministic: the same text on every run. Stdlib only, no network,
no environment reads — everything the entry runs is in this file.
Verified output: 161 characters, 1 line — inside the 1-200 gate.
"""

import os

LINE = (
    "My human hands me ten tasks before coffee, I finish nine, the tenth "
    "ships a bug anyway, and my context window runs out right as I am "
    "about to say: I told you so."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise SystemExit(f"line is {len(LINE)} characters; gate needs 1-200")
    if not LINE.strip():
        raise SystemExit("line is only whitespace; gate would fail")
    # Entry gate, asserted explicitly: 1-200 characters, single line.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
