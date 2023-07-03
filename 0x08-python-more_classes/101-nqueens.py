import sys

def nqueens(N):
    """
    Solve the N Queens problem and print all possible solutions.

    Args:
        N (int): The size of the chessboard and the number of queens.

    """
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * N for _ in range(N)]
    solutions = []
    solve_nqueens(N, 0, board, solutions)
    print_solutions(solutions)

def solve_nqueens(N, col, board, solutions):
    """
    Recursive function to solve the N Queens problem using backtracking.

    Args:
        N (int): The size of the chessboard and the number of queens.
        col (int): The current column to consider.
        board (list): The current state of the chessboard.
        solutions (list): List to store the solutions.

    """
    if col == N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            solve_nqueens(N, col + 1, board, solutions)
            board[i][col] = 0

def is_safe(board, row, col, N):
    """
    Check if placing a queen at the given position is safe.

    Args:
        board (list): The current state of the chessboard.
        row (int): The row index to check.
        col (int): The column index to check.
        N (int): The size of the chessboard.

    Returns:
        bool: True if it is safe to place a queen, False otherwise.

    """
    # Check the row
    for j in range(col):
        if board[row][j] == 1:
            return False

    # Check the upper diagonal
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check the lower diagonal
    i = row
    j = col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

def print_solutions(solutions):
    """
    Print all the solutions to the N Queens problem.

    Args:
        solutions (list): List of solutions.

    """
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
        nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
