# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    from util import Stack

    # Initialize the stack with the start state
    stack = Stack()
    stack.push((problem.getStartState(), []))  # (state, actions)

    # To keep track of visited nodes
    visited = set()

    while not stack.isEmpty():
        # Pop the current state and the actions leading to it
        state, actions = stack.pop()

        # Check if the current state is the goal
        if problem.isGoalState(state):
            return actions

        # If the state has not been visited, process it
        if state not in visited:
            visited.add(state)
            # Iterate through the successors
            for successor, action, stepCost in problem.getSuccessors(state):
                if successor not in visited:
                    # Push the successor state onto the stack along with the actions to reach it
                    stack.push((successor, actions + [action]))

    return []

    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    from util import Queue

    # Initialize the queue with the start state
    queue = Queue()
    queue.push((problem.getStartState(), []))  # (state, actions)

    # To keep track of visited nodes
    visited = set()

    while not queue.isEmpty():
        # Pop the current state and the actions leading to it
        state, actions = queue.pop()

        # Check if the current state is the goal
        if problem.isGoalState(state):
            return actions

        # If the state has not been visited, process it
        if state not in visited:
            visited.add(state)
            # Iterate through the successors
            for successor, action, stepCost in problem.getSuccessors(state):
                if successor not in visited:
                    # Push the successor state onto the queue along with the actions to reach it
                    queue.push((successor, actions + [action]))

    return []

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    from util import PriorityQueue

    # Initialize the priority queue with the start state
    priority_queue = PriorityQueue()
    priority_queue.push((problem.getStartState(), []), 0)  # (state, actions), cost

    # To keep track of visited nodes and their costs
    visited = {}

    while not priority_queue.isEmpty():
        # Pop the current state, the actions leading to it, and its cost
        state, actions = priority_queue.pop()

        # Check if the current state is the goal
        if problem.isGoalState(state):
            return actions

        # If the state has not been visited or found a cheaper way to the state
        if state not in visited or problem.getCostOfActions(actions) < visited[state]:
            visited[state] = problem.getCostOfActions(actions)
            # Iterate through the successors
            for successor, action, stepCost in problem.getSuccessors(state):
                new_actions = actions + [action]
                cost = problem.getCostOfActions(new_actions)
                # Push the successor state onto the priority queue with its cost
                priority_queue.push((successor, new_actions), cost)

    return []

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
