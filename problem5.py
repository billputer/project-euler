#!/usr/bin/env python

def infinite_integer_iterator():
    x = 0
    while True:
        x += 1
        yield x
        

def is_divisible_by(num, divisors):
    for x in divisors:
        if num % x != 0:
            return False
    return True

def smallest_evenly_divisible_by(num):
    divisors = range(1, num)
    for x in infinite_integer_iterator():
        if is_divisible_by(x, divisors):
            return x


# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.
print smallest_evenly_divisible_by(10)
assert(smallest_evenly_divisible_by(10) == 2520)

# What is the smallest positive number that is evenly divisible by all of
# the numbers from 1 to 20?
print smallest_evenly_divisible_by(20)