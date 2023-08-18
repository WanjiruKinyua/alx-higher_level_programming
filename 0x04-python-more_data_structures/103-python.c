#include <Python.h>
#include <listobject.h>
#include <object.h>
#include <bytesobject.h>

/**
 * print_python_bytes - Entry point
 *
 * Description: prints python bytes
 *
 * @p: PyObject pointer
 *
 * Return: void
 */
void print_python_bytes(PyObject *py_bytes)
{
	long int bytes_size, i;

	printf("[.] bytes object info\n");
	if (PyBytes_CheckExact(py_bytes))
	{
		bytes_size = PyBytes_Size(py_bytes);
		printf("  size: %ld\n", bytes_size);
		printf("  trying string: %s\n", PyBytes_AsString(py_bytes));
		if (bytes_size >= 10)
			bytes_size = 10;
		else
			bytes_size++;
		printf("  first %ld bytes:", bytes_size);
		for (i = 0; i < bytes_size; i++)
			printf(" %02x", (int) PyBytes_AsString(py_bytes)[i] & 0xff);
		printf("\n");
	}
	else
		printf("  [ERROR] Invalid Bytes Object\n");
}

/**
 * print_python_list - Entry point
 *
 * Description: prints basic info about Python lists
 *
 * @p: PyObject pointer
 *
 * Return: void
 */
void print_python_list(PyObject *py_list)
{
	long int list_size = PyList_GET_SIZE(py_list), list_index;
	PyObject *list_item;
	PyListObject *list_object = (PyListObject *) py_list;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", list_object->allocated);

	for (list_index = 0; list_index < list_size; list_index++)
	{
		list_item = PyList_GET_ITEM(py_list, list_index);
		printf("Element %ld: %s\n", list_index,
				list_item->ob_type->tp_name);
		if (PyBytes_CheckExact(list_item))
			print_python_bytes(list_item);
	}
}
