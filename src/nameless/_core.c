#include "Python.h"

static PyObject* main(PyObject *self, PyObject *value) {
    PyObject *module;
    PyObject *module_dict;
    PyObject *len;
    PyObject *max;
    PyObject *args;
    PyObject *kwargs;
    PyObject *result;
    module = PyImport_ImportModule("builtins");
    if (!module)
        return NULL;

    module_dict = PyModule_GetDict(module);
    len = PyDict_GetItemString(module_dict, "len");
    if (!len) {
        Py_DECREF(module);
        return NULL;
    }
    max = PyDict_GetItemString(module_dict, "max");
    if (!max) {
        Py_DECREF(module);
        return NULL;
    }
    Py_DECREF(module);

    args = PyTuple_New(1);
    if (!args) {
        return NULL;
    }
    Py_INCREF(value);
    PyTuple_SetItem(args, 0, value);

    kwargs = PyDict_New();
    if (!kwargs) {
        Py_DECREF(args);
        return NULL;
    }
    PyDict_SetItemString(kwargs, "key", len);

    result = PyObject_Call(max, args, kwargs);

    Py_DECREF(args);
    Py_DECREF(kwargs);

    return result;
}

PyDoc_STRVAR(main_doc, "Docstring for main function.");

static struct PyMethodDef module_functions[] = {
    {"main", main, METH_O, main_doc},
    {NULL, NULL}
};

static struct PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT,
    "nameless._core", /* m_name */
    NULL,             /* m_doc */
    -1,               /* m_size */
    module_functions, /* m_methods */
    NULL,             /* m_reload */
    NULL,             /* m_traverse */
    NULL,             /* m_clear */
    NULL,             /* m_free */
};

static PyObject* moduleinit(void) {
    PyObject *module;

    module = PyModule_Create(&moduledef);

    if (module == NULL)
        return NULL;

    return module;
}

PyMODINIT_FUNC PyInit__core(void) {
    return moduleinit();
}
