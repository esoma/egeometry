# generated from codegen/templates/_linesegment3d.py

from __future__ import annotations

__all__ = ["{{ name }}"]

from emath import {{ data_type }}Vector3


class {{ name }}:
    __slots__ = ["_a", "_b"]

    def __init__(self, a: {{ data_type }}Vector3, b: {{ data_type }}Vector3):
        if a == b:
            raise ValueError("line segment points must be different")
        self._a = a
        self._b = b

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, {{ name }}):
            return False
        return self._a == other._a and self._b == other._b

    def __repr__(self) -> str:
        return f"<LineSegment3d a={self._a} b={self._b}>"

    @property
    def a(self) -> {{ data_type }}Vector3:
        return self._a

    @property
    def b(self) -> {{ data_type }}Vector3:
        return self._b

    @property
    def points(self) -> tuple[{{ data_type }}Vector3, {{ data_type }}Vector3]:
        return (self._a, self._b)

    @property
    def length(self) -> float:
        return (self._b - self._a).magnitude
