#!/usr/bin/env python
# coding: utf-8

import math

# A palindromic number reads the same both ways.

def is_palindrome(num):
    # convert to string for easy comparisons
    num= str(num)
    if num[-1] == num[0]:
        if len(num) < 3:
            return True
        else:
            return is_palindrome(num[1:-1])
    else:
        return False

def combinations(digits):
    """Generator that yields possible combinations of numbers."""
    smallest_number = int(math.pow(10, digits - 1))
    largest_number = int(math.pow(10, digits) - 1)
    for x in xrange(largest_number, smallest_number, -1):
        for y in xrange(largest_number, smallest_number, -1):
            yield (x, y)

def largest_palindrome(digits):
    largest = (0,0,0)
    for x in combinations(digits):
        product = x[0] * x[1]
        if is_palindrome(product) and product > largest[2]:
            largest = (x[0], x[1], product)
    return largest

# The largest palindrome made from the product of two 2-digit numbers is
# 9009 = 91 × 99
print largest_palindrome(2)
assert(largest_palindrome(2)[2] == 9009)


# Find the largest palindrome made from the product of two 3-digit numbers.
print largest_palindrome(3)