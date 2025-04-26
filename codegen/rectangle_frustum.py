__all__ = ["generate_rectangle_frustum_files"]


from .template import get_template
from .types import FLOAT_TYPES


from datetime import datetime
from pathlib import Path
from typing import Generator


def generate_rectangle_frustum_files(build_dir: Path) -> Generator[tuple[str, str], None, None]:
    b = build_dir
    for data_type, _ in FLOAT_TYPES:
        yield from generate_rectangle_frustum_file(b, data_type)


def generate_rectangle_frustum_file(
    build_dir: Path, data_type: str
) -> Generator[tuple[str, str], None, None]:
    template = get_template("_rectanglefrustum.py")
    name = f"{data_type}RectangleFrustum"
    with open(build_dir / f"_{name.lower()}.py", "w") as f:
        f.write(
            template.render(
                data_type=data_type,
                name=name,
                when=datetime.utcnow(),
            )
        )
    yield (f"_{name.lower()}", name)
