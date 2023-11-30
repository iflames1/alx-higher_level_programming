#!/usr/bin/python3

def remove_char_at(str, n):
    str_cpy = ""

    for i in range(len(str)):
        if i != n:
            str_cpy += str[i]
    return str_cpy
