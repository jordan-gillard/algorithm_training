import pytest

from test4.alg import crypto_solution


@pytest.mark.parametrize('array, expected', [
    ([10, 20, 30, 40, 50], 40),
    ([23, 55, 67, 22, 40, 65, 44, 20, 0], 44),
    ([10], 0),
    ([50, 10, 5], 0)
])
def test_solution(array, expected):
    assert crypto_solution(array) == expected
