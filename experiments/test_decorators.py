#!/usr/bin/python3

# decorators in python

# If the second number is bigger than the first number, swap them

def div(a, b):
    if b == 0:
        print("Cannot divide to 0...")

    # if a < b:
    #     a, b = b, a

    # return a / b
    print (a / b)

def smart_div(func):
    def inner(a, b):
        if a < b:
            a, b = b, a

        return func(a, b)

    return inner

div = smart_div(div)

div(2, 4)
