#!/usr/bin/python3

for num in range(0, 10):
    for number in range(1, 10):
        if number > num:
            print("{}{}".format(num, number), end=(",\
 " if int(str(num)+str(number)) < 89 else '\n'))
