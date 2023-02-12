#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0
    numer = list(i[0] * i[1] for i in my_list)
    denom = list(i[1] for i in my_list)
    average = sum(numer) / sum(denom)
    return average
