#!/usr/bin/python3
"""Module to divides a matrix

This supplies one function, matrix_divided(). For example:
>>> matrix = [[1, 2, 3], [4, 5, 6]]
>>> matrix_divided(matrix, 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
"""


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix.

    Args:
        matrix (list): list of lists of integers/floats as matrix.
        div (int || float): number used to divide by.
    """
    if (not isinstance(matrix, list) or
        not all(isinstance(row, list) for row in matrix)
        or not all((isinstance(element, int) or (isinstance(element, float)))
                   for element in [n for row in matrix for n in row])):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [list(map(lambda n: round(n / div, 2), ro)) for ro in matrix]
    return new_matrix
