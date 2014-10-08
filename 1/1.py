#!/usr/bin/env python

def find_multiples(n):
    """Find multiples of 3 or 5 up to n."""
    for i in range(3, n):
        if not i % 3 or not i % 5:
            yield i

# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
assert(sum(find_multiples(10)) == 23)

# Find the sum of all the multiples of 3 or 5 below 1000.
print sum(find_multiples(1000))
