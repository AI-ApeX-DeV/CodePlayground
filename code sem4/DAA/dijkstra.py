import heapq

# Sample graph represented as a dictionary of dictionaries

graph = {
    1: {2: 10, 4: 5},
    2: {3: 1, 4: 2},
    3: {5: 4},
    4: {2: 3, 3: 9, 5: 2},
    5: {1: 7, 3: 6}
}

def dijkstra(graph, start):
    # Set up distances dictionary with all distances set to infinity except start node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Set up heap to store nodes to be processed
    heap = [(0, start)]

    while heap:
        # Pop the node with the smallest distance from the heap
        (dist, current_node) = heapq.heappop(heap)

        # If we've already found a shorter path to the node, skip it
      #  if dist > distances[current_node]:
         #   continue

        # Iterate over neighbors of current node
        for neighbor, weight in graph[current_node].items():
            # Calculate tentative distance to neighbor via current node
            tentative_distance = dist + weight

            # If tentative distance is shorter than current distance, update distances
            if tentative_distance < distances[neighbor]:
                distances[neighbor] = tentative_distance
                heapq.heappush(heap, (tentative_distance, neighbor))

    return distances

# Find shortest path from node 1 to all other nodes
distances = dijkstra(graph, 1)
print(distances)


