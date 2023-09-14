#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    else:
        roman_chars = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        converted_num, previous_value = 0, 0
        for numeral in reversed(roman_string):
            value = roman_chars.get(numeral, 0)
            if value < previous_value:
                converted_num -= value
            else:
                converted_num += value
            previous_value = value
    return converted_num
