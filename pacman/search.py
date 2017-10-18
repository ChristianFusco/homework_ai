"""Author: Christian Fusco
Class: CSI-480-01/02
Assignment: Python Practice
Date Assigned: 9/11/2017
Due Date: 9/28/2017

Description:
A series of different, generic grid search algorithms for a game.

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

"""search.py

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

"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in search_agents.py).
"""

import util
from copy import deepcopy
from game import Directions

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def get_start_state(self):
        """
        Returns the start state for the search problem.
        """

        return GameState()

    def is_goal_state(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """

    def get_successors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, step_cost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'step_cost' is
        the incremental cost of expanding to that successor.
        """




    def get_cost_of_actions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """


def tiny_maze_search(problem):
    """
    Returns a sequence of moves that solves tiny_maze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tiny_maze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depth_first_search(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.
    """
    # Set up fringe
    # each state in fringe is a tuple containing:
    #   state - an x,y tuple of pacmans position
    #   actions - the path down the tree
    state = problem.get_start_state()
    fringe = util.Stack()
    fringe.push((state, []))
    # Keep a list of expanded states
    expanded_states = []
    
    while not fringe.is_empty():
        parent_state,parent_path = fringe.pop()
        # Goal condition
        if problem.is_goal_state(parent_state):
                return parent_path
        # Already expanded condition
        if parent_state in expanded_states:
                continue
        expanded_states.append(parent_state)
        
        # Add fringe to stack
        successors = problem.get_successors(parent_state)
        # dfs has to be reversed for some reason ayyy
        if successors: 
            successors.reverse()
        for successor in successors:
            state,action,_ = successor
            # Keeps track of past actions to return that list
            path = parent_path + [action]
            fringe.push((state, path))
    return []


def breadth_first_search(problem):
    """Search the shallowest nodes in the search tree first."""
    # Literally bfs but with a queue and no reverse on successors
    fringe = util.Queue()
    fringe.push((problem.get_start_state(), []))
    expanded_states = []
    
    while not fringe.is_empty():
        parent_state,parent_path = fringe.pop()
        if problem.is_goal_state(parent_state):
                return parent_path
        if parent_state in expanded_states:
                continue
        expanded_states.append(parent_state)
        for successor in problem.get_successors(parent_state):
            state,action,_ = successor
            path = parent_path + [action]
            fringe.push((state, path))
    return []

def uniform_cost_search(problem):
    """Search the node of least total cost first."""
    # Set up fringe
    # each state in fringe is a tuple containing:
    #   state - an x,y tuple of pacmans position
    #   actions - the path down the tree
    fringe = util.PriorityQueue()
    state = problem.get_start_state()
    expanded_states = []
    # (state, movement history, cost)
    fringe.update((state,[]),0)
 
    while not fringe.is_empty():
        parent_state,parent_path = fringe.pop()
        if problem.is_goal_state(parent_state):
                return parent_path
        if parent_state in expanded_states:
            continue
        expanded_states.append(parent_state)
        for successor in problem.get_successors(parent_state):
            state,action,_= successor
            path = parent_path + [action]
            cost = problem.get_cost_of_actions(path)
            fringe.update((state, path), cost)
    return []



def null_heuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def a_star_search(problem, heuristic=null_heuristic):
    fringe = util.PriorityQueue()
    state = problem.get_start_state()
    expanded_states = []
    # (state, movement history)
    fringe.update((state,[]),0)
 
    while not fringe.is_empty():
        parent_state,parent_path = fringe.pop()
        if problem.is_goal_state(parent_state):
            print(parent_path)
            return parent_path
        if parent_state in expanded_states:
            continue
        expanded_states.append(parent_state)
        for successor in problem.get_successors(parent_state):
            state, action, step_cost = successor
            path = deepcopy(parent_path) + [action]
            cost = problem.get_cost_of_actions(path) + heuristic(state,problem)
            fringe.update((state, path), cost)
    return []
    


# Abbreviations
bfs = breadth_first_search
dfs = depth_first_search
astar = a_star_search
ucs = uniform_cost_search
