
// generated from codegen/templates/_boundedvolumehierarchytype.hpp

#ifndef EGEOMETRY_FU32BoundedVolumeHierarchy4_TYPE_HPP
#define EGEOMETRY_FU32BoundedVolumeHierarchy4_TYPE_HPP

#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include <glm/glm.hpp>

struct FU32BoundedVolumeHierarchy4Node
{
    float min_x[4];
    float min_y[4];
    float min_z[4];
    float max_x[4];
    float max_y[4];
    float max_z[4];
    uint32_t child[4];
};

struct FU32BoundedVolumeHierarchy4
{
    PyObject_HEAD
    PyObject *weakreflist;
    FU32BoundedVolumeHierarchy4Node *nodes;
    size_t node_count;
};

#endif
