#!/usr/bin/python3
""" Pascal's Triangle """


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the specified number of rows.

    Parameters:
        n (int): The number of rows in Pascal's triangle.

    Returns:
        list: A list representing Pascal's triangle. Each row is represented
        as a list of integers.

    Example:
        >>> pascal_triangle(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]
        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)
        triangle.append(new_row)

    return triangle
