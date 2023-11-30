#!/usr/bin/python3
import sys

if __name__ == "__main__":
    add_up = len(sys.argv) - 1
    if add_up == 0:
        print("0 arguments.")
    elif add_up == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(add_up))
    for i in range(add_up):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
