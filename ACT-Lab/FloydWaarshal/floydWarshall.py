# Floyd Warshall Algorithm in Python (with path reconstruction)

def floyd_warshall_with_path(A):
    n = len(A)
    INF = float('inf')

    # Distance and Next matrices
    dist = [row[:] for row in A]
    next_node = [[None if A[i][j] == INF else j for j in range(n)] for i in range(n)]

    # Floyd–Warshall main loop
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]

    return dist, next_node


def construct_path(u, v, next_node):
    """Reconstruct the shortest path from u to v."""
    if next_node[u][v] is None:
        return []
    path = [u]
    while u != v:
        u = next_node[u][v]
        path.append(u)
    return path


# Example usage
if __name__ == "__main__":
    INF = float('inf')
    A = [
        [0, 5, INF, 10],
        [INF, 0, 3, INF],
        [INF, INF, 0, 1],
        [INF, INF, INF, 0]
    ]

    dist, next_node = floyd_warshall_with_path(A)

    print("All-Pairs Shortest Path Distances:")
    for row in dist:
        print(["INF" if x == INF else x for x in row])

    print("\nShortest Paths Between All Pairs:")
    n = len(A)
    for i in range(n):
        for j in range(n):
            if i != j:
                path = construct_path(i, j, next_node)
                if path:
                    print(f"Path {i} → {j}: {' -> '.join(map(str, path))} | Distance = {dist[i][j]}")
                else:
                    print(f"Path {i} → {j}: No path exists")
