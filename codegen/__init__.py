__all__ = ["generate_geometry_files"]

# egeometry
from codegen.bounding_box import generate_bounding_box_2d_files
from codegen.circle import generate_circle_files
from codegen.rectangle import generate_rectangle_files
from codegen.template import get_template

# python
from datetime import datetime
from pathlib import Path
from typing import Sequence


def generate_geometry_files(build_dir: Path) -> None:
    bounding_box_2d_types = list(generate_bounding_box_2d_files(build_dir))
    circle_types = list(generate_circle_files(build_dir))
    rectangle_types = list(generate_rectangle_files(build_dir))
    generate_init_file(build_dir, (*circle_types, *bounding_box_2d_types, *rectangle_types))


def generate_init_file(build_dir: Path, types: Sequence[tuple[str, str]]) -> None:
    template = get_template("__init__.py")
    with open(build_dir / f"__init__.py", "w") as f:
        f.write(
            template.render(
                types=types,
                when=datetime.utcnow(),
            )
        )
