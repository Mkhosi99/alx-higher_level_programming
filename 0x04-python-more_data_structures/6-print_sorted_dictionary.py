#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for order in sorted(a_dictionary.keys()):
        print("{}: {}".format(order, a_dictionary[order]))
