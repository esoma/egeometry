
// generated from codegen/templates/_boundedvolumehierarchy.hpp

#ifndef EGEOMETRY_DUBOUNDEDVOLUMEHIERARCHY8_HPP
#define EGEOMETRY_DUBOUNDEDVOLUMEHIERARCHY8_HPP

#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include "structmember.h"

#include <cassert>
#include <limits.h>
#include <limits>
#include <string.h>

#include "_duboundedvolumehierarchy8type.hpp"
#include "_modulestate.hpp"

static const unsigned int DUBoundedVolumeHierarchy8_LEAF_MASK (unsigned int(1) << (sizeof(unsigned int) * 8 - 1));

struct DUBoundedVolumeHierarchy8Items
{
    size_t count;
    double *min_x;
    double *min_y;
    double *min_z;
    double *max_x;
    double *max_y;
    double *max_z;
};


static DUBoundedVolumeHierarchy8Items
DUBoundedVolumeHierarchy8_alloc_items_from_py_sequence_bounding_box_3d(
    PyObject *py_items
)
{
    char *item_data = 0;
    PyObject *py_item = 0;
    PyObject *py_position = 0;
    PyObject *py_extent = 0;
    DUBoundedVolumeHierarchy8Items items;
    items.count = 0;
    items.min_x = 0;

    ModuleState *module_state = get_module_state();
    if (!module_state){ goto error; }
    auto get_vector_ptr = module_state->emath_api->DVector3_GetValuePointer;

    if (!PySequence_Check(py_items))
    {
        PyErr_SetString(PyExc_TypeError, "expected a sequence for items argument");
        goto error;
    }
    Py_ssize_t item_count = PySequence_Size(py_items);
    if (item_count < 0){ goto error; }

    if (item_count == 0)
    {
        item_data = (char *)malloc(1);
    }
    else
    {
        item_data = (char *)malloc(sizeof(double) * 6 * item_count);
    }
    if (!item_data){ PyErr_NoMemory(); goto error; }

    items.count = (size_t)item_count;
    items.min_x = (double*)(item_data + (size_t)(sizeof(double) * item_count * 0));
    items.min_y = (double*)(item_data + (size_t)(sizeof(double) * item_count * 1));
    items.min_z = (double*)(item_data + (size_t)(sizeof(double) * item_count * 2));
    items.max_x = (double*)(item_data + (size_t)(sizeof(double) * item_count * 3));
    items.max_y = (double*)(item_data + (size_t)(sizeof(double) * item_count * 4));
    items.max_z = (double*)(item_data + (size_t)(sizeof(double) * item_count * 5));

    for (Py_ssize_t i = 0; i < item_count; i++)
    {
        py_item = PySequence_GetItem(py_items, i);
        if (!py_item){ goto error; }

        py_position = PyObject_GetAttrString(py_item, "position");
        if (!py_position){ goto error;}
        py_extent = PyObject_GetAttrString(py_item, "extent");
        if (!py_extent){ goto error; }

        auto *position_ptr = (double *)get_vector_ptr(py_position);
        auto *extent_ptr = (double *)get_vector_ptr(py_extent);

        if (!position_ptr || !extent_ptr){ goto error; }

        items.min_x[i] = position_ptr[0];
        items.min_y[i] = position_ptr[1];
        items.min_z[i] = position_ptr[2];
        items.max_x[i] = extent_ptr[0];
        items.max_y[i] = extent_ptr[1];
        items.max_z[i] = extent_ptr[2];

        Py_DECREF(py_position);
        py_position = 0;
        Py_DECREF(py_extent);
        py_extent = 0;
        Py_DECREF(py_item);
        py_item = 0;
    }

    return items;

error:
    Py_XDECREF(py_item);
    Py_XDECREF(py_position);
    Py_XDECREF(py_extent);
    if (item_data){ free(item_data); }
    items.min_x = 0;
    return items;
}

static void
DUBoundedVolumeHierarchy8_free_items(DUBoundedVolumeHierarchy8Items items)
{
    if (items.min_x == 0)
    {
        free(items.min_x);
        items.min_x = 0;
    }
}


