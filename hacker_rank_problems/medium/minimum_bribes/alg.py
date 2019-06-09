"""Taken from www.hackerrank.com/challenges/new-year-chaos/"""
from typing import List, Union


# def minimum_bribes(array: List[int]) -> Union[int, str]:
#     """Calculates the number of bribes in a chaotic line with a max of 2 bribes per person."""
#     chaotic_line = [val - 1 for val in array]
#     bribes = 0
#
#     for place, sticker_val in enumerate(chaotic_line):
#         if sticker_val - place > 2:
#             return "Too chaotic"
#
#         for i in range(max(sticker_val-1, 0), place):
#             if chaotic_line[i] > sticker_val:
#                 bribes += 1
#
#     return bribes
def minimum_bribes(array: List[int]) -> Union[int, str]:
    """Calculates the number of bribes in a chaotic line with a max of 2 bribes per person."""
    chaotic_line: List[int] = [val - 1 for val in array]
    bribes: int = 0
    line_length = len(chaotic_line)
    for i in range(line_length + 1):
        # Check the last place and the place in front of it
        # if the number in front is higher, check the place
        # in front of that number. If its higher, switch the two
        # else, switch the one
        # if the number is greater than two difference, return too chaotic
        if i == line_length:
            break
        if chaotic_line[-i] - i > 2:
            return "Too chaotic"
        if chaotic_line[-i] < chaotic_line[-i-1]:
            if chaotic_line[-i-1] < chaotic_line[-i-2]:
                # Switch their spots
                bribes += 1
                chaotic_line[-i-1], chaotic_line[-i-2] = chaotic_line[-i-2], chaotic_line[-i-1]
            bribes += 1
            chaotic_line[-i], chaotic_line[-i - 1] = chaotic_line[-i-1], chaotic_line[-i]
    return bribes

# TODO: implement with O(n) complexity by checking from the back
#  towards the front and switching positions.
#  https://www.hackerrank.com/challenges/new-year-chaos/editorial

# Initial places: [2, 1, 5, 3, 4]
# Decrement all values by 1:
# New places: [1, 0, 4, 2, 3]
# First step:
# [1, 0, 2, 4, 3]
# Second step:
# [1, 0, 2, 3, 4]
# Third step:
# [0, 1, 2, 3, 4]
