def is_safe(board, row, col):
    """
    A utility function to check if a queen can be placed on the board at the given row and column
    """
    # Check if there is a queen in the same row
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    # Check if there is a queen in the upper diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check if there is a queen in the lower diagonal
    for i, j in zip(range(row, 8, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # If there are no queens on the same row or diagonal, it's safe to place a queen
    return True


def solve_queens(board, col):
    """
    A recursive function to place queens on the board
    """
    # Base case: all queens have been placed
    if col >= 8:
        return True
    
    # Try placing a queen in each row of the current column
    for i in range(8):
        if is_safe(board, i, col):
            board[i][col] = 1
            
            # Recursively place queens in the next column
            if solve_queens(board, col+1):
                return True
            
            # If the queen placement doesn't lead to a solution, backtrack and remove the queen from the board
            board[i][col] = 0
            
    # If none of the rows work for the current column, return False
    return False


# Driver code to test the function
board = [[0 for _ in range(8)] for _ in range(8)]

if solve_queens(board, 0):
    for row in board:
        print(row)
else:
    print("No solution exists.")
