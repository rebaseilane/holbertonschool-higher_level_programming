#!/usr/bin/python3
"""
Prints a string in uppercase.
"""


def uppercase(str):
    """
    Prints a string in uppercase.

    Args:
        str: String to convert.
    """
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print("")
