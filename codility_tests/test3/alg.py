def solution(A, B):
    window = len(B)
    last_occurrence = -1
    for i in range((len(A) - window)+1):
        if A[i:window+i] == B:
            last_occurrence = i
    return last_occurrence
