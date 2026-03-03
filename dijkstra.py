import math

# Graph as adjacency matrix (exactly as in the image)
graph = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]
]

num_vertices = len(graph)

def min_distance(dist, visited):
    min_val = math.inf
    min_index = -1
    for v in range(num_vertices):
        if not visited[v] and dist[v] < min_val:
            min_val = dist[v]
            min_index = v
    return min_index

def dijkstra(start):
    dist = [math.inf] * num_vertices
    visited = [False] * num_vertices
    parent = [-1] * num_vertices

    dist[start] = 0
    table_rows = []

    for step in range(num_vertices):
        u = min_distance(dist, visited)

        # 🔴 FIX: Stop if no reachable vertex left
        if u == -1:
            break

        visited[u] = True

        # Save table row
        row = []
        for d in dist:
            row.append("INF" if d == math.inf else str(int(d)))
        table_rows.append((step + 1, u, row.copy()))

        # Update distances
        for v in range(num_vertices):
            if (graph[u][v] > 0 and
                not visited[v] and
                dist[u] + graph[u][v] < dist[v]):
                dist[v] = dist[u] + graph[u][v]
                parent[v] = u

    return dist, parent, table_rows

def get_path(parent, j):
    path = []
    while j != -1:
        path.append(str(j))
        j = parent[j]
    return " -> ".join(path[::-1])

# Run Dijkstra from node 0
distances, parents, table = dijkstra(0)

# ---------------- PRINT OUTPUT ----------------

print("\nDijkstra Iteration Table:\n")
print("Step | Visited | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8")
print("--------------------------------------------------")

for step, visited_node, row in table:
    print(f"{step:<4} | {visited_node:^7} | " + " | ".join(row))

print("\nShortest Paths from Node 0:\n")
for i in range(num_vertices):
    if distances[i] == math.inf:
        print(f"To Node {i}: No Path")
    else:
        path = get_path(parents, i)
        print(f"To Node {i}: {path}  (Distance: {int(distances[i])})")

# ---------------- SAVE TO FILE ----------------

with open("dijkstra_output.txt", "w", encoding="utf-8") as f:
    f.write("Dijkstra Iteration Table:\n\n")
    f.write("Step | Visited | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8\n")
    f.write("--------------------------------------------------\n")

    for step, visited_node, row in table:
        f.write(f"{step:<4} | {visited_node:^7} | " + " | ".join(row) + "\n")

    f.write("\nShortest Paths from Node 0:\n\n")

    for i in range(num_vertices):
        if distances[i] == math.inf:
            f.write(f"To Node {i}: No Path\n")
        else:
            path = get_path(parents, i)
            f.write(f"To Node {i}: {path}  (Distance: {int(distances[i])})\n")

print("\nOutput saved to dijkstra_output.txt")