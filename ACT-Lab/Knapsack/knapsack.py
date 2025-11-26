# 0/1 Knapsack Problem using DP

def knapsack(weights, profits, capacity):
    n = len(weights)
    
    # Create a 2D DP table where dp[i][w] represents the maximum profit 
    # for the first i items with weight limit w
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build table dp[][] in bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                # Include the item or exclude it — take the maximum profit
                dp[i][w] = max(profits[i - 1] + dp[i - 1][w - weights[i - 1]], 
                               dp[i - 1][w])
            else:
                # Cannot include the item if weight exceeds capacity
                dp[i][w] = dp[i - 1][w]

    # The bottom-right cell contains the maximum profit
    return dp[n][capacity]


# Example usage
if __name__ == "__main__":
    weights = [2, 3, 4, 5]
    profits = [3, 4, 5, 6]
    capacity = 5

    max_profit = knapsack(weights, profits, capacity)
    print("Maximum Profit:", max_profit)
