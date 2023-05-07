import queue

class Node:
    def __init__(self, grid, depth, cost, parent):
        self.grid = grid
        self.depth = depth
        self.cost = cost
        self.parent = parent

    def __lt__(self, other):
        return self.cost < other.cost

    def get_blank_pos(self):
        for i in range(4):
            for j in range(4):
                if self.grid[i][j] == " ":
                    return (i, j)

    def get_children(self):
        i, j = self.get_blank_pos()
        children = []
        if i > 0:
            child = Node(self.swap(self.grid, i, j, i-1, j), self.depth+1, 0, self)
            children.append(child)
        if i < 3:
            child = Node(self.swap(self.grid, i, j, i+1, j), self.depth+1, 0, self)
            children.append(child)
        if j > 0:
            child = Node(self.swap(self.grid, i, j, i, j-1), self.depth+1, 0, self)
            children.append(child)
        if j < 3:
            child = Node(self.swap(self.grid, i, j, i, j+1), self.depth+1, 0, self)
            children.append(child)
        return children

    def swap(self, grid, i1, j1, i2, j2):
        new_grid = [row.copy() for row in grid]
        new_grid[i1][j1], new_grid[i2][j2] = new_grid[i2][j2], new_grid[i1][j1]
        return new_grid

def get_cost(grid):
    cost = 0
    for i in range(4):
        for j in range(4):
            if grid[i][j] != " ":
                row = (int(grid[i][j])-1) // 4
                col = (int(grid[i][j])-1) % 4
                cost += abs(row-i) + abs(col-j)
    return cost

def branch_and_bound(start_grid):
    start_node = Node(start_grid, 0, 0, None)
    q = queue.PriorityQueue()
    q.put(start_node)
    while not q.empty():
        node = q.get()
        if node.grid == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, " "]]:
            path = []
            while node:
                path.append(node.grid)
                node = node.parent
            path.reverse()
            return path
        for child in node.get_children():
            child.cost = child.depth + get_cost(child.grid)
            q.put(child)
    return None

# Test the function with a random starting grid
start_grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, " "], [13, 14, 15, 12]]
solution = branch_and_bound(start_grid)
if solution:
    print("Found a solution with", len(solution)-1, "moves:")
    for i in range(len(solution)):
        print("Move", i, ":")
        for row in solution[i]:
            print(row)
else:
    print("No solution found.")
