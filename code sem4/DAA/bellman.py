graph = {
    'A': {'B': -1, 'C':  4},
    'B': {'C':  3, 'D':  2, 'E':  2},
    'C': {},
    'D': {'B':  1, 'C':  5},
    'E': {'D': -3}
}


def bellman_ford(graph, start):
    # Step 1: Initialize distances from start to all other vertices as infinity
    # and distance to start as 0
    distance = {node: float('inf') for node in graph}
    distance[start] = 0

    # Step 2: Relax edges repeatedly
    for _ in range(len(graph) - 1):
        for u in graph:
            for v, w in graph[u].items():
                if distance[u] != float('inf') and distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w

    # Step 3: Check for negative-weight cycles
    for u in graph:
        for v, w in graph[u].items():
            if distance[u] != float('inf') and distance[u] + w < distance[v]:
                print("Graph contains negative weight cycle")
                return

    return distance

print(bellman_ford(graph, 'A'))