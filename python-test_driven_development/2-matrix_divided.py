#!/usr/bin/python3
"""Module that divides a matrix."""


def matrix_divided(matrix, div):
    """Return a new matrix divided by div."""
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if (not isinstance(matrix, list) or
        not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    size = len(matrix[0])
    for row in matrix:
        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")
        for item in row:
            if type(item) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    return [[round(item / div, 2) for item in row] for row in matrix]
