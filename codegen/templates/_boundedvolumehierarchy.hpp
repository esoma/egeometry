
// generated from codegen/templates/_boundedvolumehierarchy.hpp

#ifndef EGEOMETRY_{{ name.upper() }}_HPP
#define EGEOMETRY_{{ name.upper() }}_HPP

#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include "structmember.h"

#include "_{{ name.lower() }}type.hpp"
#include "_modulestate.hpp"


static PyObject *
{{ name }}__new__(PyTypeObject *cls, PyObject *args, PyObject *kwds)
{
    {{ name }} *self = 0;
    self = ({{ name }}*)cls->tp_alloc(cls, 0);
    return (PyObject *)self;
}

static void
{{ name }}__dealloc__({{ name }} *self)
{
    if (self->weakreflist)
    {
        PyObject_ClearWeakRefs((PyObject *)self);
    }

    PyTypeObject *type = Py_TYPE(self);
    type->tp_free(self);
    Py_DECREF(type);
}

static PyObject *
{{ name }}__repr__({{ name }} *self)
{
    return PyUnicode_FromFormat(
        "<{{ name }}>"
    );
}

static PyMethodDef {{ name }}_PyMethodDef[] = {
    {0, 0, 0, 0}
};

static PyMemberDef {{ name }}_PyMemberDef[] = {
    {"__weaklistoffset__", T_PYSSIZET, offsetof({{ name }}, weakreflist), READONLY},
    {0, 0, 0, 0, 0},
};

static PyGetSetDef {{ name }}_PyGetSetDef[] = {
    {0, 0, 0, 0, 0}
};

static PyType_Slot {{ name }}_PyType_Slots [] = {
    {Py_tp_new, (void*){{ name }}__new__},
    {Py_tp_dealloc, (void*){{ name }}__dealloc__},
    {Py_tp_repr, (void*){{ name }}__repr__},
    {Py_tp_members, (void*){{ name }}_PyMemberDef},
    {Py_tp_getset, (void*){{ name }}_PyGetSetDef},
    {Py_tp_methods, (void*){{ name }}_PyMethodDef},
    {0, 0},
};

static PyType_Spec {{ name }}_PyTypeSpec = {
    "egeometry.{{ name }}",
    sizeof({{ name }}),
    0,
    Py_TPFLAGS_DEFAULT,
    {{ name }}_PyType_Slots
};

static PyTypeObject *
define_{{ name }}_type(PyObject *module)
{
    PyTypeObject *type = (PyTypeObject *)PyType_FromModuleAndSpec(
        module,
        &{{ name }}_PyTypeSpec,
        0
    );
    if (!type){ return 0; }
    // Note:
    // Unlike other functions that steal references, PyModule_AddObject() only
    // decrements the reference count of value on success.
    if (PyModule_AddObject(module, "{{ name }}", (PyObject *)type) < 0)
    {
        Py_DECREF(type);
        return 0;
    }
    return type;
}

#endif
