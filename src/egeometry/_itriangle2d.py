# generated from codegen/templates/_triangle2d.py

from __future__ import annotations

__all__ = ["ITriangle2d", "ITriangle2dOverlappable"]

# egeometry
from ._iboundingbox2d import IBoundingBox2d

# emath
from emath import DVector2
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

    def overlaps(self, other: IVector2 | ITriangle2dOverlappable) -> bool:
        if isinstance(other, IVector2):
            return self.overlaps_i_vector_2(other)
        try:
            other_overlaps = other.overlaps_i_triangle_2d
        except AttributeError:
            raise TypeError(other)
        return other_overlaps(self)

    def overlaps_i_vector_2(self, other: IVector2) -> bool:
        # solve for the point's barycentric coordinates
        p0 = self._vertices[0]
        v0 = DVector2(*(self._vertices[2] - p0))
        v1 = DVector2(*(self._vertices[1] - p0))
        v2 = DVector2(*(other - p0))
        dot00 = v0 @ v0
        dot01 = v0 @ v1
        dot02 = v0 @ v2
        dot11 = v1 @ v1
        dot12 = v1 @ v2
        inv_denom = 1.0 / (dot00 * dot11 - dot01 * dot01)
        u = (dot11 * dot02 - dot01 * dot12) * inv_denom
        if u < 0:
            return False
        v = (dot00 * dot12 - dot01 * dot02) * inv_denom
        if v >= 0 and u + v <= 1:
            return True
        return False

    def translate(self, translation: IVector2) -> ITriangle2d:
        return ITriangle2d(*(v + translation for v in self._vertices))

    @property
    def bounding_box(self) -> IBoundingBox2d:
        return self._bounding_box

    @property
    def vertices(self) -> tuple[IVector2, IVector2, IVector2]:
        return self._vertices
