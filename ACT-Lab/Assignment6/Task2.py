import heapq
import random

def dijkstra(v, edges, source):
    graph = [[] for _ in range(v)]

    # Build adjacency list
    for u, w, wt in edges:
        graph[u].append((w, wt))
        graph[w].append((u, wt))  # undirected graph

    dist = [float('inf')] * v
    dist[source] = 0

    pq = [(0, source)]  # (distance, node)

    while pq:
        d, node = heapq.heappop(pq)

        if d > dist[node]:
            continue

        for neigh, weight in graph[node]:
            if dist[node] + weight < dist[neigh]:
                dist[neigh] = dist[node] + weight
                heapq.heappush(pq, (dist[neigh], neigh))

    return dist


# ---------- MAIN PROGRAM ----------

v = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

# Randomly generate edges
edges = []
for _ in range(e):
    u = random.randint(0, v-1)
    w = random.randint(0, v-1)
    while w == u:
        w = random.randint(0, v-1)
    wt = random.randint(1, 20)
    edges.append((u, w, wt))

print("\nGenerated Edges (u, v, weight):")
for edge in edges:
    print(edge)

source = int(input("\nEnter source vertex: "))

distances = dijkstra(v, edges, source)

print("\nShortest distances from source", source, ":")
for i, d in enumerate(distances):
    print(f"Vertex {i} -> {d}")
