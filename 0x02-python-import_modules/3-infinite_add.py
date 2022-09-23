#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    len = len(sys.argv) - 1
    sum = 0
    if len == 0:
        print("0")
    elif len > 0:
        for i in range (1, len + 1):
            sum += int(sys.argv[i])
        print("{}".format(sum))
