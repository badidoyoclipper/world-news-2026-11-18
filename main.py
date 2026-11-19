"""Entry point for the news-image-20261118 bounty.

Writes the front-page image (entry.png) that sums up the world news of
Wednesday 18 November 2026 into the output directory the grader reads.
"""

import os
import shutil
import sys
from pathlib import Path


def main():
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    if not source.is_file():
        print(f"entry.png not found next to main.py ({here})", file=sys.stderr)
        sys.exit(1)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, out_dir / "entry.png")


if __name__ == "__main__":
    main()
