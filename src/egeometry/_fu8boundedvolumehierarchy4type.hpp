
// generated from codegen/templates/_boundedvolumehierarchytype.hpp

#ifndef EGEOMETRY_FU8BoundedVolumeHierarchy4_TYPE_HPP
#define EGEOMETRY_FU8BoundedVolumeHierarchy4_TYPE_HPP

#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include <glm/glm.hpp>

struct FU8BoundedVolumeHierarchy4Node
{
    float min_x[4];
    float min_y[4];
    float min_z[4];
    float max_x[4];
    float max_y[4];
    float max_z[4];
    uint8_t child[4];
};

struct FU8BoundedVolumeHierarchy4
{
    PyObject_HEAD
    PyObject *weakreflist;
    FU8BoundedVolumeHierarchy4Node *nodes;
    size_t node_count;
};

#endif
