N = 4

def print_solution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()

"""A utility function to check if a queen can be placed on board[row][col]. Note that this function is called when "col" queens are already placed in columns from 0 to col -1. So we need to check only left side for attacking queens """

def is_safe(board, row, col):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_until(board, col):
    if col >= N:
        return True

    """Consider this column and try placing this queen in all rows one by one"""
    for i in range(N):

        if is_safe(board, i, col):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # recur to place rest of the queens
            if solve_until(board, col + 1) is True:
                return True

            board[i][col] = 0

    return False

"""This function solves the N Queen problem using Backtracking. It mainly uses solveNQUtil() to solve the problem. It returns false if queens cannot be placed, otherwise return true and placement of queens in the form of 1s. note that there may be more than one solutions, this function prints one  of the feasible solutions."""

def solve_nq():

    board = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]
             ]
    if solve_until(board, 0) is False:
        print("Solution does not exist")
        return False
    print_solution(board)
    return True


if __name__ == '__main__':
    solve_nq()
