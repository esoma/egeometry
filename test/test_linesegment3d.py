import pytest


@pytest.mark.parametrize("a", [(0, 0, 0), (1, 2, 3), (-1, -2, -3)])
@pytest.mark.parametrize("b", [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1)])
def test_attrs(linesegment3d_cls, vector_3_cls, a, b):
    a_vec = vector_3_cls(*a)
    b_vec = vector_3_cls(*b)
    segment = linesegment3d_cls(a_vec, b_vec)
    assert segment.a == a_vec
    assert segment.b == b_vec
    assert segment.points == (a_vec, b_vec)
    assert repr(segment) == f"<LineSegment3d a={segment.a} b={segment.b}>"
    assert segment == segment


def test_not_equal(linesegment3d_cls, vector_3_cls):
    segment = linesegment3d_cls(vector_3_cls(0, 0, 0), vector_3_cls(1, 0, 0))
    assert segment != object()


@pytest.mark.parametrize(
    "a, b, expected_length",
    [
        ((0, 0, 0), (1, 0, 0), 1.0),
        ((0, 0, 0), (0, 1, 0), 1.0),
        ((0, 0, 0), (0, 0, 1), 1.0),
        ((0, 0, 0), (3, 4, 0), 5.0),
    ],
)
def test_length(linesegment3d_cls, vector_3_cls, a, b, expected_length):
    segment = linesegment3d_cls(vector_3_cls(*a), vector_3_cls(*b))
    assert segment.length == expected_length


@pytest.mark.parametrize(
    "a1, b1, a2, b2, expected_equal",
    [
        ((0, 0, 0), (1, 0, 0), (0, 0, 0), (1, 0, 0), True),
        ((0, 0, 0), (1, 0, 0), (1, 0, 0), (0, 0, 0), False),
        ((0, 0, 0), (1, 0, 0), (0, 0, 0), (2, 0, 0), False),
        ((1, 2, 3), (4, 5, 6), (1, 2, 3), (4, 5, 6), True),
    ],
)
def test_equality(linesegment3d_cls, vector_3_cls, a1, b1, a2, b2, expected_equal):
    segment1 = linesegment3d_cls(vector_3_cls(*a1), vector_3_cls(*b1))
    segment2 = linesegment3d_cls(vector_3_cls(*a2), vector_3_cls(*b2))
    assert (segment1 == segment2) == expected_equal
    assert (segment2 == segment1) == expected_equal


def test_degenerate_segment(linesegment3d_cls, vector_3_cls):
    with pytest.raises(ValueError) as excinfo:
        linesegment3d_cls(vector_3_cls(1, 2, 3), vector_3_cls(1, 2, 3))
    assert str(excinfo.value) == "line segment points must be different"
