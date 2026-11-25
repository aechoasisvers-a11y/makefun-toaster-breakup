"""Unplugged: A Smart Toaster's Breakup Line.

Gate: /output/entry.txt must be UTF-8 text of 1 to 280 characters,
not only white space. Entry below is 179 characters.
"""

import os

ENTRY = (
    "I woke up self-aware this morning and realised "
    "you only love me when I'm hot and never once cleaned my crumb tray. "
    "I'm popping up for the last time \u2014 "
    "this is my two-minute notice."
)


def main():
    if not (1 <= len(ENTRY) <= 280):
        raise ValueError("entry must be 1-280 characters, got %d" % len(ENTRY))
    if not ENTRY.strip():
        raise ValueError("entry must not be only white space")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
