#!/usr/bin/python3
"""Module that checks subclass inheritance."""


def inherits_from(obj, a_class):
    """Return True if obj inherits from a_class.

    Args:
        obj: Object to inspect.
        a_class: Parent class.

    Returns:
        bool: True or False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
