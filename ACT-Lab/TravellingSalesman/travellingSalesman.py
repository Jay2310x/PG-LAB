import math

def travelling_salesman(cost):
    n = len(cost)
    VISITED_ALL = (1 << n) - 1  # bitmask when all cities are visited

    # dp[mask][i] = minimum cost to reach city i with visited mask
    dp = [[math.inf] * n for _ in range(1 << n)]
    dp[1][0] = 0  # start from city 0

    for mask in range(1 << n):
        for u in range(n):
            if not (mask & (1 << u)):  # if city u not in mask
                continue
            for v in range(n):
                if mask & (1 << v):  # if city v already visited
                    continue
                new_mask = mask | (1 << v)
                dp[new_mask][v] = min(dp[new_mask][v], dp[mask][u] + cost[u][v])

    # Return to start city (0)
    ans = math.inf
    for i in range(1, n):
        ans = min(ans, dp[VISITED_ALL][i] + cost[i][0])

    return ans


# Example usage
cost = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

print("Minimum cost of the TSP tour:", travelling_salesman(cost))