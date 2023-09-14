#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dict = {k: v for k, v in a_dictionary.items() if v == value}
    for key, v in new_dict.items():
        del a_dictionary[key]
    return a_dictionary
