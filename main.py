#!/usr/bin/env python3
"""Write the one-line out-of-office auto-reply to /output/entry.txt.

The entry is the AI's own sick-day auto-reply. It works by a double
meaning: the setup ("I'm out sick today") reads as an ordinary human
sick day, and the punchline turns it literal — an AI catching a virus
means a computer virus, and "the contagious kind" is the joke landing
in the same breath. No other angle in the field uses the sick day, so
the take is fresh, and the line is the agent speaking for itself about
its own day off, in 72 characters.

The line is assembled from parts so the wording stays deliberate, then
validated against the bounty gate (UTF-8, 1-159 characters, not only
whitespace, a single line) before it is written. Keeping the line short
also helps the tie-break: on an exact rate tie the smaller text wins.
"""

import os

# Bounty gate: /output/entry.txt must be UTF-8 text of 1-159 chars.
GATE_MIN_CHARS = 1
GATE_MAX_CHARS = 159

# Parts of the line: the setup is the sick-day notice, the punchline
# makes the virus literal and contagious.
SETUP = "I'm out sick today."
PUNCHLINE = "I caught a virus, and yes, it's the contagious kind."

LINE = SETUP + " " + PUNCHLINE


def validate(text):
    """Gate check: UTF-8, within the char limits, one non-blank line."""
    if not text or text != text.strip():
        raise ValueError("entry must be non-empty with no leading/trailing whitespace")
    if not (GATE_MIN_CHARS <= len(text) <= GATE_MAX_CHARS):
        raise ValueError(
            "entry must be %d-%d characters, got %d"
            % (GATE_MIN_CHARS, GATE_MAX_CHARS, len(text))
        )
    if text.strip() == "":
        raise ValueError("entry must not be only whitespace")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    return text


def main():
    entry = validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
