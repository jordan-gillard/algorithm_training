from typing import List


def solution(A: List[int]):
    max_run = 1
    current_run = 1
    for i in range(len(A) - 1):
        if abs(A[i] - A[i+1]) == 1:
            current_run += 1
        else:
            current_run = 1
        max_run = max(max_run, current_run)
    return max_run
