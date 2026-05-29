#!/usr/bin/python3
"""
Prints a list of integers in reverse.
"""


def print_reversed_list_integer(my_list=[]):
    """
    Prints integers in reverse order.
    """
    if my_list:
        for i in reversed(my_list):
            print("{:d}".format(i))
