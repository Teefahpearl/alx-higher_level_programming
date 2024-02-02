#!/usr/bin/python3
"""Define div function"""


def matrix_divided(matrix, div):
    """
    Divide matrix by a number
    """
    if not isinstance(matrix, list) or not \
            all(isinstance(i, list) for i in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) \
            of integers/floats"
        )
    for i in matrix:
        if not all(isinstance(obj, (int, float)) for obj in i):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )
    if not all(len(i) == len(matrix[0]) for i in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(obj / div, 2) for obj in i] for i in matrix]
