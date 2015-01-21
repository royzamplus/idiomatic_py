#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Use multiple assignment to condense variables all set to the same value
x = y = z = 'a'

# Avoid using a temporary variable when performing a swap of two values 
foo = 'Foo'
bar = 'Bar'
(foo, bar) = (bar, foo)

# Chain string functions to make a simple series of transformations more clear
book_info = ' The Three Musketeers: Alexandre Dumas'
formatted_book_info = book_info.strip().upper().replace(':', ' by')

# Use ''.join when creating a single string for list elements
result_list = ['True', 'False', 'File not found']
result_string = ''.join(result_list)

# Use ord to get the ASCII code of a character and ord to get the character from an ASCII code
hash_value = 0
for e in some_string:
    hash_value += ord(e)
return hash_value

# Prefer the format function for formatting strings
def get_formatted_user_info(user):
    # Clear and concise. At a glance I can tell exactly what
    # the output should be. Note: this string could be returned
    # directly, but the string itself is too long to fit on the page.
    output = 'Name: {user.name}, Age: {user.age}, Sex: {user.sex}'.format(user=user)
    return output

