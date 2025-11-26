def is_safe(board, row, col, N):
    # Check this row on left side
    for c in range(col):
        if board[row][c] == 1:
            return False

    # Check upper-left diagonal
    r, c = row, col
    while r >= 0 and c >= 0:
        if board[r][c] == 1:
            return False
        r -= 1
        c -= 1

    # Check lower-left diagonal
    r, c = row, col
    while r < N and c >= 0:
        if board[r][c] == 1:
            return False
        r += 1
        c -= 1

    return True


def solve_nqueens(board, col, N, solutions):
    if col == N:
        # Deep copy the board
        solution = [row[:] for row in board]
        solutions.append(solution)
        return

    for row in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve_nqueens(board, col + 1, N, solutions)
            board[row][col] = 0  # BACKTRACK


def print_solutions(solutions, N):
    print(f"\nTotal Solutions Found: {len(solutions)}\n")

    for idx, sol in enumerate(solutions, 1):
        print(f"Solution {idx}:")
        for row in sol:
            print(row)
        print()


# ---------- MAIN PROGRAM ----------

N = int(input("Enter value of N for N-Queens: "))

board = [[0] * N for _ in range(N)]
solutions = []

solve_nqueens(board, 0, N, solutions)
print_solutions(solutions, N)
