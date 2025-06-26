__all__ = ["generate_rectangle_files"]


from datetime import datetime
from pathlib import Path
from typing import Generator

from .template import get_template
from .types import TYPES


def generate_rectangle_files(build_dir: Path) -> Generator[tuple[str, str], None, None]:
    b = build_dir
    for data_type, _ in TYPES:
        yield from generate_rectangle_file(b, data_type)


def generate_rectangle_file(
    build_dir: Path, data_type: str
) -> Generator[tuple[str, str], None, None]:
    template = get_template("_rectangle.py")
    name = f"{data_type}Rectangle"
    with open(build_dir / f"_{name.lower()}.py", "w") as f:
        f.write(template.render(data_type=data_type, name=name, when=datetime.utcnow()))
    yield (f"_{name.lower()}", name)
    yield (f"_{name.lower()}", f"{name}Overlappable")
