#!/usr/bin/python3
"""Module JSON string"""
import json


def from_json_string(my_str):
    """Return an object (Python data structure) represented by a JSON string.

    Args:
        my_str (str): JSON string.
    """
    json_str = json.loads(my_str)
    return json_str
