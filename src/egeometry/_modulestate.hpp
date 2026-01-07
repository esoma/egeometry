
// generated from codegen/templates/_modulestate.hpp

#ifndef EGEOMETRY_MODULESTATE_HPP
#define EGEOMETRY_MODULESTATE_HPP

#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include "_module.hpp"
#include "emath.h"

struct ModuleState
{
    EMathApi *emath_api;

    PyTypeObject *DBoundingBox2d_PyTypeObject;

    PyTypeObject *FBoundingBox2d_PyTypeObject;

    PyTypeObject *IBoundingBox2d_PyTypeObject;

    PyTypeObject *DU8BoundedVolumeHierarchy2_PyTypeObject;

    PyTypeObject *DU8BoundedVolumeHierarchy4_PyTypeObject;

    PyTypeObject *DU8BoundedVolumeHierarchy8_PyTypeObject;

    PyTypeObject *DU16BoundedVolumeHierarchy2_PyTypeObject;

    PyTypeObject *DU16BoundedVolumeHierarchy4_PyTypeObject;

    PyTypeObject *DU16BoundedVolumeHierarchy8_PyTypeObject;

    PyTypeObject *DU32BoundedVolumeHierarchy2_PyTypeObject;

    PyTypeObject *DU32BoundedVolumeHierarchy4_PyTypeObject;

    PyTypeObject *DU32BoundedVolumeHierarchy8_PyTypeObject;

    PyTypeObject *DUBoundedVolumeHierarchy2_PyTypeObject;

    PyTypeObject *DUBoundedVolumeHierarchy4_PyTypeObject;

    PyTypeObject *DUBoundedVolumeHierarchy8_PyTypeObject;

    PyTypeObject *FU8BoundedVolumeHierarchy2_PyTypeObject;

    PyTypeObject *FU8BoundedVolumeHierarchy4_PyTypeObject;

    PyTypeObject *FU8BoundedVolumeHierarchy8_PyTypeObject;

    PyTypeObject *FU16BoundedVolumeHierarchy2_PyTypeObject;

    PyTypeObject *FU16BoundedVolumeHierarchy4_PyTypeObject;

    PyTypeObject *FU16BoundedVolumeHierarchy8_PyTypeObject;

    PyTypeObject *FU32BoundedVolumeHierarchy2_PyTypeObject;

    PyTypeObject *FU32BoundedVolumeHierarchy4_PyTypeObject;

    PyTypeObject *FU32BoundedVolumeHierarchy8_PyTypeObject;

    PyTypeObject *FUBoundedVolumeHierarchy2_PyTypeObject;

    PyTypeObject *FUBoundedVolumeHierarchy4_PyTypeObject;

    PyTypeObject *FUBoundedVolumeHierarchy8_PyTypeObject;

};


static int
ModuleState_traverse(
    ModuleState *self,
    visitproc visit,
    void *arg
)
{

    Py_VISIT(self->DBoundingBox2d_PyTypeObject);

    Py_VISIT(self->FBoundingBox2d_PyTypeObject);

    Py_VISIT(self->IBoundingBox2d_PyTypeObject);

    Py_VISIT(self->DU8BoundedVolumeHierarchy2_PyTypeObject);

    Py_VISIT(self->DU8BoundedVolumeHierarchy4_PyTypeObject);

    Py_VISIT(self->DU8BoundedVolumeHierarchy8_PyTypeObject);

    Py_VISIT(self->DU16BoundedVolumeHierarchy2_PyTypeObject);

    Py_VISIT(self->DU16BoundedVolumeHierarchy4_PyTypeObject);

    Py_VISIT(self->DU16BoundedVolumeHierarchy8_PyTypeObject);

    Py_VISIT(self->DU32BoundedVolumeHierarchy2_PyTypeObject);

    Py_VISIT(self->DU32BoundedVolumeHierarchy4_PyTypeObject);

    Py_VISIT(self->DU32BoundedVolumeHierarchy8_PyTypeObject);

    Py_VISIT(self->DUBoundedVolumeHierarchy2_PyTypeObject);

    Py_VISIT(self->DUBoundedVolumeHierarchy4_PyTypeObject);

    Py_VISIT(self->DUBoundedVolumeHierarchy8_PyTypeObject);

    Py_VISIT(self->FU8BoundedVolumeHierarchy2_PyTypeObject);

    Py_VISIT(self->FU8BoundedVolumeHierarchy4_PyTypeObject);

    Py_VISIT(self->FU8BoundedVolumeHierarchy8_PyTypeObject);

    Py_VISIT(self->FU16BoundedVolumeHierarchy2_PyTypeObject);

    Py_VISIT(self->FU16BoundedVolumeHierarchy4_PyTypeObject);

    Py_VISIT(self->FU16BoundedVolumeHierarchy8_PyTypeObject);

    Py_VISIT(self->FU32BoundedVolumeHierarchy2_PyTypeObject);

    Py_VISIT(self->FU32BoundedVolumeHierarchy4_PyTypeObject);

    Py_VISIT(self->FU32BoundedVolumeHierarchy8_PyTypeObject);

    Py_VISIT(self->FUBoundedVolumeHierarchy2_PyTypeObject);

    Py_VISIT(self->FUBoundedVolumeHierarchy4_PyTypeObject);

    Py_VISIT(self->FUBoundedVolumeHierarchy8_PyTypeObject);

    return 0;
}


