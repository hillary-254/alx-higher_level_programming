#!/usr/bin/python3
"""
A module to prints a list in ascending order
"""


class MyList(list):
    """
    customizes the list class
    """

    def print_sorted(self):
        """
        Prints list in ascending order

        Sorts list and then prints on the output
        """

        sort_list = sorted(self)
        print(sort_list)
