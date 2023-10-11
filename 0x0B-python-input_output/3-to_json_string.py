#!/usr/bin/python3
"""Module to get JSON representation of a string"""
import json


def to_json_string(my_obj):
    """JSON representation of an object (string).

    Args:
        my_obj (str): string object to get JSON representation of.
    """
    str_json = json.dumps(my_obj)
    return str_json
