#!/usr/bin/python3
""" Module that defines a class MyList. """


class MyList(list):
    """ A class that inherits from list. """

    def print_sorted(self):
        """ Print the list sorted in ascending order. """
        sorted_list = sorted(self)
        if sorted_list:
            print(sorted_list)
