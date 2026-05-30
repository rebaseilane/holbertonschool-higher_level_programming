#!/usr/bin/python3
"""Module that checks instance inheritance."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or inherits from it.

    Args:
        obj: Object to inspect.
        a_class: Class to compare.

    Returns:
        bool: True or False.
    """
    return isinstance(obj, a_class)
