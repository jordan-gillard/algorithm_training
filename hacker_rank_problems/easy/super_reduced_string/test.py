import pytest

from super_reduced_string.alg import reduced_string


@pytest.mark.parametrize('original, expected', [
    ('aaabccddd', 'abd'),
    ('baab', 'Empty String'),
    ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
     'Empty String'),
    ('lrfkqyuqfjjfquyqkfrlkxyqvnrtyssytrnvqyxkfrzrmzlygffgylzmrzrfveulqfpdbhhbdpfqluevlqdqrrcrwddwrcrrqdql',
     'Empty String')
])
def test_reduced_string(original, expected):
    assert reduced_string(original) == expected
