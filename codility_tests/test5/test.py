import pytest

from alg import solution


@pytest.mark.parametrize('array, expected', [
    ([1, 2, 3, 5, 6, 7, 8, 9], 5),
    ([1, 2, 3, 10, 11, 15], 3),
    ([5, 4, 2, 1], 2),
    ([3, 5, 7, 10, 15], 1),
    ([5, -3, -2, -1, 0, 1, 5, 6, 7], 5)
])
def test_solution(array, expected):
    assert solution(array) == expected
