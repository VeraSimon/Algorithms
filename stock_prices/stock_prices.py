#!/usr/bin/python

import argparse


def find_max_profit(prices):
    # Write a function `find_max_profit` that receives as input a list of stock
    # prices. Your function should return the maximum profit that can be made
    # from a single buy and sell. You must buy first before selling; no
    # shorting is allowed here.

    # For example, `find_max_profit([1050, 270, 1540, 3800, 2])` should return
    # 3530, which is the maximum profit that can be made from a single buy and
    # then sell of these stock prices.

    # [1050, 270, 1540, 3800, 2]
    # 1050:
    #     270 - 1050 = -780
    #     1540 - 1050 = 490
    #     3800 - 1050 = 2750
    #     2 - 1050 = -1048
    # 270:
    #     1540 - 270 = 1270
    #     3800 - 270 = 3530
    #     2 - 270 = -268
    # 1540:
    #     3800 - 1540 = 2260
    #     2 - 1540 = -1538
    # 3800:
    #     2 - 3800 = -3798

    # Attempt 1: iterative
    # O(n log n)? It's passing over (almost all of) the array once in the outer
    # loop, then the sub array gets shorter by one each iteration of the outer
    # loop.
    # The `profit` initialization value gets checked twice, but :shrug:
    profit = prices[1] - prices[0]
    for i in range(len(prices) - 1):
        for j in range(i + 1, len(prices)):
            if prices[j] - prices[i] > profit:
                profit = prices[j] - prices[i]

    return profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
