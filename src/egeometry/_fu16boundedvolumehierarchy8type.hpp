
// generated from codegen/templates/_boundedvolumehierarchytype.hpp

#ifndef EGEOMETRY_FU16BoundedVolumeHierarchy8_TYPE_HPP
#define EGEOMETRY_FU16BoundedVolumeHierarchy8_TYPE_HPP

#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include <glm/glm.hpp>

struct FU16BoundedVolumeHierarchy8Node
{
    float min_x[8];
    float min_y[8];
    float min_z[8];
    float max_x[8];
    float max_y[8];
    float max_z[8];
    uint16_t child[8];
};

struct FU16BoundedVolumeHierarchy8
{
    PyObject_HEAD
    PyObject *weakreflist;
    FU16BoundedVolumeHierarchy8Node *nodes;
    size_t node_count;
};

#endif
