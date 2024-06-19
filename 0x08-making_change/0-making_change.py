#!/usr/bin/python3

""" Making change using a greedy algorithm """


def makeChange(coins, total):
    """ Returns the fewest number of coins
        needed to meet the given total amount
    """
    if total < 1:
        return 0

    coins.sort(reverse=True)
    num_coins = 0

    for coin in coins:
        num_coins += total // coin
        total %= coin

    return num_coins if total == 0 else -1
