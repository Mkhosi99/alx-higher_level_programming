#include "Python.h"

/**
 * print_python_list_info - Prints information about python objects
 * @p: PyObject pointer to print info about
 * Compile with:
 * gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared
 (* -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4
 (* 100-print_python_list_info.c
*/

void display_python_list_info(PyObject *python_list)
{
    Py_ssize_t index, list_size;
    PyObject *list_item;
    const char *element_type;
    PyListObject *list_object;

    list_object = (PyListObject *)python_list;
    list_size = PyList_Size(python_list);

    printf("[*] Size of the Python List = %d\n", (int)list_size);
    printf("[*] Allocated = %d\n", (int)list_object->allocated);

    for (index = 0; index < list_size; index++)
    {
        list_item = PyList_GetItem(python_list, index);
        element_type = Py_TYPE(list_item)->tp_name;
        printf("Element %d: %s\n", (int)index, element_type);
    }
}

