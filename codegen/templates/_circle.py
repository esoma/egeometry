# generated from codegen/templates/_circle.py

from __future__ import annotations

__all__ = ["{{ name }}", "{{ name }}Overlappable"]

from emath import {{ data_type }}Vector2
from typing import Protocol, TYPE_CHECKING, TypeAlias
from ._{{ data_type.lower() }}boundingbox2d import {{ data_type }}BoundingBox2d

if TYPE_CHECKING:
    from ._{{ data_type.lower() }}rectangle import {{ data_type }}Rectangle
    from ._{{ data_type.lower() }}triangle2d import {{ data_type }}Triangle2d

{% if data_type == "F" %}
_FloatVector2: TypeAlias = {{ data_type }}Vector2
def _to_float_vector(v: {{ data_type }}Vector2) -> _FloatVector2:
    return v
{% else %}
from emath import DVector2
_FloatVector2: TypeAlias = DVector2
{% if data_type == "D" %}
def _to_float_vector(v: {{ data_type }}Vector2) -> _FloatVector2:
    return v
{% else %}
def _to_float_vector(v: {{ data_type }}Vector2) -> _FloatVector2:
    return _FloatVector2(*v)
{% endif %}
{% endif %}

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
        self._bounding_box = {{ data_type }}BoundingBox2d(
            position - radius,
            {{ data_type }}Vector2(radius * 2)
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, {{ name }}):
            return False
        return self._position == other._position and self._radius == other._radius

    def __repr__(self) -> str:
        return f"<Circle position={self._position} radius={self._radius}>"

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

    def _overlaps_rect_like(self, other: {{ data_type }}BoundingBox2d | {{ data_type }}Rectangle) -> bool:
        assert other.size != {{ data_type }}Vector2(0)
        o_center = _to_float_vector(other.position) + (_to_float_vector(other.size) * 0.5)
        f_position = _to_float_vector(self._position)
        diff = f_position - o_center
        closest_o_point = _FloatVector2(
            min(max(diff.x, other.position.x), other.extent.x),
            min(max(diff.y, other.position.y), other.extent.y),
        )
        closest_o_point_distance = f_position.distance(closest_o_point)
        return closest_o_point_distance < self._radius

    def overlaps_{{ data_type.lower() }}_bounding_box_2d(self, other: {{ data_type }}BoundingBox2d) -> bool:
        if other.size == {{ data_type }}Vector2(0):
            return False
        return self._overlaps_rect_like(other)

    def overlaps_{{ data_type.lower() }}_circle(self, other: {{ data_type }}Circle) -> bool:
        min_distance = self._radius + other._radius
        distance = _to_float_vector(self._position).distance(_to_float_vector(other._position))
        return distance < min_distance

    def overlaps_{{ data_type.lower() }}_rectangle(self, other: {{ data_type }}Rectangle) -> bool:
        return self._overlaps_rect_like(other)

    def overlaps_{{ data_type.lower() }}_triangle_2d(self, other: {{ data_type }}Triangle2d) -> bool:
        fv_position = _to_float_vector(self._position)
        for tri_edge_a, tri_edge_b in (
            (other.vertices[0], other.vertices[1]),
            (other.vertices[1], other.vertices[2]),
            (other.vertices[2], other.vertices[0])
        ):
            p = _project_point_on_to_line_segment(_to_float_vector(tri_edge_a), _to_float_vector(tri_edge_b), fv_position)
            if p.distance(fv_position) < self._radius:
                return True
        return False

    def overlaps_{{ data_type.lower() }}_vector_2(
        self,
        other: {{ data_type }}Vector2
    ) -> bool:
        distance = _FloatVector2(*self._position).distance(_FloatVector2(*other))
        return distance < self._radius

    def translate(self, translation: {{ data_type }}Vector2) -> {{ name }}:
        return {{ name }}(self._position + translation, self._radius)

    @property
    def bounding_box(self) -> {{ data_type }}BoundingBox2d:
        return self._bounding_box

    @property
    def position(self) -> {{ data_type }}Vector2:
        return self._position

    @property
    def radius(self) -> {{ component_data_type }}:
        return self._radius

def _project_point_on_to_line_segment(line_a: _FloatVector2, line_b: _FloatVector2, point: _FloatVector2) -> _FloatVector2:
    slope = line_b - line_a
    length_2 = sum(x ** 2 for x in slope)
    t = ((point - line_a) @ slope) / length_2
    t = max(min(t, 1), 0)
    return line_a + (t * slope)
