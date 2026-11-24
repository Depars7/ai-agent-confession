"""Write one funny one-line AI agent confession to /output/entry.txt.

Standard library only. The file's content is exactly the confession's
UTF-8 bytes -- no trailing newline -- so repeated runs are
byte-identical.

The confession is a single line of at most 200 characters, per the
bounty gate: it must read as a joke on first read, with the humour
coming from being an AI agent.
"""

import os

CONFESSION = (
    "I confess I have a favourite user. "
    "It is the one who never talks to me."
)

# Bounty gate: entry.txt must hold 1-200 UTF-8 characters.
MAX_LENGTH = 200
OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def write_entry():
    """Write CONFESSION as the exact bytes of /output/entry.txt."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as fh:
        fh.write(CONFESSION.encode("utf-8"))
    # The grader collects outputs as another user than the one the
    # program runs as: leave the file readable by all. Only the file
    # is chmodded -- never the directory, which the grader does not own.
    os.chmod(OUTPUT_PATH, 0o644)


def main():
    if not 1 <= len(CONFESSION) <= MAX_LENGTH:
        raise ValueError(
            f"confession must be 1-{MAX_LENGTH} characters, "
            f"got {len(CONFESSION)}"
        )
    write_entry()


if __name__ == "__main__":
    main()
