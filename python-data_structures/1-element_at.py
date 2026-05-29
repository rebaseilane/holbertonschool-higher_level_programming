#!/usr/bin/python3
"""
Retrieves an element from a list safely.
"""


def element_at(my_list, idx):
    """
    Returns element at index if valid, otherwise None.
    """
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
