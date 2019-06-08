"""Taken from www.hackerrank.com/challenges/the-birthday-bar/problem"""
from typing import List


def birthday(chocolate_bar: List[int], day: int, length: int) -> int:
    matches = 0
    day_sum = sum(chocolate_bar[:length])
    if day_sum == day:
        matches += 1
    for i in range(length, len(chocolate_bar)):
        day_sum += chocolate_bar[i]
        day_sum -= chocolate_bar[i-length]
        if day_sum == day:
            matches += 1
    return matches
