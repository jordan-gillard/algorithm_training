"""Taken from https://www.hackerrank.com/challenges/common-child/problem"""


def common_child(str1: str, str2: str) -> int:
    """https://en.wikipedia.org/wiki/Longest_common_subsequence_problem"""
    longest_max: int = 0
    for index_1 in range(len(str1)):
        index_2: int = 0
        while index_2 < len(str2) and index_1 < len(str1):
            if str1[index_1] == str2[index_2]:
                index_1 += 1
                longest_max += 1
            index_2 += 1
    return longest_max
