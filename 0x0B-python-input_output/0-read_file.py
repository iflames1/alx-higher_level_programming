#!/usr/bin/python3
"""Defines a function read_file."""


def read_file(filename=""):
    """Read a text file (UTF8) and print it to stdout.

    Args:
        filename (str): The name of the text file.
    """
    with open(filename, 'r', encoding="utf-8") as file:
        print(file.read(), end="")
