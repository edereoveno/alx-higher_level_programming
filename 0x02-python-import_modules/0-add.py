#!/usr/bin/python3
if __name__ == "__main__":
    #import module and change its name
    import add_0 as add_
    #assign values to variables
    a = 1
    b = 2
    #pass variables as arguments in function and print
    print("{} + {} = {}".format(a,b,add_.add(a, b)))
