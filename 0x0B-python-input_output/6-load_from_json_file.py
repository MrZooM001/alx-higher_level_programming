#!/usr/bin/python3
"""Module JSON - load from file"""
import json


def load_from_json_file(filename):
    """Load an object from a JSON file.

    Args:
        filename (str): JSON file name
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
