#!/usr/bin/python3

def remove_char_at(str, n):
    frsh = ""
    x = 0
    for m in str:
        if x != n:
            frsh += m
        x += 1
    return frsh
