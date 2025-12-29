import emath
import pytest

import egeometry


@pytest.fixture(params=["D", "F", "I"])
def data_type(request):
    return request.param


@pytest.fixture(params=["D", "F", "I"])
def other_data_type(request, data_type):
    if request.param == data_type:
        pytest.skip("same data type")
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
def other_bounding_box_2d_cls(other_data_type):
    return getattr(egeometry, f"{other_data_type}BoundingBox2d")


@pytest.fixture
def bounding_box_3d_cls(data_type):
    return getattr(egeometry, f"{data_type}BoundingBox3d")


@pytest.fixture
def circle_cls(data_type):
    return getattr(egeometry, f"{data_type}Circle")


@pytest.fixture
def plane_cls(float_data_type):
    return getattr(egeometry, f"{float_data_type}Plane")


@pytest.fixture
def linesegment3d_cls(float_data_type):
    return getattr(egeometry, f"{float_data_type}LineSegment3d")


@pytest.fixture
def rectangle_cls(data_type):
    return getattr(egeometry, f"{data_type}Rectangle")


@pytest.fixture
def rectangle_frustum_cls(float_data_type):
    return getattr(egeometry, f"{float_data_type}RectangleFrustum")


@pytest.fixture
def triangle_2d_cls(data_type):
    return getattr(egeometry, f"{data_type}Triangle2d")


@pytest.fixture
def triangle_mesh_3d_cls(float_data_type):
    return getattr(egeometry, f"{float_data_type}TriangleMesh3d")


@pytest.fixture
def vector_2_cls(data_type):
    return getattr(emath, f"{data_type}Vector2")


@pytest.fixture
def other_vector_2_cls(other_data_type):
    return getattr(emath, f"{other_data_type}Vector2")


@pytest.fixture
def vector_3_cls(data_type):
    return getattr(emath, f"{data_type}Vector3")


@pytest.fixture
def vector_3_array_cls(data_type):
    return getattr(emath, f"{data_type}Vector3Array")


@pytest.fixture
def vector_4_cls(data_type):
    return getattr(emath, f"{data_type}Vector4")


@pytest.fixture
def matrix_4_cls(float_data_type):
    return getattr(emath, f"{float_data_type}Matrix4")
