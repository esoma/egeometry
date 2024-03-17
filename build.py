from __future__ import annotations

__all__ = ()

# egeometry
# codegen
from codegen import generate_geometry_files

# python
import os
from pathlib import Path


def _build() -> None:
    if os.environ.get("EGEOMETRY_GENERATE_GEOMETRY_FILES", "1") == "1":
        generate_geometry_files(Path("src/egeometry"))


if __name__ == "__main__":
    _build()
