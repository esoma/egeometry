__all__ = ["FLOAT_TYPES", "SIGNED_TYPES", "TYPES", "UNSIGNED_TYPES", "type_to_c_type"]

from typing import Final

TYPES: Final = (
    ("D", "float"),
    ("F", "float"),
    ("I", "int"),
    ("U8", "uint8_t"),
    ("U16", "uint16_t"),
    ("U32", "uint32_t"),
    ("U", "unsigned int"),
)

FLOAT_TYPES: Final = (("D", "float"), ("F", "float"))

UNSIGNED_TYPES: Final = (
    ("U8", "uint8_t"),
    ("U16", "uint16_t"),
    ("U32", "uint32_t"),
    ("U", "unsigned int"),
)

_unsigned_type_set = {dt for dt, _ in UNSIGNED_TYPES}
SIGNED_TYPES: Final = tuple((dt, ct) for dt, ct in TYPES if dt not in _unsigned_type_set)


def type_to_c_type(type: str) -> str:
    return {
        "D": "double",
        "F": "float",
        "I": "int",
        "U8": "uint8_t",
        "U16": "uint16_t",
        "U32": "uint32_t",
        "U": "unsigned int",
    }[type]