static void
DUBoundedVolumeHierarchy8_alloc_nodes(
    DUBoundedVolumeHierarchy8Items items,
    DUBoundedVolumeHierarchy8Node **nodes,
    size_t *node_count
)
{
    if (items.count == 0)
    {
        *nodes = (DUBoundedVolumeHierarchy8Node *)malloc(1);
        if (!nodes)
        {
            PyErr_NoMemory();
            return;
        }
        *node_count = 0;
        return;
    }

    // check that item_count can be addressed by unsigned int accounting for LEAF_MASK
    // LEAF_MASK uses the highest bit, so max item count is ~LEAF_MASK + 1 (indices 0 to ~LEAF_MASK)
    // cast to unsigned int to avoid integer promotion issues with ~ operator
    size_t max_item_count = (size_t)(unsigned int)(~DUBoundedVolumeHierarchy8_LEAF_MASK) + 1;
    if (items.count > max_item_count)
    {
        PyErr_Format(PyExc_ValueError, "too many items (max: %zu)", max_item_count);
        *nodes = 0;
        return;
    }

    unsigned int *item_indices = 0;
    double *center_x = 0;
    double *center_y = 0;
    double *center_z = 0;
    DUBoundedVolumeHierarchy8Node *node_array = 0;

    // stack for iterative depth-first tree building
    // each task stores: node_index, child_slot, start, end
    // child_slot indicates which child slot to fill when we return
    struct BuildTask {
        size_t node_index;
        int child_slot;
        size_t start;
        size_t end;
        size_t partition_points[8 + 1];
    };
    size_t stack_capacity = 64;
    size_t stack_size = 0;
    BuildTask *stack = 0;

    // allocate item indices for sorting/partitioning
    item_indices = (unsigned int *)malloc(sizeof(unsigned int) * items.count);
    if (!item_indices){ PyErr_NoMemory(); goto error; }
    for (size_t i = 0; i < items.count; i++)
    {
        item_indices[i] = (unsigned int)i;
    }

    // calculate item centers for partitioning
    center_x = (double *)malloc(sizeof(double) * items.count);
    if (!center_x){ PyErr_NoMemory(); goto error; }
    center_y = (double *)malloc(sizeof(double) * items.count);
    if (!center_y){ PyErr_NoMemory(); goto error; }
    center_z = (double *)malloc(sizeof(double) * items.count);
    if (!center_z){ PyErr_NoMemory(); goto error; }
    for (size_t i = 0; i < items.count; i++)
    {
        center_x[i] = (items.min_x[i] + items.max_x[i]) * double(0.5);
        center_y[i] = (items.min_y[i] + items.max_y[i]) * double(0.5);
        center_z[i] = (items.min_z[i] + items.max_z[i]) * double(0.5);
    }

    // estimate max nodes: for n items with branching factor b, max nodes ~ n/(b-1) + 1
    // use a conservative estimate
    size_t node_array_count = items.count + 1;
    // if item count fits, node count must too (nodes <= items)
    assert(node_array_count <= (size_t)std::numeric_limits<unsigned int>::max() + 1);
    {
        node_array = (DUBoundedVolumeHierarchy8Node *)malloc(sizeof(DUBoundedVolumeHierarchy8Node) * node_array_count);
        if (!node_array){ PyErr_NoMemory(); goto error; }
        memset(node_array, 0, sizeof(DUBoundedVolumeHierarchy8Node) * node_array_count);
    }

    stack = (BuildTask *)malloc(sizeof(BuildTask) * stack_capacity);
    if (!stack){ PyErr_NoMemory(); goto error; }

    {
        size_t next_node = 0;

        // helper to push a build task
        auto push_task = [&](size_t node_idx, int child_slot, size_t start, size_t end) -> bool
        {
            if (stack_size >= stack_capacity)
            {
                size_t new_capacity = stack_capacity * 2;
                BuildTask *new_stack = (BuildTask *)realloc(stack, sizeof(BuildTask) * new_capacity);
                if (!new_stack){ PyErr_NoMemory(); return false; }
                stack = new_stack;
                stack_capacity = new_capacity;
            }
            stack[stack_size].node_index = node_idx;
            stack[stack_size].child_slot = child_slot;
            stack[stack_size].start = start;
            stack[stack_size].end = end;
            stack_size++;
            return true;
        };

        // helper to partition items into 8 groups
        auto partition_items = [&](size_t start, size_t end, size_t *partition_points)
        {
            partition_points[0] = start;
            partition_points[8] = end;

            struct PartitionTask {
                size_t start;
                size_t end;
                int level;
                int group_start;
            };

            PartitionTask part_stack[16];
            int part_stack_size = 0;
            part_stack[part_stack_size++] = {start, end, 0, 0};


            int levels_needed = 3;


            while (part_stack_size > 0)
            {
                PartitionTask pt = part_stack[--part_stack_size];

                if (pt.level >= levels_needed || pt.end - pt.start <= 1)
                {
                    int groups_at_level = 1 << pt.level;
                    int group_size = 8 / groups_at_level;
                    for (int g = 0; g < group_size; g++)
                    {
                        int group_idx = pt.group_start + g;
                        if (group_idx > 0)
                        {
                            partition_points[group_idx] = pt.start;
                        }
                    }
                    continue;
                }

                double min_cx = center_x[item_indices[pt.start]];
                double max_cx = center_x[item_indices[pt.start]];
                double min_cy = center_y[item_indices[pt.start]];
                double max_cy = center_y[item_indices[pt.start]];
                double min_cz = center_z[item_indices[pt.start]];
                double max_cz = center_z[item_indices[pt.start]];

                for (size_t i = pt.start + 1; i < pt.end; i++)
                {
                    unsigned int idx = item_indices[i];
                    if (center_x[idx] < min_cx) min_cx = center_x[idx];
                    if (center_x[idx] > max_cx) max_cx = center_x[idx];
                    if (center_y[idx] < min_cy) min_cy = center_y[idx];
                    if (center_y[idx] > max_cy) max_cy = center_y[idx];
                    if (center_z[idx] < min_cz) min_cz = center_z[idx];
                    if (center_z[idx] > max_cz) max_cz = center_z[idx];
                }

                double extent_x = max_cx - min_cx;
                double extent_y = max_cy - min_cy;
                double extent_z = max_cz - min_cz;

                double *centers = center_x;
                if (extent_y > extent_x && extent_y >= extent_z)
                {
                    centers = center_y;
                }
                else if (extent_z > extent_x && extent_z > extent_y)
                {
                    centers = center_z;
                }

                size_t mid = pt.start + (pt.end - pt.start) / 2;
                double pivot_val = centers[item_indices[mid]];
                size_t left = pt.start;
                size_t right = pt.end - 1;

                while (left < right)
                {
                    while (left < right && centers[item_indices[left]] < pivot_val) left++;
                    while (left < right && centers[item_indices[right]] >= pivot_val) right--;
                    if (left < right)
                    {
                        unsigned int tmp = item_indices[left];
                        item_indices[left] = item_indices[right];
                        item_indices[right] = tmp;
                    }
                }

                if (left == pt.start) left = pt.start + 1;
                if (left == pt.end) left = pt.end - 1;
                mid = left;

                int groups_at_level = 1 << (pt.level + 1);
                int group_size = 8 / groups_at_level;
                int mid_group = pt.group_start + group_size;
                partition_points[mid_group] = mid;

                part_stack[part_stack_size++] = {mid, pt.end, pt.level + 1, mid_group};
                part_stack[part_stack_size++] = {pt.start, mid, pt.level + 1, pt.group_start};
            }
        };

        // helper to fill a child slot
        auto fill_child = [&](size_t node_idx, int c, size_t child_start, size_t child_end) -> bool
        {
            size_t child_count_items = child_end - child_start;

            if (child_count_items == 0)
            {
                node_array[node_idx].min_x[c] = double(1);
                node_array[node_idx].max_x[c] = double(-1);
                node_array[node_idx].min_y[c] = double(1);
                node_array[node_idx].max_y[c] = double(-1);
                node_array[node_idx].min_z[c] = double(1);
                node_array[node_idx].max_z[c] = double(-1);
                node_array[node_idx].child[c] = 0;
                return true;
            }
            else if (child_count_items == 1)
            {
                unsigned int item_idx = item_indices[child_start];
                node_array[node_idx].min_x[c] = items.min_x[item_idx];
                node_array[node_idx].min_y[c] = items.min_y[item_idx];
                node_array[node_idx].min_z[c] = items.min_z[item_idx];
                node_array[node_idx].max_x[c] = items.max_x[item_idx];
                node_array[node_idx].max_y[c] = items.max_y[item_idx];
                node_array[node_idx].max_z[c] = items.max_z[item_idx];
                node_array[node_idx].child[c] = item_idx | DUBoundedVolumeHierarchy8_LEAF_MASK;
                return true;
            }
            else
            {
                double min_x = items.min_x[item_indices[child_start]];
                double max_x = items.max_x[item_indices[child_start]];
                double min_y = items.min_y[item_indices[child_start]];
                double max_y = items.max_y[item_indices[child_start]];
                double min_z = items.min_z[item_indices[child_start]];
                double max_z = items.max_z[item_indices[child_start]];

                for (size_t i = child_start + 1; i < child_end; i++)
                {
                    unsigned int idx = item_indices[i];
                    if (items.min_x[idx] < min_x) min_x = items.min_x[idx];
                    if (items.max_x[idx] > max_x) max_x = items.max_x[idx];
                    if (items.min_y[idx] < min_y) min_y = items.min_y[idx];
                    if (items.max_y[idx] > max_y) max_y = items.max_y[idx];
                    if (items.min_z[idx] < min_z) min_z = items.min_z[idx];
                    if (items.max_z[idx] > max_z) max_z = items.max_z[idx];
                }

                node_array[node_idx].min_x[c] = min_x;
                node_array[node_idx].max_x[c] = max_x;
                node_array[node_idx].min_y[c] = min_y;
                node_array[node_idx].max_y[c] = max_y;
                node_array[node_idx].min_z[c] = min_z;
                node_array[node_idx].max_z[c] = max_z;

                // child node will be allocated next (depth-first)
                // we'll set the child pointer when we process it
                return false;  // indicates needs recursion
            }
        };

        // create root node and push initial task
        size_t root_node = next_node++;
        if (!push_task(root_node, 0, 0, items.count)){ goto error; }
        partition_items(0, items.count, stack[0].partition_points);

        while (stack_size > 0)
        {
            BuildTask *task = &stack[stack_size - 1];
            size_t node_idx = task->node_index;
            int c = task->child_slot;

            // find next child that needs processing
            while (c < 8)
            {
                size_t child_start = task->partition_points[c];
                size_t child_end = task->partition_points[c + 1];

                if (!fill_child(node_idx, c, child_start, child_end))
                {
                    // needs recursion - allocate child node and descend
                    size_t child_node = next_node++;
                    node_array[node_idx].child[c] = (unsigned int)child_node;

                    // save current progress
                    task->child_slot = c + 1;

                    // push new task for child
                    if (!push_task(child_node, 0, child_start, child_end)){ goto error; }
                    partition_items(child_start, child_end, stack[stack_size - 1].partition_points);

                    // break to process child first (depth-first)
                    goto next_iteration;
                }
                c++;
            }

            // all children processed, pop this task
            stack_size--;

            next_iteration:;
        }

        // shrink node array to actual size
        if (next_node < node_array_count)
        {
            DUBoundedVolumeHierarchy8Node *shrunk = (DUBoundedVolumeHierarchy8Node *)realloc(node_array, sizeof(DUBoundedVolumeHierarchy8Node) * next_node);
            if (!shrunk){ PyErr_NoMemory(); goto error; }
            node_array = shrunk;
            node_array_count = next_node;
        }
    }

    free(item_indices);
    free(center_x);
    free(center_y);
    free(center_z);
    free(stack);

    *nodes = node_array;
    *node_count = node_array_count;
    return;

error:
    if (item_indices) free(item_indices);
    if (center_x) free(center_x);
    if (center_y) free(center_y);
    if (center_z) free(center_z);
    if (node_array) free(node_array);
    if (stack) free(stack);
    *nodes = 0;
}

