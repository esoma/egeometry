# generated from codegen/templates/_plane.py

from __future__ import annotations

__all__ = ["{{ name }}"]

from emath import {{ data_type }}Vector3


class {{ name }}:
    __slots__ = ["_distance", "_normal"]

    def __init__(self, distance: float, normal: {{ data_type }}Vector3):
        self._distance = distance
        self._normal = normal

        magnitude = normal.magnitude
        try:
            self._distance /= magnitude
            self._normal /= magnitude
        except ZeroDivisionError:
            raise ValueError("invalid normal")

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, {{ name }}):
            return False
        return self._distance == other._distance and self._normal == other._normal

    def __repr__(self) -> str:
        return f"<Plane distance={self._distance} normal={self._normal}>"

    def get_signed_distance_to_point(self, point: {{ data_type }}Vector3) -> float:
        return self._normal @ point + self._distance

    @property
    def distance(self) -> float:
        return self._distance

    @property
    def normal(self) -> {{ data_type }}Vector3:
        return self._normal
