#!/usr/bin/python3
"""Module that defines BaseGeometry class."""


class BaseGeometry:
    """BaseGeometry class."""

    def area(self):
        """Raise an exception indicating area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate an integer value.

        Args:
            name (str): Attribute name.
            value (int): Value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to zero.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
