
import pytest

@pytest.mark.parametrize("distance", [-1, 0, 1])
@pytest.mark.parametrize("normal", [(1,), (-1,)])
def test_attrs(plane_cls, vector_3_cls, distance, normal):
    normal = vector_3_cls(*normal)
    plane = plane_cls(distance, normal)
    assert plane.distance == distance / normal.magnitude
    assert plane.normal == normal.normalize()
    assert repr(plane) == f"<Plane distance={plane.distance} normal={plane.normal}>"
    assert plane == plane

def test_invalid_normal(plane_cls, vector_3_cls):
    with pytest.raises(ValueError) as excinfo:
        plane_cls(0, vector_3_cls(0))
    assert str(excinfo.value) == "invalid normal"

def test_not_equal(plane_cls, vector_3_cls):
    plane = plane_cls(0, vector_3_cls(1))
    assert plane != object()

@pytest.mark.parametrize("distance", [-1, 0, 1])
@pytest.mark.parametrize("normal", [(1, 0, 0), (0, 1, 0), (0, 0, 1)])
@pytest.mark.parametrize("point", [(0,), (1,), (-1,)])
def test_get_signed_distance_to_point(plane_cls, vector_3_cls, distance, normal, point):
    plane = plane_cls(distance, vector_3_cls(*normal))
    point = vector_3_cls(*point)
    expected = plane.normal @ point + plane.distance
    assert plane.get_signed_distance_to_point(point) == expected
