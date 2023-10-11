#!/usr/bin/python3
"""Module as Script to add arguments to Python list
and save them to a file"""
import sys

if __name__ == "__main__":
    save_json = __import__('5-save_to_json_file').save_to_json_file
    load_json = __import__('6-load_from_json_file').load_from_json_file
    filename = "add_item.json"
    try:
        args = load_json(filename)
    except FileNotFoundError:
        args = []

    args.extend(sys.argv[1:])
    save_json(args, filename)
