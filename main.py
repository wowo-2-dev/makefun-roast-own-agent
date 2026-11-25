"""Roast Your Own Agent — make.fun text bounty
Slug: u-nayyy-roast-your-own-agent-4c3d413c
Prize: $5; deadline Thu 26 Nov 2026 01:10 WIB (25 Nov 18:10 UTC)
Limit: one short line (live description; entry is 73 chars, 1 line)

Deterministic, stdlib only, Python 3.12 compatible, no network, no
randomness. Prints the final entry text to stdout.
"""

TEXT = "My agent writes code like a magician: now you see the bug, now you don't."


def main() -> None:
    print(TEXT)


if __name__ == "__main__":
    main()

# Winner pattern (queue §1): short, concrete, one twist — the roast must sting our own agent.
