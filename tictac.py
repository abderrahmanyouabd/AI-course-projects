import random
from game_search_algorithms import alfabeta_search, minimax_search
from base_game_class import Game


def convert_state_to_list(state_tuple):
    return [list(x) for x in state_tuple]


def convert_state_to_tuple(state_list):
    return tuple([tuple(x) for x in state_list])


# TIC-TAC TOE CLASS
class TicTacToe(Game):
    """3x3 version."""

    def __init__(self, h=3, w=3, k=3):
        """
        Base of the game. We will save states as dictionaries. We will save data in (idx, idx) = sign format.
        """
        self.h = h
        self.w = w
        self.k = k

        init_state = [[0 for i in range(self.w)] for j in range(self.h)]
        self.initial = convert_state_to_tuple(init_state)

    def count_signs(self, state, sign):
        cnt = 0
        for i in range(self.h):
            for j in range(self.w):
                if state[i][j] == sign:
                    cnt += 1
        return cnt

    def check_triples(self, state):
        for i in range(self.h):
            if state[i][0] == state[i][1] and state[i][0] == state[i][2] and state[i][0] != 0:
                return state[i][0]

        for j in range(self.w):
            if state[0][j] == state[1][j] and state[0][j] == state[2][j] and state[0][j] != 0:
                return state[0][j]

        if state[1][1] != 0 and state[0][0] == state[1][1] and state[2][2] == state[1][1]:
            return state[1][1]

        if state[1][1] != 0 and state[0][2] == state[1][1] and state[2][0] == state[1][1]:
            return state[1][1]

        return 0

    def next_player(self, state):
        return 1 + self.count_signs(state, 1) - self.count_signs(state, 2)

    def legal_steps(self, state):
        """We can step on every empty cell"""
        steps = []
        cnt_1 = self.count_signs(state, 1)
        cnt_2 = self.count_signs(state, 2)

        for i in range(1, self.h + 1):
            for j in range(1, self.w + 1):
                for k in range(1, 3):
                    if state[i - 1][j - 1] == 0 and k == 1 + cnt_1 - cnt_2:
                        steps.append((i, j, k))

        return steps

    def goodness(self, state, player):
        """return 1 if player wins and -1 if player loses, and 0 otherwise"""
        if not self.is_leaf(state):
            return 0

        if player == 1:
            if self.check_triples(state) == 1:
                return 1
            elif self.check_triples(state) == 2:
                return -1

        if player == 2:
            if self.check_triples(state) == 1:
                return -1
            elif self.check_triples(state) == 2:
                return 1

        return 0

    def is_leaf(self, state):
        """If someone won or the table is full it will be the end of the game."""
        if self.count_signs(state, 0) == 0:
            return True

        if self.check_triples(state) != 0:
            return True

        return False

    def print(self, state):
        """Let's see the current state."""
        for x in range(self.h):
            for y in range(self.w):
                if state[x][y] == 1:
                    sign = 'X'
                elif state[x][y] == 2:
                    sign = 'O'
                else:
                    sign = '.'
                print(sign, end=' ')
            print()
        print()

    def take_step(self, step, state):
        """Effect of the step"""
        i, j, k = step

        new_state = convert_state_to_list(state)

        for p in range(1, self.h + 1):
            for q in range(1, self.w + 1):
                if p == i and q == j:
                    new_state[p - 1][q - 1] = k

        return convert_state_to_tuple(new_state)


# PLAYERS
def random_player(game, state):
    """Randomly choose between options"""
    return random.choice(game.legal_steps(state))


def alfabeta_player(game, state):
    """Search in game tree"""
    return alfabeta_search(state, game)


def minimax_player(game, state):
    """Search in game tree"""
    return minimax_search(state, game)


def play_game(game, *players):
    """Play a game with players"""
    state = game.initial
    game.print(state)

    while True:
        for player in players:
            step = player(game, state)
            state = game.take_step(step, state)
            game.print(state)
            # print(game.legal_steps(state))
            if game.is_leaf(state):
                return game.goodness(state, 1)


tt = TicTacToe()

print('Result of the game: ', play_game(tt, random_player, minimax_player))
