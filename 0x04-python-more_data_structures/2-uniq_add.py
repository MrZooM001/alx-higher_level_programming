#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniqe_list = set(my_list)
    sum_all = 0
    for n in uniqe_list:
        sum_all += n
    return sum_all
