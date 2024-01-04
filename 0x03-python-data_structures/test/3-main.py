#!/usr/bin/python3
import sys
sys.path.append('..')

path = __import__('3-print_reversed_list_integer').print_reversed_list_integer
print_reversed_list_integer = path

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)
