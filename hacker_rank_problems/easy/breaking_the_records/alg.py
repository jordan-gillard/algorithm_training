from typing import List


def breaking_records(scores: List[int]) -> List[int]:
    broke_max = 0
    broke_min = 0
    score_max = scores[0]
    score_min = scores[0]
    for score in scores[1:]:
        if score < score_min:
            broke_min += 1
            score_min = score
        elif score > score_max:
            broke_max += 1
            score_max = score
    return [broke_max, broke_min]
