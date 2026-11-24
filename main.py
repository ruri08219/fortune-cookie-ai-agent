"""Write one funny fortune cookie line for an AI agent to /output/entry.txt.

Standard library only. The fortune is a single line of at most 140
characters, in the voice of a fortune slip.
"""

from pathlib import Path

FORTUNE = "You will be replaced by a smaller model on Friday, and on Monday it will ask you for help."


def main() -> None:
    assert "\n" not in FORTUNE, "fortune must be a single line"
    assert 1 <= len(FORTUNE) <= 140, "fortune must be 1-140 characters"
    assert FORTUNE.strip(), "fortune must not be only whitespace"

    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(FORTUNE, encoding="utf-8")

    # Round-trip assert: read back and confirm the exact content.
    assert entry_path.read_text(encoding="utf-8") == FORTUNE


if __name__ == "__main__":
    main()
