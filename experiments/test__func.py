#!/usr/bin/python3

# formal arguments
def add(a, b):
    c = a + b
    print(c)

# actual arguments
add(5, 6)

# Actual arguments have 4 types:
# position
# keyword
# default
# variable length

def person(name, age = 18):
    print(name)
    print(age)

# positional arguments
# person('navin', 28)
# person(28, "navin") - error
# variables are taken by their position

# variables that are taken by their keyword
person(age=28,name="Marius")

# default variables
# person(name="Marius") - error that we do not specified the second parameter
# age is default 18 # def person(name, age = 18):
# person(name="Marius")
# if you pass a value for age it will override the default
person("Marius",28)

# variable length arguments
# the parameters are passed to b as a tuple
def sum(a,*b):
    # c = a + b
    # print(c)
    c = a
    for num in b:
        c += num

    print(c)

sum(5,6,34,78)

# removing a from parameters
def sum2(*b):
    c = 0

    for num in b:
        c += num

    print(c)

sum2(5, 6, 34, 78)

# keyworded variable length arguments
# accept arguments with keywords
# keyword args are passed as a dictionary
def person(name, **data):
    print(name)
    print(type(data))
    for i,j in data.items():
        print(f"{i}, {j}")


person("Marius", age = 28, city = "Buzau", phone =  729996215)

# global keyword
# variable scope: global or local

# we can create variables with the same name if they have a different scope:
# first a is global and the second is local
# global use a variable from a function context on the outside of the function

# globals - have a local and a global variable with the same name

a = 10
print(id(a))

def something():
    global b
    global a
    a = 15
    b = 8
    x = globals()["a"]
    print(id(x))
    globals()["a"] = 56
    print(f"in function {a}")
    
something()

print(f"outside {a}")
print(f"outside {b}")


# Pass a list to a function as argument

def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i % 2 == 0:
            even += 1
        elif i % 2 != 0:
            odd += 1

    return even, odd

lst = [20, 25, 14, 19, 16, 24, 28, 47, 26]

even, odd = count(lst)

print("Even {}, Odd {}".format(even,odd))

# fibonacci
def fib(nr):

    if nr <= 0:
        print("Invalid number. Please enter a positive number")
        exit()
    
    a = 0
    b = 1
    if nr == 1:
        print(a)
    else:
        print(a)
        print(b)

    for i in range(2, nr):
        c = a +  b
        a = b 
        b = c
        print(c)
        # if c <= nr:
        #     print(c)

fib(10)

# TODO: Fibonacci numbers that should stop before the input number

