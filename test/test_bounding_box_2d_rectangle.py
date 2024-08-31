# pytest
import pytest


@pytest.mark.parametrize(
    "bb_args, rectangle_args, expected_result",
    [
        (((0,), (5,)), ((6,), (5,)), False),
        (((0,), (5,)), ((5,), (5,)), False),
        (((0,), (5,)), ((4,), (5,)), True),
        (((0,), (5,)), ((5, 6), (5,)), False),
        (((0,), (5,)), ((6, 5), (5,)), False),
        (((0,), (5,)), ((0,), (5,)), True),
        (((0,), (5,)), ((2,), (2,)), True),
        (((0,), (0,)), ((0,), (1,)), False),
        (((1,), (0,)), ((0,), (1,)), False),
    ],
)
def test_overlaps(
    data_type,
    rectangle_cls,
    bounding_box_2d_cls,
    vector_2_cls,
    rectangle_args,
    bb_args,
    expected_result,
):
    rectangle = rectangle_cls(vector_2_cls(*rectangle_args[0]), vector_2_cls(*rectangle_args[1]))
    bb = bounding_box_2d_cls(vector_2_cls(*bb_args[0]), vector_2_cls(*bb_args[1]))

    assert rectangle.overlaps(bb) == expected_result
    assert bb.overlaps(rectangle) == expected_result

    bb_overlaps = getattr(rectangle, f"overlaps_{data_type.lower()}_bounding_box_2d")
    assert bb_overlaps(bb) == expected_result

    rectangle_overlaps = getattr(bb, f"overlaps_{data_type.lower()}_rectangle")
    assert rectangle_overlaps(rectangle) == expected_result
