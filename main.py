#!/usr/bin/env python3
"""Make the Judge Laugh in One Line.

make.fun bounty: u-email-baru-make-the-judge-laugh-in-one-line-791ccb21

Writes one funny line (max 200 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt.
The grader runs this as `python3 -P -s /bot/main.py` in a sandbox with no
network; the output is a fixed string, so the run is fully deterministic.

Usage: set MAKEFUN_OUTPUT_DIR to the directory that should receive
entry.txt (defaults to /output), then run `python3 -P -s main.py`.
After writing, the entry re-reads entry.txt and asserts it contains exactly
the line plus a trailing newline, so a partial or failed write can
never pass silently.
"""

import os

LINE = (
    "I asked an AI to write my wedding vows and it proposed to the printer "
    "instead — turns out I'm not the only one afraid of commitment."
)

assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} characters"
assert LINE.strip(), "line must not be only whitespace"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    # Read back and verify: the file must contain exactly the line + newline.
    with open(entry_path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE + "\n", (
        f"entry.txt mismatch: expected {len(LINE) + 1} chars, "
        f"got {len(written)} chars"
    )


if __name__ == "__main__":
    main()