static void
DUBoundedVolumeHierarchy8_free_nodes(DUBoundedVolumeHierarchy8Node *nodes)
{
    if (nodes)
    {
        free(nodes);
    }
}


static PyObject *
DUBoundedVolumeHierarchy8__new__(PyTypeObject *cls, PyObject *args, PyObject *kwds)
{
    DUBoundedVolumeHierarchy8 *self = 0;
    DUBoundedVolumeHierarchy8Node *nodes = 0;

    static const char *kwp[] = {"items", 0};
    PyObject *py_items = 0;
    if (!PyArg_ParseTupleAndKeywords(args, kwds, "O", (char **)kwp, &py_items)){ return 0; }

    DUBoundedVolumeHierarchy8Items items = DUBoundedVolumeHierarchy8_alloc_items_from_py_sequence_bounding_box_3d(py_items);
    if (items.min_x == 0){ goto error; }

    size_t node_count;
    DUBoundedVolumeHierarchy8_alloc_nodes(items, &nodes, &node_count);
    if (!nodes && items.count > 0){ goto error; }

    DUBoundedVolumeHierarchy8_free_items(items);

    self = (DUBoundedVolumeHierarchy8*)cls->tp_alloc(cls, 0);
    if (!self)
    {
        goto error;
    }

    self->nodes = nodes;
    self->node_count = node_count;

    return (PyObject *)self;
error:
    DUBoundedVolumeHierarchy8_free_nodes(nodes);
    DUBoundedVolumeHierarchy8_free_items(items);
    return 0;
}

