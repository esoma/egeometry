# generated from codegen/templates/_rectanglefrustum.py

from __future__ import annotations

__all__ = ["{{ name }}"]

from emath import {{ data_type }}Vector3, {{ data_type }}Vector4, {{ data_type }}Matrix4
from ._{{ data_type.lower() }}plane import {{ data_type }}Plane
from typing import overload
from typing import Protocol


class {{ name }}Overlappable(Protocol):

    def overlaps_{{ data_type.lower() }}_rectangle_frustum(
        self,
        other: {{ name }}
    ) -> bool:
        ...


class {{ name }}:
    __slots__ = [
        "_transform",
        "_projection",
        "_near_plane",
        "_far_plane",
        "_left_plane",
        "_right_plane",
        "_bottom_plane",
        "_top_plane"
    ]

    @overload
    def __init__(
        self,
        *,
        transform: {{ data_type }}Matrix4 = {{ data_type }}Matrix4(1),
        orthographic: tuple[float, float, float, float, float, float]
    ):
        ...

    @overload
    def __init__(
        self,
        *,
        transform: {{ data_type }}Matrix4 = {{ data_type }}Matrix4(1),
        perspective: tuple[float, float, float, float]
    ):
        ...

    def __init__(self,
        *,
        transform: {{ data_type }}Matrix4 = {{ data_type }}Matrix4(1),
        orthographic: tuple[float, float, float, float, float, float] | None = None,
        perspective: tuple[float, float, float, float] | None = None,
    ):
        if orthographic is None and perspective is None:
            raise TypeError("either orthographic or perspective must be specified, but not both")
        elif orthographic is not None and perspective is not None:
            raise TypeError("either orthographic or perspective must be specified")
        elif orthographic is not None:
            projection = {{ data_type }}Matrix4.orthographic(*orthographic)
        else:
            assert perspective is not None
            projection = {{ data_type }}Matrix4.perspective(*perspective)

        self._transform = transform
        self._projection = projection

        r = [projection.get_row(i) for i in range(4)]
        tip = transform.inverse().transpose()
        self._near_plane = _create_transformed_plane(tip, r[3] + r[2])
        self._far_plane = _create_transformed_plane(tip, r[3] - r[2])
        self._left_plane = _create_transformed_plane(tip, r[3] + r[0])
        self._right_plane = _create_transformed_plane(tip, r[3] - r[0])
        self._bottom_plane = _create_transformed_plane(tip, r[3] + r[1])
        self._top_plane = _create_transformed_plane(tip, r[3] - r[1])

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, {{ name }}):
            return False
        return self.planes == other.planes

    def __repr__(self) -> str:
        return (
            f"<RectangleFrustum "
            f"near_plane={self._near_plane} "
            f"far_plane={self._far_plane} "
            f"left_plane={self._left_plane} "
            f"right_plane={self._right_plane} "
            f"bottom_plane={self._bottom_plane} "
            f"top_plane={self._top_plane}>"
        )

    def overlaps(
        self,
        other: {{ data_type }}Vector3 |
               {{ name }}Overlappable
   ) -> bool:
        if isinstance(other, {{ data_type }}Vector3):
            return self.overlaps_{{ data_type.lower() }}_vector_3(other)
        try:
            other_overlaps = other.overlaps_{{ data_type.lower() }}_rectangle_frustum
        except AttributeError:
            raise TypeError(other)
        return other_overlaps(self)

    def overlaps_{{ data_type.lower() }}_vector_3(
        self,
        other: {{ data_type }}Vector3
    ) -> bool:
        for plane in self.planes:
            if plane.get_signed_distance_to_point(other) < 0:
                return False
        return True

    @property
    def transform(self) -> {{ data_type }}Matrix4:
        return self._transform

    @property
    def projection(self) -> {{ data_type }}Matrix4:
        return self._projection

    @property
    def near_plane(self) -> {{ data_type }}Plane:
        return self._near_plane

    @property
    def far_plane(self) -> {{ data_type }}Plane:
        return self._far_plane

    @property
    def left_plane(self) -> {{ data_type }}Plane:
        return self._left_plane

    @property
    def right_plane(self) -> {{ data_type }}Plane:
        return self._right_plane

    @property
    def top_plane(self) -> {{ data_type }}Plane:
        return self._top_plane

    @property
    def bottom_plane(self) -> {{ data_type }}Plane:
        return self._bottom_plane

    @property
    def planes(self) -> tuple[
        {{ data_type }}Plane,
        {{ data_type }}Plane,
        {{ data_type }}Plane,
        {{ data_type }}Plane,
        {{ data_type }}Plane,
        {{ data_type }}Plane
    ]:
        return (
            self._near_plane,
            self._far_plane,
            self._left_plane,
            self._right_plane,
            self._top_plane,
            self._bottom_plane
        )

def _create_transformed_plane(
    inversed_transposed_transform: {{ data_type }}Matrix4,
    plane: {{ data_type }}Vector4
) -> {{ data_type }}Plane:
    plane = inversed_transposed_transform @ plane
    return {{ data_type }}Plane(plane.w, plane.xyz)
