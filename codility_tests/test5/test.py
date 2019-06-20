import pytest

from test5.alg import max_run


@pytest.mark.parametrize('array, expected', [
    ([1, 2, 3, 5, 6, 7, 8, 9], 5),
    ([1, 2, 3, 10, 11, 15], 3),
    ([5, 4, 2, 1], 2),
    ([3, 5, 7, 10, 15], 1),
    ([5, -3, -2, -1, 0, 1, 5, 6, 7], 5)
])
def test_max_run(array, expected):
    assert max_run(array) == expected
