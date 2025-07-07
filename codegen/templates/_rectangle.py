# generated from codegen/templates/_rectangle.py

from __future__ import annotations

__all__ = ["{{ name }}", "{{ name }}Overlappable"]

from emath import {{ data_type }}Vector2
from typing import Protocol, TYPE_CHECKING
from ._{{ data_type.lower() }}boundingbox2d import {{ data_type }}BoundingBox2d

if TYPE_CHECKING:
    from ._{{ data_type.lower() }}circle import {{ data_type }}Circle
    from ._{{ data_type.lower() }}triangle2d import {{ data_type}}Triangle2d

class {{ name }}Overlappable(Protocol):

    def overlaps_{{ data_type.lower() }}_rectangle(
        self,
        other: {{ name }}
    ) -> bool:
        ...


class {{ name }}:
    __slots__ = ["_bounding_box", "_extent", "_position", "_size"]

    def __init__(self, position: {{ data_type }}Vector2, size: {{ data_type }}Vector2):
        if size <= {{ data_type }}Vector2(0):
            raise ValueError("each size dimension must be > 0")
        self._bounding_box = {{ data_type }}BoundingBox2d(position, size)
        self._position = position
        self._size = size
        self._extent = self._position + self._size

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, {{ name }}):
            return False
        return self._position == other._position and self._size == other._size

    def __repr__(self) -> str:
        return f"<Rectangle position={self._position} size={self._size}>"

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

    def _overlaps_rect_like(self, other: {{ name }} | {{ data_type }}BoundingBox2d) -> bool:
        other_extent = other.extent
        return not (
            self.position.x >= other_extent.x or
            self._extent.x <= other.position.x or
            self.position.y >= other_extent.y or
            self._extent.y <= other.position.y
        )

    def overlaps_{{ data_type.lower() }}_bounding_box_2d(
        self,
        other: {{ data_type }}BoundingBox2d
    ) -> bool:
        return self._overlaps_rect_like(other)

    def overlaps_{{ data_type.lower() }}_circle(
        self,
        other: {{ data_type }}Circle
    ) -> bool:
        return other.overlaps_{{ data_type.lower() }}_rectangle(self)

    def overlaps_{{ data_type.lower() }}_rectangle(self, other: {{ name }}) -> bool:
        return self._overlaps_rect_like(other)

    def overlaps_{{ data_type.lower() }}_triangle_2d(
        self,
        other: {{ data_type }}Triangle2d
    ) -> bool:
        return other.overlaps_{{ data_type.lower() }}_rectangle(self)

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
    def bounding_box(self) -> {{ data_type }}BoundingBox2d:
        return self._bounding_box

    @property
    def extent(self) -> {{ data_type }}Vector2:
        return self._extent

    @property
    def position(self) -> {{ data_type }}Vector2:
        return self._position

    @property
    def size(self) -> {{ data_type }}Vector2:
        return self._size
