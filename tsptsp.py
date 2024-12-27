import numpy as np

def tsp_nearest_neighbor(graph):
    n = len(graph)
    visited = [False] * n
    path = [0]  # Start from the first node
    visited[0] = True

    for _ in range(n - 1):
        last = path[-1]
        next_city = np.argmin([graph[last][j] if not visited[j] else float('inf') for j in range(n)])
        path.append(next_city)
        visited[next_city] = True

    path.append(0)  # Return to the starting point
    return path

# Input graph from the user
n = int(input("Enter number of cities: "))
print("Enter distance matrix row by row (space-separated):")
graph = [list(map(int, input().split())) for _ in range(n)]

# Solve TSP
path = tsp_nearest_neighbor(graph)
print("TSP Path:", path)
