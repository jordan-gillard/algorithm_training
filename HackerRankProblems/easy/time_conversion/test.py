import pytest

from time_conversion.alg import time_conversion


@pytest.mark.parametrize('string, expected', [
    ('12:00:00AM', '00:00:00'),
    ('07:05:45PM', '19:05:45'),
    ('12:45:54PM', '12:45:54')
])
def test_time_conversion(string, expected):
    assert time_conversion(string) == expected
