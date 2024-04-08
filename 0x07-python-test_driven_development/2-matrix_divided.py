#!/usr/bin/python3
""" module for matrix_divided() method """


def matrix_divided(matrix, div):
    """ Divides two lists.

    Args:
        matrix: a list of two list of integer or float
        div: the divisor
    Raises:
        TypeError:
            - if matrix isn't list of list(s)
            - if row in matrix isn't list
            - if div is not int or float.
        ZeroDivisionError: if div is 0

    Returns (list): Division of list in matrix
    """
    if not all(isinstance(row, list)
               and all(isinstance(num, (int, float)) for num in row)
               for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = [[round(num / div, 2) for num in row] for row in matrix]

    return result
