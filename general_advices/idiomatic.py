#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Make use of the appropriate assert methods in unit tests

class Test(unittest.TestCase):
    def test_adding_positive_ints(self):
        """Does adding together two positive integers work?"""
        self.assertEqual(my_addition(2, 2), 4)

    def test_increment(self):
        """Does increment return a value greater than what was passed as an 
        argument?"""
        self.assertGreaterThan(increment(1), 1)

    def test_divisors_of_prime_number(self):
        self.assertIsNone(get_divisors(11))

# Use functions in the os.path module when working with directory paths

from datetime import date
import os

current_directory = os.getcwd()
filename_to_archive = 'test.txt'
new_filename = os.path.splitext(filename_to_archive)[0] + '.bak'
target_directory = os.path.join(current_directory, 'archives')
today = date.today()
new_path = os.path.join(target_directory, str(today))
if (os.path.isdir(target_directory)):
    if not os.path.exists(new_path):
        os.mkdir(new_path)
    os.rename(
        os.path.join(current_directory, filename_to_archive),
        os.path.join(new_path, new_filename))