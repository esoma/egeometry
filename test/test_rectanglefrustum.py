from math import radians

import pytest
from emath import FMatrix4
from emath import FVector3


@pytest.mark.parametrize(
    "projection_kwargs",
    [
        {"orthographic": (0, 800, 0, 600, 0.1, 100)},
        {"perspective": (radians(60), 4.0 / 3.0, 0.1, 100)},
    ],
)
@pytest.mark.parametrize(
    "transform_kwargs",
    [
        {},
        {"transform": FMatrix4(1)},
        {"transform": FMatrix4(1).translate(FVector3(99999))},
        {"transform": FMatrix4(1).translate(FVector3(-99999))},
        {"transform": FMatrix4(1).scale(FVector3(2))},
        {"transform": FMatrix4(1).scale(FVector3(0.5))},
        {"transform": FMatrix4(1).rotate(1.0, FVector3(1).normalize())},
    ],
)
def test_attrs(
    rectangle_frustum_cls,
    plane_cls,
    vector_4_cls,
    matrix_4_cls,
    transform_kwargs,
    projection_kwargs,
):
    try:
        transform = matrix_4_cls(*(vector_4_cls(*v) for v in transform_kwargs["transform"]))
        transform_kwargs["transform"] = transform
    except KeyError:
        transform = matrix_4_cls(1)
    if "orthographic" in projection_kwargs:
        projection = matrix_4_cls.orthographic(*projection_kwargs["orthographic"])
    else:
        projection = matrix_4_cls.perspective(*projection_kwargs["perspective"])
    frustum = rectangle_frustum_cls(**transform_kwargs, **projection_kwargs)

    r = [projection.get_row(i) for i in range(4)]
    tip = transform.inverse().transpose()
    near_plane = tip @ (r[3] + r[2])
    near_plane = plane_cls(near_plane.w, near_plane.xyz)
    far_plane = tip @ (r[3] - r[2])
    far_plane = plane_cls(far_plane.w, far_plane.xyz)
    left_plane = tip @ (r[3] + r[0])
    left_plane = plane_cls(left_plane.w, left_plane.xyz)
    right_plane = tip @ (r[3] - r[0])
    right_plane = plane_cls(right_plane.w, right_plane.xyz)
    bottom_plane = tip @ (r[3] + r[1])
    bottom_plane = plane_cls(bottom_plane.w, bottom_plane.xyz)
    top_plane = tip @ (r[3] - r[1])
    top_plane = plane_cls(top_plane.w, top_plane.xyz)

    assert frustum.transform == transform
    assert frustum.projection == projection
    assert frustum.near_plane == near_plane
    assert frustum.far_plane == far_plane
    assert frustum.left_plane == left_plane
    assert frustum.right_plane == right_plane
    assert frustum.bottom_plane == bottom_plane
    assert frustum.top_plane == top_plane
    assert frustum.planes == (
        near_plane,
        far_plane,
        left_plane,
        right_plane,
        top_plane,
        bottom_plane,
    )
    assert repr(frustum) == (
        f"<RectangleFrustum "
        f"near_plane={near_plane} "
        f"far_plane={far_plane} "
        f"left_plane={left_plane} "
        f"right_plane={right_plane} "
        f"bottom_plane={bottom_plane} "
        f"top_plane={top_plane}>"
    )
    assert frustum == frustum


def test_missing_projection(rectangle_frustum_cls):
    with pytest.raises(TypeError) as excinfo:
        rectangle_frustum_cls()
    assert (
        str(excinfo.value) == "either orthographic or perspective must be specified, but not both"
    )


def test_double_projection(rectangle_frustum_cls):
    with pytest.raises(TypeError) as excinfo:
        rectangle_frustum_cls(
            orthographic=(0, 800, 0, 600, 0.1, 100), perspective=(radians(60), 4.0 / 3.0, 0.1, 100)
        )
    assert str(excinfo.value) == "either orthographic or perspective must be specified"


