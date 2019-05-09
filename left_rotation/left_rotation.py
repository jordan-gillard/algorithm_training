from typing import List


def rotate_left(array: List[int], number_of_rotations: int) -> List[int]:
    return array[number_of_rotations:] + array[:number_of_rotations]