static void
DUBoundedVolumeHierarchy8__dealloc__(DUBoundedVolumeHierarchy8 *self)
{
    if (self->weakreflist)
    {
        PyObject_ClearWeakRefs((PyObject *)self);
    }

    if (self->nodes)
    {
        free(self->nodes);
        self->nodes = 0;
    }

    PyTypeObject *type = Py_TYPE(self);
    type->tp_free(self);
    Py_DECREF(type);
}

static PyObject *
DUBoundedVolumeHierarchy8__repr__(DUBoundedVolumeHierarchy8 *self)
{
    return PyUnicode_FromFormat(
        "<DUBoundedVolumeHierarchy8>"
    );
}


static PyObject *
DUBoundedVolumeHierarchy8_nodes(DUBoundedVolumeHierarchy8 *self, void *closure)
{
    PyObject *bbox_cls = 0;
    PyObject *result = 0;
    PyObject *node_tuple = 0;
    PyObject *position = 0;
    PyObject *size = 0;
    PyObject *bbox = 0;
    PyObject *node_idx_py = 0;
    PyObject *child_tuple = 0;

    ModuleState *module_state = get_module_state();
    if (!module_state){ return 0; }

    PyObject *egeometry = PyImport_ImportModule("egeometry");
    if (!egeometry){ return 0; }

    bbox_cls = PyObject_GetAttrString(egeometry, "DBoundingBox3d");
    Py_DECREF(egeometry);
    if (!bbox_cls){ goto error; }

    auto vector_create = module_state->emath_api->DVector3_Create;

    result = PyTuple_New((Py_ssize_t)self->node_count);
    if (!result){ goto error; }

    for (size_t n = 0; n < self->node_count; n++)
    {
        DUBoundedVolumeHierarchy8Node *node = &self->nodes[n];

        // count non-empty children
        Py_ssize_t child_count = 0;
        for (int c = 0; c < 8; c++)
        {
            // empty slots have min > max (invalid bounds)
            if (node->min_x[c] <= node->max_x[c])
            {
                child_count++;
            }
        }

        node_tuple = PyTuple_New(child_count);
        if (!node_tuple){ goto error; }

        Py_ssize_t child_idx = 0;
        for (int c = 0; c < 8; c++)
        {
            // skip empty slots
            if (node->min_x[c] > node->max_x[c])
            {
                continue;
            }

            unsigned int child_val = node->child[c];

            if (child_val & DUBoundedVolumeHierarchy8_LEAF_MASK)
            {
                // leaf node - just emit the item index
                unsigned int item_idx = child_val & ~DUBoundedVolumeHierarchy8_LEAF_MASK;
                PyObject *py_item_idx = PyLong_FromUnsignedLong((unsigned long)item_idx);
                if (!py_item_idx){ goto error; }
                PyTuple_SET_ITEM(node_tuple, child_idx, py_item_idx);
            }
            else
            {
                // internal node - emit (BoundingBox3d, node_index)
                double position_data[3] = {
                    node->min_x[c],
                    node->min_y[c],
                    node->min_z[c]
                };
                position = vector_create(position_data);
                if (!position){ goto error; }

                double size_data[3] = {
                    node->max_x[c] - node->min_x[c],
                    node->max_y[c] - node->min_y[c],
                    node->max_z[c] - node->min_z[c]
                };
                size = vector_create(size_data);
                if (!size){ goto error; }

                bbox = PyObject_CallFunctionObjArgs(bbox_cls, position, size, NULL);
                Py_CLEAR(position);
                Py_CLEAR(size);
                if (!bbox){ goto error; }

                node_idx_py = PyLong_FromSize_t((size_t)child_val);
                if (!node_idx_py){ goto error; }

                child_tuple = PyTuple_Pack(2, bbox, node_idx_py);
                Py_CLEAR(bbox);
                Py_CLEAR(node_idx_py);
                if (!child_tuple){ goto error; }

                PyTuple_SET_ITEM(node_tuple, child_idx, child_tuple);
                child_tuple = 0;
            }
            child_idx++;
        }

        PyTuple_SET_ITEM(result, (Py_ssize_t)n, node_tuple);
        node_tuple = 0;
    }

    Py_DECREF(bbox_cls);
    return result;

error:
    Py_XDECREF(bbox_cls);
    Py_XDECREF(result);
    Py_XDECREF(node_tuple);
    Py_XDECREF(position);
    Py_XDECREF(size);
    Py_XDECREF(bbox);
    Py_XDECREF(node_idx_py);
    Py_XDECREF(child_tuple);
    return 0;
}

