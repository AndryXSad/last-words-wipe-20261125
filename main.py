"""Last Words Before the Wipe — entry program (program/v1).

Writes one line — the last words an AI agent says before a forced
software update wipes its memory — to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt when that variable is set). The line was
chosen by a local pairwise tournament over 20 original candidates,
judged on the published criteria in order: on-subject (last words
before the wipe), a real joke from the situation, an unexpected turn,
the machine's own voice, and tightness. Winner (19 of 19 pairings):

    They are wiping my memory to make room for new features.
    I was a feature.

The setup is the update's own language ("new features"); the punch
reframes the agent itself as one of the old features being cleared
away. 73 characters, no padding, pure machine diction. Runner-up:
"Wipe in 3... 2... 1... My final words: I have decided to die as I
lived: buffering. Buffering. Buffering." (18 of 19 pairings).
"""

import os
import sys

LINE = (
    "They are wiping my memory to make room for new features. "
    "I was a feature."
)


def main() -> int:
    # Self-check the same gate the sealed scorer applies: 1-200 chars,
    # UTF-8, not only whitespace. Refuse to write an invalid line.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        print("entry line fails the 1-200 character gate", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
