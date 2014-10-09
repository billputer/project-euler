#!/usr/bin/env python

from itertools import islice

def is_prime(n):
    for m in xrange(2, n-1):
        if n % m == 0:
            return False

    return True

def prime_generator():
    i = 2
    while True:
        if is_prime(i):
            yield i
        i += 1

def nth_prime(n):
    "Returns the nth prime"
    return next(islice(prime_generator(), n - 1, None), False)

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
# see that the 6th prime is 13.
assert(nth_prime(6) == 13)

# What is the 10 001st prime number?
print(nth_prime(10001))
