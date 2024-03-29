__all__ = ["generate_geometry_files"]

# codegen
# egeometry
from codegen.rectangle2d import generate_rectangle_2d_files
from codegen.template import get_template

# python
from datetime import datetime
from pathlib import Path
from typing import Sequence


def generate_geometry_files(build_dir: Path) -> None:
    rectangle_2d_types = list(generate_rectangle_2d_files(build_dir))
    generate_init_file(build_dir, rectangle_2d_types)


def generate_init_file(build_dir: Path, types: Sequence[str]) -> None:
    template = get_template("__init__.py")
    with open(build_dir / f"__init__.py", "w") as f:
        f.write(
            template.render(
                types=types,
                when=datetime.utcnow(),
            )
        )
