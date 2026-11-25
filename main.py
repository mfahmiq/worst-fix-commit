#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message.

Writes the entry -- a single commit message for a bug fix that made
everything worse -- to /output/entry.txt.

The entry: "fix: crash is gone because the app no longer starts"
The joke: the fix technically worked. The crash is gone. It is gone
because the whole app no longer starts. The repair cured the symptom
by killing the patient.
"""

import os

ENTRY = "fix: crash is gone because the app no longer starts"


def main():
    """Write the entry to /output/entry.txt, byte for byte."""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
