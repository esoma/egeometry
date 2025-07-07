
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
{% for type in types %}
    PyTypeObject *{{ type }}_PyTypeObject;
{% endfor %}
};


static int
ModuleState_traverse(
    ModuleState *self,
    visitproc visit,
    void *arg
)
{
{% for type in types %}
    Py_VISIT(self->{{ type }}_PyTypeObject);
{% endfor %}
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
{% for type in types %}
    Py_CLEAR(self->{{ type }}_PyTypeObject);
{% endfor %}
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
