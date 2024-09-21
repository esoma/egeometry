# pytest
import pytest


@pytest.mark.parametrize(
    "points_args, expected_vertices_args",
    [
        ([(0, 0), (1, 0), (0, 1)], [(0, 0), (0, 1), (1, 0)]),
        ([(1, 0), (0, 0), (0, 1)], [(0, 0), (0, 1), (1, 0)]),
        ([(1, 0), (0, 1), (0, 0)], [(0, 0), (1, 0), (0, 1)]),
    ],
)
def test_attrs(
    triangle_2d_cls, bounding_box_2d_cls, vector_2_cls, points_args, expected_vertices_args
):
    points = [vector_2_cls(*pa) for pa in points_args]
    expected_vertices = tuple(vector_2_cls(*pa) for pa in points_args)
    tri = triangle_2d_cls(*points)
    assert tri.bounding_box == bounding_box_2d_cls(shapes=points)
    assert tri.vertices == expected_vertices
    assert repr(tri) == f"<Triangle2d vertices={tri.vertices}>"
    assert hash(tri) == hash(expected_vertices)
    assert tri == tri


@pytest.mark.parametrize(
    "points_args",
    [
        [(0, 0), (0, 0), (0, 0)],
        [(0, 1), (0, 0), (0, 1)],
        [(0, 0), (0, 1), (0, 2)],
    ],
)
def test_invalid_vertices(triangle_2d_cls, vector_2_cls, points_args):
    points = [vector_2_cls(*pa) for pa in points_args]
    with pytest.raises(ValueError) as excinfo:
        triangle_2d_cls(*points)
    assert str(excinfo.value) == "vertices do not form a triangle"


def test_not_equal(triangle_2d_cls, vector_2_cls):
    tri = triangle_2d_cls(vector_2_cls(0), vector_2_cls(0, 1), vector_2_cls(1, 0))
    assert tri != object()


@pytest.mark.parametrize(
    "points_args",
    [
        [(0, 0), (1, 0), (0, 1)],
        [(0, 1), (100, 80), (-12, 5)],
    ],
)
@pytest.mark.parametrize("translation_args", [(0,), (1, -1)])
def test_translate(triangle_2d_cls, vector_2_cls, points_args, translation_args):
    points = [vector_2_cls(*pa) for pa in points_args]
    tri = triangle_2d_cls(*points)
    translation = vector_2_cls(*translation_args)
    assert tri.translate(translation) == triangle_2d_cls(*(p + translation for p in points))
