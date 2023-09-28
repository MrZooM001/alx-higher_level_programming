#!/usr/bin/python3
import sys
"""A class to defines a square with a size"""


class Square:
    """A class to defines a square with a size"""
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
        sqr_area = self.__size ** 2
        return sqr_area

    @property
    def size(self):
        """Get the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set a new size's value of the square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size, file=sys.stdout)
