
// generated from codegen/templates/_boundedvolumehierarchytype.hpp

#ifndef EGEOMETRY_FU8BoundedVolumeHierarchy8_TYPE_HPP
#define EGEOMETRY_FU8BoundedVolumeHierarchy8_TYPE_HPP

#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include <glm/glm.hpp>

struct FU8BoundedVolumeHierarchy8Node
{
    float min_x[8];
    float min_y[8];
    float min_z[8];
    float max_x[8];
    float max_y[8];
    float max_z[8];
    uint8_t child[8];
};

struct FU8BoundedVolumeHierarchy8
{
    PyObject_HEAD
    PyObject *weakreflist;
    FU8BoundedVolumeHierarchy8Node *nodes;
    size_t node_count;
};

#endif
