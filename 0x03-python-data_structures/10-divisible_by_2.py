#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    bool_list = []
    if my_list:
        for i in my_list:
            if i % 2 == 0:
                bool_list = bool_list + [True]
            else:
                bool_list = bool_list + [False]

        return bool_list
