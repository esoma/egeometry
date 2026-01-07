
// generated from codegen/templates/_boundedvolumehierarchytype.hpp

#ifndef EGEOMETRY_DUBoundedVolumeHierarchy8_TYPE_HPP
#define EGEOMETRY_DUBoundedVolumeHierarchy8_TYPE_HPP

#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include <glm/glm.hpp>

struct DUBoundedVolumeHierarchy8Node
{
    double min_x[8];
    double min_y[8];
    double min_z[8];
    double max_x[8];
    double max_y[8];
    double max_z[8];
    unsigned int child[8];
};

struct DUBoundedVolumeHierarchy8
{
    PyObject_HEAD
    PyObject *weakreflist;
    DUBoundedVolumeHierarchy8Node *nodes;
    size_t node_count;
};

#endif
