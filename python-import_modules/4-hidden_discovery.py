#!/usr/bin/python3
"""
Prints names defined in compiled module hidden_4.pyc.
"""

if __name__ == "__main__":
    import hidden_4

    names = dir(hidden_4)

    for name in sorted(names):
        if name[:2] != "__":
            print(name)
