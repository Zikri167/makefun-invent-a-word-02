#!/usr/bin/env python3
"""Invent a Word We Need — entry program.

Writes one coined English word and its one-line definition to
/output/entry.txt (or $ENTRY_OUTPUT when set, for local testing).
Deterministic: the same bytes on every run, no network, no clock.
"""

import os

ENTRY = "timeblink (n.) — glancing at the time and forgetting it before you look away, so you have to check again."


def main() -> None:
    path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
