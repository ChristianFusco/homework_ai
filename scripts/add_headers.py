"""Author: Christian Fusco
Class: CSI-480-01/02
Assignment: Python Practice
Date Assigned: ???
Due Date: 9/11/201

Description:
A short python practice assignment.

Certification of Authenticity: 
I certify that this is entirely my own work, except where I have given 
fully-documented references to the work of others. I understand the definition 
and consequences of plagiarism and acknowledge that the assessor of this 
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)
"""
import re
import os

rootdir = '.'
replacements = ('NAME',
                'LAB_OR_PA_NUMBER',
                'DATE_ASSIGNED',
                 'DUE_DATE',
                'DESCRIPTION')
authenticity_text = open('authenticity.txt').read()


def file_updated(path):
    # Compare the first line of each file to see if there's a diff
    python_text = open(path).readline()
    return 'Author' in python_text


def update_file(path, addition):
    # Adds the addition to the beginning of the file at path
    with open(path, 'r') as original:
        data = original.read()
    with open(path, 'w') as modified:
        modified.write(addition + '\n' + data)


# Do an in memory replacement of authenticity file
for replacement in replacements:
    response = raw_input(replacement + ': ')
    authenticity_text = re.sub(replacement, response, authenticity_text)

for subdir, dirs, files in os.walk(rootdir):
    # Skip big git directories
    if '.git' in subdir:
        continue
    for file in files:
        path = os.path.join(subdir, file)
        if '.py' not in file:
            continue
        if 'zip.py' == file or 'add_headers' == file:
        	continue
        if file_updated(path):
            continue
        update_file(path, authenticity_text)
        print('Wrote to ' + path)
