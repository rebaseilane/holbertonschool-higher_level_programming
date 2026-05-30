#!/usr/bin/python3
"""
Module that converts class object to dictionary.
"""


def class_to_json(obj):
    """Returns dictionary of serializable attributes."""
    return obj.__dict__
