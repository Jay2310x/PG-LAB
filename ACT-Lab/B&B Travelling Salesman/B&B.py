import math

def tsp_branch_and_bound(dist):
    n = len(dist)

    # Precompute the minimum outgoing edge from each city (for lower bound)
    min_edge = []
    for i in range(n):
        m = math.inf
        for j in range(n):
            if i != j and dist[i][j] > 0:
                m = min(m, dist[i][j])
        min_edge.append(0 if m == math.inf else m)

    best_cost = math.inf
    best_path = []

    def dfs(curr_city, visited, curr_cost, path):
        nonlocal best_cost, best_path

        # If all cities visited, close the tour by returning to start (0)
        if len(path) == n:
            tour_cost = curr_cost + dist[curr_city][0]
            if tour_cost < best_cost:
                best_cost = tour_cost
                best_path = path + [0]
            return

        # Try all next cities
        for next_city in range(n):
            if not visited[next_city] and dist[curr_city][next_city] > 0:
                new_cost = curr_cost + dist[curr_city][next_city]

                # --- Lower bound estimation ---
                remaining_bound = 0
                for k in range(n):
                    if not visited[k] and k != next_city:
                        remaining_bound += min_edge[k]
                bound = new_cost + remaining_bound

                # Prune if bound already worse than best known solution
                if bound >= best_cost:
                    continue

                visited[next_city] = True
                dfs(next_city, visited, new_cost, path + [next_city])
                visited[next_city] = False

    # Start from city 0
    visited = [False] * n
    visited[0] = True
    dfs(0, visited, 0, [0])

    return best_cost, best_path


# ------------ MAIN PROGRAM ------------

n = int(input("Enter number of cities: "))

print("\nEnter distance matrix (use 0 for no self-distance):")
dist = []
for i in range(n):
    row = list(map(int, input(f"Row {i} (space separated): ").split()))
    dist.append(row)

min_cost, route = tsp_branch_and_bound(dist)

print("\nShortest route (tour):", " -> ".join(map(str, route)))
print("Minimum cost:", min_cost)
