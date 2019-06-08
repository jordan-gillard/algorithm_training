"""from www.hackerrank.com/challenges/apple-and-orange/"""
from typing import List, Tuple


def count_apples_and_oranges(s: int, t: int, a: int, b: int, apples: List[int], oranges: List[int]) -> Tuple[int, int]:
    # s = left of house
    # t = right of house
    # a = apple tree
    # b = orange tree
    # lists are of fallen fruit distances from their tree
    def number_of_hits(house_l: int, house_r: int, tree_loc: int, fruits: List[int]) -> int:
        hits = 0
        for fruit in fruits:
            fruit += tree_loc
            if house_l <= fruit <= house_r:
                hits += 1
        return hits

    apple_hits = number_of_hits(s, t, a, apples)
    orange_hits = number_of_hits(s, t, b, oranges)
    return apple_hits, orange_hits
