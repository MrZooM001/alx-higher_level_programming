#!/usr/bin/python3
"""Module to check for instance"""


def is_same_class(obj, a_class):
    """Function to check if an object is an instance of a class.

    Args:
        obj (object): an object to check for
        a_class (class): class that check with
    """
    if type(obj) == a_class:
        return True

    return False
