#!/usr/bin/python3
"""
Module that writes an object to a JSON file.
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes object to file using JSON representation."""
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
