
import pytest
from math import radians
from emath import FMatrix4

@pytest.mark.parametrize("projection_kwargs", [
    {"orthographic": (0, 800, 0, 600, .1, 100)},
    {"perspective": (radians(60), 4.0 / 3.0, .1, 100)}
])
@pytest.mark.parametrize("transform_kwargs", [
    {},
    {"transform": FMatrix4(1)},
])
def test_attrs(rectangle_frustum_cls, plane_cls, vector_4_cls, matrix_4_cls, transform_kwargs, projection_kwargs):
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

    r = [(transform @ projection).get_row(i) for i in range(4)]
    near_plane = plane_cls(r[3].w + r[2].w, r[3].xyz + r[2].xyz)
    far_plane = plane_cls(r[3].w - r[2].w, r[3].xyz - r[2].xyz)
    left_plane = plane_cls(r[3].w + r[0].w, r[3].xyz + r[0].xyz)
    right_plane = plane_cls(r[3].w - r[0].w, r[3].xyz - r[0].xyz)
    bottom_plane = plane_cls(r[3].w + r[1].w, r[3].xyz + r[1].xyz)
    top_plane = plane_cls(r[3].w - r[1].w, r[3].xyz - r[1].xyz)

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
        bottom_plane
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
    assert str(excinfo.value) == "either orthographic or perspective must be specified, but not both"

def test_double_projection(rectangle_frustum_cls):
    with pytest.raises(TypeError) as excinfo:
        rectangle_frustum_cls(
            orthographic=(0, 800, 0, 600, .1, 100),
            perspective=(radians(60), 4.0 / 3.0, .1, 100)
        )
    assert str(excinfo.value) == "either orthographic or perspective must be specified"

def test_not_equal(rectangle_frustum_cls):
    frustum = rectangle_frustum_cls(orthographic=(0, 800, 0, 600, .1, 100))
    assert frustum != object()
