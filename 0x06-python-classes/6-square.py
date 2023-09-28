#!/usr/bin/python3
"""A class to defines a square with a size and a position"""


class Square:
    """A class to defines a square with a size and a position"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialization of the square
        Attributes:
        size (int): represents size of square"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
            self.__position = position

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
            for space in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

    @property
    def position(self):
        """Get the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set a new position's values of the square"""
        if not (isinstance(self.__position, tuple) or len(self.__position) != 2
                or type(self.__position[0]) is not int
                or type(self.__position[1]) is not int
                or self.__position[0] < 0 or self.__position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
