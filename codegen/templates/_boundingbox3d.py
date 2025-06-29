# generated from codegen/templates/_boundingbox3d.py

from __future__ import annotations

__all__ = [
    "{{ name }}", "{{ name }}Overlappable", "Has{{ name }}",
{% if data_type in "DF" %}
    "{{ name }}RaycastResult"
{% endif %}
]

from emath import {{ data_type }}Vector3, {{ data_type }}Vector4
{% if data_type in "DF" %}
from emath import {{ data_type }}Matrix4
{% endif %}
from typing import Protocol, overload, Iterable, TYPE_CHECKING, Generator, NamedTuple
from ._separating_axis_theorem import separating_axis_theorem

{% if data_type in "DF" %}
if TYPE_CHECKING:
    from ._{{ data_type.lower() }}rectanglefrustum import {{ data_type }}RectangleFrustum
{% endif %}

class {{ name }}Overlappable(Protocol):

    def overlaps_{{ data_type.lower() }}_bounding_box_3d(
        self,
        other: {{ name }}
    ) -> bool:
        ...


class Has{{ name }}(Protocol):

    @property
    def bounding_box(self) -> {{ name }}:
        ...

{% if data_type in "DF" %}
class {{ name }}RaycastResult(NamedTuple):
    position: {{ data_type }}Vector3
    distance: float
{% endif %}


class {{ name }}:
    __slots__ = ["_extent", "_position", "_size"]

    @overload
    def __init__(self, position: {{ data_type }}Vector3, size: {{ data_type }}Vector3) -> None:
        ...

    @overload
    def __init__(self, *, shapes: Iterable[Has{{ name }} | {{ data_type }}Vector3]) -> None:
        ...

    def __init__(self,
        position: {{ data_type }}Vector3 | None = None,
        size: {{ data_type }}Vector3 | None = None,
        *,
        shapes: Iterable[Has{{ name }} | {{ data_type }}Vector3] | None = None,
    ):
        if shapes is not None:
            if position is not None:
                raise TypeError("position cannot be supplied with shapes argument")
            if size is not None:
                raise TypeError("size cannot be supplied with shapes argument")
            accum_position: {{ data_type }}Vector3 | None = None
            accum_extent: {{ data_type }}Vector3 | None = None
            for s in shapes:
                if isinstance(s, {{ data_type }}Vector3):
                    p = e = s
                else:
                    p = s.bounding_box.position
                    e = s.bounding_box.extent
                if accum_position is None:
                    accum_position = p
                else:
                    accum_position = {{ data_type }}Vector3(
                        min(p.x, accum_position.x),
                        min(p.y, accum_position.y),
                        min(p.z, accum_position.z)
                    )
                if accum_extent is None:
                    accum_extent = e
                else:
                    accum_extent = {{ data_type }}Vector3(
                        max(e.x, accum_extent.x),
                        max(e.y, accum_extent.y),
                        max(e.z, accum_extent.z)
                    )
            if accum_position is None:
                position = {{ data_type }}Vector3(0)
                size = {{ data_type }}Vector3(0)
            else:
                assert accum_extent is not None
                position = accum_position
                size = accum_extent - accum_position

        assert position is not None
        assert size is not None
        if size < {{ data_type }}Vector3(0):
            raise ValueError("each size dimension must be >= 0")
        self._position = position
        self._size = size
        self._extent = self._position + self._size


    def __eq__(self, other: object) -> bool:
        if not isinstance(other, {{ name }}):
            return False
        return self._position == other._position and self._size == other._size

    def __repr__(self) -> str:
        return f"<BoundingBox3d position={self._position} size={self._size}>"

    def overlaps(
        self,
        other: {{ data_type }}Vector3 |
               {{ name }}Overlappable
   ) -> bool:
        if isinstance(other, {{ data_type }}Vector3):
            return self.overlaps_{{ data_type.lower() }}_vector_3(other)
        try:
            other_overlaps = other.overlaps_{{ data_type.lower() }}_bounding_box_3d
        except AttributeError:
            raise TypeError(other)
        return other_overlaps(self)

