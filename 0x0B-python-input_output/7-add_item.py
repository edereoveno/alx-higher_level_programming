#!/usr/bin/python3
"""
Module adds all argument to a python list, then saves to a file using JSON represntation
"""
import json, sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file =__import__('6-load_from_json_file').load_from_json_file


argv = sys.argv
item_list = []
filename = "add_item.json"
for i in range(1, len(argv)):
    item_list.append(argv[i])
save_to_json_file(item_list, filename)
my_list = load_from_json_file(filename)
