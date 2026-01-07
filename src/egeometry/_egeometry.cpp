
// generated from codegen/templates/_egeometry.cpp

#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <structmember.h>

#include "_modulestate.hpp"

    #include "_dboundingbox2d.hpp"

    #include "_fboundingbox2d.hpp"

    #include "_iboundingbox2d.hpp"

    #include "_du8boundedvolumehierarchy2.hpp"

    #include "_du8boundedvolumehierarchy4.hpp"

    #include "_du8boundedvolumehierarchy8.hpp"

    #include "_du16boundedvolumehierarchy2.hpp"

    #include "_du16boundedvolumehierarchy4.hpp"

    #include "_du16boundedvolumehierarchy8.hpp"

    #include "_du32boundedvolumehierarchy2.hpp"

    #include "_du32boundedvolumehierarchy4.hpp"

    #include "_du32boundedvolumehierarchy8.hpp"

    #include "_duboundedvolumehierarchy2.hpp"

    #include "_duboundedvolumehierarchy4.hpp"

    #include "_duboundedvolumehierarchy8.hpp"

    #include "_fu8boundedvolumehierarchy2.hpp"

    #include "_fu8boundedvolumehierarchy4.hpp"

    #include "_fu8boundedvolumehierarchy8.hpp"

    #include "_fu16boundedvolumehierarchy2.hpp"

    #include "_fu16boundedvolumehierarchy4.hpp"

    #include "_fu16boundedvolumehierarchy8.hpp"

    #include "_fu32boundedvolumehierarchy2.hpp"

    #include "_fu32boundedvolumehierarchy4.hpp"

    #include "_fu32boundedvolumehierarchy8.hpp"

    #include "_fuboundedvolumehierarchy2.hpp"

    #include "_fuboundedvolumehierarchy4.hpp"

    #include "_fuboundedvolumehierarchy8.hpp"

#include "emath.h"


static PyMethodDef module_methods[] = {
    {0, 0, 0, 0}
};


static int
module_traverse(PyObject *self, visitproc visit, void *arg)
{
    ModuleState *state = (ModuleState *)PyModule_GetState(self);
    return ModuleState_traverse(state, visit, arg);
}


static int
module_clear(PyObject *self)
{
    ModuleState *state = (ModuleState *)PyModule_GetState(self);
    return ModuleState_clear(state);
}


static struct PyModuleDef module_PyModuleDef = {
    PyModuleDef_HEAD_INIT,
    "egeometry._egeometry",
    0,
    sizeof(ModuleState),
    module_methods,
    0,
    module_traverse,
    module_clear
};


PyMODINIT_FUNC
PyInit__egeometry()
{
    PyObject *module = PyModule_Create(&module_PyModuleDef);
    ModuleState *state = 0;
    if (!module){ goto error; }
    if (PyState_AddModule(module, &module_PyModuleDef) == -1){ goto error; }
    state = (ModuleState *)PyModule_GetState(module);
    state->emath_api = EMathApi_Get();
    if (state->emath_api == 0)
    {
        goto error;
    }

    {
        PyTypeObject *type = define_DBoundingBox2d_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->DBoundingBox2d_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_FBoundingBox2d_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->FBoundingBox2d_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_IBoundingBox2d_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->IBoundingBox2d_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_DU8BoundedVolumeHierarchy2_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->DU8BoundedVolumeHierarchy2_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_DU8BoundedVolumeHierarchy4_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->DU8BoundedVolumeHierarchy4_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_DU8BoundedVolumeHierarchy8_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->DU8BoundedVolumeHierarchy8_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_DU16BoundedVolumeHierarchy2_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->DU16BoundedVolumeHierarchy2_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_DU16BoundedVolumeHierarchy4_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->DU16BoundedVolumeHierarchy4_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_DU16BoundedVolumeHierarchy8_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->DU16BoundedVolumeHierarchy8_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_DU32BoundedVolumeHierarchy2_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->DU32BoundedVolumeHierarchy2_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_DU32BoundedVolumeHierarchy4_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->DU32BoundedVolumeHierarchy4_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_DU32BoundedVolumeHierarchy8_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->DU32BoundedVolumeHierarchy8_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_DUBoundedVolumeHierarchy2_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->DUBoundedVolumeHierarchy2_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_DUBoundedVolumeHierarchy4_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->DUBoundedVolumeHierarchy4_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_DUBoundedVolumeHierarchy8_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->DUBoundedVolumeHierarchy8_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_FU8BoundedVolumeHierarchy2_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->FU8BoundedVolumeHierarchy2_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_FU8BoundedVolumeHierarchy4_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->FU8BoundedVolumeHierarchy4_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_FU8BoundedVolumeHierarchy8_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->FU8BoundedVolumeHierarchy8_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_FU16BoundedVolumeHierarchy2_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->FU16BoundedVolumeHierarchy2_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_FU16BoundedVolumeHierarchy4_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->FU16BoundedVolumeHierarchy4_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_FU16BoundedVolumeHierarchy8_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->FU16BoundedVolumeHierarchy8_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_FU32BoundedVolumeHierarchy2_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->FU32BoundedVolumeHierarchy2_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_FU32BoundedVolumeHierarchy4_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->FU32BoundedVolumeHierarchy4_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_FU32BoundedVolumeHierarchy8_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->FU32BoundedVolumeHierarchy8_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_FUBoundedVolumeHierarchy2_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->FUBoundedVolumeHierarchy2_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_FUBoundedVolumeHierarchy4_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->FUBoundedVolumeHierarchy4_PyTypeObject = type;
    }

    {
        PyTypeObject *type = define_FUBoundedVolumeHierarchy8_type(module);
        if (!type){ goto error; }
        Py_INCREF(type);
        state->FUBoundedVolumeHierarchy8_PyTypeObject = type;
    }


    return module;
error:
    Py_CLEAR(module);
    return 0;
}


static PyObject *
get_module()
{
    PyObject *module = PyState_FindModule(&module_PyModuleDef);
    if (!module)
    {
        return PyErr_Format(PyExc_RuntimeError, "egeometry module not ready");
    }
    return module;
}