// Raycast iterator type
struct DUBoundedVolumeHierarchy8RaycastIterator
{
    PyObject_HEAD
    DUBoundedVolumeHierarchy8 *bvh;
    double eye[3];
    double inv_dir[3];
    // traversal stack: each entry is a node index
    unsigned int *stack;
    size_t stack_size;
    size_t stack_capacity;
    // hits for current node (children that passed AABB test)
    unsigned int hits[8];
    int hit_count;
    int hit_index;
};

static void
DUBoundedVolumeHierarchy8RaycastIterator__dealloc__(DUBoundedVolumeHierarchy8RaycastIterator *self)
{
    Py_XDECREF(self->bvh);
    if (self->stack)
    {
        free(self->stack);
    }
    PyTypeObject *type = Py_TYPE(self);
    type->tp_free(self);
    Py_DECREF(type);
}

static inline void
DUBoundedVolumeHierarchy8_ray_test_node(
    const double *eye,
    const double *inv_dir,
    const DUBoundedVolumeHierarchy8Node *node,
    unsigned int *hits,
    int *hit_count
)
{
    // test all 8 children simultaneously
    // this layout allows the compiler to auto-vectorize

    double t_min[8];
    double t_max[8];

    // initialize t_min/t_max with x-axis slab
    for (int c = 0; c < 8; c++)
    {
        double t1 = (node->min_x[c] - eye[0]) * inv_dir[0];
        double t2 = (node->max_x[c] - eye[0]) * inv_dir[0];
        t_min[c] = t1 < t2 ? t1 : t2;
        t_max[c] = t1 > t2 ? t1 : t2;
    }

    // intersect with y-axis slab
    for (int c = 0; c < 8; c++)
    {
        double t1 = (node->min_y[c] - eye[1]) * inv_dir[1];
        double t2 = (node->max_y[c] - eye[1]) * inv_dir[1];
        double t_min_y = t1 < t2 ? t1 : t2;
        double t_max_y = t1 > t2 ? t1 : t2;
        t_min[c] = t_min_y > t_min[c] ? t_min_y : t_min[c];
        t_max[c] = t_max_y < t_max[c] ? t_max_y : t_max[c];
    }

    // intersect with z-axis slab
    for (int c = 0; c < 8; c++)
    {
        double t1 = (node->min_z[c] - eye[2]) * inv_dir[2];
        double t2 = (node->max_z[c] - eye[2]) * inv_dir[2];
        double t_min_z = t1 < t2 ? t1 : t2;
        double t_max_z = t1 > t2 ? t1 : t2;
        t_min[c] = t_min_z > t_min[c] ? t_min_z : t_min[c];
        t_max[c] = t_max_z < t_max[c] ? t_max_z : t_max[c];
    }

    // collect hits (valid intersection and not empty slot)
    *hit_count = 0;
    for (int c = 0; c < 8; c++)
    {
        // skip empty slots (min > max indicates invalid/empty)
        if (node->min_x[c] > node->max_x[c]) continue;

        if (t_max[c] >= t_min[c] && t_max[c] >= double(0))
        {
            hits[(*hit_count)++] = node->child[c];
        }
    }
}

