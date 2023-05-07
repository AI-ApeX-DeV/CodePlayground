from queue import PriorityQueue

def astar_search(graph, start, goal, heuristic):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for neighbor in graph[current]:
            new_cost = cost_so_far[current] + graph[current][neighbor]
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(goal, neighbor)
                frontier.put(neighbor, priority)
                came_from[neighbor] = current

    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path

# Example usage
graph = {
    'A': {'B': 1, 'C': 2},
    'B': {'D': 3},
    'C': {'D': 1},
    'D': {'E': 4},
    'E': {}
}
heuristic = lambda a, b: abs(ord(a) - ord(b))
start = 'A'
goal = 'E'
path = astar_search(graph, start, goal, heuristic)
print(path)
