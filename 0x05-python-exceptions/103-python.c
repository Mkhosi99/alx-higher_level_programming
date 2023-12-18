#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Function prints basic info about Python lists.
 * @p: A PyObject list object.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t l_size, l_alloc, x;
	const char *l_type;
	PyListObject *p_list = (PyListObject *)p;
	PyVarObject *l_var = (PyVarObject *)p;

	l_size = l_var->ob_size;
	l_alloc = p_list->allocated;

	fflush(stdout);

	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Size of the Python List = %ld\n", l_size);
	printf("[*] Allocated = %ld\n", l_alloc);

	for (x = 0; x < l_size; x++)
	{
		l_type = p_list->ob_item[x]->ob_type->tp_name;
		printf("Element %ld: %s\n", x, l_type);
		if (strcmp(l_type, "bytes") == 0)
			print_python_bytes(p_list->ob_item[x]);
		else if (strcmp(l_type, "float") == 0)
			print_python_float(p_list->ob_item[x]);
	}
}

/**
 * print_python_bytes - Fuction prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t b_size, x;
	PyBytesObject *b_bytes = (PyBytesObject *)p;

	fflush(stdout);

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", b_bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size >= 10)
		b_size = 10;
	else
		b_size = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %ld bytes: ", b_size);
	for (x = 0; x < b_size; x++)
	{
		printf("%02hhx", b_bytes->ob_sval[x]);
		if (x == (b_size - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_float - Function prints basic info about Python float objects.
 * @p: A PyObject float object.
 */
void print_python_float(PyObject *p)
{
	char *bufr = NULL;

	PyFloatObject *f_obj = (PyFloatObject *)p;

	fflush(stdout);

	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	bufr = PyOS_double_to_string(f_obj->ob_fval, 'r', 0,
			Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", bufr);
	PyMem_Free(bufr);
}
