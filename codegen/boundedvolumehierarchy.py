__all__ = ["generate_boundedvolumehierarchy_files"]


from datetime import datetime
from pathlib import Path
from typing import Generator
from typing import Sequence

from .template import get_template
from .types import UNSIGNED_TYPES
from .types import type_to_c_type


def generate_boundedvolumehierarchy_files(
    build_dir: Path,
) -> tuple[Sequence[str], Sequence[tuple[str, str]]]:
    b = build_dir
    c_types = []
    py_types = []

    for data_type, _ in UNSIGNED_TYPES:
        generate_boundedvolumehierarchy_type_hpp(b, data_type)
        c_types.extend(generate_boundedvolumehierarchy_hpp(b, data_type))
        py_types.extend(generate_boundedvolumehierarchy_py(b, data_type))

    return c_types, py_types


def generate_boundedvolumehierarchy_type_hpp(build_dir: Path, data_type: str) -> None:
    template = get_template("_boundedvolumehierarchytype.hpp")
    name = f"{data_type}BoundedVolumeHierarchy"
    with open(build_dir / f"_{name.lower()}type.hpp", "w") as f:
        f.write(
            template.render(
                data_type=data_type,
                c_type=type_to_c_type(data_type),
                name=name,
                when=datetime.utcnow(),
            )
        )


def generate_boundedvolumehierarchy_hpp(
    build_dir: Path, data_type: str
) -> Generator[str, None, None]:
    template = get_template("_boundedvolumehierarchy.hpp")
    name = f"{data_type}BoundedVolumeHierarchy"
    with open(build_dir / f"_{name.lower()}.hpp", "w") as f:
        f.write(
            template.render(
                data_type=data_type,
                c_type=type_to_c_type(data_type),
                name=name,
                when=datetime.utcnow(),
            )
        )
    yield name


def generate_boundedvolumehierarchy_py(
    build_dir: Path, data_type: str
) -> Generator[tuple[str, str], None, None]:
    template = get_template("_boundedvolumehierarchy.py")
    name = f"{data_type}BoundedVolumeHierarchy"
    with open(build_dir / f"_{name.lower()}.py", "w") as f:
        f.write(template.render(data_type=data_type, name=name, when=datetime.utcnow()))
    yield (f"_{name.lower()}", name)
