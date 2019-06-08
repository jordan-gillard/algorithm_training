import pytest

from birthday_chocolate.alg import birthday


@pytest.mark.parametrize("chocolate_bar, day, length, expected", [
    ([1, 2, 1, 3, 2], 3, 2, 2),
    ([4], 4, 1, 1)
])
def test_birthday(chocolate_bar, day, length, expected):
    assert birthday(chocolate_bar, day, length) == expected
