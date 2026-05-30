#!/usr/bin/python3
"""Module that defines Square with property."""


class Square:
    """Square class with getter and setter."""

    def __init__(self, size=0):
        """Initialize square."""
        self.size = size

    @property
    def size(self):
        """Retrieve size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size with validation."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return square area."""
        return self.__size ** 2
