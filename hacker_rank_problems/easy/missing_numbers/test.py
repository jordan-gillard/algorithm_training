from hacker_rank_problems.easy.missing_numbers.alg import missing_numbers


def test_missing_numbers():
    assert missing_numbers([7, 2, 5, 3, 5, 3], [7, 2, 5, 4, 6, 3, 5, 3]) == [4, 6]
