#!/usr/bin/python3
"""Module insert a line to a file"""


def append_after(filename="", search_string="", new_string=""):
    """Initialization of inserting a line of text to a file
    after each line containing a specific string.

    Args:
        filename (str): file name
        search_string (str): text to seach for
        new_string (str): text to replaced when found
    """
    current_string = ""
    with open(filename, encoding="utf-8") as fr:
        for line in fr:
            current_string += line
            if search_string in line:
                current_string += new_string

    with open(filename, "w", encoding="utf-8") as fw:
        fw.write(current_string)
