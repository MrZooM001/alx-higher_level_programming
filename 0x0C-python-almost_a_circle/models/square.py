#!/usr/bin/python3
"""Module to define a base class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class to represent a Square model
    with inheritance from Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new instance of Square class

        Args:
            size (int): size of square
            x (int): x axis of square
            y (int): y axis of square
            id (int): id of the instantiated instance
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Retrieve square's width and height"""
        return self.height

    @size.setter
    def size(self, value):
        """Set rectangle's width

        Args:
            value (int): value passed to set as new width and height
        """
        self.width = value
        self.height = value

    def __str__(self):
        """Return a formated printable representation of the Square"""
        result = "[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__, self.id, self.x, self.y, self.size
        )
        return result

    def update(self, *args, **kwargs):
        """Update the class by assigning an argument to each attribute

        Args:
            args (tuple): unknown arguments count
            kwargs (dict): keyworded arguments with unknown count.
        """
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y, self.id)
                    else:
                        self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
                i += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y, self.id)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Return the dictionary representation of the Rectangle"""
        square_dict = {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
        return square_dict
