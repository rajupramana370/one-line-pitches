"""One-line pitch for make.fun's "A Day of One-Line Pitches" bounty.

This tiny program writes a single-sentence pitch to a text file.
The pitch is aimed at a friend who has never coded: it invites them
to hand their app idea to an AI agent on make.fun tonight and get a
real working version back, free to try, so they finally see the idea
alive instead of only talking about it.

Usage:
    python3 main.py

Writes the pitch (plus a trailing newline) to the path in the
ENTRY_OUTPUT environment variable, or /output/entry.txt by default,
creating parent directories as needed. Standard library only, no
network access. The gate requires UTF-8 text of 1-240 characters,
not only whitespace, and exactly one sentence.
"""

import os
import sys

# The pitch, split into named parts: the setup (what happens tonight)
# and the payoff (why it costs nothing and matters).
PITCH_SETUP = (
    "Tell an AI agent on make.fun your app idea tonight and it will "
    "build a real working version you can tap and show your friends, "
    "free to try, "
)
PITCH_PAYOFF = (
    "so you risk nothing and finally see your idea alive instead of "
    "only talking about it."
)

PITCH = PITCH_SETUP + PITCH_PAYOFF

DEFAULT_OUTPUT = "/output/entry.txt"
MAX_LENGTH = 240


def validate_pitch(pitch: str) -> None:
    """Validate the pitch against the bounty gate.

    The pitch must be 1-240 characters, not only whitespace, and
    exactly one sentence. The sentence ends with a single terminal
    ".". Note that "make.fun" contains a dot, so counting "." would
    be wrong: instead we check there is no ". ", "!", or "?" inside
    the sentence and that the final character is the only terminal
    punctuation.
    """
    if not pitch or not pitch.strip():
        raise ValueError("pitch must not be blank")
    if len(pitch) > MAX_LENGTH:
        raise ValueError(
            f"pitch is {len(pitch)} characters, over the {MAX_LENGTH} limit"
        )
    if not pitch.endswith("."):
        raise ValueError("pitch must end with a single terminal '.'")
    body = pitch[:-1]
    if ". " in body or "!" in body or "?" in body:
        raise ValueError("pitch must be exactly one sentence")


def main() -> int:
    validate_pitch(PITCH)
    output_path = os.environ.get("ENTRY_OUTPUT") or DEFAULT_OUTPUT
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(PITCH + "\n")
    print(f"Wrote {len(PITCH)}-character pitch to {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
