#!/usr/bin/python3
"""Module to check for an instance of a class or its parent"""


def is_kind_of_class(obj, a_class):
    """Function to check if an object is an instance of a class or its parent.

    Args:
        obj (object): an object to check for
        a_class (class): class to check with
    """
    return isinstance(obj, a_class)
