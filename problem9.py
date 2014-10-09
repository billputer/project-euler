#!/usr/bin/env python
# coding: utf-8

import math

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#   a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

def is_pythagorean_triplet(a, b, c):
    return math.pow(a, 2) + math.pow(b, 2) == math.pow(c, 2)

def get_triplets(n):
    """"Return all triplets of natural numbers that add up to n"""
    for x in range(1, n / 3):
        for y in range(x + 1, int((n - x) / 2 + 1)):
            for z in range(y + 1, n - x - y + 1):
                if x + y + z == n:
                    yield x, y, z


# (3,4,5) is a triplet of 12
assert((3,4,5) in get_triplets(12))

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
for trip in get_triplets(1000):
    a, b, c = trip
    if(is_pythagorean_triplet(a,b,c)):
        print a * b * c
