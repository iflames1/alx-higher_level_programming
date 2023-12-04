#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    new_list = my_list[:]
    if new_list:
        new_list.reverse()
        for num in new_list:
            print("{:d}".format(num))
