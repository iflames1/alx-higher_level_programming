#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    bool_list = my_list[:]
    if bool_list:
        for i in bool_list:
            if bool_list[i] % 2 == 0:
                bool_list[i] = True
            else:
                bool_list[i] = False

        return bool_list
