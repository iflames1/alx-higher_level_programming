#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    new_list = list(map(number * x, my_list))
    return new_list
