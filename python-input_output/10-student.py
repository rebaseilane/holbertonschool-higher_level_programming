#!/usr/bin/python3
"""
Student class with filtering.
"""


class Student:
    """Defines a student."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns filtered dictionary representation."""
        if attrs is None:
            return self.__dict__

        filtered = {}
        for key in attrs:
            if key in self.__dict__:
                filtered[key] = self.__dict__[key]
        return filtered
