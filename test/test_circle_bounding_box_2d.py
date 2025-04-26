
import pytest


@pytest.mark.parametrize(
    "circle_args, bb_args, expected_result",
    [
        (((0,), 1), ((0,), (1,)), True),
        (((0,), 1), ((1,), (1,)), False),
        (((0,), 1), ((1,), (2,)), False),
        (((0,), 1), ((-1,), (2,)), True),
        (((0,), 1), ((0,), (0,)), False),
    ],
)
def test_overlaps(
    data_type,
    circle_cls,
    bounding_box_2d_cls,
    vector_2_cls,
    circle_args,
    bb_args,
    expected_result,
):
    circle = circle_cls(vector_2_cls(*circle_args[0]), circle_args[1])
    bb = bounding_box_2d_cls(vector_2_cls(*bb_args[0]), vector_2_cls(*bb_args[1]))

    assert circle.overlaps(bb) == expected_result
    assert bb.overlaps(circle) == expected_result

    circle_overlaps = getattr(circle, f"overlaps_{data_type.lower()}_bounding_box_2d")
    assert circle_overlaps(bb) == expected_result

    rectangle_overlaps = getattr(bb, f"overlaps_{data_type.lower()}_circle")
    assert rectangle_overlaps(circle) == expected_result
