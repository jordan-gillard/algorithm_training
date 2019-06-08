import pytest

from grading_students.alg import grading_students


@pytest.mark.parametrize('given, expected', [
    ([73, 67, 38, 33], [75, 67, 40, 33])
])
def test_grading_students(given, expected):
    assert grading_students(given) == expected
