#!/usr/bin/python3
"""Module that checks exact class instances."""


def is_same_class(obj, a_class):
    """Return True if obj is exactly an instance of a_class.

    Args:
        obj: Object to inspect.
        a_class: Class to compare.

    Returns:
        bool: True or False.
    """
    return type(obj) is a_class
