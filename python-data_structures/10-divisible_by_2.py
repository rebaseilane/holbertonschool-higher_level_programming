#!/usr/bin/python3
"""
Checks if elements are divisible by 2.
"""


def divisible_by_2(my_list=[]):
    """
    Returns list of booleans.
    """
    result = []
    for i in my_list:
        if i % 2 == 0:
            result.append(True)
        else:
            result.append(False)
    return result
