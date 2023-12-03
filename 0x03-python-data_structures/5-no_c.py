#!/usr/bin/python3
def no_c(my_string):
    string_var = ""
    for x in my_string:
        if x not in "cC":
            string_var += x
    return string_var