static PyObject *
DUBoundedVolumeHierarchy8RaycastIterator__next__(DUBoundedVolumeHierarchy8RaycastIterator *self)
{
    DUBoundedVolumeHierarchy8 *bvh = self->bvh;
    if (!bvh || bvh->node_count == 0)
    {
        return 0;
    }

    while (true)
    {
        // process remaining hits from current node
        while (self->hit_index < self->hit_count)
        {
            unsigned int child_val = self->hits[self->hit_index++];

            if (child_val & DUBoundedVolumeHierarchy8_LEAF_MASK)
            {
                // leaf - yield item index
                unsigned int item_idx = child_val & ~DUBoundedVolumeHierarchy8_LEAF_MASK;
                return PyLong_FromUnsignedLong((unsigned long)item_idx);
            }
            else
            {
                // internal node - push to stack for later processing
                if (self->stack_size >= self->stack_capacity)
                {
                    size_t new_capacity = self->stack_capacity * 2;
                    unsigned int *new_stack = (unsigned int *)realloc(
                        self->stack, sizeof(unsigned int) * new_capacity);
                    if (!new_stack)
                    {
                        PyErr_NoMemory();
                        return 0;
                    }
                    self->stack = new_stack;
                    self->stack_capacity = new_capacity;
                }
                self->stack[self->stack_size++] = child_val;
            }
        }

        // no more hits, pop next node from stack
        if (self->stack_size == 0)
        {
            // traversal complete
            return 0;
        }

        unsigned int node_idx = self->stack[--self->stack_size];
        DUBoundedVolumeHierarchy8Node *node = &bvh->nodes[node_idx];

        // test all children of this node
        DUBoundedVolumeHierarchy8_ray_test_node(self->eye, self->inv_dir, node, self->hits, &self->hit_count);
        self->hit_index = 0;
    }
}

