
// generated from codegen/templates/_boundedvolumehierarchytype.hpp

#ifndef EGEOMETRY_{{ name }}_TYPE_HPP
#define EGEOMETRY_{{ name }}_TYPE_HPP

#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include <glm/glm.hpp>

struct {{ name }}Node
{
    {{ space_c_type }} min_x[{{ child_count }}];
    {{ space_c_type }} min_y[{{ child_count }}];
    {{ space_c_type }} min_z[{{ child_count }}];
    {{ space_c_type }} max_x[{{ child_count }}];
    {{ space_c_type }} max_y[{{ child_count }}];
    {{ space_c_type }} max_z[{{ child_count }}];
    {{ object_c_type }} child[{{ child_count }}];
};

struct {{ name }}
{
    PyObject_HEAD
    PyObject *weakreflist;
    {{ name }}Node *nodes;
    size_t node_count;
};

#endif
