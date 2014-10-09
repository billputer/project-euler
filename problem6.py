#!/usr/bin/env python

import math

# The sum of the squares of the first ten natural numbers is,
#   1^2 + 2^2 + ... + 10^2 = 385
def sum_of_squares(n):
    sum = 0
    for x in xrange(1, n+1):
        sum += math.pow(x, 2)
    return sum

print sum_of_squares(10)

# The square of the sum of the first ten natural numbers is,
#   (1 + 2 + ... + 10)^2 = 55^2 = 3025
def square_of_sums(n):
    sum = 0
    for x in xrange(1, n+1):
        sum += x
    return math.pow(sum, 2)

print square_of_sums(10)


#  Hence the difference between the sum of the squares of the first ten
#  natural numbers and the square of the sum is 3025 - 385 = 2640.

# Find the difference between the sum of the squares of the first one
# hundred natural numbers and the square of the sum.

print square_of_sums(100) - sum_of_squares(100)
