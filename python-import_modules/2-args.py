#!/usr/bin/python3
"""
Prints the number of arguments and their values.
"""

if __name__ == "__main__":
    from sys import argv

    argc = len(argv) - 1

    if argc == 0:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(argc, "" if argc == 1 else "s"))

        for i in range(1, argc + 1):
            print("{}: {}".format(i, argv[i]))
