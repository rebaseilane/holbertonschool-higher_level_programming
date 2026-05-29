#!/usr/bin/python3
"""
Prints a matrix of integers.
"""


def print_matrix_integer(matrix=[[]]):
    """
    Prints a matrix row by row.
    """
    if matrix == [[]]:
        print()
        return

    for row in matrix:
        for i in range(len(row)):
            if i == len(row) - 1:
                print("{:d}".format(row[i]), end="")
            else:
                print("{:d}".format(row[i]), end=" ")
        print()
