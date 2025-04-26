# generated from codegen/templates/_rectanglefrustum.py

from __future__ import annotations

__all__ = ["{{ name }}"]

from emath import {{ data_type }}Vector3, {{ data_type }}Matrix4
from ._{{ data_type.lower() }}plane import {{ data_type }}Plane
from typing import overload


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

        r = [(transform @ projection).get_row(i) for i in range(4)]
        self._near_plane = {{ data_type }}Plane(r[3].w + r[2].w, r[3].xyz + r[2].xyz)
        self._far_plane = {{ data_type }}Plane(r[3].w - r[2].w, r[3].xyz - r[2].xyz)
        self._left_plane = {{ data_type }}Plane(r[3].w + r[0].w, r[3].xyz + r[0].xyz)
        self._right_plane = {{ data_type }}Plane(r[3].w - r[0].w, r[3].xyz - r[0].xyz)
        self._bottom_plane = {{ data_type }}Plane(r[3].w + r[1].w, r[3].xyz + r[1].xyz)
        self._top_plane = {{ data_type }}Plane(r[3].w - r[1].w, r[3].xyz - r[1].xyz)

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
