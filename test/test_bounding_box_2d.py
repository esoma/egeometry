import pytest


@pytest.mark.parametrize("x", [-1, 0, 1])
@pytest.mark.parametrize("y", [-1, 0, 1])
@pytest.mark.parametrize("w", [0, 1, 100])
@pytest.mark.parametrize("h", [0, 2, 200])
def test_attrs(bounding_box_2d_cls, vector_2_cls, x, y, w, h):
    bb = bounding_box_2d_cls(vector_2_cls(x, y), vector_2_cls(w, h))
    assert bb.position == vector_2_cls(x, y)
    assert bb.size == vector_2_cls(w, h)
    assert bb.extent == bb.position + bb.size
    assert bb.bounding_box is bb
    assert repr(bb) == f"<BoundingBox2d position={bb.position} size={bb.size}>"


@pytest.mark.parametrize("w", [-1, -100])
@pytest.mark.parametrize("h", [-2, -200])
def test_invalid_size(bounding_box_2d_cls, vector_2_cls, w, h):
    with pytest.raises(ValueError) as excinfo:
        bounding_box_2d_cls(vector_2_cls(0, 0), vector_2_cls(w, h))
    assert str(excinfo.value) == "each size dimension must be >= 0"


def test_shapes_extra(bounding_box_2d_cls, vector_2_cls):
    with pytest.raises(TypeError):
        bounding_box_2d_cls(vector_2_cls(0), vector_2_cls(0), shapes=[])
    with pytest.raises(TypeError):
        bounding_box_2d_cls(vector_2_cls(0), shapes=[])
    with pytest.raises(TypeError):
        bounding_box_2d_cls(position=vector_2_cls(0), shapes=[])
    with pytest.raises(TypeError):
        bounding_box_2d_cls(size=vector_2_cls(0), shapes=[])


def test_shapes(vector_2_cls, bounding_box_2d_cls, rectangle_cls, circle_cls):
    assert bounding_box_2d_cls(shapes=[]) == bounding_box_2d_cls(vector_2_cls(0), vector_2_cls(0))
    assert bounding_box_2d_cls(
        shapes=[vector_2_cls(0), vector_2_cls(-1, 1), vector_2_cls(1, -1)]
    ) == bounding_box_2d_cls(vector_2_cls(-1), vector_2_cls(2))
    assert bounding_box_2d_cls(
        shapes=[
            rectangle_cls(vector_2_cls(-2, 3), vector_2_cls(4, 7)),
            circle_cls(vector_2_cls(4, 0), 5),
        ]
    ) == bounding_box_2d_cls(vector_2_cls(-2, -5), vector_2_cls(11, 15))


def test_not_equal(bounding_box_2d_cls, vector_2_cls):
    bb = bounding_box_2d_cls(vector_2_cls(0), vector_2_cls(1))
    assert bb != object()


@pytest.mark.parametrize(
    "a_args, b_args, expected_result",
    [
        (((0,), (5,)), (0,), True),
        (((0,), (5,)), (5,), False),
        (((0,), (5,)), (2,), True),
        (((0,), (5,)), (4,), True),
        (((0,), (5,)), (2, 5), False),
        (((0,), (5,)), (5, 2), False),
        (((0,), (0,)), (0,), False),
    ],
)
def test_overlaps_vector_2(
    data_type, bounding_box_2d_cls, vector_2_cls, a_args, b_args, expected_result
):
    a = bounding_box_2d_cls(vector_2_cls(*a_args[0]), vector_2_cls(*a_args[1]))
    b = vector_2_cls(*b_args)

    assert a.overlaps(b) == expected_result

    a_overlaps = getattr(a, f"overlaps_{data_type.lower()}_vector_2")
    assert a_overlaps(b) == expected_result


@pytest.mark.parametrize(
    "a_args, b_args, expected_result",
    [
        (((0,), (5,)), ((6,), (5,)), False),
        (((0,), (5,)), ((5,), (5,)), False),
        (((0,), (5,)), ((4,), (5,)), True),
        (((0,), (5,)), ((5, 6), (5,)), False),
        (((0,), (5,)), ((6, 5), (5,)), False),
        (((0,), (5,)), ((0,), (5,)), True),
        (((0,), (5,)), ((2,), (2,)), True),
        (((0,), (0,)), ((0,), (0,)), False),
        (((0,), (1,)), ((0,), (0,)), False),
        (((0,), (0,)), ((0,), (1,)), False),
        (((0,), (1,)), ((1,), (0,)), False),
        (((1,), (0,)), ((0,), (1,)), False),
    ],
)
def test_overlaps_bounding_box_2d(
    data_type, bounding_box_2d_cls, vector_2_cls, a_args, b_args, expected_result
):
    a = bounding_box_2d_cls(vector_2_cls(*a_args[0]), vector_2_cls(*a_args[1]))
    b = bounding_box_2d_cls(vector_2_cls(*b_args[0]), vector_2_cls(*b_args[1]))

    assert a.overlaps(b) == expected_result
    assert b.overlaps(a) == expected_result

    a_overlaps = getattr(a, f"overlaps_{data_type.lower()}_bounding_box_2d")
    assert a_overlaps(b) == expected_result

    b_overlaps = getattr(b, f"overlaps_{data_type.lower()}_bounding_box_2d")
    assert b_overlaps(a) == expected_result


@pytest.mark.parametrize("bb_args", [((0,), (1,)), ((4, 5), (3, 6))])
@pytest.mark.parametrize("translation_args", [(0,), (1, -1)])
def test_translate(bounding_box_2d_cls, vector_2_cls, bb_args, translation_args):
    bb = bounding_box_2d_cls(vector_2_cls(*bb_args[0]), vector_2_cls(*bb_args[1]))
    translation = vector_2_cls(*translation_args)
    assert bb.translate(translation) == bounding_box_2d_cls(bb.position + translation, bb.size)


def test_not_overlaps(bounding_box_2d_cls, vector_2_cls):
    bb = bounding_box_2d_cls(vector_2_cls(0), vector_2_cls(1))
    with pytest.raises(TypeError):
        bb.overlaps(object())


def test_clip(bounding_box_2d_cls, vector_2_cls):
    bb = bounding_box_2d_cls(vector_2_cls(0), vector_2_cls(10))

    result = bb.clip(bb)
    assert result == bb

    result = bb.clip(bounding_box_2d_cls(vector_2_cls(5), vector_2_cls(0)))
    assert result == bounding_box_2d_cls(vector_2_cls(5), vector_2_cls(0))

    result = bb.clip(bounding_box_2d_cls(vector_2_cls(1), vector_2_cls(5)))
    assert result == bounding_box_2d_cls(vector_2_cls(1), vector_2_cls(5))

    result = bb.clip(bounding_box_2d_cls(vector_2_cls(-1), vector_2_cls(5)))
    assert result == bounding_box_2d_cls(vector_2_cls(0), vector_2_cls(4))

    result = bb.clip(bounding_box_2d_cls(vector_2_cls(1), vector_2_cls(200)))
    assert result == bounding_box_2d_cls(vector_2_cls(1), vector_2_cls(9))
