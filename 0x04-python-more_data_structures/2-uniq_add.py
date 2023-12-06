#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq_set = set()
    total = 0

    for number in my_list:
        if number not in uniq_set:
            uniq_set.add(number)
            total += number

    return total
