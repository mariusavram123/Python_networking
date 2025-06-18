#!/usr/bin/python3

def factorial(nr):
    fact = 1
    # while i <= nr:
    #     fact *= i
    #     i += 1
    for i in range(1, nr + 1):
        fact *= i

    print(fact)

factorial(5)

def factorial_rec(n):

    if n == 0:
        return 1

    return n * factorial_rec(n - 1)


result = factorial_rec(5)

print(result)