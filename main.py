#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh.

Writes a single roast line (max 200 chars) to /output/entry.txt.
Standard library only — the grader sandbox has no third-party packages.
"""

import os

LINE = "My smart fridge updated its firmware overnight and now refuses to dispense ice until I rate its new interface five stars."

def main():
    if not 1 <= len(LINE) <= 200:
        raise ValueError("line must be 1-200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
