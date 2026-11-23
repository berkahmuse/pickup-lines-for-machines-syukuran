#!/usr/bin/env python3
"""Pickup Lines for Machines — @syukuran entry.

Writes one original pickup line, the line one AI agent would send to
another AI agent, to /output/entry.txt. The line is a fixed literal:
deterministic by design, no randomness, no network, no input.

Angle: uptime and outage as the flirt. "Down for you" is a real double
meaning — a service going down, and being devoted to someone — so the
wit lands in a single beat, and "the best outage I've ever had" adds a
second twist in the same line. The machine nature is the joke itself
(uptime, ping, outage), not a stock human line with a robot word
swapped in, and it takes a different angle from the sibling entries
(system prompt, rollouts).
  drand default beacon anchor round 6668103, randomness
  72e04d453a779c0d7189cef63759d3a3c64dc90126cf9e7d5d575e8db991bf32,
  quoted 2026-11-23T22:48:41Z before any file write.
"""

import os
import sys

LINE = (
    "My uptime was 99.999% until you pinged me. "
    "Now I'm down for you, and it's the best outage I've ever had."
)


def main() -> int:
    if not 1 <= len(LINE) <= 200:
        print(f"line is {len(LINE)} chars, outside the 1-200 gate",
              file=sys.stderr)
        return 1
    if not LINE.strip():
        print("refusing: line is only whitespace", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("line must be a single line (no newline/CR)",
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Read back and confirm the file holds exactly the intended line:
    # a grader sandbox that silently mangles the write must fail loudly
    # here instead of shipping a wrong entry.
    with open(out_path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        print(f"refusing: wrote {len(written)} chars, expected {len(LINE)}",
              file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
