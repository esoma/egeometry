from __future__ import annotations

__all__ = ()

try:
    from codegen import generate_geometry_files
except ImportError as ex:
    generate_geometry_files = None  # type: ignore

import os
from pathlib import Path


def _build() -> None:
    if (
        os.environ.get("EGEOMETRY_GENERATE_GEOMETRY_FILES", "0") == "1"
        and generate_geometry_files is not None
    ):
        generate_geometry_files(Path("src/egeometry"))


if __name__ == "__main__":
    _build()
