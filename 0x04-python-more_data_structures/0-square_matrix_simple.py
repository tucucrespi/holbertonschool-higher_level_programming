#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    copy_matrix = []
    for i in matrix:
        copy_matrix.append(list(map(lambda x: x ** 2, i)))
    return copy_matrix
