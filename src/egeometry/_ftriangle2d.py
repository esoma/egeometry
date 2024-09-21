# generated from codegen/templates/_triangle2d.py

from __future__ import annotations

__all__ = ["FTriangle2d", "FTriangle2dOverlappable"]

# egeometry
from ._fboundingbox2d import FBoundingBox2d

# emath
from emath import FVector2

# python
from typing import Protocol


class FTriangle2dOverlappable(Protocol):
    def overlaps_f_triangle_2d(self, other: FTriangle2d) -> bool:
        ...


class FTriangle2d:
    __slots__ = ["_bounding_box", "_vertices"]

    def __init__(self, point_0: FVector2, point_1: FVector2, point_2: FVector2, /):
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

        self._bounding_box = FBoundingBox2d(shapes=self._vertices)

    def __hash__(self) -> int:
        return hash(self._vertices)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, FTriangle2d):
            return False
        return self._vertices == other._vertices

    def __repr__(self) -> str:
        return f"<Triangle2d vertices={self._vertices}>"

    def translate(self, translation: FVector2) -> FTriangle2d:
        return FTriangle2d(*(v + translation for v in self._vertices))

    @property
    def bounding_box(self) -> FBoundingBox2d:
        return self._bounding_box

    @property
    def vertices(self) -> tuple[FVector2, FVector2, FVector2]:
        return self._vertices
