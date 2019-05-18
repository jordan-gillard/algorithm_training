"""Taken from https://www.hackerrank.com/challenges/climbing-the-leaderboard/"""
from typing import List, Set, Optional


def climbing_leaderboard(leaderboard_scores: List[int], alices_scores: List[int]) -> List[int]:
    leaderboard_scores: Set[int] = set(leaderboard_scores)
    leaderboard_scores: List[int] = sorted(list(leaderboard_scores), reverse=False)
    place: int = len(leaderboard_scores) + 1
    index: int = 0
    alices_places: List[Optional[int]] = []
    max_score: int = max(leaderboard_scores)
    for score in leaderboard_scores:
        if index == len(alices_scores):
            break
        if alices_scores[index] < score:
            alices_places.append(place)
            index += 1
        elif alices_scores[index] == score:
            place -= 1
            alices_places.append(place)
            index += 1
        elif alices_scores[index] > max_score:
            alices_places.append(1)
            index += 1
        place -= 1
    return alices_places

# Iterate over each score, place -= 1 for each score
# If Alice has no more scores, then return Alice's places.
# If Alice's score is more than the score, move onto the next score.
# If Alice's score is less than the score, store Alice's place
# If Alice's score is equal to the score, increment the place by one and store it.
# Repeat for each of Alice's scores.
