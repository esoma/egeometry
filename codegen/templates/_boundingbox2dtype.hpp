
// generated from codegen/templates/_boundingbox2dtype.hpp

#ifndef EGEOMETRY_{{ name }}_TYPE_HPP
#define EGEOMETRY_{{ name }}_TYPE_HPP

#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include <glm/glm.hpp>

typedef glm::vec<2, {{ c_type }}, glm::defaultp> {{ name }}GlmVector;
typedef glm::vec<4, {{ c_type }}, glm::defaultp> {{ name }}GlmVector4;

struct {{ name }}
{
    PyObject_HEAD
    PyObject *weakreflist;
    PyObject *py_position;
    PyObject *py_size;
};

#endif
