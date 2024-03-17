# generated from codegen/templates/_rectangle_2d.cpp

from __future__ import annotations

__all__ = ["DRectangle2d"]

# emath
from emath import DVector2


class DRectangle2d:
    __slots__ = ["_extent", "_position", "_size"]

    def __init__(self, position: DVector2, size: DVector2):
        if size <= DVector2(0):
            raise ValueError("each size dimension must be > 0")
        self._position = position
        self._size = size
        self._extent = self._position + self._size

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, DRectangle2d):
            return False
        return self._position == other._position and self._size == other._size

    @property
    def bounding_box(self) -> DRectangle2d:
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
