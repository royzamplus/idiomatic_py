#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Use a list comprehension to create a transformed version of an existing list
some_other_list = range(10)
some_list = [element + 5 for element in some_other_list]

# Make use of negative indexes
def get_suffix(word):
    return word[-2:]

# Prefer list comprehensions to the built-in map() and filter() functions
the_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers_times_two = [n * 2 for n in the_list if n % 2 == 1]

# Use the built-in function sum to calculate the sum of a list of values
the_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
the_sum = sum(the_list)

# Use all to determine if all elements of an iterable are True
def contains_zero(iterable):
    # 0 is "Falsy," so this works
    return not all(iterable)

# Prefer xrange to range unless you need the resulting list
even_number = int()
for index in xrange(1000000):
    if index % 2 == 0:
        even_number = index
        break

