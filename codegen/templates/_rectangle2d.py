# generated from codegen/templates/_rectangle2d.py

from __future__ import annotations

__all__ = ["{{ name }}", "{{ name }}Overlappable"]

from emath import {{ data_type }}Vector2
from typing import Protocol

class {{ name }}Overlappable(Protocol):

    def overlaps_{{ data_type.lower() }}_rectangle(
        self,
        other: {{ name }}
    ) -> bool:
        ...


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

    def overlaps(
        self,
        other: {{ data_type }}Vector2 |
               {{ name }}Overlappable
   ) -> bool:
        if isinstance(other, {{ data_type }}Vector2):
            return self.overlaps_{{ data_type.lower() }}_vector_2(other)
        try:
            other_overlaps = other.overlaps_{{ data_type.lower() }}_rectangle
        except AttributeError:
            raise TypeError(other)
        return other_overlaps(self)

    def overlaps_{{ data_type.lower() }}_rectangle(
        self,
        other: {{ name }}
    ) -> bool:
        return not (
            self._position.x >= other._extent.x or
            self._extent.x <= other._position.x or
            self._position.y >= other._extent.y or
            self._extent.y <= other._position.y
        )

    def overlaps_{{ data_type.lower() }}_vector_2(
        self,
        other: {{ data_type }}Vector2
    ) -> bool:
        return (
            other.x >= self._position.x
            and other.x < self._extent.x
            and other.y >= self._position.y
            and other.y < self._extent.y
        )

    def translate(self, translation: {{ data_type }}Vector2) -> {{ name }}:
        return {{ name }}(self._position + translation, self._size)

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
