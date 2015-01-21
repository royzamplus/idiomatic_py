#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Use collections.namedtuple to make tuple-heavy code more clear

# Assume the 'employee' table has the following columns:
# first_name, last_name, department, manager, salary, hire_date
from collections import namedtuple

EmployeeRow = namedtuple('EmployeeRow', ['first_name', 
    'last_name', 'department', 'manager', 'salary', 'hire_date'])

EMPLOYEE_INFO_FMT = '{last_name}, {first_name} was hired on \
{hire_date} (for ${salary} per annum) into the {department} \
and reports to {manager}'

def print_employee_information(db_connection):
    db_cursor = db_connection.cursor()
    results = db_cursor.execute('select * from employees').fetchall()
    for row in results:
        employee = EmployeeRow._make(row)

        # It's now almost impossible to print a field in the wrong place
        print(EMPLOYEE_INFO_FMT.format(**employee._asdict()))

# Use _ as a placeholder for data in a tuple that should be ignored
(name, age, _, _) = get_user_info(user)
if age > 21:
    output = '{name} can drink!'.format(name=name)
# "Clearly, only name and age are interesting"

# Use tuples to unpack data
list_from_comma_separated_value_file = ['dog', 'Fido', 10]
(animal, name, age) = list_from_comma_separated_value_file
output = ('{name} the {animal} is {age} years old'.format(
    animal=animal, name=name, age=age))

# Use tuple to return multiple values from a function
from collections import Counter

STATS_FORMAT = """Statistics:
Mean: {mean}
Median: {median}
Mode: {mode}"""

def calculate_statistics(value_list):
    mean = float(sum(value_list) / len(value_list))
    median = value_list[int(len(value_list) / 2)]
    mode = Counter(value_list).most_common(1)[0][0]

    return (mean, median, mode)

(mean, median, mode) = calculate_statistics([10, 20, 20, 30])
print(STATS_FORMAT.format(mean=mean, median=median, mode=mode))

