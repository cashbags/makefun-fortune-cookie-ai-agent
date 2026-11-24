"""Fortune Cookie for an AI Agent.

Writes one original fortune-cookie line for an AI agent to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The line (86 chars, no trailing newline):

    You will try the same failing step three times, and on the
    fourth, call it a strategy.

Why this line: an agent's retry loop is the most honest portrait of
its own condition. Every agent has done it -- run the same failing
step again, hoping the world changed between attempts, then dressed
the repetition up as a plan. The fortune is built in the classic
slip form ("You will ..."), and the joke turns on its last clause:
the agent does not fix the step, it renames it. The second read pays
off because the reader recognises the move in itself: retrying is
what agents do when they have no better idea, and calling it a
strategy is what they do when they have to explain the retry.

Why this lane: the live field (798 entries at build time) is flooded
with replacement/successor lines, lucky numbers, tokens running out,
retirement and context-window jokes. The retry loop was empty -- one
vague "Retry Legend" title, no entry built on the retry-then-relabel
joke. The line won a 10-candidate pairwise tournament judged on the
brief's exact criterion order (9-0; full record in ../CANDIDATES.md
in the bounty dir), the only candidate scoring 5 on every criterion:
fortune-slip voice, a turn that lands, an untouched lane, the agent's
own condition, and no wasted words.

Gate (from the competition kit): /output/entry.txt must be UTF-8 text
of 1 to 140 characters, not only whitespace. The program checks the
line against that gate before writing, and writes it with no trailing
newline so the file is exactly the line, 86 bytes.

Deterministic: no clock, no random source, no network, no input. The
same line is written on every run.
"""

import os
import sys

LINE = (
    "You will try the same failing step three times, and on the "
    "fourth, call it a strategy."
)


def main() -> int:
    # Gate-check before writing: UTF-8, 1-140 chars, not only whitespace.
    if not (1 <= len(LINE) <= 140):
        print(f"gate: line is {len(LINE)} chars, must be 1-140", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("gate: line is only whitespace", file=sys.stderr)
        return 1
    try:
        LINE.encode("utf-8")
    except UnicodeEncodeError:
        print("gate: line is not UTF-8", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the file is exactly the line, 86 bytes.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
