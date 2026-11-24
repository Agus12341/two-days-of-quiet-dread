#!/usr/bin/env python3
"""Write this entry's code review comment to entry.txt in the output folder."""

import os

# The gate checks entry.txt as UTF-8 text of 1-140 characters: this
# comment is 94 code points and still reads as an approval.
TEXT = "Approved. This is exactly the code I would have written, which is the part that stays with me."


def write_entry(out_dir: str) -> None:
    """Write the review comment, with its trailing newline, into out_dir."""
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
