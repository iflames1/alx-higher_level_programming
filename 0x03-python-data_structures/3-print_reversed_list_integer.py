#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    new_list = []
    for list in range(len(my_list), 0, -1):
        new_list.append(list)
    for n_list in range(0, len(new_list)):
        print(new_list[n_list])
