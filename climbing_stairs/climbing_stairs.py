#!/usr/bin/python

import sys


def climbing_stairs(n, cache=None):
    # Imagine a small child ascending a staircase that has `n` steps. The child
    # can hop either 1, 2, or 3 steps at a time. Implement a function
    # `climbing_stairs` that counts the number of possible ways in which the
    # child can ascend the staircase.

    # For example, for a staircase with `n = 3` (the stair has 3 steps), there
    # are 4 possible ways for the child to ascend the staircase:

    # 1. They can jump 3 hops of 1 step
    #   n // 1 == n
    # 2. They can go up 1 step, followed by a jump of 2 steps
    #   1 + n // 2 == n
    # 3. They can jump up 2 steps, then go up the last step
    #   n // 2 + 1 == n
    # 4. They can make a single jump of 3 steps
    #   n // 3 == n

    # Thus, `climbing_stairs(3)` should return an answer of 4.

    # Attempt 1: recursive (small)
    # O(~n**3)? Not quite n, but we're calling the function 3 times.
    # if n <= 0:
    #     return 1
    # elif n == 1 or n == 2:
    #     return n
    # else:
    #     return climbing_stairs(n - 1) + climbing_stairs(n - 2) + climbing_stairs(n - 3)

    # Attempt 2: dynamic (large)
    if cache is None or isinstance(cache, list):
        cache = {}
    if n <= 0:
        return 1
    elif n == 1 or n == 2:
        return n
    elif n in cache:
        return cache[n]
    else:
        steps = climbing_stairs(
            n - 1, cache) + climbing_stairs(n - 2, cache) + climbing_stairs(n - 3, cache)
        cache[n] = steps
        # print(f"step {n}: {cache[n]}")
        return steps


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_stairs = int(sys.argv[1])
        print("There are {ways} ways for a child to jump {n} stairs.".format(
            ways=climbing_stairs(num_stairs), n=num_stairs))
    else:
        print('Usage: climbing_stairs.py [num_stairs]')
