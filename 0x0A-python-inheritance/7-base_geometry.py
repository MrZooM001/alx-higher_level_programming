#!/usr/bin/python3
"""Module presents MyList class"""


class BaseGeometry():
    """A class that inherits from 'list' object"""

    def __init__(self) -> None:
        """Initialization of BaseGeometry class"""
        pass

    def area(self):
        """Function to get the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function to validate value's type"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
