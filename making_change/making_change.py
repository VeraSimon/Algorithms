#!/usr/bin/python

import sys

# One day one of the wealthiest and also most eccentric patrons of the bank
# walks up to your stall. They hand you some cash and tell you they want you to
# figure out exactly how many ways there are to make change for the amount of
# money they plopped down in front of you using only pennies, nickels, dimes,
# quarters, and half-dollars.

# Since this is a bank, you have an infinite supply of coinange. Write a
# function `making_change` that receives as input an amount of money in cents
# as well as an array of coin denominations and calculates the total number of
# ways in which change can be made for the input amount using the given coin denominations.

# For example, `making_change(10)` should return 4, since there are 4 ways to make change
# for 10 cents using pennies, nickels, dimes, quarters, and half-dollars:

#  1. We can make change for 10 cents using 10 pennies
#  2. We can use 5 pennies and a nickel
#  3. We can use 2 nickels
#  4. We can use a single dime


def making_change(amount, denominations):
    cache = {}

    def change_calc(amount_left):
        # else:
        #     steps = climbing_stairs(n - 1, cache) + climbing_stairs(n - 2, cache) + climbing_stairs(n - 3, cache)
        #     cache[n] = steps
        #     return steps

        if amount_left <= 4:
            return 1
        elif amount_left in cache:
            return cache[amount_left]
        else:
            ways = 0
            for i in denominations:
                # print(i)
                ways += change_calc(amount_left - i)
                # print(ways)
            cache[amount_left] = ways
            return ways

    return change_calc(amount)


if __name__ == "__main__":
    # Test out your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
