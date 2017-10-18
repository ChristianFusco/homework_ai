"""Author: Christian Fusco
Class: CSI-480-01/02
Assignment: Python Practice
Date Assigned: 9/11/2017
Due Date: 9/11/2017

Description:
A short python intro assignment.

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
"""shop.py


    To run this script, type

      python shop.py

    Once you have correctly implemented the get_price_of_order function,
    the script should produce the output:

    Cost of [('apples', 2.0), ('pears', 3.0), ('limes', 4.0)] is 12.25

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


class FruitShop:

    def __init__(self, name, fruit_prices):
        """
            name: Name of the fruit shop

            fruit_prices: Dictionary with keys as fruit
            strings and prices for values e.g.
            {'apples':2.00, 'oranges': 1.50, 'pears': 1.75}
        """
        self.fruit_prices = fruit_prices
        self.name = name
        print 'Welcome to %s fruit shop' % (name)

    def get_cost_per_pound(self, fruit):
        """
            fruit: Fruit string
        Returns cost of 'fruit', assuming 'fruit'
        is in our inventory or None otherwise
        """
        if fruit not in self.fruit_prices:
            return None
        return self.fruit_prices[fruit]

    def get_price_of_order(self, order_list):
        """
            order_list: List of (fruit, num_pounds) tuples

        Returns cost of order_list, assuming all fruit
        are in our inventory or None otherwise
        """

        total_cost = 0
        for fruit, pounds in order_list:
            if fruit not in self.fruit_prices:
                return None
            total_cost += self.get_cost_per_pound(fruit) * pounds
        return total_cost

    def get_name(self):
        return self.name

    def __str__(self):
        return "<FruitShop: %s>" % self.get_name()

    def __repr__(self):
        return str(self)


if __name__ == '__main__':
    """This code runs when you invoke the script from the command line"""
    fruit_prices = {'apples': 2.00, 'oranges': 1.50, 'pears': 1.75,
                    'limes': 0.75, 'strawberries': 1.00}

    fruitShop = FruitShop('TestShop', fruit_prices)

    order_list = [('apples', 2.0), ('pears', 3.0), ('limes', 4.0)]
    print 'Cost of', order_list, 'is', fruitShop.get_price_of_order(order_list)
