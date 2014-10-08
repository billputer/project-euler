#!/usr/bin/env python

import math

def is_prime(n):
    for m in xrange(2, n-1):
        if n % m == 0:
            return False

    return True

def determine_prime_factors(num):
    largest_possible_factor = int(math.floor(math.sqrt(num)))
    for i in xrange(2, largest_possible_factor):
        if num % i == 0 and is_prime(i):
            yield i

# prime factors of 13195 are 5, 7, 13, 29
print [x for x in determine_prime_factors(13195)]

# What is the largest prime factor of the number 600851475143?
print [x for x in determine_prime_factors(600851475143)]

