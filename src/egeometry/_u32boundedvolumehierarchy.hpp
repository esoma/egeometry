
// generated from codegen/templates/_boundedvolumehierarchy.hpp

#ifndef EGEOMETRY_U32BOUNDEDVOLUMEHIERARCHY_HPP
#define EGEOMETRY_U32BOUNDEDVOLUMEHIERARCHY_HPP

#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include "structmember.h"

#include "_u32boundedvolumehierarchytype.hpp"
#include "_modulestate.hpp"


static PyObject *
U32BoundedVolumeHierarchy__new__(PyTypeObject *cls, PyObject *args, PyObject *kwds)
{
    U32BoundedVolumeHierarchy *self = 0;
    self = (U32BoundedVolumeHierarchy*)cls->tp_alloc(cls, 0);
    return (PyObject *)self;
}

static void
U32BoundedVolumeHierarchy__dealloc__(U32BoundedVolumeHierarchy *self)
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
U32BoundedVolumeHierarchy__repr__(U32BoundedVolumeHierarchy *self)
{
    return PyUnicode_FromFormat(
        "<U32BoundedVolumeHierarchy>"
    );
}

static PyMethodDef U32BoundedVolumeHierarchy_PyMethodDef[] = {
    {0, 0, 0, 0}
};

static PyMemberDef U32BoundedVolumeHierarchy_PyMemberDef[] = {
    {"__weaklistoffset__", T_PYSSIZET, offsetof(U32BoundedVolumeHierarchy, weakreflist), READONLY},
    {0, 0, 0, 0, 0},
};

static PyGetSetDef U32BoundedVolumeHierarchy_PyGetSetDef[] = {
    {0, 0, 0, 0, 0}
};

static PyType_Slot U32BoundedVolumeHierarchy_PyType_Slots [] = {
    {Py_tp_new, (void*)U32BoundedVolumeHierarchy__new__},
    {Py_tp_dealloc, (void*)U32BoundedVolumeHierarchy__dealloc__},
    {Py_tp_repr, (void*)U32BoundedVolumeHierarchy__repr__},
    {Py_tp_members, (void*)U32BoundedVolumeHierarchy_PyMemberDef},
    {Py_tp_getset, (void*)U32BoundedVolumeHierarchy_PyGetSetDef},
    {Py_tp_methods, (void*)U32BoundedVolumeHierarchy_PyMethodDef},
    {0, 0},
};

static PyType_Spec U32BoundedVolumeHierarchy_PyTypeSpec = {
    "egeometry.U32BoundedVolumeHierarchy",
    sizeof(U32BoundedVolumeHierarchy),
    0,
    Py_TPFLAGS_DEFAULT,
    U32BoundedVolumeHierarchy_PyType_Slots
};

static PyTypeObject *
define_U32BoundedVolumeHierarchy_type(PyObject *module)
{
    PyTypeObject *type = (PyTypeObject *)PyType_FromModuleAndSpec(
        module,
        &U32BoundedVolumeHierarchy_PyTypeSpec,
        0
    );
    if (!type){ return 0; }
    // Note:
    // Unlike other functions that steal references, PyModule_AddObject() only
    // decrements the reference count of value on success.
    if (PyModule_AddObject(module, "U32BoundedVolumeHierarchy", (PyObject *)type) < 0)
    {
        Py_DECREF(type);
        return 0;
    }
    return type;
}

#endif
