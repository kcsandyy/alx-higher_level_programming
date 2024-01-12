#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    number = 0
    prev_num = 0
    for c in reversed(roman_string):
        value = roman_dict[c]
        if value < prev_num:
            number -= value
        else:
            number += value
        prev_num = value
    return number
