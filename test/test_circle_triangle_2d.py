# pytest
import pytest


@pytest.mark.parametrize(
    "circle_args, tri_args, expected_result",
    [
        ([(0,), 5], [(5, 0), (5, 5), (10, 0)], False),
        ([(0,), 5], [(4, 0), (4, 5), (9, 0)], True),
        ([(0,), 5], [(0, 0), (1, 0), (0, 1)], True),
        ([(0,), 5], [(0, -10), (0, 10), (20, 0)], True),
    ],
)
def test_overlaps(
    data_type,
    triangle_2d_cls,
    circle_cls,
    vector_2_cls,
    tri_args,
    circle_args,
    expected_result,
):
    tri = triangle_2d_cls(*(vector_2_cls(*a) for a in tri_args))
    circle = circle_cls(vector_2_cls(*circle_args[0]), circle_args[1])

    assert tri.overlaps(circle) == expected_result
    assert circle.overlaps(tri) == expected_result

    circle_overlaps = getattr(tri, f"overlaps_{data_type.lower()}_circle")
    assert circle_overlaps(circle) == expected_result

    triangle_overlaps = getattr(circle, f"overlaps_{data_type.lower()}_triangle_2d")
    assert triangle_overlaps(tri) == expected_result
