#!/usr/bin/python3
"""Module to define a base class"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method that return the JSON string representation
        of 'list_dictionaries'

        Args:
            list_dictionaries (list): list of dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """class method that writes the JSON string representation
        of 'list_objs' to a file

        Args:
            list_objs (list): list of instances who inherits of Base class
        """
        file_name = "{}.json".format(cls.__name__)
        with open(file_name, 'w', encoding="utf-8") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [j.to_dictionary() for j in list_objs]
                file.write(Base.to_json_string(list_dicts))
