#!/usr/bin/python3
def roman_to_int(roman_string):
    rom_num = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if (roman_string is None) or (type(roman_string) is not str):
        return 0

    numb = len(roman_string)
    int_val = rom_num[roman_string[numb-1]]
    for i in range(numb - 1, 0, -1):
        currnt_val = rom_num[roman_string[i]]
        prev_val = rom`_num[roman_string[i-1]]

        if prev_val >= currnt_val:
            int_val += prev_val
        else:
            int_val -= prev_val

    return int_val
