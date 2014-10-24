#!/usr/bin/env python
# coding: utf-8

#The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

def collatz_sequence(n):
  while n != 1:
    yield n
    # even
    if n % 2 == 0:
      n = n / 2
    # odd
    else:
      n = 3 * n + 1

  yield 1

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

print [x for x in collatz_sequence(13)]

def sequence_length(seq):
  """Calculate length, given a collatz_sequence generator."""
  count = 1
  while seq.next() != 1:
    count += 1
  return count

print sequence_length(collatz_sequence(13))

# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.

def longest_collatz(limit):
  longest = (0, 0)
  for x in xrange(2, limit):
    length = sequence_length(collatz_sequence(x))
    if length > longest[1]:
      longest = (x, length)

  return longest

print longest_collatz(1000000)
