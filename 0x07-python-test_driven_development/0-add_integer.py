#!/usr/bin/python3
"""Module to add integers

This supplies one function, add_integer(). For example:
>>> add_integer(5, 7)
12
"""


def add_integer(a, b=98):
    """Function that adds 2 integers.
    
    Args:
        a (int): first operand.
        b (int): second operand with default value.
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
