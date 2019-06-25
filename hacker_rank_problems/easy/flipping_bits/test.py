import pytest

from hacker_rank_problems.easy.flipping_bits.alg import flipping_bits


@pytest.mark.parametrize("num, expected_num", [
    (2147483647, 2147483648),
    (1, 4294967294),
    (0, 4294967295)
])
def test_flipping_bits(num, expected_num):
    assert flipping_bits(num) == expected_num
