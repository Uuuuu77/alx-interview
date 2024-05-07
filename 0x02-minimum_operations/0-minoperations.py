#!/usr/bin/python3

""" Module to calculate minimum operations """


def minOperations(n):
    """ Returns minimum operations """
    if n <= 1:
        return 0

    minOps = 0
    divisor = 2

    while divisor * divisor <= n:
        while n % divisor == 0:
            minOps += divisor
            n //= divisor
        divisor += 1

    if n > 1:
        minOps += n

    return minOps
