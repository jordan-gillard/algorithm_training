import pytest

from kangaroo_jumps.alg import kangaroo


@pytest.mark.parametrize('start1, jump1, start2, jump2, expected', [
    (0, 3, 4, 2, 'YES'),
    (0, 2, 5, 3, 'NO'),
    (43, 2, 70, 2, 'NO')
])
def test_kangaroo(start1, jump1, start2, jump2, expected):
    assert kangaroo(start1, jump1, start2, jump2) == expected
