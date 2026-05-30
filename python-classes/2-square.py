#!/usr/bin/python3
"""Module that defines a Square with validation."""


class Square:
    """Square class with size validation."""

    def __init__(self, size=0):
        """Initialize square and validate size."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
