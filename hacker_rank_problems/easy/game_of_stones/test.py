import pytest

from hacker_rank_problems.easy.game_of_stones.alg import game_of_stones


@pytest.mark.parametrize('stones, expected', [
    (1, 'Second'),
    (2, 'First'),
    (3, 'First'),
    (4, 'First'),
    (5, 'First'),
    (6, 'First'),
    (7, 'Second'),
    (8, 'Second'),
    (9, 'First'),
    (10, 'First'),
    (11, 'First'),
    (12, 'First'),
    (13, 'First'),
    (14, 'Second'),
    (15, 'Second'),
    (16, 'First'),
    (17, 'First'),
    (18, 'First'),
    (19, 'First'),
    (20, 'First'),
    (21, 'Second'),
    (22, 'Second'),
])
def test_game_of_stones(stones, expected):
    assert game_of_stones(stones) == expected
