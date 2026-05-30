#!/usr/bin/python3
"""Module for printing a sorted dictionary."""


def print_sorted_dictionary(a_dictionary):
    """Print a dictionary ordered by keys."""
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
