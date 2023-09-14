#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_keys =  list(a_dictionary.keys())
    sorted_keys.sort()
    sorted_dict = {i: a_dictionary.get(i) for i in sorted_keys}
    print(sorted_dict)
