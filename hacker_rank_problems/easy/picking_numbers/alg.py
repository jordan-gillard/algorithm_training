"""Taken from www.hackerrank.com/challenges/picking-numbers/"""
from typing import List


def picking_numbers(array: List[int]) -> int:
    highest_count: int = 0
    for i in array:
        counts_here = array.count(i)
        counts_ahead = array.count(i+1)
        highest_count = max(counts_here + counts_ahead, highest_count)
    return highest_count
