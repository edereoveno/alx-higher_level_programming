#!/usr/bin/python3

def weight_average(my_list=[]):
    numer = list(i[0] * i[1] for i in my_list)
    denom = list(i[1] for i in my_list)
    average = sum(numer) / sum(denom)
    return average if my_list else 0
