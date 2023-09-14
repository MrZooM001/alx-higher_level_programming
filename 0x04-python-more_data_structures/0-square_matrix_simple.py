#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        second_dim = []
        for j in i:
            second_dim.append(j ** 2)
        new_matrix.append(second_dim)
    return new_matrix
