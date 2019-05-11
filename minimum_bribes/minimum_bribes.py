"""Taken from www.hackerrank.com/challenges/new-year-chaos/"""
from typing import List, Union


def minimum_bribes(array: List[int]) -> Union[int, str]:
    """Calculates the number of bribes in a chaotic line with a max of 2 bribes per person."""
    chaotic_line = [val - 1 for val in array]
    bribes = 0

    for place, sticker_val in enumerate(chaotic_line):
        if sticker_val - place > 2:
            return "Too chaotic"

        for i in range(max(sticker_val-1, 0), place):
            if chaotic_line[i] > sticker_val:
                bribes += 1

    return bribes
