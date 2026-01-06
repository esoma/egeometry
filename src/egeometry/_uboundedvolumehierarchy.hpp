
// generated from codegen/templates/_boundedvolumehierarchy.hpp

#ifndef EGEOMETRY_UBOUNDEDVOLUMEHIERARCHY_HPP
#define EGEOMETRY_UBOUNDEDVOLUMEHIERARCHY_HPP

#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include "structmember.h"

#include "_uboundedvolumehierarchytype.hpp"
#include "_modulestate.hpp"


static PyObject *
UBoundedVolumeHierarchy__new__(PyTypeObject *cls, PyObject *args, PyObject *kwds)
{
    UBoundedVolumeHierarchy *self = 0;
    self = (UBoundedVolumeHierarchy*)cls->tp_alloc(cls, 0);
    return (PyObject *)self;
}

static void
UBoundedVolumeHierarchy__dealloc__(UBoundedVolumeHierarchy *self)
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
UBoundedVolumeHierarchy__repr__(UBoundedVolumeHierarchy *self)
{
    return PyUnicode_FromFormat(
        "<UBoundedVolumeHierarchy>"
    );
}

static PyMethodDef UBoundedVolumeHierarchy_PyMethodDef[] = {
    {0, 0, 0, 0}
};

static PyMemberDef UBoundedVolumeHierarchy_PyMemberDef[] = {
    {"__weaklistoffset__", T_PYSSIZET, offsetof(UBoundedVolumeHierarchy, weakreflist), READONLY},
    {0, 0, 0, 0, 0},
};

static PyGetSetDef UBoundedVolumeHierarchy_PyGetSetDef[] = {
    {0, 0, 0, 0, 0}
};

static PyType_Slot UBoundedVolumeHierarchy_PyType_Slots [] = {
    {Py_tp_new, (void*)UBoundedVolumeHierarchy__new__},
    {Py_tp_dealloc, (void*)UBoundedVolumeHierarchy__dealloc__},
    {Py_tp_repr, (void*)UBoundedVolumeHierarchy__repr__},
    {Py_tp_members, (void*)UBoundedVolumeHierarchy_PyMemberDef},
    {Py_tp_getset, (void*)UBoundedVolumeHierarchy_PyGetSetDef},
    {Py_tp_methods, (void*)UBoundedVolumeHierarchy_PyMethodDef},
    {0, 0},
};

static PyType_Spec UBoundedVolumeHierarchy_PyTypeSpec = {
    "egeometry.UBoundedVolumeHierarchy",
    sizeof(UBoundedVolumeHierarchy),
    0,
    Py_TPFLAGS_DEFAULT,
    UBoundedVolumeHierarchy_PyType_Slots
};

static PyTypeObject *
define_UBoundedVolumeHierarchy_type(PyObject *module)
{
    PyTypeObject *type = (PyTypeObject *)PyType_FromModuleAndSpec(
        module,
        &UBoundedVolumeHierarchy_PyTypeSpec,
        0
    );
    if (!type){ return 0; }
    // Note:
    // Unlike other functions that steal references, PyModule_AddObject() only
    // decrements the reference count of value on success.
    if (PyModule_AddObject(module, "UBoundedVolumeHierarchy", (PyObject *)type) < 0)
    {
        Py_DECREF(type);
        return 0;
    }
    return type;
}

#endif
