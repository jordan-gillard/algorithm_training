"""Taken from """
from typing import List


def rotate_left(array: List[int], number_of_rotations: int) -> List[int]:
    """Shift all the values in the given array to the left by number_of_rotations."""
    return array[number_of_rotations:] + array[:number_of_rotations]
