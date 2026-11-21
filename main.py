"""Write one short relaxing text to the make.fun output directory.

Pure stdlib, deterministic, no network. The text is a fixed constant:
it is written byte-identically on every run.
"""

import os

TEXT = (
    "You have read a thousand entries today, and not one of them "
    "needed you to hurry. Somewhere, a river is still cutting the "
    "same canyon it began a million years ago, in no hurry at all "
    "\u2014 and the night is long enough for both of you."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
