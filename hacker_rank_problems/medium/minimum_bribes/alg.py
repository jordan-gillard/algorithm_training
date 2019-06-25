"""Taken from www.hackerrank.com/challenges/new-year-chaos/"""
from typing import List, Union


def minimum_bribes(array: List[int]) -> Union[int, str]:
    """Calculates the number of bribes in a chaotic line with a max of 2 bribes per person."""
    bribes: int = 0
    length_line = len(array)
    for i in range(1, len(array) + 1):
        displacement: int = array[-i] - (length_line - (i-1))
        if displacement > 2:
            return "Too chaotic"
        bribes += max(displacement, 0)
    return bribes

# TODO: implement with O(n) complexity by checking from the back
#  towards the front and switching positions.
#  https://www.hackerrank.com/challenges/new-year-chaos/editorial
