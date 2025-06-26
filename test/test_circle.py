import pytest


@pytest.mark.parametrize("x", [-1, 0, 1])
@pytest.mark.parametrize("y", [-1, 0, 1])
@pytest.mark.parametrize("r", [1, 100])
def test_attrs(circle_cls, bounding_box_2d_cls, rectangle_cls, vector_2_cls, x, y, r):
    circle = circle_cls(vector_2_cls(x, y), r)
    assert circle.position == vector_2_cls(x, y)
    assert circle.radius == r
    assert circle.bounding_box == bounding_box_2d_cls(circle.position - r, vector_2_cls(r * 2))
    assert repr(circle) == f"<Circle position={circle.position} radius={circle.radius}>"


@pytest.mark.parametrize("r", [-1, 0])
def test_invalid_radius(circle_cls, vector_2_cls, r):
    with pytest.raises(ValueError) as excinfo:
        circle_cls(vector_2_cls(0), r)
    assert str(excinfo.value) == "radius must be > 0"


def test_not_equal(circle_cls, vector_2_cls):
    circle = circle_cls(vector_2_cls(0), 1)
    assert circle != object()


@pytest.mark.parametrize(
    "a_args, b_args, expected_result",
    [
        (((0,), 5), (0,), True),
        (((0,), 5), (5,), False),
        (((0,), 5), (2,), True),
        (((0,), 5), (4,), False),
        (((0,), 5), (2, 5), False),
        (((0,), 5), (5, 2), False),
    ],
)
def test_overlaps_vector_2(data_type, circle_cls, vector_2_cls, a_args, b_args, expected_result):
    a = circle_cls(vector_2_cls(*a_args[0]), a_args[1])
    b = vector_2_cls(*b_args)

    assert a.overlaps(b) == expected_result

    a_overlaps = getattr(a, f"overlaps_{data_type.lower()}_vector_2")
    assert a_overlaps(b) == expected_result


@pytest.mark.parametrize(
    "a_args, b_args, expected_result",
    [
        (((0,), 1), ((2,), 1), False),
        (((0,), 1), ((2, 0), 1), False),
        (((0,), 1), ((0, 2), 1), False),
        (((0,), 1), ((0, 2), 2), True),
        (((0,), 1), ((2, 0), 2), True),
        # (((0,), 1), ((2, 2), 2), True),
        (((0,), 2), ((2, 2), 2), True),
        (((0,), 1), ((0,), 2), True),
    ],
)
def test_overlaps_circle(data_type, circle_cls, vector_2_cls, a_args, b_args, expected_result):
    a = circle_cls(vector_2_cls(*a_args[0]), a_args[1])
    b = circle_cls(vector_2_cls(*b_args[0]), b_args[1])
    if expected_result:
        assert a.bounding_box.overlaps(b.bounding_box)
        assert b.bounding_box.overlaps(a.bounding_box)
    assert a.overlaps(b) == expected_result
    assert b.overlaps(a) == expected_result

    a_overlaps = getattr(a, f"overlaps_{data_type.lower()}_circle")
    assert a_overlaps(b) == expected_result

    b_overlaps = getattr(b, f"overlaps_{data_type.lower()}_circle")
    assert b_overlaps(a) == expected_result


@pytest.mark.parametrize("a_args, b_args, expected_result", [(((0,), 1), ((2, 2), 2), True)])
def test_float_overlaps_circle(
    float_data_type, circle_cls, vector_2_cls, a_args, b_args, expected_result
):
    a = circle_cls(vector_2_cls(*a_args[0]), a_args[1])
    b = circle_cls(vector_2_cls(*b_args[0]), b_args[1])
    if expected_result:
        assert a.bounding_box.overlaps(b.bounding_box)
        assert b.bounding_box.overlaps(a.bounding_box)
    assert a.overlaps(b) == expected_result
    assert b.overlaps(a) == expected_result

    a_overlaps = getattr(a, f"overlaps_{float_data_type.lower()}_circle")
    assert a_overlaps(b) == expected_result

    b_overlaps = getattr(b, f"overlaps_{float_data_type.lower()}_circle")
    assert b_overlaps(a) == expected_result


@pytest.mark.parametrize("a_args, b_args, expected_result", [(((0,), 1), ((2, 2), 2), False)])
def test_int_overlaps_circle(
    int_data_type, circle_cls, vector_2_cls, a_args, b_args, expected_result
):
    a = circle_cls(vector_2_cls(*a_args[0]), a_args[1])
    b = circle_cls(vector_2_cls(*b_args[0]), b_args[1])
    if expected_result:
        assert a.bounding_box.overlaps(b.bounding_box)
        assert b.bounding_box.overlaps(a.bounding_box)
    assert a.overlaps(b) == expected_result
    assert b.overlaps(a) == expected_result

    a_overlaps = getattr(a, f"overlaps_{int_data_type.lower()}_circle")
    assert a_overlaps(b) == expected_result

    b_overlaps = getattr(b, f"overlaps_{int_data_type.lower()}_circle")
    assert b_overlaps(a) == expected_result


@pytest.mark.parametrize("circle_args", [((0,), 1), ((4, 5), 6)])
@pytest.mark.parametrize("translation_args", [(0,), (1, -1)])
def test_translate(circle_cls, vector_2_cls, circle_args, translation_args):
    circle = circle_cls(vector_2_cls(*circle_args[0]), circle_args[1])
    translation = translation = vector_2_cls(*translation_args)
    assert circle.translate(translation) == circle_cls(
        circle.position + translation, circle.radius
    )


def test_not_overlaps(circle_cls, vector_2_cls):
    circle = circle_cls(vector_2_cls(0), 1)
    with pytest.raises(TypeError):
        circle.overlaps(object())
