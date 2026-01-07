
// generated from codegen/templates/_boundedvolumehierarchytype.hpp

#ifndef EGEOMETRY_DU8BoundedVolumeHierarchy8_TYPE_HPP
#define EGEOMETRY_DU8BoundedVolumeHierarchy8_TYPE_HPP

#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include <glm/glm.hpp>

struct DU8BoundedVolumeHierarchy8Node
{
    double min_x[8];
    double min_y[8];
    double min_z[8];
    double max_x[8];
    double max_y[8];
    double max_z[8];
    uint8_t child[8];
};

struct DU8BoundedVolumeHierarchy8
{
    PyObject_HEAD
    PyObject *weakreflist;
    DU8BoundedVolumeHierarchy8Node *nodes;
    size_t node_count;
};

#endif
