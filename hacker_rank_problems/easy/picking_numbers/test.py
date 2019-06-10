import pytest

from easy.picking_numbers.alg import picking_numbers


@pytest.mark.parametrize('array, expected', [
    ([1, 2, 2, 3, 1, 2], 5),
    ([4, 6, 5, 3, 3, 1], 3),
    ([1, 1, 1, 1, 1, 1, 1], 7)
])
def test_picking_numbers(array, expected):
    assert picking_numbers(array) == expected
