import pytest

@pytest.mark.parametrize(
    "bb_args, f_kwargs, expected_result", [
    ([(0,), (0,)], {"orthographic": (-10, 10, -10, 10, -10, 10)}, True),
    ([(0,), (0,)], {"orthographic": (-10, 10, -10, 10, 1, 10)}, False),
    ([(0,), (0,)], {"orthographic": (-10, 10, -10, 10, -10, -1)}, False),
    ([(0,), (0,)], {"orthographic": (-10, 10, 1, 10, -10, 10)}, False),
    ([(0,), (0,)], {"orthographic": (-10, 10, -10, -1, -10, 10)}, False),
    ([(0,), (0,)], {"orthographic": (1, 10, -10, 10, -10, 10)}, False),
    ([(0,), (0,)], {"orthographic": (-10, -1, -10, 10, -10, 10)}, False),
    ([(-100,), (200,)], {"orthographic": (-10, 10, -10, 10, -10, 10)}, True),
    ([(-5,), (10,)], {"orthographic": (-10, 10, -10, 10, -10, 10)}, True),
    ([(-15, -5, -5), (10, 10, 10)], {"orthographic": (-10, 10, -10, 10, -10, 10)}, True),
    ([(5, -5, -5), (10, 10, 10)], {"orthographic": (-10, 10, -10, 10, -10, 10)}, True),
    ([(-5, -15, -5), (10, 10, 10)], {"orthographic": (-10, 10, -10, 10, -10, 10)}, True),
    ([(-5, 5, -5), (10, 10, 10)], {"orthographic": (-10, 10, -10, 10, -10, 10)}, True),
    ([(-5, -5, -15), (10, 10, 10)], {"orthographic": (-10, 10, -10, 10, -10, 10)}, True),
    ([(-5, -5, 5), (10, 10, 10)], {"orthographic": (-10, 10, -10, 10, -10, 10)}, True),
    ([(-21, -5, -5), (10, 10, 10)], {"orthographic": (-10, 10, -10, 10, -10, 10)}, False),
    ([(11, -5, -5), (10, 10, 10)], {"orthographic": (-10, 10, -10, 10, -10, 10)}, False),
    ([(-5, -21, -5), (10, 10, 10)], {"orthographic": (-10, 10, -10, 10, -10, 10)}, False),
    ([(-5, 11, -5), (10, 10, 10)], {"orthographic": (-10, 10, -10, 10, -10, 10)}, False),
    ([(-5, -5, -21), (10, 10, 10)], {"orthographic": (-10, 10, -10, 10, -10, 10)}, False),
    ([(-5, -5, 11), (10, 10, 10)], {"orthographic": (-10, 10, -10, 10, -10, 10)}, False),
])
def test_overlaps(data_type, bounding_box_3d_cls, rectangle_frustum_cls, matrix_4_cls, vector_4_cls, vector_3_cls, bb_args, f_kwargs, expected_result):
    frustum = rectangle_frustum_cls(
        transform=matrix_4_cls(*(vector_4_cls(*v) for v in f_kwargs.pop("transform", matrix_4_cls(1)))),
        **f_kwargs
    )
    bb = bounding_box_3d_cls(vector_3_cls(*bb_args[0]), vector_3_cls(*bb_args[1]))

    assert frustum.overlaps(bb) == expected_result
    assert bb.overlaps(frustum) == expected_result

    bb_overlaps = getattr(frustum, f"overlaps_{data_type.lower()}_bounding_box_3d")
    assert bb_overlaps(bb) == expected_result

    frustum_overlaps = getattr(bb, f"overlaps_{data_type.lower()}_rectangle_frustum")
    assert frustum_overlaps(frustum) == expected_result
