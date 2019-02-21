#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    # Write a function `rock_paper_scissors` to generate all of the possible
    # plays that can be made in a game of "Rock Paper Scissors", given some
    # input `n`, which represents the number of plays per round.

    # For example, given n = 2, your function should output the following:

    # ```python
    # [['rock', 'rock'], ['rock', 'paper'], ['rock', 'scissors'],
    # ['paper', 'rock'], ['paper', 'paper'], ['paper', 'scissors'],
    # ['scissors', 'rock'], ['scissors', 'paper'], ['scissors', 'scissors']]
    # ```

    # n = 3

    # [['rock', 'rock', 'rock'], ['rock', 'rock', 'paper'], ['rock', 'rock', 'scissors'],
    # ['rock', 'paper', 'rock'], ['rock', 'paper', 'paper'], ['rock', 'paper', 'scissors'],
    # ['rock', 'scissors', 'rock'], ['rock', 'scissors', 'paper'], ['rock', 'scissors', 'scissors'],
    #
    # ['paper', 'rock', 'rock'], ['paper', 'rock', 'paper'], ['paper', 'rock', 'scissors'],
    # ['paper', 'paper', 'rock'], ['paper', 'paper', 'paper'], ['paper', 'paper', 'scissors'],
    # ['paper', 'scissors', 'rock'], ['paper', 'scissors', 'paper'], ['paper', 'scissors', 'scissors'],
    #
    # ['scissors', 'rock', 'rock'], ['scissors', 'rock', 'paper'], ['scissors', 'rock', 'scissors'],
    # ['scissors', 'paper', 'rock'], ['scissors', 'paper', 'paper'], ['scissors', 'paper', 'scissors'],
    # ['scissors', 'scissors', 'rock'], ['scissors', 'scissors', 'paper'], ['scissors', 'scissors', 'scissors']]

    # Your output should be a list of lists containing strings. Each inner list
    # should have length equal to the input n.
    rps = ['rock', 'paper', 'scissors']
    plays = []

    def round_outcome(rnd_res, rnd_left):
        if rnd_left == 0:
            return plays.append(rnd_res.copy())
        for move in rps:
            round_outcome(rnd_res + [move], rnd_left - 1)

    round_outcome([], n)
    return plays


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
