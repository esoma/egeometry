
// generated from codegen/templates/_boundedvolumehierarchytype.hpp

#ifndef EGEOMETRY_DUBoundedVolumeHierarchy4_TYPE_HPP
#define EGEOMETRY_DUBoundedVolumeHierarchy4_TYPE_HPP

#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include <glm/glm.hpp>

struct DUBoundedVolumeHierarchy4Node
{
    double min_x[4];
    double min_y[4];
    double min_z[4];
    double max_x[4];
    double max_y[4];
    double max_z[4];
    unsigned int child[4];
};

struct DUBoundedVolumeHierarchy4
{
    PyObject_HEAD
    PyObject *weakreflist;
    DUBoundedVolumeHierarchy4Node *nodes;
    size_t node_count;
};

#endif