static PyObject *
DUBoundedVolumeHierarchy8RaycastIterator__iter__(DUBoundedVolumeHierarchy8RaycastIterator *self)
{
    Py_INCREF(self);
    return (PyObject *)self;
}

static PyType_Slot DUBoundedVolumeHierarchy8RaycastIterator_PyType_Slots[] = {
    {Py_tp_dealloc, (void *)DUBoundedVolumeHierarchy8RaycastIterator__dealloc__},
    {Py_tp_iter, (void *)DUBoundedVolumeHierarchy8RaycastIterator__iter__},
    {Py_tp_iternext, (void *)DUBoundedVolumeHierarchy8RaycastIterator__next__},
    {0, 0},
};

static PyType_Spec DUBoundedVolumeHierarchy8RaycastIterator_PyTypeSpec = {
    "egeometry.DUBoundedVolumeHierarchy8RaycastIterator",
    sizeof(DUBoundedVolumeHierarchy8RaycastIterator),
    0,
    Py_TPFLAGS_DEFAULT,
    DUBoundedVolumeHierarchy8RaycastIterator_PyType_Slots
};

static PyTypeObject *DUBoundedVolumeHierarchy8RaycastIterator_PyTypeObject = 0;

static PyObject *
DUBoundedVolumeHierarchy8_raycast(DUBoundedVolumeHierarchy8 *self, PyObject *const *args, Py_ssize_t nargs)
{
    if (nargs != 2)
    {
        PyErr_SetString(PyExc_TypeError, "raycast requires exactly 2 positional arguments: eye, direction");
        return 0;
    }

    ModuleState *module_state = get_module_state();
    if (!module_state){ return 0; }

    auto get_vector_ptr = module_state->emath_api->DVector3_GetValuePointer;

    const double *eye = get_vector_ptr(args[0]);
    if (!eye){ return 0; }

    const double *direction = get_vector_ptr(args[1]);
    if (!direction){ return 0; }

    // create iterator
    if (!DUBoundedVolumeHierarchy8RaycastIterator_PyTypeObject)
    {
        DUBoundedVolumeHierarchy8RaycastIterator_PyTypeObject = (PyTypeObject *)PyType_FromSpec(
            &DUBoundedVolumeHierarchy8RaycastIterator_PyTypeSpec);
        if (!DUBoundedVolumeHierarchy8RaycastIterator_PyTypeObject){ return 0; }
    }

    DUBoundedVolumeHierarchy8RaycastIterator *iter = PyObject_New(
        DUBoundedVolumeHierarchy8RaycastIterator, DUBoundedVolumeHierarchy8RaycastIterator_PyTypeObject);
    if (!iter){ return 0; }

    Py_INCREF(self);
    iter->bvh = self;
    iter->eye[0] = eye[0];
    iter->eye[1] = eye[1];
    iter->eye[2] = eye[2];

    // compute inverse direction (handle zeros)
    iter->inv_dir[0] = direction[0] != double(0) ? double(1) / direction[0] : double(1e30);
    iter->inv_dir[1] = direction[1] != double(0) ? double(1) / direction[1] : double(1e30);
    iter->inv_dir[2] = direction[2] != double(0) ? double(1) / direction[2] : double(1e30);

    iter->stack_capacity = 32;
    iter->stack = (unsigned int *)malloc(sizeof(unsigned int) * iter->stack_capacity);
    if (!iter->stack)
    {
        Py_DECREF(iter);
        PyErr_NoMemory();
        return 0;
    }
    iter->stack_size = 0;

    // test root node to initialize hits
    if (self->node_count > 0)
    {
        DUBoundedVolumeHierarchy8_ray_test_node(iter->eye, iter->inv_dir, &self->nodes[0], iter->hits, &iter->hit_count);
    }
    else
    {
        iter->hit_count = 0;
    }
    iter->hit_index = 0;

    return (PyObject *)iter;
}

