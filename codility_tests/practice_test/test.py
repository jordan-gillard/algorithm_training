import pytest

from codility_tests.practice_test.practice_test import solution


@pytest.mark.parametrize('array, expected', [
    ([1, 2, 3], 4),
    ([-1, -3], 1),
    ([1, 3, 6, 4, 1, 2], 5),
    ([0, 1, -1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12], 11)
])
def test_demo_problem(array, expected):
    assert solution(array) == expected
