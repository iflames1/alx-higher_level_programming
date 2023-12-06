#!/usr/bin/pythhon3

def square_matrix_simple(matrix=[]):
    if matrix:
        new_matrix = [[element ** 2 for element in row] for row in matrix]
        return new_matrix
