#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Arrange your import statements in a standard order
"""
1. standard library modules
2. third-party library modules installed in site-packages
3. modules local to the current project
"""

# Easy to see exactly what my dependencies are and where to 
# make changes if a module or package name changes
import concurrent.futures
import os.path
import sys
from flask import (Flask, request, session, g,
    redirect, url_for, abort,
    render_template, flash, _app_ctx_stack)
import requests
import this_project.utilities.sentient_network as skynet
import this_project.widgets

# Avoid placing multiple statements on a single line
for element in my_list:
    print(element)
    print('--------')

# Document what something does not how
def is_prime(number):
    """Return True if number is prime"""

    for candidate in range(2, number):
        if number % candidate == 0:
            return False

    return number > 0

# Follow the docstring conventions described in PEP-257
def calculate_statistics(value_list):
    """Return a tuple containing the mean, median,
    and mode of a list of integers

    Arguments:
    value_list -- a list of integer values

    """
    <The body of the function>

# Make use of __init__.py to simplify package interfaces
from gizmo.client.interface import Gizmo
from gizmo.client.contrib.utils import GizmoHelper

# client code:
from gizmo import Gizmo, GizmoHelper

# Prefer absolute imports to relative imports

# My location is package.sub_package.another_sub_package.module
# and I want to import package.other_module.
# Either of the following are acceptable:

import package.other_module
import package.other_module as other

# Use all capital letters when declaring global constant values
SECONDS_IN_A_DAY = 60 * 60 * 24

def display_uptime(uptime_in_seconds):
    percentage_run_time = (
        uptime_in_seconds / SECONDS_IN_A_DAY) * 100

    return 'The process was up {percent} percent of the day'.format(
        percent=int(percentage_run_time))

uptime_in_seconds = 60 * 60 * 24
display_uptime(uptime_in_seconds)

# Use a try block to determine if a package is available
try:
    import cProfile as profiler
except:
    import profile as profiler

print(profiler.__all__)

# Use inline documentation sparingly

def calculate_mean(numbers):
    """Return the mean of a list of numbers"""
    return sum(numbers) / len(numbers)

# Use sys argv to reference command line parameters
if __name__ == '__main__':
    try:
        print(open(sys.argv[1]).read())
    except IndexError:
        print('You forgot the file name!')

# Use sys exit in your script to return proper error codes
def main():
    import sys
    if len(sys.argv) < 2:
        # Calling sys.exit with a string automatically
        # prints the string to stderr ad exits with
        # a value of '1' (error)
        sys.exit('You forgot to pass an argument')
    argument = sys.argv[1]
    result = do_stuff(argument)
    if not result:
        sys.exit(1)
        # We can also exit with just the return code

    do_stuff_with_result(result)

    # Optinal, since the return value without this return
    # statement would default to None, which sys.exit treats
    # as 'exit with 0'
    return 0

# The two lines below are the canonical script entry
# point lines. You'll see them often in other Python scripts
if __name__ == '__main__':
    sys.exit(main())

# Use the tuples to organize a long list of modules to import

from django.db.models import (AutoField, BigIntegerField, BooleanField,
    CharField, CommaSeparatedIntegerField, DateField, DateTimeField)
