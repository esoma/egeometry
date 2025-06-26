import pytest


@pytest.mark.parametrize(
    "circle_args, rectangle_args, expected_result",
    [
        (((0,), 1), ((0,), (1,)), True),
        (((0,), 1), ((1,), (1,)), False),
        (((0,), 1), ((1,), (2,)), False),
        (((0,), 1), ((-1,), (2,)), True),
    ],
)
def test_overlaps(
    data_type,
    circle_cls,
    rectangle_cls,
    vector_2_cls,
    circle_args,
    rectangle_args,
    expected_result,
):
    circle = circle_cls(vector_2_cls(*circle_args[0]), circle_args[1])
    rectangle = rectangle_cls(vector_2_cls(*rectangle_args[0]), vector_2_cls(*rectangle_args[1]))

    assert circle.overlaps(rectangle) == expected_result
    assert rectangle.overlaps(circle) == expected_result

    circle_overlaps = getattr(circle, f"overlaps_{data_type.lower()}_rectangle")
    assert circle_overlaps(rectangle) == expected_result

    rectangle_overlaps = getattr(rectangle, f"overlaps_{data_type.lower()}_circle")
    assert rectangle_overlaps(circle) == expected_result
