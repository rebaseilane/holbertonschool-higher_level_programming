#!/usr/bin/python3
"""Module that defines Square and prints it."""


class Square:
    """Square class with printing capability."""

    def __init__(self, size=0):
        """Initialize square."""
        self.size = size

    @property
    def size(self):
        """Get size."""
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
        """Return area."""
        return self.__size ** 2

    def my_print(self):
        """Print square using #."""
        if self.__size == 0:
            print("")
            return

        for i in range(self.__size):
            print("#" * self.__size)
