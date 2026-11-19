"""news-image-20261118 entry: write the day's front page to /output/entry.png.

The image beside this file (entry.png) is a newspaper front page summing up
the world news of Wednesday 18 November 2026. This program copies it, byte
for byte, to the output directory, so both grader runs produce identical
bytes. Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
/output. Python 3.13, standard library only, no network. The five stories
on the page: the Iran war's Gulf strikes, the Shenzhen summit, the Kerch
Bridge hit again, the US Senate flipping to the Democrats, and Voyager 1
reaching one light-day from Earth.
"""

import os
import shutil
from pathlib import Path


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    source = Path(__file__).resolve().parent / "entry.png"
    shutil.copyfile(source, out_dir / "entry.png")


if __name__ == "__main__":
    main()
