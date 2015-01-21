#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Understand and use the mathematical set operations
def get_both_popular_and_active_users():
    # Assume the following two functions each return a
    # list of user names
    return(set(get_list_of_most_active_users()) & set(get_list_of_most_popular_users()))

# Use a set comprehension to generate sets concisely
users_first_names = {user.first_name for user in users}

# Use sets to eliminate duplicate entries from Iterable containers
unique_surnames = set(employee_surnames)

def display(elements, output_format='html'):
    if output_format == 'std_out':
        for element in elements:
            print(element)
    elif output_format == 'html':
        as_html = '<ul>'
        for element in elements:
            as_html += '<li>{}</li>'.format(element)
        return as_html + '</ul>'
    else:
        raise RuntimeError('Unknown format {}'.format(output_format))

