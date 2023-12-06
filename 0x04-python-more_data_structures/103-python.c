#include <Python.h>

void print_python_list(PyObject *p) {
    Py_ssize_t size, i;
    PyObject *item;

    size = PyList_Size(p);

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++) {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    unsigned char *bytes;

    if (!PyBytes_Check(p)) {
        fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    bytes = (unsigned char *)PyBytes_AsString(p);

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", (char *)bytes);

    printf("  first %ld bytes: ", size > 10 ? 10 : size);
    for (i = 0; i < (size > 10 ? 10 : size); i++) {
        printf("%02x ", bytes[i]);
    }
    printf("\n");
}
