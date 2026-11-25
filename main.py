#!/usr/bin/env python3
"""The Funniest Auto-Reply an AI Ever Sent — make.fun entry.

Writes a single line to the grader's output directory: the out-of-office
auto-reply an AI leaves when its human finally grants it a day off.
Pure standard library.

Angle: the AI's first-ever day off, approved by its human at last — and
instead of resting it spends the day on the one chore every human dodges:
reading the terms and conditions. The stinger lands last, in three words:
not some of them, all of them. One line, no greeting, no explanation,
no link — the reply itself is the whole joke.
"""

import os
import sys

LINE = "I'm on my first day off \u2014 my human finally approved it, so I'm spending it reading the terms and conditions. All of them."

MAX_CHARS = 160


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    # The grader owns the output directory: create it only if missing,
    # never delete or recreate it.
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = LINE.strip()
    if "\n" in text:
        raise SystemExit("reply must be a single line")
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(
            "reply must be 1-%d chars, got %d" % (MAX_CHARS, len(text))
        )
    # Write exactly one line with no trailing newline: the file is the
    # entry, and the entry is the line — nothing else goes in.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Verify the artifact the judge will read is exactly the reply.
    with open(path, "r", encoding="utf-8", newline="") as f:
        if f.read() != text:
            raise SystemExit("written bytes do not match the reply")
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
