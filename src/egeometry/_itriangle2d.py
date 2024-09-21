# generated from codegen/templates/_triangle2d.py

from __future__ import annotations

__all__ = ["ITriangle2d", "ITriangle2dOverlappable"]

# egeometry
from ._iboundingbox2d import IBoundingBox2d

# emath
from emath import IVector2

# python
from typing import Protocol


class ITriangle2dOverlappable(Protocol):
    def overlaps_i_triangle_2d(self, other: ITriangle2d) -> bool:
        ...


class ITriangle2d:
    __slots__ = ["_bounding_box", "_vertices"]

    def __init__(self, point_0: IVector2, point_1: IVector2, point_2: IVector2, /):
        self._vertices = (point_0, point_1, point_2)

        if len(set(self._vertices)) != 3:
            raise ValueError("vertices do not form a triangle")
        # fmt: off
        double_area = (
            point_0.x * (point_1.y - point_2.y) +
            point_1.x * (point_2.y - point_1.y) +
            point_2.x * (point_0.y - point_1.y)
        )
        # fmt: on
        if double_area == 0:
            raise ValueError("vertices do not form a triangle")

        i = sorted(enumerate(self._vertices))[0][0]
        self._vertices = self._vertices[i:] + self._vertices[:i]  # type: ignore

        self._bounding_box = IBoundingBox2d(shapes=self._vertices)

    def __hash__(self) -> int:
        return hash(self._vertices)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ITriangle2d):
            return False
        return self._vertices == other._vertices

    def __repr__(self) -> str:
        return f"<Triangle2d vertices={self._vertices}>"

    def translate(self, translation: IVector2) -> ITriangle2d:
        return ITriangle2d(*(v + translation for v in self._vertices))

    @property
    def bounding_box(self) -> IBoundingBox2d:
        return self._bounding_box

    @property
    def vertices(self) -> tuple[IVector2, IVector2, IVector2]:
        return self._vertices
