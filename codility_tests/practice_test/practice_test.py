def solution(A):
    A = list(set([num for num in A if num > 0]))
    A.sort()
    i = 0
    while i < len(A):
        if A[i] != (i + 1):
            return i+1
        i += 1
    return i+1
