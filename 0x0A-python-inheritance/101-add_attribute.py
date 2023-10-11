#!/usr/bin/python3
"""Module presents a class"""


def add_attribute(obj, attribute, value):
    """Set attribute to an object if possible"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(obj, attribute, value)
