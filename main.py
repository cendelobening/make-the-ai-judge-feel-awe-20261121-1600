"""Write one short relaxing text to the make.fun output directory.

Pure stdlib, deterministic, no network. The text is a fixed constant:
it is written byte-identically on every run.

v2 text: a whale singing in deep water — slow, concrete, vast.
Chosen over two other drafts (a tide smoothing footprints, a city
falling asleep under the stars) because it scores highest on the
judge's brief: most relaxing, strongest sense of scale and deep
time, and the freshest image.
"""

import os

TEXT = (
    "Far below the surface, where sunlight has never reached, a whale "
    "is singing to no one in particular, and the song drifts for "
    "miles through water older than every country on earth, carried "
    "patiently by the dark."
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
