#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include "lists.h"

/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: pointer to python object.
 *
 * Return: Void.
 */
void print_python_list_info(PyObject *p)
{
PyListObject *py_list;
PyObject *object;
Py_ssize_t i;

py_list = (PyListObject *)p;
printf("[*] Size of the Python List = %d\n", (int)Py_SIZE(py_list));
printf("[*] Allocated = %d\n", (int)py_list->allocated);
i = 0;
while (i < Py_SIZE(py_list))
{
object = PyList_GetItem(p, i);
if (object != NULL)
printf("Element %d: %s\n", (int)i, object->ob_type->tp_name);
i++;
}
}
