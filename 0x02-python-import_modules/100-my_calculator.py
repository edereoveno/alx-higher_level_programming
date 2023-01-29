#!/usr/bin/python3

if __name__ == "__main__":
    from  calculator_1 import add, mul, sub, div
    from sys import argv

if len(argv) - 1 == 3:
    x = int(argv[1])
    y = int(argv [3])
    z = argv[2]

    if z == "+":
        print("{} + {} = {}".format(x, y, add(x, y)))
    elif z == "-":
        print("{} - {} = {}".format(x, y, sub(x, y)))
    elif z == "*":
        print("{} * {} = {}".format(x, y, mul(x, y)))
    elif z == "/":
        print("{} / {} = {}".format(x, y, div(x, y)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
else:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
