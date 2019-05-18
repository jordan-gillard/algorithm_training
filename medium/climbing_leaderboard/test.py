from medium.climbing_leaderboard.algorithm import climbing_leaderboard


def test_leaderboard():
    assert climbing_leaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]) == [6, 4, 2, 1]
