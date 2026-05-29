#!/usr/bin/python3
"""
Prints all integers of a list.
"""


def print_list_integer(my_list=[]):
    """
    Prints each integer in a list on a new line.
    """
    for i in my_list:
        print("{:d}".format(i))
