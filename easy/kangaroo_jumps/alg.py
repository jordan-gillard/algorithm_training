"""Taken from www.hackerrank.com/challenges/kangaroo/problem"""


def kangaroo(x1: int, v1: int, x2: int, v2: int):
    if v1 - v2 == 0:
        return 'NO'
    jumps = -(x1-x2)/(v1-v2)
    if jumps % 1 == 0 and jumps > 0:
        return 'YES'
    return 'NO'
