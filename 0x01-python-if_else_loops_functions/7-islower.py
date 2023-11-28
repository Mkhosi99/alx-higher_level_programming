#!/usr/bin/python3
"function checks for lowercase character"

def islower(ch):
    if ord(ch) >= 97 and ord(ch) <= 122:
        return True
    else:
        return False
