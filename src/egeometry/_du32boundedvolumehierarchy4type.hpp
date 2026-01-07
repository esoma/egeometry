
// generated from codegen/templates/_boundedvolumehierarchytype.hpp

#ifndef EGEOMETRY_DU32BoundedVolumeHierarchy4_TYPE_HPP
#define EGEOMETRY_DU32BoundedVolumeHierarchy4_TYPE_HPP

#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include <glm/glm.hpp>

struct DU32BoundedVolumeHierarchy4Node
{
    double min_x[4];
    double min_y[4];
    double min_z[4];
    double max_x[4];
    double max_y[4];
    double max_z[4];
    uint32_t child[4];
};

struct DU32BoundedVolumeHierarchy4
{
    PyObject_HEAD
    PyObject *weakreflist;
    DU32BoundedVolumeHierarchy4Node *nodes;
    size_t node_count;
};

#endif
