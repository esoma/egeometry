import emath
import pytest

import egeometry


@pytest.fixture(params=["D", "F"])
def space_type(request):
    return request.param


@pytest.fixture(params=["U8", "U16", "U32", "U"])
def object_type(request):
    return request.param


@pytest.fixture(params=[2, 4, 8])
def child_count(request):
    return request.param


@pytest.fixture
def bvh_cls(space_type, object_type, child_count):
    return getattr(egeometry, f"{space_type}{object_type}BoundedVolumeHierarchy{child_count}")


@pytest.fixture
def vector_3_cls(space_type):
    return getattr(emath, f"{space_type}Vector3")


@pytest.fixture
def bounding_box_3d_cls(space_type):
    return getattr(egeometry, f"{space_type}BoundingBox3d")


def test_empty(bvh_cls, bounding_box_3d_cls):
    bvh = bvh_cls([])
    assert bvh.nodes == ()


def test_single_item(bvh_cls, bounding_box_3d_cls, vector_3_cls):
    bb = bounding_box_3d_cls(vector_3_cls(0, 0, 0), vector_3_cls(1, 1, 1))
    bvh = bvh_cls([bb])
    nodes = bvh.nodes
    assert len(nodes) == 1
    # single item should be a leaf
    assert len(nodes[0]) == 1
    assert nodes[0][0] == 0  # leaf with item index 0


def test_two_items(bvh_cls, bounding_box_3d_cls, vector_3_cls):
    bb1 = bounding_box_3d_cls(vector_3_cls(0, 0, 0), vector_3_cls(1, 1, 1))
    bb2 = bounding_box_3d_cls(vector_3_cls(2, 0, 0), vector_3_cls(1, 1, 1))
    bvh = bvh_cls([bb1, bb2])
    nodes = bvh.nodes
    assert len(nodes) >= 1
    # should have leaves for both items
    all_leaves = []
    for node in nodes:
        for child in node:
            if isinstance(child, int):
                all_leaves.append(child)
    assert set(all_leaves) == {0, 1}


def test_multiple_items(bvh_cls, bounding_box_3d_cls, vector_3_cls):
    items = [
        bounding_box_3d_cls(vector_3_cls(i * 2, 0, 0), vector_3_cls(1, 1, 1)) for i in range(10)
    ]
    bvh = bvh_cls(items)
    nodes = bvh.nodes
    assert len(nodes) >= 1
    # collect all leaf indices
    all_leaves = []
    for node in nodes:
        for child in node:
            if isinstance(child, int):
                all_leaves.append(child)
    assert set(all_leaves) == set(range(10))


def test_invalid_items_type(bvh_cls):
    with pytest.raises(TypeError):
        bvh_cls(object())


def test_invalid_item_type(bvh_cls):
    with pytest.raises(AttributeError):
        bvh_cls([1, 2, 3])


def test_too_many_items_u8(space_type, child_count, bounding_box_3d_cls, vector_3_cls):
    bvh_cls = getattr(egeometry, f"{space_type}U8BoundedVolumeHierarchy{child_count}")
    items = [bounding_box_3d_cls(vector_3_cls(i, 0, 0), vector_3_cls(1, 1, 1)) for i in range(129)]
    with pytest.raises(ValueError) as excinfo:
        bvh_cls(items)
    assert "too many items" in str(excinfo.value)


def test_too_many_items_u16(space_type, child_count, bounding_box_3d_cls, vector_3_cls):
    bvh_cls = getattr(egeometry, f"{space_type}U16BoundedVolumeHierarchy{child_count}")
    items = [
        bounding_box_3d_cls(vector_3_cls(i, 0, 0), vector_3_cls(1, 1, 1)) for i in range(32769)
    ]
    with pytest.raises(ValueError) as excinfo:
        bvh_cls(items)
    assert "too many items" in str(excinfo.value)


