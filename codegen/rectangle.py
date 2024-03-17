__all__ = ["generate_rectangle_files"]

# codegen
from codegen.template import get_template

# python
from datetime import datetime
from pathlib import Path
from typing import Generator


def generate_rectangle_files(build_dir: Path) -> Generator[str, None, None]:
    b = build_dir
    yield generate_rectangle_file(b, "D")
    yield generate_rectangle_file(b, "F")

def generate_rectangle_file(
    build_dir: Path,
    data_type: str
) -> str:
    template = get_template("_rectangle.py")
    name = f"{data_type}Rectangle"
    with open(build_dir / f"_{name.lower()}.py", "w") as f:
        f.write(
            template.render(
                data_type=data_type,
                name=name,
                when=datetime.utcnow(),
            )
        )
    return name
