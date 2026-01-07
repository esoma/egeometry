
// generated from codegen/templates/_boundedvolumehierarchytype.hpp

#ifndef EGEOMETRY_FUBoundedVolumeHierarchy8_TYPE_HPP
#define EGEOMETRY_FUBoundedVolumeHierarchy8_TYPE_HPP

#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include <glm/glm.hpp>

struct FUBoundedVolumeHierarchy8Node
{
    float min_x[8];
    float min_y[8];
    float min_z[8];
    float max_x[8];
    float max_y[8];
    float max_z[8];
    unsigned int child[8];
};

struct FUBoundedVolumeHierarchy8
{
    PyObject_HEAD
    PyObject *weakreflist;
    FUBoundedVolumeHierarchy8Node *nodes;
    size_t node_count;
};

#endif
