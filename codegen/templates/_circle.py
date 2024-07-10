# generated from codegen/templates/_circle.py

from __future__ import annotations

__all__ = ["{{ name }}", "{{ name }}Overlappable"]

from emath import {{ data_type }}Vector2
from emath import DVector2
from typing import Protocol
from ._{{ data_type.lower() }}rectangle import {{ data_type }}Rectangle

class {{ name }}Overlappable(Protocol):

    def overlaps_{{ data_type.lower() }}_circle(
        self,
        other: {{ name }}
    ) -> bool:
        ...


class {{ name }}:
    __slots__ = ["_bounding_box", "_position", "_radius"]

    def __init__(self, position: {{ data_type }}Vector2, radius: {{ component_data_type }}):
        if radius <= 0:
            raise ValueError("radius must be > 0")
        self._position = position
        self._radius = radius
        self._bounding_box = {{ data_type }}Rectangle(
            position - radius,
            {{ data_type }}Vector2(radius * 2)
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, {{ name }}):
            return False
        return self._position == other._position and self._radius == other._radius

    def overlaps(
        self,
        other: {{ data_type }}Vector2 |
               {{ name }}Overlappable
   ) -> bool:
        if isinstance(other, {{ data_type }}Vector2):
            return self.overlaps_{{ data_type.lower() }}_vector_2(other)
        try:
            other_overlaps = other.overlaps_{{ data_type.lower() }}_circle
        except AttributeError:
            raise TypeError(other)
        return other_overlaps(self)

    def overlaps_{{ data_type.lower() }}_circle(self, other: {{ data_type }}Circle) -> bool:
        min_distance = self._radius + other._radius
        distance = round(DVector2(*self._position).distance(DVector2(*other._position)))
        return distance < min_distance

    def overlaps_{{ data_type.lower() }}_rectangle(self, other: {{ data_type}}Rectangle) -> bool:
        rect_center = DVector2(*other.position) + (DVector2(*other.size) * 0.5)
        f_position = DVector2(*self._position)
        diff = f_position - rect_center
        closest_rect_point = DVector2(
            min(max(diff.x, other.position.x), other.extent.x),
            min(max(diff.y, other.position.y), other.extent.y),
        )
        closest_rect_point_distance = round(f_position.distance(closest_rect_point))
        return closest_rect_point_distance < self._radius

    def overlaps_{{ data_type.lower() }}_vector_2(
        self,
        other: {{ data_type }}Vector2
    ) -> bool:
        distance = round(DVector2(*self._position).distance(DVector2(*other)))
        return distance < self._radius

    def translate(self, translation: {{ data_type }}Vector2) -> {{ name }}:
        return {{ name }}(self._position + translation, self._radius)

    @property
    def bounding_box(self) -> {{ data_type }}Rectangle:
        return self._bounding_box

    @property
    def position(self) -> {{ data_type }}Vector2:
        return self._position

    @property
    def radius(self) -> {{ component_data_type }}:
        return self._radius
