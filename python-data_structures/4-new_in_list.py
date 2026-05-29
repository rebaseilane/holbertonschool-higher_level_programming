#!/usr/bin/python3
"""
Replaces element in a copy of a list.
"""


def new_in_list(my_list, idx, element):
    """
    Returns a copy with replaced element if index valid.
    """
    new_list = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return new_list
    new_list[idx] = element
    return new_list
