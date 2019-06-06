"""Taken from www.hackerrank.com/challenges/between-two-sets/"""
from typing import List, Optional


def get_total_x(array1: List[int], array2: List[int]) -> int:
    """
    1) The elements of the first array are all factors of the integer being considered
    2) The integer being considered is a factor of all elements of the second array
    """
    hpf: int = min(array2)  # highest possible factor
    lpf: int = max(array1)  # lowest possible factor
    possible_factors: List[Optional[int]] = []

    for i in range(lpf, hpf+1):
        if hpf % i == 0:
            possible_factors.append(i)

    first_array_factors = List[Optional[int]] = []
    for i in possible_factors:
        i_is_good = True
        for val in array1:
            if i % val != 0:
                i_is_good = False
        if i_is_good:
            first_array_factors.append(i)

    final: int = 0
    for i in first_array_factors:
        i_is_good = True
        for num in array2:
            if num % i != 0:
                i_is_good = False
        if i_is_good:
            final += 1
    return final
