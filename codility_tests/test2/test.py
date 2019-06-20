import pytest

from codility_tests.test2.alg import solution


@pytest.mark.parametrize('string, expected', [
    ('Hello world!', 2),
    ('', 0),
    ('one', 1),
    ('This is a really long string right here.', 8),
    ('Hey   young     world ', 3),
    ('the world is   yours   .', 4)
])
def test_num_words(string, expected):
    assert solution(string) == expected
