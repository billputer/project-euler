#!/usr/bin/env python
# coding: utf-8

from itertools import takewhile

# First stab - generate primes by trial division (soooo slow)

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

# Second stab - use someone else's prime sieve, because I am lazy

# Sieve of Eratosthenes
# David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/
def eratosthenes():
    '''Yields the sequence of prime numbers via the Sieve of Eratosthenes.'''
    D = {}  # map composite integers to primes witnessing their compositeness
    q = 2   # first integer to test for primality
    while 1:
        if q not in D:
            yield q        # not marked composite, must be prime
            D[q*q] = [q]   # first multiple of q not already marked
        else:
            for p in D[q]: # move each witness to its next multiple
                D.setdefault(p+q,[]).append(p)
            del D[q]       # no longer need D[q], free memory
        q += 1

# </copypasta>


# with a prime sieve, this is incredibly simple
def sum_primes(limit):
    return sum(takewhile(lambda x : x < limit, eratosthenes()))


# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
assert(sum_primes(10) == 17)

# Find the sum of all the primes below two million.
print sum_primes(2000000)

