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
def float_data_type(data_type):
    if data_type not in "FD":
        pytest.skip("float data type only test")
    return data_type


@pytest.fixture
def int_data_type(data_type):
    if data_type not in "I":
        pytest.skip("int data type only test")
    return data_type


@pytest.fixture
def bounding_box_2d_cls(data_type):
    return getattr(egeometry, f"{data_type}BoundingBox2d")


@pytest.fixture
def circle_cls(data_type):
    return getattr(egeometry, f"{data_type}Circle")


@pytest.fixture
def rectangle_cls(data_type):
    return getattr(egeometry, f"{data_type}Rectangle")


@pytest.fixture
def triangle_2d_cls(data_type):
    return getattr(egeometry, f"{data_type}Triangle2d")


@pytest.fixture
def vector_2_cls(data_type):
    return getattr(emath, f"{data_type}Vector2")
