#!/usr/bin/python3
"""Module that write to a file.

This supplies one function, write_file().
"""


def write_file(filename="", text=""):
    """Function that write a string to file.

    Args:
        filename (str): file to be write to.
        text (str): text to be written.
    """

    with open(filename, 'w', encoding="utf-8") as f:
        return(f.write(text))
