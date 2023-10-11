#!/usr/bin/python3
"""Module JSON - object to file"""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file as JSON.

    Args:
        my_obj (object): an object to be written in a file
        filename (str): file name that will be write
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
