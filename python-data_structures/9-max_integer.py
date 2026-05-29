#!/usr/bin/python3
"""
Finds the biggest integer in a list.
"""


def max_integer(my_list=[]):
    """
    Returns max integer or None if empty list.
    """
    if len(my_list) == 0:
        return None

    max_val = my_list[0]
    for i in my_list:
        if i > max_val:
            max_val = i

    return max_val
