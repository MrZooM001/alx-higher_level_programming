#!/usr/bin/python3
"""Module to define a base class"""


class Base:
    """Class to represent a Base model for all classes

    Attributes:
        __nb_objects (int): Count created instances
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Method to initialize a new instance of Base class

        Args:
            id (int): id of the instantiated instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
