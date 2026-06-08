#!/usr/bin/python3
"""Module that defines MyList class."""


class MyList(list):

    def print_sorted(self):
        print(sorted(self))
