import pytest

from alg import solution


@pytest.mark.parametrize('array, seq, expected', [
    ([9, 3, 7, 9, 2], [9, 3, 7], 0),
    ([9, 3, 7, 9, 2], [7, 9], 2),
    ([9, 3, 7, 9, 2], [1, 7, 9], -1),
    ([9, 3, 7, 9, 2], [2], 4),
    ([9, 3, 7, 9, 2], [9, 3, 7, 9, 2], 0)
])
def test_solution(array, seq, expected):
    assert solution(array, seq) == expected
