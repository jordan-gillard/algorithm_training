import pytest

from alg import solution


@pytest.mark.parametrize('word, expected', [
    ('AbBa', True),
    ('aBbA', True),
    ('abBA', True),
    ('ABba', True),
    ('abba', False),
    ('Abba', False),
    ('AbbA', False),
    ('ABBA', False)
])
def test_palindrome(word, expected):
    assert solution(word) == expected
