#!/usr/bin/python3
"""
Module for pickling and unpickling custom objects.
"""
import pickle


class CustomObject:
    """Custom object with serialization support."""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints object attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serializes object to a file using pickle."""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Loads object from pickle file."""
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None
