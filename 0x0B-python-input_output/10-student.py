#!/usr/bin/python3
"""Module represent Student"""


class Student:
    """A student class"""

    def __init__(self, first_name, last_name, age):
        """Initialization of Student class.

        Args:
            first_name (str): student first name
            last_name (str): student last name
            age (int): student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student"""
        if (type(attrs) == list and
                all(type(element) == str for element in attrs)):
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}

        return self.__dict__
