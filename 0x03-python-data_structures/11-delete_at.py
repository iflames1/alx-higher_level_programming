#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    pop_list = []
    for i, value in enumerate(my_list):
        if i != idx:
            pop_list.append(value)
    return pop_list