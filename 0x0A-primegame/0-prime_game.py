#!/usr/bin/python3

""" Prime Game """


def is_prime(n):
    """ Checking if it's a prime number """

    if n <= 1:
        return False
    for x in range(2, int(n**0.5) + 1):
        if n % x == 0:
            return False

    return True


def calculate_primes_up_to(n):
    """ Calculates the prime numbers upto n """

    primes = []
    for x in range(2, n + 1):
        if is_prime(x):
            primes.append(x)

    return primes


def isWinner(x, nums):
    """ Determines who's the winner of each game """

    wins = {"Maria": 0, "Ben": 0}

    for y in nums:
        primes = calculate_primes_up_to(y)
        if len(primes) % 2 == 0:
            wins["Ben"] += 1
        else:
            wins["Maria"] += 1

    if wins["Maria"] == wins["Ben"]:
        return None

    return max(wins, key=wins.get)
