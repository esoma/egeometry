# egeometry
from egeometry import separating_axis_theorem

# emath
from emath import DVector2
from emath import FVector2

# pytest
import pytest


@pytest.mark.parametrize("vector_2_cls", [FVector2, DVector2])
@pytest.mark.parametrize("axes_c", [1, -1])
@pytest.mark.parametrize(
    "axes_args, a_vertices_args, b_vertices_args, expected_result",
    [
        # simple aabb tests
        (
            [(1, 0), (0, 1)],
            [(0, 0), (0, 5), (5, 0), (5, 5)],
            [(6, 0), (6, 5), (11, 0), (11, 5)],
            False,
        ),
        (
            [(1, 0), (0, 1)],
            [(0, 0), (0, 5), (5, 0), (5, 5)],
            [(0, 0), (0, 5), (5, 0), (5, 5)],
            True,
        ),
        (
            [(1, 0), (0, 1)],
            [(0, 0), (0, 5), (5, 0), (5, 5)],
            [(5, 0), (5, 5), (10, 0), (10, 5)],
            True,
        ),
        (
            [(1, 0), (0, 1)],
            [(0, 0), (0, 5), (5, 0), (5, 5)],
            [(5, 0), (5, 5), (10, 0), (10, 5)],
            True,
        ),
        (
            [(1, 0), (0, 1)],
            [(0, 0), (0, 5), (5, 0), (5, 5)],
            [(0, 6), (0, 11), (5, 6), (5, 11)],
            False,
        ),
        (
            [(1, 0), (0, 1)],
            [(0, 0), (0, 5), (5, 0), (5, 5)],
            [(0, 5), (0, 10), (5, 5), (5, 10)],
            True,
        ),
        # aabb/triangle test
        (
            [(1, 0), (0, 1), (0.7071068286895752, 0.7071068286895752)],
            [(0, 0), (0, 5), (5, 0), (5, 5)],
            [(6, 0), (6, 5), (11, 0)],
            False,
        ),
        (
            [(1, 0), (0, 1), (0.7071068286895752, 0.7071068286895752)],
            [(0, 0), (0, 5), (5, 0), (5, 5)],
            [(5, 0), (5, 5), (10, 0)],
            True,
        ),
        (
            [
                (1, 0),
                (0.44721361994743347, -0.8944272398948669),
                (0.44721361994743347, 0.8944272398948669),
            ],
            [(0, 0), (0, 5), (5, 0), (5, 5)],
            [(6, 0), (6, 5), (11, 2.5)],
            False,
        ),
        (
            [
                (1, 0),
                (0.44721361994743347, -0.8944272398948669),
                (0.44721361994743347, 0.8944272398948669),
            ],
            [(0, 0), (0, 5), (5, 0), (5, 5)],
            [(5, 0), (5, 5), (10, 2.5)],
            True,
        ),
        (
            [
                (1, 0),
                (0.44721361994743347, -0.8944272398948669),
                (0.44721361994743347, 0.8944272398948669),
            ],
            [(0, 0), (0, 5), (5, 0), (5, 5)],
            [(-5, 0), (-5, 5), (0, 2.5)],
            True,
        ),
    ],
)
def test_separating_axis_theorem(
    vector_2_cls, axes_args, axes_c, a_vertices_args, b_vertices_args, expected_result
):
    axes = (vector_2_cls(*a) * axes_c for a in axes_args)
    a_vertices = tuple(vector_2_cls(*a) for a in a_vertices_args)
    b_vertices = tuple(vector_2_cls(*a) for a in b_vertices_args)
    assert separating_axis_theorem(axes, a_vertices, b_vertices) == expected_result