def test_node_children_are_valid(bvh_cls, bounding_box_3d_cls, vector_3_cls):
    items = [
        bounding_box_3d_cls(vector_3_cls(i * 2, j * 2, k * 2), vector_3_cls(1, 1, 1))
        for i in range(3)
        for j in range(3)
        for k in range(3)
    ]
    bvh = bvh_cls(items)
    nodes = bvh.nodes

    for node_idx, node in enumerate(nodes):
        for child in node:
            if isinstance(child, int):
                # leaf - index should be valid
                assert 0 <= child < len(items)
            else:
                # internal node - should be (BoundingBox3d, node_index) tuple
                assert isinstance(child, tuple)
                assert len(child) == 2
                bbox, child_node_idx = child
                assert isinstance(child_node_idx, int)
                assert 0 <= child_node_idx < len(nodes)


def test_raycast_hit_single(bvh_cls, bounding_box_3d_cls, vector_3_cls):
    bb = bounding_box_3d_cls(vector_3_cls(0, 0, 0), vector_3_cls(2, 2, 2))
    bvh = bvh_cls([bb])

    hits = list(bvh.raycast(vector_3_cls(-1, 1, 1), vector_3_cls(1, 0, 0)))
    assert hits == [0]


def test_raycast_miss_single(bvh_cls, bounding_box_3d_cls, vector_3_cls):
    bb = bounding_box_3d_cls(vector_3_cls(0, 0, 0), vector_3_cls(2, 2, 2))
    bvh = bvh_cls([bb])

    hits = list(bvh.raycast(vector_3_cls(-1, 10, 1), vector_3_cls(1, 0, 0)))
    assert hits == []


def test_raycast_multiple_hits(bvh_cls, bounding_box_3d_cls, vector_3_cls):
    items = [
        bounding_box_3d_cls(vector_3_cls(0, 0, 0), vector_3_cls(1, 1, 1)),
        bounding_box_3d_cls(vector_3_cls(2, 0, 0), vector_3_cls(1, 1, 1)),
        bounding_box_3d_cls(vector_3_cls(4, 0, 0), vector_3_cls(1, 1, 1)),
    ]
    bvh = bvh_cls(items)

    hits = list(bvh.raycast(vector_3_cls(-1, 0.5, 0.5), vector_3_cls(1, 0, 0)))
    assert set(hits) == {0, 1, 2}


def test_raycast_partial_hits(bvh_cls, bounding_box_3d_cls, vector_3_cls):
    items = [
        bounding_box_3d_cls(vector_3_cls(0, 0, 0), vector_3_cls(1, 1, 1)),
        bounding_box_3d_cls(vector_3_cls(2, 5, 0), vector_3_cls(1, 1, 1)),
        bounding_box_3d_cls(vector_3_cls(4, 0, 0), vector_3_cls(1, 1, 1)),
    ]
    bvh = bvh_cls(items)

    hits = list(bvh.raycast(vector_3_cls(-1, 0.5, 0.5), vector_3_cls(1, 0, 0)))
    assert set(hits) == {0, 2}


def test_raycast_empty_bvh(bvh_cls, bounding_box_3d_cls, vector_3_cls):
    bvh = bvh_cls([])
    hits = list(bvh.raycast(vector_3_cls(0, 0, 0), vector_3_cls(1, 0, 0)))
    assert hits == []


def test_raycast_from_inside(bvh_cls, bounding_box_3d_cls, vector_3_cls):
    bb = bounding_box_3d_cls(vector_3_cls(0, 0, 0), vector_3_cls(2, 2, 2))
    bvh = bvh_cls([bb])
    hits = list(bvh.raycast(vector_3_cls(1, 1, 1), vector_3_cls(1, 0, 0)))
    assert hits == [0]


def test_raycast_diagonal(bvh_cls, bounding_box_3d_cls, vector_3_cls):
    items = [
        bounding_box_3d_cls(vector_3_cls(0, 0, 0), vector_3_cls(1, 1, 1)),
        bounding_box_3d_cls(vector_3_cls(2, 2, 2), vector_3_cls(1, 1, 1)),
    ]
    bvh = bvh_cls(items)
    hits = list(bvh.raycast(vector_3_cls(-1, -1, -1), vector_3_cls(1, 1, 1)))
    assert set(hits) == {0, 1}


