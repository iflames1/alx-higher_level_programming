#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list:
        total_score, total_weight = 0, 0

        for score, weight in my_list:
            total_score += score * weight
            total_weight += weight

        return total_score / total_weight

    return 0
