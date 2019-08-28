
#include "Python.h"

static PyObject* longest(PyObject *self, PyObject *value) {
    PyObject *module;
    PyObject *module_dict;
    PyObject *len;
    PyObject *max;
    PyObject *args;
    PyObject *kwargs;
    PyObject *result;

    #if PY_MAJOR_VERSION < 3
      module = PyImport_ImportModule("__builtin__");
    #else
      module = PyImport_ImportModule("builtins");
    #endif
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

PyDoc_STRVAR(longest_doc, "Docstring for longest function.");

static struct PyMethodDef module_functions[] = {
    {"longest", longest, METH_O, longest_doc},
    {NULL, NULL}
};

#if PY_MAJOR_VERSION >= 3
static struct PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT,
    "nameless._nameless", /* m_name */
    NULL,             /* m_doc */
    -1,               /* m_size */
    module_functions, /* m_methods */
    NULL,             /* m_reload */
    NULL,             /* m_traverse */
    NULL,             /* m_clear */
    NULL,             /* m_free */
};
#endif

static PyObject* moduleinit(void) {
    PyObject *module;

#if PY_MAJOR_VERSION >= 3
    module = PyModule_Create(&moduledef);
#else
    module = Py_InitModule3("nameless._nameless", module_functions, NULL);
#endif

    if (module == NULL)
        return NULL;

    return module;
}

#if PY_MAJOR_VERSION < 3
PyMODINIT_FUNC init_nameless(void) {
    moduleinit();
}
#else
PyMODINIT_FUNC PyInit__nameless(void) {
    return moduleinit();
}
#endif

