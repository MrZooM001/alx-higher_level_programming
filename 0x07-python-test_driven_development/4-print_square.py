#!/usr/bin/python3
"""Module to print a square

This supplies one function, print_square(). For example:
>>> print_square(4)
####
####
####
####
"""


def print_square(size):
    """Function that prints a square with a character

    Args:
        size (int): size length of the square
    """
    if not isinstance(size, int) or (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print()
