import pytest

from hacker_rank_problems.medium.common_child.alg import common_child


@pytest.mark.parametrize("str1, str2, expected", [
    ("HARRY", "SALLY", 2),
    ("AA", "BB", 0),
    ("SHINCHAN", "NOHARAAA", 3),
    ("ABCDEF", "FBDAMN", 2)
])
def test_common_child(str1, str2, expected):
    assert common_child(str1, str2) == expected
