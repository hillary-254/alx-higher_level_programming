#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
# variable initialization. prev_val will keep track of value during iteration
# result will store the final int value
    prev_value = 0
    result = 0

    for char in roman_string[::-1]:
        value = roman_dict.get(char, 0)

        if value >= prev_value:
            result += value
        else:
            result -= value

        prev_value = value

    return result
