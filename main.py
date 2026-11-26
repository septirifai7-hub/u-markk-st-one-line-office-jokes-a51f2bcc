"""One-Line Office Jokes — a single line about office life.

The bounty asks for one line, at most 199 characters, that makes office
life funny. The joke below is built on a detail everyone who has worked
in an office recognises: the printer has perfect timing, and its timing
is always terrible. It jams exactly when the deadline is real and the
one person who can fix it is away.

Running this program writes the joke to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt when that variable is unset).
"""

import os
from pathlib import Path

ENTRY = (
    "The printer has never jammed on a quiet Tuesday — "
    "only on deadline day, when IT is on holiday."
)


def get_entry() -> str:
    """Return the joke exactly as it should be judged."""
    return ENTRY


def write_entry() -> Path:
    """Write the joke to entry.txt with no trailing newline."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(get_entry(), encoding="utf-8")
    return target


def main() -> None:
    target = write_entry()
    print(f"Wrote {len(get_entry())} characters to {target}")


if __name__ == "__main__":
    main()
