# generated from codegen/templates/_boundingbox3d.py

from __future__ import annotations

__all__ = ["{{ name }}", "{{ name }}Overlappable", "Has{{ name }}"]

from emath import {{ data_type }}Vector3
from typing import Protocol, overload, Iterable

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
