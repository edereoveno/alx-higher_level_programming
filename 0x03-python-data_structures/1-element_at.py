#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < 0:
        return None
    if idx >= len(my_list):
        return None
    result = my_list[idx]
    return result
