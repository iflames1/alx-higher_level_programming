#!/usr/bin/pythhon3

def square_matrix_simple(matrix=[]):
    def square(x):
        return x * x
    new_matrix = [[square(element) for element in row] for row in matrix]
    '''
    new_matrix = []
    for row in matrix:
        new_row = [square(element) for element in row]
        new_matrix.append(new_row)
    '''
    return new_matrix
