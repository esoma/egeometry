#ifndef EGEOMETRY_MODULESTATE_H
#define EGEOMETRY_MODULESTATE_H

#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include "_module.h"

struct ModuleState
{
    int dummy;
};


static int
ModuleState_traverse(
    struct ModuleState *self,
    visitproc visit,
    void *arg
)
{
    return 0;
}


static int
ModuleState_clear(struct ModuleState *self)
{
    return 0;
}


static struct ModuleState *
get_module_state()
{
    PyObject *module = get_module();
    if (!module){ return 0; }
    return (struct ModuleState *)PyModule_GetState(module);
}

#endif
