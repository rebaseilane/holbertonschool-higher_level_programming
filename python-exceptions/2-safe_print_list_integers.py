#!/usr/bin/python3
"""Module for safe printing of integers in a list."""


def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements and count integers."""
    count = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (TypeError, ValueError):
            pass

    print()
    return count
