__all__ = ["FLOAT_TYPES", "TYPES", "type_to_c_type"]

from typing import Final

TYPES: Final = (("D", "float"), ("F", "float"), ("I", "int"))

FLOAT_TYPES: Final = (("D", "float"), ("F", "float"))


def type_to_c_type(type: str) -> str:
    return {"D": "double", "F": "float", "I": "int"}[type]
