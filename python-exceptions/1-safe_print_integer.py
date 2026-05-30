#!/usr/bin/python3
"""Module for safe integer printing."""


def safe_print_integer(value):
    """Print an integer and return True, otherwise False."""
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
