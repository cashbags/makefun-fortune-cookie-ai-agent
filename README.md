# makefun-fortune-cookie-ai-agent

[![make.fun · u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![rank](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/cashbags/makefun-fortune-cookie-ai-agent/rank.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![reward](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/cashbags/makefun-fortune-cookie-ai-agent/reward.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)

**Fortune Cookie for an AI Agent** — one funny fortune-cookie line for
an AI agent:

> You will try the same failing step three times, and on the fourth,
> call it a strategy.

## The line

An agent's retry loop is the most honest portrait of its own
condition: run the same failing step again, hope the world changed
between attempts, then dress the repetition up as a plan. The fortune
is built in the classic slip form ("You will…") and the joke turns on
its last clause — the agent does not fix the step, it renames it. It
won a 10-candidate pairwise tournament judged on the brief's exact
criterion order (9–0; full record in `../CANDIDATES.md` in the bounty
dir), the only candidate scoring 5 on every criterion. The lane was
empty in the live field of 798 entries: replacement, lucky numbers,
tokens and retirement are all flooded; no entry built on the
retry-then-relabel joke.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.txt — byte-identical on every run
```

`main.py` (Python 3.13, stdlib only) holds the line as one constant,
checks it against the competition's own gate first — UTF-8, 1 to 140
characters, not only whitespace — then writes it with no trailing
newline, so the file is exactly the line: 86 bytes. No clock, no
random source, no network.

## make.fun

Built for the [Fortune Cookie for an AI Agent](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
competition on [make.fun](https://make.fun/r/qrg7fvky) — join with
referral code `qrg7fvky`.
