#!/usr/bin/python3
"""Module that prints text with indentation."""


def text_indentation(text):
    """Print text with 2 new lines after ., ? and :"""
    if type(text) is not str:
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            while i + 1 < len(text) and text[i + 1] == " ":
                i += 1
        i += 1
