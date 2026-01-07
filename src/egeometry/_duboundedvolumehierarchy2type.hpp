
// generated from codegen/templates/_boundedvolumehierarchytype.hpp

#ifndef EGEOMETRY_DUBoundedVolumeHierarchy2_TYPE_HPP
#define EGEOMETRY_DUBoundedVolumeHierarchy2_TYPE_HPP

#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include <glm/glm.hpp>

struct DUBoundedVolumeHierarchy2Node
{
    double min_x[2];
    double min_y[2];
    double min_z[2];
    double max_x[2];
    double max_y[2];
    double max_z[2];
    unsigned int child[2];
};

struct DUBoundedVolumeHierarchy2
{
    PyObject_HEAD
    PyObject *weakreflist;
    DUBoundedVolumeHierarchy2Node *nodes;
    size_t node_count;
};

#endif
