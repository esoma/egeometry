__all__ = ["generate_cicle_files"]


from .template import get_template
from .types import TYPES


from datetime import datetime
from pathlib import Path
from typing import Generator


def generate_circle_files(build_dir: Path) -> Generator[tuple[str, str], None, None]:
    b = build_dir
    for data_type, component_data_type in TYPES:
        yield from generate_circle_file(b, data_type, component_data_type)


def generate_circle_file(
    build_dir: Path, data_type: str, component_data_type: str
) -> Generator[tuple[str, str], None, None]:
    template = get_template("_circle.py")
    name = f"{data_type}Circle"
    with open(build_dir / f"_{name.lower()}.py", "w") as f:
        f.write(
            template.render(
                data_type=data_type,
                component_data_type=component_data_type,
                name=name,
                when=datetime.utcnow(),
            )
        )
    yield (f"_{name.lower()}", name)
    yield (f"_{name.lower()}", f"{name}Overlappable")
