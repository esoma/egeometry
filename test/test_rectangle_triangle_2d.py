# pytest
import pytest


@pytest.mark.parametrize(
    "bb_args, tri_args, expected_result",
    [
        ([(0,), (5,)], [(6, 0), (6, 5), (11, 0)], False),
        ([(0,), (5,)], [(5, 0), (5, 5), (10, 0)], True),
        ([(0,), (5,)], [(6, 0), (6, 5), (11, 2)], False),
        ([(0,), (5,)], [(-5, 0), (-5, 5), (0, 2)], True),
    ],
)
def test_overlaps(
    data_type, triangle_2d_cls, rectangle_cls, vector_2_cls, tri_args, bb_args, expected_result
):
    tri = triangle_2d_cls(*(vector_2_cls(*a) for a in tri_args))
    rect = rectangle_cls(vector_2_cls(*bb_args[0]), vector_2_cls(*bb_args[1]))

    assert tri.overlaps(rect) == expected_result
    assert rect.overlaps(tri) == expected_result

    rect_overlaps = getattr(tri, f"overlaps_{data_type.lower()}_rectangle")
    assert rect_overlaps(rect) == expected_result

    triangle_overlaps = getattr(rect, f"overlaps_{data_type.lower()}_triangle_2d")
    assert triangle_overlaps(tri) == expected_result
