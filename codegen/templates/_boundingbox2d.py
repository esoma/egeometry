# generated from codegen/templates/_boundingbox2d.py


__all__ = ["{{ name }}", "{{ name }}Overlappable", "Has{{ name }}"]

from typing import Protocol
from ._egeometry import {{ name }}

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
