
// generated from codegen/templates/_boundedvolumehierarchytype.hpp

#ifndef EGEOMETRY_FU16BoundedVolumeHierarchy2_TYPE_HPP
#define EGEOMETRY_FU16BoundedVolumeHierarchy2_TYPE_HPP

#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include <glm/glm.hpp>

struct FU16BoundedVolumeHierarchy2Node
{
    float min_x[2];
    float min_y[2];
    float min_z[2];
    float max_x[2];
    float max_y[2];
    float max_z[2];
    uint16_t child[2];
};

struct FU16BoundedVolumeHierarchy2
{
    PyObject_HEAD
    PyObject *weakreflist;
    FU16BoundedVolumeHierarchy2Node *nodes;
    size_t node_count;
};

#endif
