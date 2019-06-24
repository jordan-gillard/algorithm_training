"""Taken from https://www.hackerrank.com/challenges/missing-numbers/problem"""
from collections import Counter
from typing import List


def missing_numbers(arr: List[int], brr: List[int]):
    arr_counts = Counter(arr)
    brr_counts = Counter(brr)
    return sorted([i for i in brr_counts.keys() if arr_counts.get(i) != brr_counts.get(i)])
