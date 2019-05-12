import pytest

from easy.left_rotation import rotate_left


@pytest.mark.parametrize('array, number_of_rotations, expected', [
                         ([1, 2, 3, 4, 5], 0, [1, 2, 3, 4, 5]),
                         ([1, 2, 3, 4, 5], 1, [2, 3, 4, 5, 1]),
                         ([1, 2, 3, 4, 5], 2, [3, 4, 5, 1, 2])])
def test_left_rotation(array, number_of_rotations, expected):
    assert rotate_left(array, number_of_rotations) == expected
