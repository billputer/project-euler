#!/usr/bin/env python
# coding: utf-8

import math
from itertools import islice, count

# The sequence of triangle numbers is generated by adding the natural numbers.
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

def triangle_generator():
  for n in count(1):
    yield (n * (n + 1)) / 2

print [x for x in islice(triangle_generator(), 10)]

# Let us list the factors of the first seven triangle numbers:

#   1: 1
#   3: 1,3
#   6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28

def count_factors(num):
  """Counts all factors for an integer"""
  count = 1
  for i in xrange(1, (num / 2) + 1 ):
    if num % i == 0:
      count += 1
  return count


def first_triangle_with_num_divisors(num):
  """Returns first triangle with limit divisors"""
  for triangle in triangle_generator():
    factors = count_factors(triangle)
    
    #print "{}: {}".format(triangle, factors)
    if factors > num:
      return triangle

# What is the value of the first triangle number to have over five hundred divisors?
print first_triangle_with_num_divisors(500)