{% if data_type in "DF" %}
    def overlaps_{{ data_type.lower() }}_rectangle_frustum(
        self,
        other: {{ data_type }}RectangleFrustum
    ) -> bool:
        return separating_axis_theorem(
            {
                {{ data_type }}Vector3(1, 0, 0),
                {{ data_type }}Vector3(0, 1, 0),
                {{ data_type }}Vector3(0, 0, 1),
                *(p.normal for p in other.planes)
            },
            set(other.points),
            set(self.points)
        )
{% endif %}

    def overlaps_{{ data_type.lower() }}_bounding_box_3d(
        self,
        other: {{ name }}
    ) -> bool:
        return not (
            self._position.x >= other._extent.x or
            self._extent.x <= other._position.x or
            self._position.y >= other._extent.y or
            self._extent.y <= other._position.y or
            self._position.z >= other._extent.z or
            self._extent.z <= other._position.z
        )

    def overlaps_{{ data_type.lower() }}_vector_3(
        self,
        other: {{ data_type }}Vector3
    ) -> bool:
        return (
            other.x >= self._position.x
            and other.x < self._extent.x
            and other.y >= self._position.y
            and other.y < self._extent.y
            and other.z >= self._position.z
            and other.z < self._extent.z
        )

    def translate(self, translation: {{ data_type }}Vector3) -> {{ name }}:
        return {{ name }}(self._position + translation, self._size)

{% if data_type in "DF" %}
    def __rmatmul__(self, transform: {{ data_type }}Matrix4) -> {{ name }}:
        return {{ name }}(shapes=(transform @ p for p in self.points ))
{% endif %}

    @property
    def bounding_box(self) -> {{ name }}:
        return self

    @property
    def extent(self) -> {{ data_type }}Vector3:
        return self._extent

    @property
    def position(self) -> {{ data_type }}Vector3:
        return self._position

    @property
    def size(self) -> {{ data_type }}Vector3:
        return self._size

    @property
    def points(self) -> tuple[
        {{ data_type }}Vector3,
        {{ data_type }}Vector3,
        {{ data_type }}Vector3,
        {{ data_type }}Vector3,
        {{ data_type }}Vector3,
        {{ data_type }}Vector3,
        {{ data_type }}Vector3,
        {{ data_type }}Vector3
    ]:
        return (
            self._position,
            self._position + self._size.xoo,
            self._position + self._size.oyo,
            self._position + self._size.ooz,
            self._position + self._size.xyo,
            self._position + self._size.xoz,
            self._position + self._size.oyz,
            self._extent
        )

{% if data_type in "DF" %}
    def raycast(self, eye: {{ data_type }}Vector3, direction: {{ data_type }}Vector3) -> Generator[{{ name }}RaycastResult, None, None]:
        t_min = float("-inf")
        t_max = float("inf")

        if abs(direction.x) > 1e-6:
            t1 = (self._position.x - eye.x) / direction.x
            t2 = (self._extent.x - eye.x) / direction.x
            t_min = max(t_min, min(t1, t2))
            t_max = min(t_max, max(t1, t2))
        elif eye.x < self._position.x or eye.x > self._extent.x:
            return

        if abs(direction.y) > 1e-6:
            t1 = (self._position.y - eye.y) / direction.y
            t2 = (self._extent.y - eye.y) / direction.y
            t_min = max(t_min, min(t1, t2))
            t_max = min(t_max, max(t1, t2))
        elif eye.y < self._position.y or eye.y > self._extent.y:
            return

        if abs(direction.z) > 1e-6:
            t1 = (self._position.z - eye.z) / direction.z
            t2 = (self._extent.z - eye.z) / direction.z
            t_min = max(t_min, min(t1, t2))
            t_max = min(t_max, max(t1, t2))
        elif eye.z < self._position.z or eye.z > self._extent.z:
            return

        if t_min <= t_max and t_max >= 0:
            if t_min < 0:
                t_min = 0
            intersection_point = eye + t_min * direction
            yield {{ name }}RaycastResult(intersection_point, t_min)
{% endif %}
