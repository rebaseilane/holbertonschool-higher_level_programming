#!/usr/bin/python3
"""
Replaces element in a list at a specific position.
"""


def replace_in_list(my_list, idx, element):
    """
    Replaces element if index is valid.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
