from __future__ import annotations

__all__ = ["{{ name }}"]

# emath
from emath import {{ data_type }}Vector2


class {{ name }}:
    __slots__ = ["_extent", "_position", "_size"]

    def __init__(self, position: {{ data_type }}Vector2, size: {{ data_type }}Vector2):
        if size <= {{ data_type }}Vector2(0):
            raise ValueError("each size dimension must be > 0")
        self._position = position
        self._size = size
        self._extent = self._position + self._size

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, {{name}}):
            return False
        return self._position == other._position and self._size == other._size

    @property
    def bounding_box(self) -> {{name}}:
        return self

    @property
    def extent(self) -> {{ data_type }}Vector2:
        return self._extent

    @property
    def position(self) -> {{ data_type }}Vector2:
        return self._position

    @property
    def size(self) -> {{ data_type }}Vector2:
        return self._size