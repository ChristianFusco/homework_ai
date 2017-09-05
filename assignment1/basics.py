# Author: Christian Fusco
# Class: CSI-480-01/02
# Assignment: Python Practice
# Date Assigned: ???
# Due Date: 9/11/2017
#  
# Description:
# A short introduction to python.
#  
# Certification of Authenticity: 
# I certify that this is entirely my own work, except where I have given 
# fully-documented references to the work of others. I understand the definition 
# and consequences of plagiarism and acknowledge that the assessor of this 
# assignment may, for the purpose of assessing this assignment:
# - Reproduce this assignment and provide a copy to another member of academic
# - staff; and/or Communicate a copy of this assignment to a plagiarism checking
# - service (which may then retain a copy of this assignment on its database for
# - the purpose of future plagiarism checking)
"""basics.py

    Run python autograder.py

Champlain College CSI-480, Fall 2017
The following code was adapted by Joshua Auerbach (jauerbach@champlain.edu)
from the UC Berkeley Pacman Projects (see license and attribution below).

----------------------
Licensing Information:  You are free to use or extend these projects for
educational purposes provided that (1) you do not distribute or publish
solutions, (2) you retain this notice, and (3) you provide clear
attribution to UC Berkeley, including a link to http://ai.berkeley.edu.

Attribution Information: The Pacman AI projects were developed at UC Berkeley.
The core projects and autograders were primarily created by John DeNero
(denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
Student side autograding was added by Brad Miller, Nick Hay, and
Pieter Abbeel (pabbeel@cs.berkeley.edu).
"""


def add(a, b):
    """Return the sum of a and b"""
    return a + b


def comprehension(lst):
    """
        lst: List of strings

    Returns a list containing an uppercased version of each string in lst
    that has length greater than five.
    """
    return [value.upper() for value in lst if len(value) > 5]
