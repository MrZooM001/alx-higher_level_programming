#!/usr/bin/python3
def number_keys(a_dictionary):
    count = 0
    for k, _ in a_dictionary.items():
        count += 1
    return count
