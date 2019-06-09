"""Taken from https://www.hackerrank.com/challenges/climbing-the-leaderboard/"""
from typing import List, Set, Optional


def climbing_leaderboard(leaderboard_scores: List[int], alices_scores: List[int]) -> List[int]:
    """Steps:
        Iterate over each score, place -= 1 for each score
        If Alice has no more scores, then return Alice's places.
        If Alice's score is more than the score, move onto the next score.
        If Alice's score is less than the score, store Alice's place
        If Alice's score is equal to the score, increment the place by one and store it.
        Repeat for each of Alice's scores.
    """
    leaderboard_scores: Set[int] = set(leaderboard_scores)
    leaderboard_scores: List[int] = sorted(list(leaderboard_scores), reverse=False)
    place: int = len(leaderboard_scores) + 1
    index: int = 0
    alices_places: List[Optional[int]] = []
    for alice_score in alices_scores:
        while index < len(leaderboard_scores) and alice_score >= leaderboard_scores[index]:
            place -= 1
            index += 1
        alices_places.append(place)
    return alices_places
