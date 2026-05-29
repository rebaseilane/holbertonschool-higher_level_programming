#!/usr/bin/python3
"""
Imports a function from another file and prints the result of addition.
"""

if __name__ == "__main__":
    add = __import__("add_0").add
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
