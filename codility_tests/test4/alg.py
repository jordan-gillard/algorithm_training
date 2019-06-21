from typing import List


def crypto_solution(arr: List[int]) -> int:
    local_min_index: int = 0
    highest_val: int = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[local_min_index]:
            local_min_index = i
        highest_val = max(highest_val, arr[i] - arr[local_min_index])
    return highest_val
