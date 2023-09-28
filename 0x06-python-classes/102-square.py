#!/usr/bin/python3
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

    def __eq__(self, square: object):
        """Overloading the default == operator
        to to define if two objects are equal"""
        return self.area() == square.area()

    def __ne__(self, square: object):
        """Overloading the default != operator
        to to define if two objects are not equal"""
        return self.area() != square.area()

    def __gt__(self, square: object):
        """Overloading the default > operator
        to to define if one objects is greater than other object"""
        return self.area() > square.area()

    def __ge__(self, square: object):
        """Overloading the default >= operator
        to to define if one objects is greater than or equal to other object"""
        return self.area() >= square.area()

    def __lt__(self, square: object):
        """Overloading the default < operator
        to to define if one objects is less than other object"""
        return self.area() < square.area()

    def __le__(self, square: object):
        """Overloading the default <= operator
        to to define if one objects is less than or equal to other object"""
        return self.area() <= square.area()
