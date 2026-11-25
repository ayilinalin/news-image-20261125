#!/usr/bin/env python3
"""Sum up the world's news of Wednesday 25 November 2026 in one image.

The repository holds the finished 1024x1024 PNG; this program copies it to
the output directory unchanged, so both runs write byte-identical files.

Local test (outside the grader, MAKEFUN_OUTPUT_DIR stands in for /output):
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def main() -> None:
    os.umask(0o022)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    os.chmod(dst, 0o644)


if __name__ == "__main__":
    main()
