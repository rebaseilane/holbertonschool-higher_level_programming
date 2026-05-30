#!/usr/bin/python3
"""Module for unique elements between sets."""


def only_diff_elements(set_1, set_2):
    """Return elements present in only one set."""
    return set_1 ^ set_2
