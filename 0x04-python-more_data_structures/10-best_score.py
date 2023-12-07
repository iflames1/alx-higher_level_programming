#!/usr/bin/python3

def best_score(a_dictionary):
    best_score = None
    best_score = float('-inf')

    if a_dictionary:
        for key, value in a_dictionary.items():
            if value > best_score:
                best_key = key
                best_score = value
        return best_key
    else:
        return None