def test_raycast_backwards(bvh_cls, bounding_box_3d_cls, vector_3_cls):
    bb = bounding_box_3d_cls(vector_3_cls(0, 0, 0), vector_3_cls(2, 2, 2))
    bvh = bvh_cls([bb])
    hits = list(bvh.raycast(vector_3_cls(-1, 1, 1), vector_3_cls(-1, 0, 0)))
    assert hits == []


def test_raycast_parallel_miss(bvh_cls, bounding_box_3d_cls, vector_3_cls):
    bb = bounding_box_3d_cls(vector_3_cls(0, 0, 0), vector_3_cls(2, 2, 2))
    bvh = bvh_cls([bb])
    hits = list(bvh.raycast(vector_3_cls(-1, -1, 1), vector_3_cls(1, 0, 0)))
    assert hits == []


def test_raycast_wrong_eye_type(bvh_cls, bounding_box_3d_cls, vector_3_cls):
    bb = bounding_box_3d_cls(vector_3_cls(0, 0, 0), vector_3_cls(1, 1, 1))
    bvh = bvh_cls([bb])
    with pytest.raises(TypeError):
        list(bvh.raycast("not a vector", vector_3_cls(1, 0, 0)))


def test_raycast_wrong_direction_type(bvh_cls, bounding_box_3d_cls, vector_3_cls):
    bb = bounding_box_3d_cls(vector_3_cls(0, 0, 0), vector_3_cls(1, 1, 1))
    bvh = bvh_cls([bb])
    with pytest.raises(TypeError):
        list(bvh.raycast(vector_3_cls(0, 0, 0), "not a vector"))


def test_raycast_wrong_arg_count(bvh_cls, bounding_box_3d_cls, vector_3_cls):
    bb = bounding_box_3d_cls(vector_3_cls(0, 0, 0), vector_3_cls(1, 1, 1))
    bvh = bvh_cls([bb])
    with pytest.raises(TypeError):
        list(bvh.raycast(vector_3_cls(0, 0, 0)))
    with pytest.raises(TypeError):
        list(bvh.raycast())


def test_raycast_generator_behavior(bvh_cls, bounding_box_3d_cls, vector_3_cls):
    items = [
        bounding_box_3d_cls(vector_3_cls(i * 2, 0, 0), vector_3_cls(1, 1, 1)) for i in range(5)
    ]
    bvh = bvh_cls(items)

    gen = bvh.raycast(vector_3_cls(-1, 0.5, 0.5), vector_3_cls(1, 0, 0))

    first = next(gen)
    assert first in range(5)

    remaining = list(gen)
    assert len(remaining) == 4

    with pytest.raises(StopIteration):
        next(gen)


def test_many_items(bvh_cls, bounding_box_3d_cls, vector_3_cls):
    """Test with a larger number of items"""
    items = [
        bounding_box_3d_cls(
            vector_3_cls(i % 10 * 2, (i // 10) % 10 * 2, i // 100 * 2), vector_3_cls(1, 1, 1)
        )
        for i in range(100)
    ]
    bvh = bvh_cls(items)

    all_leaves = []
    for node in bvh.nodes:
        for child in node:
            if isinstance(child, int):
                all_leaves.append(child)
    assert set(all_leaves) == set(range(100))


def test_raycast_many_items(bvh_cls, bounding_box_3d_cls, vector_3_cls):
    items = [
        bounding_box_3d_cls(vector_3_cls(i * 2, 0, 0), vector_3_cls(1, 1, 1)) for i in range(50)
    ]
    bvh = bvh_cls(items)

    hits = list(bvh.raycast(vector_3_cls(-1, 0.5, 0.5), vector_3_cls(1, 0, 0)))
    assert set(hits) == set(range(50))