def test_not_equal(rectangle_frustum_cls):
    frustum = rectangle_frustum_cls(orthographic=(0, 800, 0, 600, 0.1, 100))
    assert frustum != object()


@pytest.mark.parametrize(
    "transform",
    [
        FMatrix4(1),
        FMatrix4(1).translate(FVector3(99999)),
        FMatrix4(1).translate(FVector3(-99999)),
        FMatrix4(1).scale(FVector3(2)),
        FMatrix4(1).scale(FVector3(0.5)),
        FMatrix4(1).rotate(1.0, FVector3(1).normalize()),
    ],
)
@pytest.mark.parametrize(
    "projection, point, expected_result",
    [
        ({"perspective": (radians(60), 4.0 / 3.0, 0.1, 100)}, (0,), False),
        ({"perspective": (radians(60), 4.0 / 3.0, 0.1, 100)}, (0, 0, -0.11), True),
        ({"perspective": (radians(60), 4.0 / 3.0, 0.1, 100)}, (0, 0, -99.9), True),
        ({"perspective": (radians(60), 4.0 / 3.0, 0.1, 100)}, (0, 0, -101), False),
        ({"perspective": (radians(60), 4.0 / 3.0, 0.1, 100)}, (0, 0, -50), True),
        ({"perspective": (radians(60), 4.0 / 3.0, 0.1, 100)}, (1000, 0, -50), False),
        ({"perspective": (radians(60), 4.0 / 3.0, 0.1, 100)}, (-1000, 0, -50), False),
        ({"perspective": (radians(60), 4.0 / 3.0, 0.1, 100)}, (0, 1000, -50), False),
        ({"perspective": (radians(60), 4.0 / 3.0, 0.1, 100)}, (0, -1000, -50), False),
        ({"orthographic": (-10, 10, -5, 5, 0.1, 100)}, (0,), False),
        ({"orthographic": (-10, 10, -5, 5, 0.1, 100)}, (0, 0, -0.09), False),
        ({"orthographic": (-10, 10, -5, 5, 0.1, 100)}, (0, 0, -0.11), True),
        ({"orthographic": (-10, 10, -5, 5, 0.1, 100)}, (0, 0, -99.9), True),
        ({"orthographic": (-10, 10, -5, 5, 0.1, 100)}, (0, 0, -101.1), False),
        ({"orthographic": (-10, 10, -5, 5, 0.1, 100)}, (-10.1, 0, -50), False),
        ({"orthographic": (-10, 10, -5, 5, 0.1, 100)}, (-9.9, 0, -50), True),
        ({"orthographic": (-10, 10, -5, 5, 0.1, 100)}, (10.1, 0, -50), False),
        ({"orthographic": (-10, 10, -5, 5, 0.1, 100)}, (9.9, 0, -50), True),
        ({"orthographic": (-10, 10, -5, 5, 0.1, 100)}, (0, -5.1, -50), False),
        ({"orthographic": (-10, 10, -5, 5, 0.1, 100)}, (0, -4.9, -50), True),
        ({"orthographic": (-10, 10, -5, 5, 0.1, 100)}, (0, 5.1, -50), False),
        ({"orthographic": (-10, 10, -5, 5, 0.1, 100)}, (0, 4.9, -50), True),
    ],
)
def test_overlaps_vector_3(
    data_type,
    rectangle_frustum_cls,
    vector_3_cls,
    matrix_4_cls,
    vector_4_cls,
    transform,
    projection,
    point,
    expected_result,
):
    transform = matrix_4_cls(*(vector_4_cls(*v) for v in transform))
    frustum = rectangle_frustum_cls(transform=transform, **projection)
    point = transform @ vector_3_cls(*point)

    assert frustum.overlaps(point) == expected_result
    overlaps = getattr(frustum, f"overlaps_{data_type.lower()}_vector_3")
    assert overlaps(point) == expected_result