static int
ModuleState_clear(ModuleState *self)
{
    if (self->emath_api)
    {
        EMathApi_Release();
        PyErr_Clear();
        self->emath_api = 0;
    }

    Py_CLEAR(self->DBoundingBox2d_PyTypeObject);

    Py_CLEAR(self->FBoundingBox2d_PyTypeObject);

    Py_CLEAR(self->IBoundingBox2d_PyTypeObject);

    Py_CLEAR(self->DU8BoundedVolumeHierarchy2_PyTypeObject);

    Py_CLEAR(self->DU8BoundedVolumeHierarchy4_PyTypeObject);

    Py_CLEAR(self->DU8BoundedVolumeHierarchy8_PyTypeObject);

    Py_CLEAR(self->DU16BoundedVolumeHierarchy2_PyTypeObject);

    Py_CLEAR(self->DU16BoundedVolumeHierarchy4_PyTypeObject);

    Py_CLEAR(self->DU16BoundedVolumeHierarchy8_PyTypeObject);

    Py_CLEAR(self->DU32BoundedVolumeHierarchy2_PyTypeObject);

    Py_CLEAR(self->DU32BoundedVolumeHierarchy4_PyTypeObject);

    Py_CLEAR(self->DU32BoundedVolumeHierarchy8_PyTypeObject);

    Py_CLEAR(self->DUBoundedVolumeHierarchy2_PyTypeObject);

    Py_CLEAR(self->DUBoundedVolumeHierarchy4_PyTypeObject);

    Py_CLEAR(self->DUBoundedVolumeHierarchy8_PyTypeObject);

    Py_CLEAR(self->FU8BoundedVolumeHierarchy2_PyTypeObject);

    Py_CLEAR(self->FU8BoundedVolumeHierarchy4_PyTypeObject);

    Py_CLEAR(self->FU8BoundedVolumeHierarchy8_PyTypeObject);

    Py_CLEAR(self->FU16BoundedVolumeHierarchy2_PyTypeObject);

    Py_CLEAR(self->FU16BoundedVolumeHierarchy4_PyTypeObject);

    Py_CLEAR(self->FU16BoundedVolumeHierarchy8_PyTypeObject);

    Py_CLEAR(self->FU32BoundedVolumeHierarchy2_PyTypeObject);

    Py_CLEAR(self->FU32BoundedVolumeHierarchy4_PyTypeObject);

    Py_CLEAR(self->FU32BoundedVolumeHierarchy8_PyTypeObject);

    Py_CLEAR(self->FUBoundedVolumeHierarchy2_PyTypeObject);

    Py_CLEAR(self->FUBoundedVolumeHierarchy4_PyTypeObject);

    Py_CLEAR(self->FUBoundedVolumeHierarchy8_PyTypeObject);

    return 0;
}


static ModuleState *
get_module_state()
{
    PyObject *module = get_module();
    if (!module){ return 0; }
    return (ModuleState *)PyModule_GetState(module);
}

#endif
