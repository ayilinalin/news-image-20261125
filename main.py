#!/usr/bin/env python3
"""Write the world-news image for Wednesday, 25 November 2026.

The broadsheet page lives in this repository as entry.png. This program
copies those bytes to the grader's output path without changing them, so the
two runs of the entry produce identical files. A small PNG header check keeps
a damaged checkout from being handed to the judge.

Local test:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil

# The image is committed beside this program; no network and no randomness.
SOURCE_NAME = "entry.png"
OUTPUT_NAME = "entry.png"
HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, SOURCE_NAME)
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def check_source(path: str) -> None:
    """Refuse a truncated or non-PNG source before writing anything."""
    with open(path, "rb") as handle:
        header = handle.read(24)
    if header[:8] != PNG_MAGIC:
        raise ValueError("entry.png is not a PNG image")
    width = int.from_bytes(header[16:20], "big")
    height = int.from_bytes(header[20:24], "big")
    if (width, height) != (1024, 1024):
        raise ValueError(f"expected a 1024x1024 image, got {width}x{height}")


def main() -> None:
    """Copy the checked image into the output directory with fixed permissions.

    The output name stays entry.png even though the file is a PNG: the rules
    name the file, not the format, and the judge reads the image's magic bytes.
    """
    os.umask(0o022)
    check_source(SOURCE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, OUTPUT_NAME)
    shutil.copyfile(SOURCE, target)
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
