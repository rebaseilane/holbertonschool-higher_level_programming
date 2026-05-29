#!/usr/bin/python3
"""
Prints the last digit of a number.
"""


def print_last_digit(number):
    """
    Prints the last digit of a number.

    Args:
        number: Number to process.

    Returns:
        The last digit of the number.
    """
    last_digit = abs(number) % 10
    print("{}".format(last_digit), end="")
    return last_digit
