//
// Created by andreas on 4/3/16.
//

#include <Python.h>
#include "fib.h"

static PyObject *fib_fib_rec(PyObject *self, PyObject *args) {
    unsigned long int n;
    unsigned long int result;

    if (!PyArg_ParseTuple(args, "l", &n)) {
        return NULL;
    }

    result = fib_rec(n);
    return Py_BuildValue("i", result);
}

static PyObject *fib_fib_it(PyObject *self, PyObject *args) {
    unsigned long int n;
    unsigned long int result;

    if (!PyArg_ParseTuple(args, "l", &n)) {
        return NULL;
    }

    result = fib_it(n);
    return Py_BuildValue("l", result);
}


static PyMethodDef pyfib_methods[] = {
        //"PythonName"  C0function name,    argument presentation,  description
        {"fib_rec", fib_fib_rec, METH_VARARGS, "return score only"},
        {"fib_it",  fib_fib_it,  METH_VARARGS, "return score only"},
        {NULL,      NULL,        0,            NULL}  /*Sentinel*/
};

static struct PyModuleDef extfib = {
        PyModuleDef_HEAD_INIT,
        "pyfib", /* name of module */
        "",          /* module documentation, may be NULL */
        -1,          /* size of per-interpreter state of the module, or -1 if the module keeps state in global variables. */
        pyfib_methods
};

PyMODINIT_FUNC
PyInit_ext_fib(void) {
    return PyModule_Create(&extfib);
}