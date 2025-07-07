__all__ = ["generate_bounding_box_2d_files"]


from datetime import datetime
from pathlib import Path
from typing import Generator
from typing import Sequence

from .template import get_template
from .types import TYPES
from .types import type_to_c_type


def generate_bounding_box_2d_files(
    build_dir: Path,
) -> tuple[Sequence[str], Sequence[tuple[str, str]]]:
    b = build_dir
    c_types = []
    py_types = []

    for data_type, _ in TYPES:
        generate_bouncing_box_2d_type_hpp(b, data_type)
        c_types.extend(generate_bouncing_box_2d_hpp(b, data_type))
        py_types.extend(generate_bouncing_box_2d_py(b, data_type))

    return c_types, py_types


def generate_bouncing_box_2d_type_hpp(build_dir: Path, data_type: str) -> None:
    template = get_template("_boundingbox2dtype.hpp")
    name = f"{data_type}BoundingBox2d"
    with open(build_dir / f"_{name.lower()}type.hpp", "w") as f:
        f.write(
            template.render(
                data_type=data_type,
                c_type=type_to_c_type(data_type),
                name=name,
                when=datetime.utcnow(),
            )
        )


def generate_bouncing_box_2d_hpp(build_dir: Path, data_type: str) -> Generator[str, None, None]:
    template = get_template("_boundingbox2d.hpp")
    name = f"{data_type}BoundingBox2d"
    with open(build_dir / f"_{name.lower()}.hpp", "w") as f:
        f.write(
            template.render(
                data_type=data_type,
                c_type=type_to_c_type(data_type),
                other_data_types=[(dt, type_to_c_type(dt)) for dt, _ in TYPES if dt != data_type],
                name=name,
                when=datetime.utcnow(),
            )
        )
    yield name


def generate_bouncing_box_2d_py(
    build_dir: Path, data_type: str
) -> Generator[tuple[str, str], None, None]:
    template = get_template("_boundingbox2d.py")
    name = f"{data_type}BoundingBox2d"
    with open(build_dir / f"_{name.lower()}.py", "w") as f:
        f.write(
            template.render(
                data_type=data_type,
                other_data_types=[dt for dt, _ in TYPES if dt != data_type],
                name=name,
                when=datetime.utcnow(),
            )
        )
    yield (f"_{name.lower()}", name)
    yield (f"_{name.lower()}", f"{name}Overlappable")
    yield (f"_{name.lower()}", f"Has{name}")
