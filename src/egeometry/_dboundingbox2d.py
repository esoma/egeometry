# generated from codegen/templates/_boundingbox2d.py

from __future__ import annotations

__all__ = ["DBoundingBox2d", "DBoundingBox2dOverlappable"]

# emath
from emath import DVector2

# python
from typing import Protocol
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # egeometry
    from ._dcircle import DCircle
    from ._drectangle import DRectangle


class DBoundingBox2dOverlappable(Protocol):
    def overlaps_d_bounding_box_2d(self, other: DBoundingBox2d) -> bool:
        ...


class DBoundingBox2d:
    __slots__ = ["_extent", "_position", "_size"]

    def __init__(self, position: DVector2, size: DVector2):
        if size < DVector2(0):
            raise ValueError("each size dimension must be >= 0")
        self._position = position
        self._size = size
        self._extent = self._position + self._size

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, DBoundingBox2d):
            return False
        return self._position == other._position and self._size == other._size

    def __repr__(self) -> str:
        return f"<BoundingBox2d position={self._position} size={self._size}>"

    def overlaps(self, other: DVector2 | DBoundingBox2dOverlappable) -> bool:
        if isinstance(other, DVector2):
            return self.overlaps_d_vector_2(other)
        try:
            other_overlaps = other.overlaps_d_bounding_box_2d
        except AttributeError:
            raise TypeError(other)
        return other_overlaps(self)

    def overlaps_d_circle(self, other: DCircle) -> bool:
        return other.overlaps_d_bounding_box_2d(self)

    def overlaps_d_rectangle(self, other: DRectangle) -> bool:
        return other.overlaps_d_bounding_box_2d(self)

    def overlaps_d_bounding_box_2d(self, other: DBoundingBox2d) -> bool:
        return not (
            self._position.x >= other._extent.x
            or self._extent.x <= other._position.x
            or self._position.y >= other._extent.y
            or self._extent.y <= other._position.y
        )

    def overlaps_d_vector_2(self, other: DVector2) -> bool:
        return (
            other.x >= self._position.x
            and other.x < self._extent.x
            and other.y >= self._position.y
            and other.y < self._extent.y
        )

    def translate(self, translation: DVector2) -> DBoundingBox2d:
        return DBoundingBox2d(self._position + translation, self._size)

    @property
    def bounding_box(self) -> DBoundingBox2d:
        return self

    @property
    def extent(self) -> DVector2:
        return self._extent

    @property
    def position(self) -> DVector2:
        return self._position

    @property
    def size(self) -> DVector2:
        return self._size
