#!/usr/bin/env python3
"""Funniest Autocorrect Fail — make.fun bounty.

Writes one line (under 200 characters) to /output/entry.txt: a work
message as sent, with the autocorrect slip left in place. No explanation,
no commentary — the slip speaks for itself.

Stdlib only. Deterministic: the same line every run.
"""

import os

ENTRY = (
    "Hi team, just a reminder that our anal staff meeting is tomorrow "
    "at 9am. Attendance is mandatory, see you there!"
)


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 199, f"entry must be 1-199 chars, got {len(text)}"
    assert text == text.strip(), "entry must not be only whitespace"
    assert text.isascii(), "entry must be plain ASCII"
    assert "\n" not in text, "entry must be a single line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
