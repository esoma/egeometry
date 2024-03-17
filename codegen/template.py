__all__ = ["get_template"]

# jinja2
from jinja2 import Environment
from jinja2 import FileSystemLoader
from jinja2 import Template

# python
import itertools
from pathlib import Path

env = Environment(
    loader=FileSystemLoader(Path(__file__).resolve().parent / "templates"),
)
env.globals["len"] = len
env.globals["set"] = set
env.globals["str"] = str
env.globals["int"] = int
env.globals["itertools"] = itertools
env.globals["enumerate"] = enumerate


def get_template(name: str) -> Template:
    return env.get_template(name)
