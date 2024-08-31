__all__ = ["generate_bounding_box_files"]

# egeometry
from .template import get_template
from .types import TYPES

# python
from datetime import datetime
from pathlib import Path
from typing import Generator


def generate_bounding_box_2d_files(build_dir: Path) -> Generator[tuple[str, str], None, None]:
    b = build_dir
    for data_type, _ in TYPES:
        yield from generate_bouncing_box_2d_file(b, data_type)


def generate_bouncing_box_2d_file(
    build_dir: Path, data_type: str
) -> Generator[tuple[str, str], None, None]:
    template = get_template("_boundingbox2d.py")
    name = f"{data_type}BoundingBox2d"
    with open(build_dir / f"_{name.lower()}.py", "w") as f:
        f.write(
            template.render(
                data_type=data_type,
                name=name,
                when=datetime.utcnow(),
            )
        )
    yield (f"_{name.lower()}", name)
    yield (f"_{name.lower()}", f"{name}Overlappable")
