__all__ = ["generate_geometry_files"]

from datetime import datetime
from pathlib import Path
from typing import Sequence

from codegen.bounding_box_2d import generate_bounding_box_2d_files
from codegen.bounding_box_3d import generate_bounding_box_3d_files
from codegen.circle import generate_circle_files
from codegen.plane import generate_plane_files
from codegen.rectangle import generate_rectangle_files
from codegen.rectangle_frustum import generate_rectangle_frustum_files
from codegen.template import get_template
from codegen.triangle2d import generate_triangle_2d_files
from codegen.trianglemesh3d import generate_triangle_mesh_3d_files
from codegen.types import TYPES


def generate_geometry_files(build_dir: Path) -> None:
    bounding_box_2d_extension_types, bounding_box_2d_types = list(
        generate_bounding_box_2d_files(build_dir)
    )
    bounding_box_3d_types = list(generate_bounding_box_3d_files(build_dir))
    circle_types = list(generate_circle_files(build_dir))
    plane_types = list(generate_plane_files(build_dir))
    rectangle_types = list(generate_rectangle_files(build_dir))
    rectangle_frustum_types = list(generate_rectangle_frustum_files(build_dir))
    triangle_2d_types = list(generate_triangle_2d_files(build_dir))
    triangle_mesh_3d_types = list(generate_triangle_mesh_3d_files(build_dir))
    generate_module_state(build_dir, (*bounding_box_2d_extension_types,))
    generate_extension(build_dir, (*bounding_box_2d_extension_types,))
    generate_typestub(build_dir, bounding_box_2d_extension_types)
    generate_init_file(
        build_dir,
        (
            *bounding_box_2d_types,
            *bounding_box_3d_types,
            *circle_types,
            *plane_types,
            *rectangle_types,
            *rectangle_frustum_types,
            *triangle_2d_types,
            *triangle_mesh_3d_types,
        ),
    )


def generate_init_file(build_dir: Path, types: Sequence[tuple[str, str]]) -> None:
    template = get_template("__init__.py")
    with open(build_dir / "__init__.py", "w") as f:
        f.write(template.render(types=types, when=datetime.utcnow()))


def generate_module_state(build_dir: Path, types: Sequence[str]) -> None:
    template = get_template("_modulestate.hpp")
    with open(build_dir / f"_modulestate.hpp", "w") as f:
        f.write(template.render(types=types, when=datetime.utcnow()))


def generate_extension(build_dir: Path, types: Sequence[str]) -> None:
    template = get_template("_egeometry.cpp")
    with open(build_dir / f"_egeometry.cpp", "w") as f:
        f.write(template.render(types=types, when=datetime.utcnow()))


def generate_typestub(build_dir: Path, bounding_box_2d_types: Sequence[str]) -> None:
    template = get_template("_egeometry.pyi")
    with open(build_dir / f"_egeometry.pyi", "w") as f:
        f.write(
            template.render(
                bounding_box_2d_types=bounding_box_2d_types,
                types=[t[0] for t in TYPES],
                when=datetime.utcnow(),
            )
        )
