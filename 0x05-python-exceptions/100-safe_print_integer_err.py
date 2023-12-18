#!/usr/bin/python3
from sys import stderr

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except ValueError as ve:
        print("Exception:", ve, file=stderr)
        return False
    return True
