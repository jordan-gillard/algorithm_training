import pytest

from hacker_rank_problems.medium.encryption.alg import encryption


@pytest.mark.parametrize('sentence, expected', [
    ('haveaniceday', 'hae and via ecy'),
    ('feedthedog', 'fto ehg ee dd'),
    ('chillout', 'clu hlt io')
])
def test_encryption(sentence, expected):
    assert encryption(sentence) == expected
