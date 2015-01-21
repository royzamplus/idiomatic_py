#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

#if x <= y <= z:
#    return True

name = 'Jeff'
address = 'New York, NY'

if name:
    print(name)
print(address)

# Learn to treat functions as values

import operator as op

def print_table(operator):
    for x in range(1, 3):
        for y in range(1, 3):
            print(str(operator(x, y)) + '\n')

# op.add, sub, mul and div are all functions with the same implementation
# as their literal equivalents (i.e. 'op.add' is the same as '+')
for operator in (op.add, op.sub, op.mul, op.div):
    print_table(operator)

# Use the function based version of print

from __future__ import print_function

print(1, 'foo', __name__)