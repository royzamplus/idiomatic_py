#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Use a dict as a substitute for a switch...case statement
def apply_operation(left_operand, right_operand, operator):
    import operator as op
    operator_mapper = {'+': op.add, '-': op.sub, '*': op.mul, '/': op.truediv}
    return operator_mapper[operator](left_operand, right_operand)

# Use the default parameter of dict.get to provide default values
log_severity = configuration.get('severity', 'Info')

# Use a dict comprehension to build a dict clearly and efficiently
user_email = {user.name: user.email
              for user in users_list if user.email}

