import random


def generate_neighbors(x):
    # generate a list of neighbors by randomly changing one element of x
    neighbors = []
    for i in range(len(x)):
        neighbor = x[:]
        neighbor[i] = random.randint(0, 1)
        neighbors.append(neighbor)
    return neighbors


def hill_climbing(f, x0):
    x = x0  # initial solution
    while True:
        neighbors = generate_neighbors(x)  # generate neighbors of x
        # find the neighbor with the highest function value
        best_neighbor = max(neighbors, key=f)
        if f(best_neighbor) <= f(x):  # if the best neighbor is not better than x, stop
            return x
        x = best_neighbor  # otherwise, continue with the best neighbor


# Example usage
def f(x):
    return sum(x)  # maximize the sum of the elements in the list

x0 = [0, 0, 0, 0]  # initial solution
best_solution = hill_climbing(f, x0)
print("Best solution:", best_solution)
print("Best value:", f(best_solution))
