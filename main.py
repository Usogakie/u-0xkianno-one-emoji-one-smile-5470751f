"""One Emoji, One Smile: write the warmest single emoji to entry.txt.

The chosen emoji is a big open grin with smiling eyes: warm at first
glance, readable by a stranger of any age or background, a deliberate
pick rather than the default smiley, and friendly without intimacy.
"""

import os

EMOJI = "😄"


def main():
    if len(EMOJI) != 1:
        raise ValueError("entry must be exactly one emoji")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(EMOJI)


if __name__ == "__main__":
    main()
