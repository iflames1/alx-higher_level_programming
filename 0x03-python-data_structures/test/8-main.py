#!/usr/bin/python3
import sys
sys.path.append('..')

multiple_returns = __import__('8-multiple_returns').multiple_returns

sentence = ""
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))
