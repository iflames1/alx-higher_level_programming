#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) != 0:
        length, first = len(sentence), sentence[0]
        return (length, first)
    else:
        length, first = len(sentence), None
        return (length, first)
