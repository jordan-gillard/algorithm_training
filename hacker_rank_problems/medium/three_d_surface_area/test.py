import pytest

from hacker_rank_problems.medium.three_d_surface_area.alg import surface_area


@pytest.mark.parametrize("areas, expected_price", [
    ([[1]], 6),
    ([[1, 3, 4], [2, 2, 3], [1, 2, 4]], 60)
])
def test_surface_area(areas, expected_price):
    assert surface_area(areas) == expected_price

# 12 * 1
# 6 * 2
# 8 * 1
