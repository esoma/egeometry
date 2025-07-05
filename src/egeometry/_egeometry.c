
// generated from codegen/templates/_egeometry.c

#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <structmember.h>
#include "_modulestate.h"


static PyMethodDef module_methods[] = {
    {0, 0, 0, 0}
};


static int
module_traverse(PyObject *self, visitproc visit, void *arg)
{
    struct ModuleState *state = (struct ModuleState *)PyModule_GetState(self);
    return ModuleState_traverse(state, visit, arg);
}


static int
module_clear(PyObject *self)
{
    struct ModuleState *state = (struct ModuleState *)PyModule_GetState(self);
    return ModuleState_clear(state);
}


static struct PyModuleDef module_PyModuleDef = {
    PyModuleDef_HEAD_INIT,
    "egeometry._egeometry",
    0,
    sizeof(struct ModuleState),
    module_methods,
    0,
    module_traverse,
    module_clear
};


PyMODINIT_FUNC
PyInit__egeometry()
{
    PyObject *module = PyModule_Create(&module_PyModuleDef);
    struct ModuleState *state = 0;
    if (!module){ goto error; }
    if (PyState_AddModule(module, &module_PyModuleDef) == -1){ goto error; }
    state = (struct ModuleState *)PyModule_GetState(module);

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
