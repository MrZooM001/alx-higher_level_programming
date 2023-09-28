#!/usr/bin/python3
"""A class to defines a square with a size based on 2-square.py"""


class Square:
    """A class to defines a square with a size based on 2-square.py"""
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

    def area(self):
        """Get and return the area of the square"""
        sqr_area = self.__size ** 2
        return sqr_area
