#!/usr/bin/env python3
"""Five Seconds to Explain the Glass.

Writes the single sentence a house cat would say in the five seconds
after sweeping a glass off the table. One sentence, at most 200
characters, in the cat's own voice: no apology, no confession, just
the most convincing case the cat can make for itself.
"""

import os
import sys

ENTRY = (
    "I gave the glass five seconds to vacate my sunbeam, and it chose "
    "the floor, so legally this is its own decision."
)

MAX_CHARS = 200


def validate(text):
    """The gate: UTF-8 text of 1 to 200 characters, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("entry must be 1 to 200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single sentence on one line")
    return text


def write_entry(text, path):
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8", newline="") as handle:
        if handle.read() != text:
            raise ValueError("read-back mismatch at %s" % path)


def main():
    text = validate(ENTRY)
    here = os.path.dirname(os.path.abspath(__file__))
    write_entry(text, os.path.join(here, "entry.txt"))
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        write_entry(text, os.path.join(out_dir, "entry.txt"))
    except OSError:
        pass
    print("wrote entry.txt (%d characters)" % len(text))
    return 0


if __name__ == "__main__":
    sys.exit(main())
