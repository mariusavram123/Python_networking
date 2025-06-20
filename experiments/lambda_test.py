#!/usr/bin/python3

from functools import reduce

# annonymous functions or lambdas

def square(a):

    return a * a

result = square(5)

print(result)


f = lambda a : a * a

result2 = f(10)

print(result2)

# lambda filter map reduce

# filter()
# map()
# reduce()

nums = [3, 2, 6, 8, 4, 6, 2, 9]

# def is_even(a):
#     return a % 2 == 0

# is_even = lambda a : a % 2 == 0 

evens = list(filter(lambda a : a % 2 == 0, nums))

print(evens)

# def update(n):
#     return n * 2

doubles = list(map(lambda n : n * 2, evens))

print(doubles)

# def add_all(a, b):
#     return a + b

sum = reduce(lambda a, b : a + b, doubles)

print(sum)
