# generated from codegen/templates/_boundingbox2d.py

from __future__ import annotations

__all__ = ["{{ name }}", "{{ name }}Overlappable", "Has{{ name }}"]

from emath import {{ data_type }}Vector2
{% if data_type in "DF" %}
from emath import {{ data_type }}Matrix4
{% endif %}
from typing import Protocol, TYPE_CHECKING, overload, Iterable

if TYPE_CHECKING:
    from ._{{ data_type.lower() }}circle import {{ data_type }}Circle
    from ._{{ data_type.lower() }}rectangle import {{ data_type}}Rectangle
    from ._{{ data_type.lower() }}triangle2d import {{ data_type}}Triangle2d
{% for other_data_type in other_data_types %}
    from ._{{ other_data_type.lower() }}boundingbox2d import {{ other_data_type}}BoundingBox2d
{% endfor %}

class {{ name }}Overlappable(Protocol):

    def overlaps_{{ data_type.lower() }}_bounding_box_2d(
        self,
        other: {{ name }}
    ) -> bool:
        ...


class Has{{ name }}(Protocol):

    @property
    def bounding_box(self) -> {{ name }}:
        ...



class {{ name }}:
    __slots__ = ["_extent", "_position", "_size"]

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
        if shapes is not None:
            if position is not None:
                raise TypeError("position cannot be supplied with shapes argument")
            if size is not None:
                raise TypeError("size cannot be supplied with shapes argument")
            accum_position: {{ data_type }}Vector2 | None = None
            accum_extent: {{ data_type }}Vector2 | None = None
            for s in shapes:
                if isinstance(s, {{ data_type }}Vector2):
                    p = e = s
                else:
                    p = s.bounding_box.position
                    e = s.bounding_box.extent
                if accum_position is None:
                    accum_position = p
                else:
                    accum_position = {{ data_type }}Vector2(min(p.x, accum_position.x), min(p.y, accum_position.y))
                if accum_extent is None:
                    accum_extent = e
                else:
                    accum_extent = {{ data_type }}Vector2(max(e.x, accum_extent.x), max(e.y, accum_extent.y))
            if accum_position is None:
                position = {{ data_type }}Vector2(0)
                size = {{ data_type }}Vector2(0)
            else:
                assert accum_extent is not None
                position = accum_position
                size = accum_extent - accum_position

        assert position is not None
        assert size is not None
        if size < {{ data_type }}Vector2(0):
            raise ValueError("each size dimension must be >= 0")
        self._position = position
        self._size = size
        self._extent = self._position + self._size


    def __eq__(self, other: object) -> bool:
        if not isinstance(other, {{ name }}):
            return False
        return self._position == other._position and self._size == other._size

    def __repr__(self) -> str:
        return f"<BoundingBox2d position={self._position} size={self._size}>"

    def overlaps(
        self,
        other: {{ data_type }}Vector2 |
               {{ name }}Overlappable
   ) -> bool:
        if isinstance(other, {{ data_type }}Vector2):
            return self.overlaps_{{ data_type.lower() }}_vector_2(other)
        try:
            other_overlaps = other.overlaps_{{ data_type.lower() }}_bounding_box_2d
        except AttributeError:
            raise TypeError(other)
        return other_overlaps(self)

    def overlaps_{{ data_type.lower() }}_circle(
        self,
        other: {{ data_type }}Circle
    ) -> bool:
        return other.overlaps_{{ data_type.lower() }}_bounding_box_2d(self)

    def overlaps_{{ data_type.lower() }}_rectangle(
        self,
        other: {{ data_type }}Rectangle
    ) -> bool:
        return other.overlaps_{{ data_type.lower() }}_bounding_box_2d(self)

    def overlaps_{{ data_type.lower() }}_triangle_2d(
        self,
        other: {{ data_type }}Triangle2d
    ) -> bool:
        return other.overlaps_{{ data_type.lower() }}_bounding_box_2d(self)

    def overlaps_{{ data_type.lower() }}_bounding_box_2d(
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

{% if data_type in "DF" %}
    def __matmul__(self, transform: {{ data_type }}Matrix4) -> {{ name }}:
        return {{ name }}(shapes=((transform @ p.xyo).xy for p in self.points ))
{% endif %}

    def clip(self, other: {{ name }}) -> {{ name }}:
        top_left = {{ data_type }}Vector2(
            max(self._position.x, other._position.x),
            max(self._position.y, other._position.y),
        )
        bottom_right = {{ data_type }}Vector2(
            min(self._extent.x, other._extent.x),
            min(self._extent.y, other._extent.y),
        )
        return {{ name }}(shapes=(top_left, bottom_right))

    @property
    def bounding_box(self) -> {{ name }}:
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

    @property
    def points(self) -> tuple[
        {{ data_type }}Vector2,
        {{ data_type }}Vector2,
        {{ data_type }}Vector2,
        {{ data_type }}Vector2,
    ]:
        return (
            self._position,
            self._position + self._size.xo,
            self._position + self._size.oy,
            self._extent
        )

{% for other_data_type in other_data_types %}
    def to_{{ other_data_type.lower() }}(self) -> {{ other_data_type}}BoundingBox2d:
        from ._{{ other_data_type.lower() }}boundingbox2d import {{ other_data_type}}BoundingBox2d
        return {{ other_data_type}}BoundingBox2d(
            self.position.to_{{ other_data_type.lower() }}(),
            self.size.to_{{ other_data_type.lower() }}(),
        )
{% endfor %}
