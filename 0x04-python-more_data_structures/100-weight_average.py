#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        score = 0
        weight = 0
        for s, w in my_list:
            score += s * w
            weight += w
        if weight == 0:
            return 0
        else:
            return score / weight
