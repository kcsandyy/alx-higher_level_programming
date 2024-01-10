#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    dup = [row[:] for row in matrix]
    new_matrix = [[x**2 for x in row] for row in dup]
    return new_matrix
