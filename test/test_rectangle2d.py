# egeometry
import egeometry

# emath
import emath

# pytest
import pytest


@pytest.fixture(params=["D", "F", "I"])
def data_type(request):
    return request.param


@pytest.fixture
def rectangle_cls(data_type):
    return getattr(egeometry, f"{data_type}Rectangle2d")


@pytest.fixture
def vector_2_cls(data_type):
    return getattr(emath, f"{data_type}Vector2")


@pytest.mark.parametrize("x", [-1, 0, 1])
@pytest.mark.parametrize("y", [-1, 0, 1])
@pytest.mark.parametrize("w", [1, 100])
@pytest.mark.parametrize("h", [2, 200])
def test_attrs(rectangle_cls, vector_2_cls, x, y, w, h):
    rect = rectangle_cls(vector_2_cls(x, y), vector_2_cls(w, h))
    assert rect.position == vector_2_cls(x, y)
    assert rect.size == vector_2_cls(w, h)
    assert rect.extent == rect.position + rect.size
    assert rect.bounding_box == rect


@pytest.mark.parametrize("w", [-1, 0])
@pytest.mark.parametrize("h", [-2, 0])
def test_invalid_size(rectangle_cls, vector_2_cls, w, h):
    with pytest.raises(ValueError) as excinfo:
        rectangle_cls(vector_2_cls(0, 0), vector_2_cls(w, h))
    assert str(excinfo.value) == "each size dimension must be > 0"


@pytest.mark.parametrize(
    "a_args, b_args, expected_result",
    [
        (((0,), (5,)), (0,), True),
        (((0,), (5,)), (5,), False),
        (((0,), (5,)), (2,), True),
        (((0,), (5,)), (4,), True),
        (((0,), (5,)), (2, 5), False),
        (((0,), (5,)), (5, 2), False),
    ],
)
def test_overlaps_vector_2(
    data_type, rectangle_cls, vector_2_cls, a_args, b_args, expected_result
):
    a = rectangle_cls(vector_2_cls(*a_args[0]), vector_2_cls(*a_args[1]))
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
    ],
)
def test_overlaps_rectangle(
    data_type, rectangle_cls, vector_2_cls, a_args, b_args, expected_result
):
    a = rectangle_cls(vector_2_cls(*a_args[0]), vector_2_cls(*a_args[1]))
    b = rectangle_cls(vector_2_cls(*b_args[0]), vector_2_cls(*b_args[1]))

    assert a.overlaps(b) == expected_result
    assert b.overlaps(a) == expected_result

    a_overlaps = getattr(a, f"overlaps_{data_type.lower()}_rectangle")
    assert a_overlaps(b) == expected_result

    b_overlaps = getattr(b, f"overlaps_{data_type.lower()}_rectangle")
    assert b_overlaps(a) == expected_result


@pytest.mark.parametrize("rect_args", [((0,), (1,)), ((4, 5), (3, 6))])
@pytest.mark.parametrize("translation_args", [(0,), (1, -1)])
def test_translate(rectangle_cls, vector_2_cls, rect_args, translation_args):
    rect = rectangle_cls(vector_2_cls(*rect_args[0]), vector_2_cls(*rect_args[1]))
    translation = vector_2_cls(*translation_args)
    assert rect.translate(translation) == rectangle_cls(rect.position + translation, rect.size)
