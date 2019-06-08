import pytest

from between_two_sets.alg import get_total_x


@pytest.mark.parametrize('array1, array2, expected', [
    ([2, 4], [16, 32, 96], 3),
    ([3, 4], [24, 48], 2),
    ([2, 6], [24, 36], 2)
])
def test_get_total_x(array1, array2, expected):
    assert get_total_x(array1, array2) == expected
