import pytest

from easy.camel_case.alg import camel_case


@pytest.mark.parametrize('string, expected', [
    ('', 0),
    ('saveTheWorld', 3)
])
def test_camel_case(string, expected):
    assert camel_case(string) == expected
