#!/usr/bin/python3
"""
Returns length of string and first character.
"""


def multiple_returns(sentence):
    """
    Returns tuple (length, first character or None).
    """
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
