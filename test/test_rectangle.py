# egeometry
import egeometry

# emath
import emath

# pytest
import pytest


@pytest.fixture(params=["D", "F"])
def data_type(request):
    return request.param


@pytest.fixture
def rectangle_cls(data_type):
    return getattr(egeometry, f"{data_type}Rectangle")


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
