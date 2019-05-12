import pytest

from mark_and_toys.max_toys import max_toys


@pytest.mark.parametrize("toy_prices, budget, expected", [
    ([1, 2, 3, 4], 7, 3),
    ([1, 12, 5, 111, 200, 1000, 10], 50, 4)
])
def test_max_toys(toy_prices, budget, expected):
    assert max_toys(toy_prices, budget) == expected
