import pytest

from hacker_rank_problems.easy.breaking_the_records.alg import breaking_records


@pytest.mark.parametrize("scores, results", [
    ([10, 5, 20, 20, 4, 5, 2, 25, 1], [2, 4]),
    ([3, 4, 21, 36, 10, 28, 35, 5, 24, 42], [4, 0])
])
def test_breaking_records(scores, results):
    assert breaking_records(scores) == results
