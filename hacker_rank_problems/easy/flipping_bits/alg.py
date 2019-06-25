"""Taken from https://www.hackerrank.com/challenges/flipping-bits/problem"""


def flipping_bits(num: int) -> int:
    """You will be given a list of 32 bit unsigned integers. Flip all the bits and print the result as an
    unsigned integer.
    """
    byte_utf: str = '{:032b}'.format(num)
    flipped: str = ''
    for str_num in byte_utf:
        flipped += str(int(not int(str_num)))
    return int(flipped, 2)
