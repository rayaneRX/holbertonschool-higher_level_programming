#!/usr/bin/python3


def roman_to_int(roman_string):
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    if type(roman_string) is not str or roman_string is None:
        return 0
    res = 0
    prv = 0
    roman_list = list(roman_string)
    for i in roman_list:
        if i in roman:
            val = roman[i]
            if val > prv:
                res += val - 2 * prv
            else:
                res += val
            prv = val
    return res
