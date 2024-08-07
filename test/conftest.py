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
def circle_cls(data_type):
    return getattr(egeometry, f"{data_type}Circle")


@pytest.fixture
def rectangle_cls(data_type):
    return getattr(egeometry, f"{data_type}Rectangle")


@pytest.fixture
def vector_2_cls(data_type):
    return getattr(emath, f"{data_type}Vector2")
