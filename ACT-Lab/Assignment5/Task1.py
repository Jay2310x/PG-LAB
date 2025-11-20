import random

def fractional_knapsack(weights, values, W):
    n = len(weights)
    items = []

    # Calculate value-to-weight ratio
    for i in range(n):
        items.append((values[i] / weights[i], weights[i], values[i]))

    # Sort items by ratio descending
    items.sort(reverse=True)

    total_value = 0.0
    remaining_capacity = W

    for ratio, wt, val in items:
        if remaining_capacity == 0:
            break

        if wt <= remaining_capacity:
            total_value += val
            remaining_capacity -= wt
        else:
            fraction = remaining_capacity / wt
            total_value += val * fraction
            remaining_capacity = 0

    return total_value


# -------- MAIN PROGRAM --------

# Take number of items
N = int(input("Enter number of items: "))

# Random weight & value generation
weights = [random.randint(1, 20) for _ in range(N)]
values  = [random.randint(10, 200) for _ in range(N)]

print("\nGenerated Weights:", weights)
print("Generated Values :", values)

# Take knapsack capacity
W = int(input("\nEnter knapsack capacity: "))

# Calculate result
max_value = fractional_knapsack(weights, values, W)
print("\nMaximum Value that can be obtained =", max_value)
