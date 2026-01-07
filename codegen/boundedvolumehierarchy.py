__all__ = ["generate_boundedvolumehierarchy_files"]


from datetime import datetime
from pathlib import Path
from typing import Generator
from typing import Sequence

from .template import get_template
from .types import FLOAT_TYPES
from .types import UNSIGNED_TYPES
from .types import type_to_c_type


def generate_boundedvolumehierarchy_files(
    build_dir: Path,
) -> tuple[Sequence[str], Sequence[tuple[str, str]]]:
    b = build_dir
    c_types = []
    py_types = []

    child_counts = [2, 4, 8]
    for space_type, space_c_type in FLOAT_TYPES:
        for object_type, object_c_type in UNSIGNED_TYPES:
            for child_count in child_counts:
                generate_boundedvolumehierarchy_type_hpp(b, space_type, object_type, child_count)
                c_types.extend(
                    generate_boundedvolumehierarchy_hpp(b, space_type, object_type, child_count)
                )
                py_types.extend(
                    generate_boundedvolumehierarchy_py(b, space_type, object_type, child_count)
                )

    return c_types, py_types


def generate_boundedvolumehierarchy_type_hpp(
    build_dir: Path, space_type: str, object_type: str, child_count: int
) -> None:
    template = get_template("_boundedvolumehierarchytype.hpp")
    name = f"{space_type}{object_type}BoundedVolumeHierarchy{child_count}"
    with open(build_dir / f"_{name.lower()}type.hpp", "w") as f:
        f.write(
            template.render(
                space_type=space_type,
                object_type=object_type,
                child_count=child_count,
                space_c_type=type_to_c_type(space_type),
                object_c_type=type_to_c_type(object_type),
                name=name,
                when=datetime.utcnow(),
            )
        )


def generate_boundedvolumehierarchy_hpp(
    build_dir: Path, space_type: str, object_type: str, child_count: int
) -> Generator[str, None, None]:
    template = get_template("_boundedvolumehierarchy.hpp")
    name = f"{space_type}{object_type}BoundedVolumeHierarchy{child_count}"
    with open(build_dir / f"_{name.lower()}.hpp", "w") as f:
        f.write(
            template.render(
                space_type=space_type,
                object_type=object_type,
                child_count=child_count,
                space_c_type=type_to_c_type(space_type),
                object_c_type=type_to_c_type(object_type),
                name=name,
                when=datetime.utcnow(),
            )
        )
    yield name


def generate_boundedvolumehierarchy_py(
    build_dir: Path, space_type: str, object_type: str, child_count: int
) -> Generator[tuple[str, str], None, None]:
    template = get_template("_boundedvolumehierarchy.py")
    name = f"{space_type}{object_type}BoundedVolumeHierarchy{child_count}"
    with open(build_dir / f"_{name.lower()}.py", "w") as f:
        f.write(
            template.render(
                space_type=space_type,
                object_type=object_type,
                child_count=child_count,
                name=name,
                when=datetime.utcnow(),
            )
        )
    yield (f"_{name.lower()}", name)
