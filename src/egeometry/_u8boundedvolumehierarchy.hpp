
// generated from codegen/templates/_boundedvolumehierarchy.hpp

#ifndef EGEOMETRY_U8BOUNDEDVOLUMEHIERARCHY_HPP
#define EGEOMETRY_U8BOUNDEDVOLUMEHIERARCHY_HPP

#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include "structmember.h"

#include "_u8boundedvolumehierarchytype.hpp"
#include "_modulestate.hpp"


static PyObject *
U8BoundedVolumeHierarchy__new__(PyTypeObject *cls, PyObject *args, PyObject *kwds)
{
    U8BoundedVolumeHierarchy *self = 0;
    self = (U8BoundedVolumeHierarchy*)cls->tp_alloc(cls, 0);
    return (PyObject *)self;
}

static void
U8BoundedVolumeHierarchy__dealloc__(U8BoundedVolumeHierarchy *self)
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
U8BoundedVolumeHierarchy__repr__(U8BoundedVolumeHierarchy *self)
{
    return PyUnicode_FromFormat(
        "<U8BoundedVolumeHierarchy>"
    );
}

static PyMethodDef U8BoundedVolumeHierarchy_PyMethodDef[] = {
    {0, 0, 0, 0}
};

static PyMemberDef U8BoundedVolumeHierarchy_PyMemberDef[] = {
    {"__weaklistoffset__", T_PYSSIZET, offsetof(U8BoundedVolumeHierarchy, weakreflist), READONLY},
    {0, 0, 0, 0, 0},
};

static PyGetSetDef U8BoundedVolumeHierarchy_PyGetSetDef[] = {
    {0, 0, 0, 0, 0}
};

static PyType_Slot U8BoundedVolumeHierarchy_PyType_Slots [] = {
    {Py_tp_new, (void*)U8BoundedVolumeHierarchy__new__},
    {Py_tp_dealloc, (void*)U8BoundedVolumeHierarchy__dealloc__},
    {Py_tp_repr, (void*)U8BoundedVolumeHierarchy__repr__},
    {Py_tp_members, (void*)U8BoundedVolumeHierarchy_PyMemberDef},
    {Py_tp_getset, (void*)U8BoundedVolumeHierarchy_PyGetSetDef},
    {Py_tp_methods, (void*)U8BoundedVolumeHierarchy_PyMethodDef},
    {0, 0},
};

static PyType_Spec U8BoundedVolumeHierarchy_PyTypeSpec = {
    "egeometry.U8BoundedVolumeHierarchy",
    sizeof(U8BoundedVolumeHierarchy),
    0,
    Py_TPFLAGS_DEFAULT,
    U8BoundedVolumeHierarchy_PyType_Slots
};

static PyTypeObject *
define_U8BoundedVolumeHierarchy_type(PyObject *module)
{
    PyTypeObject *type = (PyTypeObject *)PyType_FromModuleAndSpec(
        module,
        &U8BoundedVolumeHierarchy_PyTypeSpec,
        0
    );
    if (!type){ return 0; }
    // Note:
    // Unlike other functions that steal references, PyModule_AddObject() only
    // decrements the reference count of value on success.
    if (PyModule_AddObject(module, "U8BoundedVolumeHierarchy", (PyObject *)type) < 0)
    {
        Py_DECREF(type);
        return 0;
    }
    return type;
}

#endif
