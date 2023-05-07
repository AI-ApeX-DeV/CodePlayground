graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 4, 'D': 1},
    'C': {'A': 3, 'B': 4, 'D': 5},
    'D': {'B': 1, 'C': 5}
}
import heapq

def prim(graph, start):
    # Create a set to store visited nodes and a dictionary to store the minimum distance to each node
    visited = set()
    min_distances = {node: float('inf') for node in graph}
    min_distances[start] = 0

    # Create a heap to store nodes to be processed
    heap = [(0, start)]

    while heap:
        # Pop the node with the smallest distance from the heap
        (dist, current_node) = heapq.heappop(heap)

        # If the node has already been visited, continue
        if current_node in visited:
            continue

        # Add the node to the visited set
        visited.add(current_node)

        # Iterate over neighbors of current node
        for neighbor, weight in graph[current_node].items():
            # If the neighbor has not been visited and the weight of the edge is less than the current minimum distance,
            # update the minimum distance and add the neighbor to the heap
            if neighbor not in visited and weight < min_distances[neighbor]:
                min_distances[neighbor] = weight
                heapq.heappush(heap, (weight, neighbor))

    return sum(min_distances.values())

d=prim(graph,'A')
print(d)
