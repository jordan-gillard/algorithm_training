test_cases = int(input())

for case in range(test_cases):
    N, K, x1, y1, C, D, E1, E2, F = [int(i) for i in input().split()]
    xi = []
    yi = []
    for i in range(2, N+1):
        xi.append((C * (x1-1) + D * (y1-1) + E1) % F)
        yi.append((D * (x1-1) + C * (y1-1) + E2) % F)
    case += 1  # move this down later
    A = [((i[0]+i[1]) % F) for i in zip(xi, yi)]
    # power % 1000000007
    power = 0
    for window in range(K):
        pass
