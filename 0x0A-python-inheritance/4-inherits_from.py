#!/usr/bin/python3
"""Module to check for an instance of a class or its ancestors"""


def inherits_from(obj, a_class):
    """Function to check if an object is an instance of a class or its parent
    or its ancestors.

    Args:
        obj (object): an object to check for
        a_class (class): class to check with
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True

    return False