def test_not_overlaps(rectangle_frustum_cls):
    frustum = rectangle_frustum_cls(orthographic=(0, 800, 0, 600, 0.1, 100))
    with pytest.raises(TypeError):
        frustum.overlaps(object())


@pytest.mark.parametrize(
    "projection_kwargs",
    [
        {"orthographic": (0, 800, 0, 600, 0.1, 100)},
        {"perspective": (radians(60), 4.0 / 3.0, 0.1, 100)},
    ],
)
@pytest.mark.parametrize(
    "transform_kwargs",
    [
        {},
        {"transform": FMatrix4(1)},
        {"transform": FMatrix4(1).translate(FVector3(10, 20, 30))},
        {"transform": FMatrix4(1).scale(FVector3(2))},
    ],
)
def test_edges(
    rectangle_frustum_cls,
    linesegment3d_cls,
    matrix_4_cls,
    vector_4_cls,
    transform_kwargs,
    projection_kwargs,
):
    try:
        transform = matrix_4_cls(*(vector_4_cls(*v) for v in transform_kwargs["transform"]))
        transform_kwargs["transform"] = transform
    except KeyError:
        pass
    print(transform_kwargs)
    print(projection_kwargs)
    frustum = rectangle_frustum_cls(**transform_kwargs, **projection_kwargs)
    p0, p1, p2, p3, p4, p5, p6, p7 = frustum.points
    print(frustum.points)
    edges = frustum.edges

    expected_edges = (
        # near face edges
        linesegment3d_cls(p0, p1),
        linesegment3d_cls(p1, p7),
        linesegment3d_cls(p7, p2),
        linesegment3d_cls(p2, p0),
        # far face edges
        linesegment3d_cls(p3, p6),
        linesegment3d_cls(p6, p4),
        linesegment3d_cls(p4, p5),
        linesegment3d_cls(p5, p3),
        # connecting edges
        linesegment3d_cls(p0, p3),
        linesegment3d_cls(p1, p6),
        linesegment3d_cls(p7, p4),
        linesegment3d_cls(p2, p5),
    )

    assert edges == expected_edges


@pytest.mark.parametrize(
    "projection_kwargs",
    [
        {"orthographic": (0, 800, 0, 600, 0.1, 100)},
        {"perspective": (radians(60), 4.0 / 3.0, 0.1, 100)},
    ],
)
@pytest.mark.parametrize(
    "transform_kwargs",
    [
        {},
        {"transform": FMatrix4(1)},
        {"transform": FMatrix4(1).translate(FVector3(10, 20, 30))},
        {"transform": FMatrix4(1).scale(FVector3(2))},
    ],
)
def test_points(
    rectangle_frustum_cls,
    vector_3_cls,
    matrix_4_cls,
    vector_4_cls,
    transform_kwargs,
    projection_kwargs,
):
    try:
        transform = matrix_4_cls(*(vector_4_cls(*v) for v in transform_kwargs["transform"]))
        transform_kwargs["transform"] = transform
    except KeyError:
        transform = matrix_4_cls(1)
    if "orthographic" in projection_kwargs:
        projection = matrix_4_cls.orthographic(*projection_kwargs["orthographic"])
    else:
        projection = matrix_4_cls.perspective(*projection_kwargs["perspective"])
    frustum = rectangle_frustum_cls(**transform_kwargs, **projection_kwargs)
    points = frustum.points

    vp = (transform @ projection).inverse()

    def unproject(x: float, y: float, z: float):
        clip = vp @ vector_4_cls(x, y, z, 1)
        return clip.xyz / clip.w

    expected_points = (
        unproject(-1, -1, -1),
        unproject(1, -1, -1),
        unproject(-1, 1, -1),
        unproject(-1, -1, 1),
        unproject(1, 1, 1),
        unproject(-1, 1, 1),
        unproject(1, -1, 1),
        unproject(1, 1, -1),
    )

    assert points == expected_points
