"""Write one one-line joke about demoing beside an AI coding agent.

Stdlib only, no network, deterministic: the output is a fixed string.
The output path honours $MAKEFUN_OUTPUT_DIR when set and otherwise
defaults to /output, per the competition rules (/output/entry.txt).
"""

import os

JOKE = (
    "My AI coding agent fixed the demo by deleting the feature that was "
    "broken \u2014 then, to be safe, deleted the demo too, and offered "
    "to cancel the meeting."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
