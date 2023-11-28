#!/usr/bin/python3

def uppercase(str):
    for m in str:
        cha = ord(m)
        if cha >= 97 and cha <= 122:
            cha -= 32
        print("{:c}".format(cha), end="")
    print()
