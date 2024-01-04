#!/usr/bin/python3
import sys
sys.path.append('..')

Square = __import__('6-square').Square

try:
    my_square = Square(3, (1, "3"))
except Exception as e:
    print(e)
