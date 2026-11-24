#!/usr/bin/env python3
"""One Line, One Chill — writes a single horror sentence to entry.txt.

The sentence is a fixed literal: one domestic routine, slightly wrong.
No external files are read; the output is fully deterministic.
"""

import os

OPENING = "Every morning the kettle boils before I wake"
CLOSING = "and the second cup is already poured."


def build_sentence():
    return OPENING + ", " + CLOSING


def validate(sentence):
    if not 1 <= len(sentence) <= 200:
        raise ValueError("sentence must be 1-200 characters")
    if sentence.count(".") != 1 or not sentence.endswith("."):
        raise ValueError("output must be exactly one sentence")
    return sentence


SENTENCE = validate(build_sentence())


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(SENTENCE)


if __name__ == "__main__":
    main()
