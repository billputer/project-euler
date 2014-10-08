#!/usr/bin/env python

def fib():
    """Infinite Fibbonacci sequence generator"""
    yield 1
    yield 2
    nminus2 = 1
    nminus1 = 2

    while True:
        n = nminus2 + nminus1
        nminus2 = nminus1
        nminus1 = n
        yield n

# By considering the terms in the Fibonacci sequence whose values do not
# exceed four million, find the sum of the even-valued terms.
s = 0
for x in fib():
    # stop when we exceed 4 million
    if x > 4000000:
        break
    # if even, add to s
    elif x % 2 == 0:
        s += x

print s