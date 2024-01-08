#!/usr/bin/python3
"""
Creates a class inheriting from Mylist class
"""


class MyList(list):
    """Class MyList inherits from list"""

    def print_sorted(self):
        """Function Prints the list in ascending order"""

        new_list = self[:]
        new_list.sort()
        print("{}".format(new_list))
