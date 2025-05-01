
from emath import U8Array

def test_attrs(triangle_mesh_3d_cls, vector_3_array_cls, vector_3_cls):
    vertices = vector_3_array_cls(
        vector_3_cls(0, 0, 0),
        vector_3_cls(1, 0, 0),
        vector_3_cls(0, 1, 0),
    )
    indices = U8Array(0, 1, 2)
    trimesh = triangle_mesh_3d_cls(vertices, indices)
    assert trimesh.vertices is vertices
    assert trimesh.indices is indices
    assert list(trimesh.triangles) == [
        (
            vector_3_cls(0, 0, 0),
            vector_3_cls(1, 0, 0),
            vector_3_cls(0, 1, 0),
        ),
    ]

def test_raycast(triangle_mesh_3d_cls, vector_3_array_cls, vector_3_cls):
    vertices = vector_3_array_cls(
        vector_3_cls(0, 0, 0),
        vector_3_cls(1, 0, 0),
        vector_3_cls(0, 1, 0),
        vector_3_cls(0, 0, 1),
        vector_3_cls(.5, 0, 1),
        vector_3_cls(0, .5, 1),
    )
    indices = U8Array(0, 1, 2, 3, 4, 5)
    trimesh = triangle_mesh_3d_cls(vertices, indices)

    results = list(trimesh.raycast(vector_3_cls(0, 0, 0), vector_3_cls(0, 0, 1)))
    assert results == [
        (
            vector_3_cls(0, 0, 0),
            0,
            (vector_3_cls(0, 0, 0), vector_3_cls(1, 0, 0), vector_3_cls(0, 1, 0)),
        ),
        (
            vector_3_cls(0, 0, 1),
            1,
            (vector_3_cls(0, 0, 1), vector_3_cls(.5, 0, 1), vector_3_cls(0, .5, 1)),
        )
    ]

    results = list(trimesh.raycast(vector_3_cls(0, 0, 0), vector_3_cls(0, 0, -1)))
    assert results == [
        (
            vector_3_cls(0, 0, 0),
            0,
            (vector_3_cls(0, 0, 0), vector_3_cls(1, 0, 0), vector_3_cls(0, 1, 0)),
        )
    ]

    results = list(trimesh.raycast(vector_3_cls(0, 0, .5), vector_3_cls(0, 0, 1)))
    assert results == [
        (
            vector_3_cls(0, 0, 1),
            .5,
            (vector_3_cls(0, 0, 1), vector_3_cls(.5, 0, 1), vector_3_cls(0, .5, 1)),
        )
    ]

    results = list(trimesh.raycast(vector_3_cls(2, 0, 0), vector_3_cls(0, 0, 1)))
    assert results == []
