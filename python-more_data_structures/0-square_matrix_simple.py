#!/usr/bin/python3
"""Module for squaring matrix values."""


def square_matrix_simple(matrix=[]):
    """Return a new matrix with squared values."""
    return [[value ** 2 for value in row] for row in matrix]
