#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    global j
    try:
        j = 0
        for i in range(x):
            print(my_list[i], end="")
            j += 1
        print()
        return j
    except IndexError:
        print()
        return j
