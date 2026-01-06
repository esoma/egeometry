
// generated from codegen/templates/_boundedvolumehierarchy.hpp

#ifndef EGEOMETRY_U16BOUNDEDVOLUMEHIERARCHY_HPP
#define EGEOMETRY_U16BOUNDEDVOLUMEHIERARCHY_HPP

#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include "structmember.h"

#include "_u16boundedvolumehierarchytype.hpp"
#include "_modulestate.hpp"


static PyObject *
U16BoundedVolumeHierarchy__new__(PyTypeObject *cls, PyObject *args, PyObject *kwds)
{
    U16BoundedVolumeHierarchy *self = 0;
    self = (U16BoundedVolumeHierarchy*)cls->tp_alloc(cls, 0);
    return (PyObject *)self;
}

static void
U16BoundedVolumeHierarchy__dealloc__(U16BoundedVolumeHierarchy *self)
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
U16BoundedVolumeHierarchy__repr__(U16BoundedVolumeHierarchy *self)
{
    return PyUnicode_FromFormat(
        "<U16BoundedVolumeHierarchy>"
    );
}

static PyMethodDef U16BoundedVolumeHierarchy_PyMethodDef[] = {
    {0, 0, 0, 0}
};

static PyMemberDef U16BoundedVolumeHierarchy_PyMemberDef[] = {
    {"__weaklistoffset__", T_PYSSIZET, offsetof(U16BoundedVolumeHierarchy, weakreflist), READONLY},
    {0, 0, 0, 0, 0},
};

static PyGetSetDef U16BoundedVolumeHierarchy_PyGetSetDef[] = {
    {0, 0, 0, 0, 0}
};

static PyType_Slot U16BoundedVolumeHierarchy_PyType_Slots [] = {
    {Py_tp_new, (void*)U16BoundedVolumeHierarchy__new__},
    {Py_tp_dealloc, (void*)U16BoundedVolumeHierarchy__dealloc__},
    {Py_tp_repr, (void*)U16BoundedVolumeHierarchy__repr__},
    {Py_tp_members, (void*)U16BoundedVolumeHierarchy_PyMemberDef},
    {Py_tp_getset, (void*)U16BoundedVolumeHierarchy_PyGetSetDef},
    {Py_tp_methods, (void*)U16BoundedVolumeHierarchy_PyMethodDef},
    {0, 0},
};

static PyType_Spec U16BoundedVolumeHierarchy_PyTypeSpec = {
    "egeometry.U16BoundedVolumeHierarchy",
    sizeof(U16BoundedVolumeHierarchy),
    0,
    Py_TPFLAGS_DEFAULT,
    U16BoundedVolumeHierarchy_PyType_Slots
};

static PyTypeObject *
define_U16BoundedVolumeHierarchy_type(PyObject *module)
{
    PyTypeObject *type = (PyTypeObject *)PyType_FromModuleAndSpec(
        module,
        &U16BoundedVolumeHierarchy_PyTypeSpec,
        0
    );
    if (!type){ return 0; }
    // Note:
    // Unlike other functions that steal references, PyModule_AddObject() only
    // decrements the reference count of value on success.
    if (PyModule_AddObject(module, "U16BoundedVolumeHierarchy", (PyObject *)type) < 0)
    {
        Py_DECREF(type);
        return 0;
    }
    return type;
}

#endif
