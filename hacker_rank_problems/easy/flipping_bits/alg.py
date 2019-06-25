"""Taken from https://www.hackerrank.com/challenges/flipping-bits/problem"""


def flipping_bits(num: int) -> int:
    """You will be given a list of 32 bit unsigned integers. Flip all the bits and print the result as an
    unsigned integer.
    """
    flipper = 4294967295
    return num ^ flipper
