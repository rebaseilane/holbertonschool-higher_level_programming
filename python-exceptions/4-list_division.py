#!/usr/bin/python3
"""Module for dividing two lists."""


def list_division(my_list_1, my_list_2, list_length):
    """Divide list elements and return a new list."""
    result = []

    for i in range(list_length):
        try:
            value = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            value = 0
        except TypeError:
            print("wrong type")
            value = 0
        except IndexError:
            print("out of range")
            value = 0
        finally:
            result.append(value)

    return result
