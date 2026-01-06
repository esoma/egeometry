
// generated from codegen/templates/_boundedvolumehierarchytype.hpp

#ifndef EGEOMETRY_{{ name }}_TYPE_HPP
#define EGEOMETRY_{{ name }}_TYPE_HPP

#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include <glm/glm.hpp>

struct {{ name }}
{
    PyObject_HEAD
    PyObject *weakreflist;
};

#endif