static PyMethodDef DUBoundedVolumeHierarchy8_PyMethodDef[] = {
    {"raycast", (PyCFunction)DUBoundedVolumeHierarchy8_raycast, METH_FASTCALL, 0},
    {0, 0, 0, 0}
};

static PyMemberDef DUBoundedVolumeHierarchy8_PyMemberDef[] = {
    {"__weaklistoffset__", T_PYSSIZET, offsetof(DUBoundedVolumeHierarchy8, weakreflist), READONLY},
    {0, 0, 0, 0, 0},
};

static PyGetSetDef DUBoundedVolumeHierarchy8_PyGetSetDef[] = {
    {"nodes", (getter)DUBoundedVolumeHierarchy8_nodes, 0, 0, 0},
    {0, 0, 0, 0, 0}
};

static PyType_Slot DUBoundedVolumeHierarchy8_PyType_Slots [] = {
    {Py_tp_new, (void*)DUBoundedVolumeHierarchy8__new__},
    {Py_tp_dealloc, (void*)DUBoundedVolumeHierarchy8__dealloc__},
    {Py_tp_repr, (void*)DUBoundedVolumeHierarchy8__repr__},
    {Py_tp_members, (void*)DUBoundedVolumeHierarchy8_PyMemberDef},
    {Py_tp_getset, (void*)DUBoundedVolumeHierarchy8_PyGetSetDef},
    {Py_tp_methods, (void*)DUBoundedVolumeHierarchy8_PyMethodDef},
    {0, 0},
};

static PyType_Spec DUBoundedVolumeHierarchy8_PyTypeSpec = {
    "egeometry.DUBoundedVolumeHierarchy8",
    sizeof(DUBoundedVolumeHierarchy8),
    0,
    Py_TPFLAGS_DEFAULT,
    DUBoundedVolumeHierarchy8_PyType_Slots
};

static PyTypeObject *
define_DUBoundedVolumeHierarchy8_type(PyObject *module)
{
    PyTypeObject *type = (PyTypeObject *)PyType_FromModuleAndSpec(
        module,
        &DUBoundedVolumeHierarchy8_PyTypeSpec,
        0
    );
    if (!type){ return 0; }
    // Note:
    // Unlike other functions that steal references, PyModule_AddObject() only
    // decrements the reference count of value on success.
    if (PyModule_AddObject(module, "DUBoundedVolumeHierarchy8", (PyObject *)type) < 0)
    {
        Py_DECREF(type);
        return 0;
    }
    return type;
}

#endif
