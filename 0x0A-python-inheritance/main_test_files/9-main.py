#!/usr/bin/python3
import sys
sys.path.append('..')

Rectangle = __import__('9-rectangle').Rectangle

r = Rectangle(3, 5)

print(r)
print(r.area())
