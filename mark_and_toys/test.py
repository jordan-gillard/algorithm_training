import pytest

from mark_and_toys.max_toys import max_toys


@pytest.mark.parametrize("toy_prices, budget, expected", [
    ([1, 2, 3, 4], 7, 3)
])
def test_max_toys(toy_prices, budget, expected):
    assert max_toys(toy_prices, budget) == expected
