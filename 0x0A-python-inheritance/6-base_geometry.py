#!/usr/bin/python3
"""Module presents MyList class"""


class BaseGeometry():
    """A class that inherits from 'list' object"""

    def __init__(self) -> None:
        pass

    def area(self):
        raise Exception("area() is not implemented")
