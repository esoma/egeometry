# generated from codegen/templates/_triangle2d.py

from __future__ import annotations

__all__ = ["{{ name }}", "{{ name }}Overlappable"]

from emath import {{ data_type }}Vector2
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

    def translate(self, translation: {{ data_type }}Vector2) -> {{ name }}:
        return {{ name }}(*(v + translation for v in self._vertices))

    @property
    def bounding_box(self) -> {{ data_type }}BoundingBox2d:
        return self._bounding_box

    @property
    def vertices(self) -> tuple[{{ data_type }}Vector2, {{ data_type }}Vector2, {{ data_type }}Vector2]:
        return self._vertices
