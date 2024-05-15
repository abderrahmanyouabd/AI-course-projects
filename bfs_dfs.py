from collections import deque

from search import Node


def breadth_first_graph_search(problem):
    open_bgs = deque([Node(problem.initial)])
    close_bgs = []
    explored = set()

    i = 0
    while open_bgs:
        x = open_bgs.popleft()
        close_bgs.append(x)
        explored.add(x)

        children = x.expand(problem)

        for child in children:
            print(f"Step{i}: ", child.state)
            if child not in explored and child not in open_bgs:  # check in 'open_bgs' not in 'close_bgs'
                if problem.goal_test(child.state):
                    print("The number of steps to solve the problem: ", len(close_bgs))
                    return child.state

                open_bgs.append(child)

        i += 1

    return None


def breadth_first_tree_search(problem):
    open_bts = deque([Node(problem.initial)])
    close_bts = []

    i = 0
    while open_bts:
        x = open_bts.popleft()
        close_bts.append(x)

        print(f"Step{i}: ", x.state)
        if problem.goal_test(x.state):
            print(f"The number of steps to solve the problem with BTS: ", len(close_bts))
            return x.state

        open_bts.extend(x.expand(problem))

        i += 1

    return None


def depth_first_graph_search(problem):
    open_dgs = [Node(problem.initial)]
    close_dgs = []
    explored = set()

    i = 0
    while open_dgs:
        x = open_dgs.pop()
        explored.add(x)
        close_dgs.append(x)

        children = x.expand(problem)

        for child in children:
            print(f"Step{i}: ", child.state)
            if child not in explored and child not in open_dgs:
                if problem.goal_test(child.state):
                    print("The number of steps to solve the problem: ", len(close_dgs))
                    return child.state

                open_dgs.append(child)
        i += 1

    return None


def depth_first_tree_search(problem):
    open_dts = [Node(problem.initial)]
    close_dts = []

    i = 0
    while open_dts:
        x = open_dts.pop()
        close_dts.append(x)

        print(f"Step{i}: ", x.state)
        if problem.goal_test(x.state):
            print("The number of steps to solve the problem with DTS: ", len(close_dts))
            return x.state

        open_dts.extend(x.expand(problem))

        i += 1

    return None
