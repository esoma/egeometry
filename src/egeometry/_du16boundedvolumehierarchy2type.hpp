
// generated from codegen/templates/_boundedvolumehierarchytype.hpp

#ifndef EGEOMETRY_DU16BoundedVolumeHierarchy2_TYPE_HPP
#define EGEOMETRY_DU16BoundedVolumeHierarchy2_TYPE_HPP

#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include <glm/glm.hpp>

struct DU16BoundedVolumeHierarchy2Node
{
    double min_x[2];
    double min_y[2];
    double min_z[2];
    double max_x[2];
    double max_y[2];
    double max_z[2];
    uint16_t child[2];
};

struct DU16BoundedVolumeHierarchy2
{
    PyObject_HEAD
    PyObject *weakreflist;
    DU16BoundedVolumeHierarchy2Node *nodes;
    size_t node_count;
};

#endif
