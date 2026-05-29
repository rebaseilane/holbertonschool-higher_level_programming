#!/usr/bin/python3
"""
Removes all 'c' and 'C' characters from a string.
"""


def no_c(my_string):
    """
    Returns string without c and C.
    """
    new_str = ""
    for ch in my_string:
        if ch != 'c' and ch != 'C':
            new_str += ch
    return new_str
