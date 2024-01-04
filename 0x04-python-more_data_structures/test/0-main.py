#!/usr/bin/python3
import sys
sys.path.append('..')

path = __import__('0-square_matrix_simple').square_matrix_simple
square_matrix_simple = path

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)
