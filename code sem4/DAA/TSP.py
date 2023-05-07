import sys

def tsp(graph, start):
    # Set up memoization table
    memo = {}

    # Define recursive helper function
    def tsp_helper(current, visited):
        # Check if subproblem has already been solved
        if (current, visited) in memo:
            return memo[(current, visited)]

        # Base case: all nodes have been visited
        if visited == (1 << len(graph)) - 1:
            return graph[current][start]

        # Recursive case: find the minimum cost of visiting each unvisited node
        min_cost = sys.maxsize
        for i in range(len(graph)):
            if visited & (1 << i) == 0:
                cost = graph[current][i] + tsp_helper(i, visited | (1 << i))
                min_cost = min(min_cost, cost)

        # Memoize result and return
        memo[(current, visited)] = min_cost
        return min_cost

    # Call helper function with start node and return result
    return tsp_helper(start, 1 << start)


# Sample graph represented as a 2D array
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Call TSP function with start node 0
print(tsp(graph, 0))
