from search import *


def convert_state_to_list(state_tuple):
    return [list(x) for x in state_tuple]


def convert_state_to_tuple(state_list):
    return tuple([tuple(x) for x in state_list])


class KnightSearch(Problem):

    def __init__(self):
        # Complete the implementation of initial function by calling
        # the parent constructor and initialize with the initial and goal state
        # Write your code below this line!
        # Write your code above this line! Delete the 'pass' keyword
        initial = ((0, 0, 0, 0, 0, 0),
                   (0, 0, 0, 0, 0, 0),
                   (0, 0, 0, 0, 0, 0),
                   (0, 0, 0, 1, 0, 0),
                   (0, 0, 0, 0, 0, 0),
                   (0, 0, 0, 0, 0, 1))
        self.initial = initial
        super().__init__(self.initial)

    def goal_test(self, state):
        # Check if the given state is a goal state. Return True if it is, and False if it is not
        # Write your code below this line!
        return state[0][0] == 1

    def actions(self, state):
        # Complete the implementation of possible operators.
        # The function should return all next possible actions from the input state.
        # Use the "o i j l k" format for the operators
        i, j = 0, 0
        for x in range(6):
            for y in range(6):
                if state[x][y] == 1:
                    i, j = x, y  # these are the current indices of the knight
                    break

        # Write your code below this line!
        acts = []
        for k in range(6):
            for l in range(6):
                if (abs(i - k) == 2 and abs(j - l) == 1) or (abs(i - k) == 1 and abs(j - l) == 2):
                    acts.append(f"o {i} {j} {k} {l}")
        return acts

    def result(self, state, action):
        # Write a function that return the new state when using the given action in case of the input state

        i, j, l, k = int(action.split(' ')[1]), int(action.split(' ')[2]), \
                     int(action.split(' ')[3]), int(action.split(' ')[4])
        new_state = convert_state_to_list(state)

        # Write your code below this line!
        new_state[i][j] = 0
        new_state[l][k] = 1
        return convert_state_to_tuple(new_state)






def depth_first_graph_search(problem):
    # Write your code below this line
    frontier = [(Node(problem.initial))]
    res_path = []
    explored = set()
    while frontier:
        node = frontier.pop()
        res_path.append(node)
        if problem.goal_test(node.state):
            print(res_path)
            return node.solution()
        explored.add(node.state)
        frontier.extend(child for child in node.expand(problem)
                        if child.state not in explored and child not in frontier)
    return None


def main():
    # 1. Exercise: Fill out the init function and print out the initial state (1 point)
    # Write your code below this line!
    problem = KnightSearch()
    print(problem.initial)
    # Write your code above this line! Delete the 'pass' keyword.

    # 2. Exercise: Fill out the goal_test function and test if it works correctly (2 points)
    # Write your code below this line!
    print(problem.goal_test(problem.initial))
    # Write your code above this line!

    # 3. Exercise: Fill out the actions function and test if it works correctly (using the initial state) (2 points)
    # Write your code below this line!
    print(problem.actions(problem.initial))

    # Write your code above this line!

    # 4. Exercise: Fill out the result function and test if it works correctly (2 points)
    # Write your code below this line!
    new_state = problem.result(problem.initial, "o 3 3 1 4")
    print(new_state)
    print(problem.actions(new_state))
    print(problem.result(new_state, "o 1 4 3 3"))
    print(problem.actions(problem.result(new_state, "o 1 4 3 3")))
    print(breadth_first_graph_search(problem))

    # Write your code above this line!


if __name__ == "__main__":
    main()
