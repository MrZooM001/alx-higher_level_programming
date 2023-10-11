#!/usr/bin/python3
"""Module JSON serialization"""


def class_to_json(obj):
    """Returns dictionary description for JSON serialization of an object

    Args:
        obj (object): an instance of a class
    """
    dc = obj.__dict__
    return dc
