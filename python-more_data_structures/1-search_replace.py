#!/usr/bin/python3
"""Module for search and replace in a list."""


def search_replace(my_list, search, replace):
    """Return a new list with replaced values."""
    return [replace if item == search else item for item in my_list]
