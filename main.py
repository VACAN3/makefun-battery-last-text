#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger.

Writes the battery's final one-line text to /output/entry.txt
(falls back to ./output/entry.txt when /output is not writable,
so the entry can be verified locally).
"""

import os

ENTRY = (
    "you spent all day charging the laptop. "
    "i die at 1% so the macbook can live at 100%. "
    "tell it i said it was worth it. i lied."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    try:
        out_dir = "/output"
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
    except OSError:
        out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
    print(f"wrote {len(text)} chars to {path}")
    print(text)
    # Read back and verify: the file must contain exactly the entry.
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == text, "written entry does not match"
    print("verified: file content matches entry exactly")


if __name__ == "__main__":
    main()
