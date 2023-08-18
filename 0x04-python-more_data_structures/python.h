#ifndef PYTHON_H
#define PYTHON_H

#include <stddef.h>
#include <stdint.h>
#include <Python.h>

typedef struct _object PyObject;

typedef struct {
    PyObject *ob_refcnt;
    struct _typeobject *ob_type;
} PyObject_HEAD;

typedef struct _typeobject {
    const char *tp_name;
    size_t tp_basicsize;
} PyTypeObject;

typedef struct {
    PyObject_HEAD
    PyTypeObject *ob_type;
} PyListObject;

typedef struct {
    PyObject_HEAD
    size_t ob_size;
    char ob_sval[10];
} PyBytesObject;

typedef long Py_ssize_t;

#define PyBytes_Check(op) ((op)->ob_type == &PyBytes_Type)
#define PyList_Check(op) ((op)->ob_type == &PyList_Type)
#define PyTuple_Check(op) ((op)->ob_type == &PyTuple_Type)
#define PyFloat_Check(op) ((op)->ob_type == &PyFloat_Type)
#define PyLong_Check(op) ((op)->ob_type == &PyLong_Type)
#define PyUnicode_Check(op) ((op)->ob_type == &PyUnicode_Type)

#define PyBytes_Size(op) (((PyBytesObject *)(op))->ob_size)
#define PyBytes_AsString(op) (((PyBytesObject *)(op))->ob_sval)

#define PyList_Size(op) (((PyListObject *)(op))->ob_size)
#define PyList_GetItem(op, i) (((PyListObject *)(op))->ob_item[i])

extern PyTypeObject PyBytes_Type;
extern PyTypeObject PyList_Type;
extern PyTypeObject PyTuple_Type;
extern PyTypeObject PyFloat_Type;
extern PyTypeObject PyLong_Type;
extern PyTypeObject PyUnicode_Type;

PyObject *PyFloat_FromDouble(double v);
PyObject *PyLong_FromLong(long v);
PyObject *PyUnicode_FromString(const char *u);

#endif /* PYTHON_H */
