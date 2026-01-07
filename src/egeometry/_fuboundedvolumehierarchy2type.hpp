
// generated from codegen/templates/_boundedvolumehierarchytype.hpp

#ifndef EGEOMETRY_FUBoundedVolumeHierarchy2_TYPE_HPP
#define EGEOMETRY_FUBoundedVolumeHierarchy2_TYPE_HPP

#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include <glm/glm.hpp>

struct FUBoundedVolumeHierarchy2Node
{
    float min_x[2];
    float min_y[2];
    float min_z[2];
    float max_x[2];
    float max_y[2];
    float max_z[2];
    unsigned int child[2];
};

struct FUBoundedVolumeHierarchy2
{
    PyObject_HEAD
    PyObject *weakreflist;
    FUBoundedVolumeHierarchy2Node *nodes;
    size_t node_count;
};

#endif
