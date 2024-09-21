# generated from codegen/templates/_triangle2d.py

from __future__ import annotations

__all__ = ["{{ name }}", "{{ name }}Overlappable"]

from emath import {{ data_type }}Vector2, DVector2
from typing import Protocol
from ._{{ data_type.lower() }}boundingbox2d import {{ data_type }}BoundingBox2d

class {{ name }}Overlappable(Protocol):

    def overlaps_{{ data_type.lower() }}_triangle_2d(
        self,
        other: {{ name }}
    ) -> bool:
        ...


class {{ name }}:
    __slots__ = ["_bounding_box", "_vertices"]

    def __init__(self, point_0: {{ data_type }}Vector2, point_1: {{ data_type }}Vector2, point_2: {{ data_type }}Vector2, /):
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
        self._vertices = self._vertices[i:] + self._vertices[:i] # type: ignore

        self._bounding_box = {{ data_type }}BoundingBox2d(shapes=self._vertices)

    def __hash__(self) -> int:
        return hash(self._vertices)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, {{ name }}):
            return False
        return self._vertices == other._vertices

    def __repr__(self) -> str:
        return f"<Triangle2d vertices={self._vertices}>"

    def overlaps(
        self,
        other: {{ data_type }}Vector2 |
               {{ name }}Overlappable
    ) -> bool:
        if isinstance(other, {{ data_type }}Vector2):
            return self.overlaps_{{ data_type.lower() }}_vector_2(other)
        try:
            other_overlaps = other.overlaps_{{ data_type.lower() }}_triangle_2d
        except AttributeError:
            raise TypeError(other)
        return other_overlaps(self)

    def overlaps_{{ data_type.lower() }}_vector_2(
        self,
        other: {{ data_type }}Vector2
    ) -> bool:
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

    def translate(self, translation: {{ data_type }}Vector2) -> {{ name }}:
        return {{ name }}(*(v + translation for v in self._vertices))

    @property
    def bounding_box(self) -> {{ data_type }}BoundingBox2d:
        return self._bounding_box

    @property
    def vertices(self) -> tuple[{{ data_type }}Vector2, {{ data_type }}Vector2, {{ data_type }}Vector2]:
        return self._vertices
