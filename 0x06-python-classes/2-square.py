#!/usr/bin/python3
"""A class to defines a square with a size based on 1-square.py"""


class Square:
    """A class to defines a square with a size based on 1-square.py"""
    def __init__(self, size=0):
        """Initialization of the square
        Attributes:
        size (int): represents size of square"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
