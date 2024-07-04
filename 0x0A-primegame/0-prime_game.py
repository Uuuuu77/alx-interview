#!/usr/bin/python3

""" Prime Game """

def isWinner(x, nums):
    """ Winner of the prime game """
    def is_prime(n):
        if n < 2:
            return False
        for x in range(2, int(n**0.5) + 1):
            if n % x == 0:
                return False
        return True

    def count_primes(n):
        return sum(is_prime(x) for x in range(2, n+1))

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = count_primes(n)
        if primes % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
