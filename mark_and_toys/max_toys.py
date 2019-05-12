"""Taken from www.hackerrank.com/challenges/mark-and-toys/"""


def max_toys(prices, k) -> int:
    """Returns an int representing the max number of toys that can be bought with k."""
    prices.sort()
    toys = 0
    for toy_price in prices:
        if k - toy_price >= 0:
            toys += 1
            k -= toy_price
    return toys
