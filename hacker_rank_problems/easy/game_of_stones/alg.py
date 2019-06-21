"""Taken from https://www.hackerrank.com/challenges/game-of-stones-1/"""


def game_of_stones(stones: int) -> str:
    val = stones % 7
    if val <= 1:
        return 'Second'
    return 'First'
