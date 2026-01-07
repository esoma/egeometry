# generated from codegen/templates/_egeometry.pyi

__all__ = [
{% for name in bounding_box_2d_types %}
    "{{ name }}",
{% endfor %}
{% for name in bounded_volume_hierarchy_types %}
    "{{ name }}",
{% endfor %}
]

from typing import overload, Iterable, Generator, Sequence
from ._dboundingbox3d import DBoundingBox3d
from ._fboundingbox3d import FBoundingBox3d
from emath import *

{% for name in bounding_box_2d_types %}
{% with data_type=name[0] %}
{% with other_data_types=set(signed_types) - set([data_type]) %}

from ._{{ name.lower() }} import {{ name }}Overlappable, Has{{ name }}
from ._{{ data_type.lower() }}circle import {{ data_type }}Circle
from ._{{ data_type.lower() }}rectangle import {{ data_type }}Rectangle
from ._{{ data_type.lower() }}triangle2d import {{ data_type }}Triangle2d
{% for other_data_type in other_data_types %}
from ._{{ other_data_type.lower() }}boundingbox2d import {{ other_data_type}}BoundingBox2d
{% endfor %}

class {{ name }}:
    @overload
    def __init__(self, position: {{ data_type }}Vector2, size: {{ data_type }}Vector2) -> None:
        ...

    @overload
    def __init__(self, *, shapes: Iterable[Has{{ name }} | {{ data_type }}Vector2]) -> None:
        ...

    def __init__(self,
        position: {{ data_type }}Vector2 | None = None,
        size: {{ data_type }}Vector2 | None = None,
        *,
        shapes: Iterable[Has{{ name }} | {{ data_type }}Vector2] | None = None,
    ):
        ...

    def __eq__(self, other: object) -> bool:
        ...

    def __repr__(self) -> str:
        ...

    def overlaps(
        self,
        other: {{ data_type }}Vector2 |
               {{ name }}Overlappable
   ) -> bool:
        ...

    def overlaps_{{ data_type.lower() }}_circle(
        self,
        other: {{ data_type }}Circle
    ) -> bool:
        ...

    def overlaps_{{ data_type.lower() }}_rectangle(
        self,
        other: {{ data_type }}Rectangle
    ) -> bool:
        ...

    def overlaps_{{ data_type.lower() }}_triangle_2d(
        self,
        other: {{ data_type }}Triangle2d
    ) -> bool:
        ...

    def overlaps_{{ data_type.lower() }}_bounding_box_2d(
        self,
        other: {{ name }}
    ) -> bool:
        ...

    def overlaps_{{ data_type.lower() }}_vector_2(
        self,
        other: {{ data_type }}Vector2
    ) -> bool:
        ...

    def translate(self, translation: {{ data_type }}Vector2) -> {{ name }}:
        ...

{% if data_type in "DF" %}
    def __rmatmul__(self, transform: {{ data_type }}Matrix4) -> {{ name }}:
        ...
{% endif %}

    def clip(self, other: {{ name }}) -> {{ name }}:
        ...

    @property
    def bounding_box(self) -> {{ name }}:
        ...

    @property
    def extent(self) -> {{ data_type }}Vector2:
        ...

    @property
    def position(self) -> {{ data_type }}Vector2:
        ...

    @property
    def size(self) -> {{ data_type }}Vector2:
        ...

    @property
    def points(self) -> tuple[
        {{ data_type }}Vector2,
        {{ data_type }}Vector2,
        {{ data_type }}Vector2,
        {{ data_type }}Vector2,
    ]:
        ...

{% for other_data_type in other_data_types %}
    def to_{{ other_data_type.lower() }}(self) -> {{ other_data_type}}BoundingBox2d:
        ...
{% endfor %}

{% endwith %}
{% endwith %}
{% endfor %}

{% for name in bounded_volume_hierarchy_types %}
{% with space_type=name[0] %}

class {{ name }}:
    def __init__(self, items: Sequence[{{ space_type }}BoundingBox3d], /) -> None:
        ...

    @property
    def nodes(self) -> tuple[
        tuple[int | tuple[{{ space_type }}BoundingBox3d, int], ...],
        ...
    ]:
        ...

    def raycast(
        self,
        eye: {{ space_type }}Vector3,
        direction: {{ space_type }}Vector3,
        /
    ) -> Generator[int, None, None]:
        ...

{% endwith %}
{% endfor %}
