def is_safe(board, row, col, n):
    # Check for a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens(board, row, n):
    # Base case: all queens placed
    if row == n:
        for r in board:
            print(r)
        print()
        return

    # Try placing a queen in each column
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1      # Place queen
            solve_n_queens(board, row + 1, n)
            board[row][col] = 0      # Backtrack


def n_queens(n):
    board = [[0] * n for _ in range(n)]
    solve_n_queens(board, 0, n)


# ->>>>MAIN PROGRAM <<<<<<-
n = int(input("Enter number of queens: "))
n_queens(n)
