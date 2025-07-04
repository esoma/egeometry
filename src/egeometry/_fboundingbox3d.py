# generated from codegen/templates/_boundingbox3d.py

from __future__ import annotations

__all__ = [
    "FBoundingBox3d",
    "FBoundingBox3dOverlappable",
    "HasFBoundingBox3d",
    "FBoundingBox3dRaycastResult",
]

from typing import TYPE_CHECKING
from typing import Generator
from typing import Iterable
from typing import NamedTuple
from typing import Protocol
from typing import overload

from emath import FMatrix4
from emath import FVector3

from ._separating_axis_theorem import separating_axis_theorem

if TYPE_CHECKING:
    from ._frectanglefrustum import FRectangleFrustum


class FBoundingBox3dOverlappable(Protocol):
    def overlaps_f_bounding_box_3d(self, other: FBoundingBox3d) -> bool: ...


class HasFBoundingBox3d(Protocol):
    @property
    def bounding_box(self) -> FBoundingBox3d: ...


class FBoundingBox3dRaycastResult(NamedTuple):
    position: FVector3
    distance: float


class FBoundingBox3d:
    __slots__ = ["_extent", "_position", "_size"]

    @overload
    def __init__(self, position: FVector3, size: FVector3) -> None: ...

    @overload
    def __init__(self, *, shapes: Iterable[HasFBoundingBox3d | FVector3]) -> None: ...

    def __init__(
        self,
        position: FVector3 | None = None,
        size: FVector3 | None = None,
        *,
        shapes: Iterable[HasFBoundingBox3d | FVector3] | None = None,
    ):
        if shapes is not None:
            if position is not None:
                raise TypeError("position cannot be supplied with shapes argument")
            if size is not None:
                raise TypeError("size cannot be supplied with shapes argument")
            accum_position: FVector3 | None = None
            accum_extent: FVector3 | None = None
            for s in shapes:
                if isinstance(s, FVector3):
                    p = e = s
                else:
                    p = s.bounding_box.position
                    e = s.bounding_box.extent
                if accum_position is None:
                    accum_position = p
                else:
                    accum_position = FVector3(
                        min(p.x, accum_position.x),
                        min(p.y, accum_position.y),
                        min(p.z, accum_position.z),
                    )
                if accum_extent is None:
                    accum_extent = e
                else:
                    accum_extent = FVector3(
                        max(e.x, accum_extent.x),
                        max(e.y, accum_extent.y),
                        max(e.z, accum_extent.z),
                    )
            if accum_position is None:
                position = FVector3(0)
                size = FVector3(0)
            else:
                assert accum_extent is not None
                position = accum_position
                size = accum_extent - accum_position

        assert position is not None
        assert size is not None
        if size < FVector3(0):
            raise ValueError("each size dimension must be >= 0")
        self._position = position
        self._size = size
        self._extent = self._position + self._size

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, FBoundingBox3d):
            return False
        return self._position == other._position and self._size == other._size

    def __repr__(self) -> str:
        return f"<BoundingBox3d position={self._position} size={self._size}>"

    def overlaps(self, other: FVector3 | FBoundingBox3dOverlappable) -> bool:
        if isinstance(other, FVector3):
            return self.overlaps_f_vector_3(other)
        try:
            other_overlaps = other.overlaps_f_bounding_box_3d
        except AttributeError:
            raise TypeError(other)
        return other_overlaps(self)

    def overlaps_f_rectangle_frustum(self, other: FRectangleFrustum) -> bool:
        return separating_axis_theorem(
            {
                FVector3(1, 0, 0),
                FVector3(0, 1, 0),
                FVector3(0, 0, 1),
                *(p.normal for p in other.planes),
            },
            set(other.points),
            set(self.points),
        )

    def overlaps_f_bounding_box_3d(self, other: FBoundingBox3d) -> bool:
        return not (
            self._position.x >= other._extent.x
            or self._extent.x <= other._position.x
            or self._position.y >= other._extent.y
            or self._extent.y <= other._position.y
            or self._position.z >= other._extent.z
            or self._extent.z <= other._position.z
        )

    def overlaps_f_vector_3(self, other: FVector3) -> bool:
        return (
            other.x >= self._position.x
            and other.x < self._extent.x
            and other.y >= self._position.y
            and other.y < self._extent.y
            and other.z >= self._position.z
            and other.z < self._extent.z
        )

    def translate(self, translation: FVector3) -> FBoundingBox3d:
        return FBoundingBox3d(self._position + translation, self._size)

    def __rmatmul__(self, transform: FMatrix4) -> FBoundingBox3d:
        return FBoundingBox3d(shapes=(transform @ p for p in self.points))

    @property
    def bounding_box(self) -> FBoundingBox3d:
        return self

    @property
    def extent(self) -> FVector3:
        return self._extent

    @property
    def position(self) -> FVector3:
        return self._position

    @property
    def size(self) -> FVector3:
        return self._size

    @property
    def points(
        self,
    ) -> tuple[FVector3, FVector3, FVector3, FVector3, FVector3, FVector3, FVector3, FVector3]:
        return (
            self._position,
            self._position + self._size.xoo,
            self._position + self._size.oyo,
            self._position + self._size.ooz,
            self._position + self._size.xyo,
            self._position + self._size.xoz,
            self._position + self._size.oyz,
            self._extent,
        )

    def raycast(
        self, eye: FVector3, direction: FVector3
    ) -> Generator[FBoundingBox3dRaycastResult, None, None]:
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
            yield FBoundingBox3dRaycastResult(intersection_point, t_min)
