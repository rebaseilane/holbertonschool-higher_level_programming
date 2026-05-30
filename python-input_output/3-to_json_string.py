#!/usr/bin/python3
"""
Module that converts Python object to JSON string.
"""
import json


def to_json_string(my_obj):
    """Returns JSON string representation of object."""
    return json.dumps(my_obj)
