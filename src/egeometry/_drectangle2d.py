# generated from codegen/templates/_rectangle2d.py

from __future__ import annotations

__all__ = ["DRectangle2d", "DRectangle2dOverlappable"]

# emath
from emath import DVector2

# python
from typing import Protocol


class DRectangle2dOverlappable(Protocol):
    def overlaps_d_rectangle(self, other: DRectangle2d) -> bool:
        ...


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

    def overlaps(self, other: DVector2 | DRectangle2dOverlappable) -> bool:
        if isinstance(other, DVector2):
            return self.overlaps_d_vector_2(other)
        try:
            other_overlaps = other.overlaps_d_rectangle
        except AttributeError:
            raise TypeError(other)
        return other_overlaps(self)

    def overlaps_d_rectangle(self, other: DRectangle2d) -> bool:
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
