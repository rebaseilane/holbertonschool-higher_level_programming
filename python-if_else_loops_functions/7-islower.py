#!/usr/bin/python3
"""
Checks for lowercase characters.
"""


def islower(c):
    """
    Checks if a character is lowercase.

    Args:
        c: Character to check.

    Returns:
        True if lowercase, otherwise False.
    """
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    return False
