#!/usr/bin/python3

def uniq_add(my_list=[]):
    add = 0
    my_list = list(set(my_list))
    for i in range(len(my_list)):
        add += (my_list[i])
    return add
