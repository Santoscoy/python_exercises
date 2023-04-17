"""
There are several difficulty of sudoku games, we can estimate the difficulty of a sudoku game based on
how many cells are given of the 81 cells of the game.

Easy sudoku generally have over 32 givens
Medium sudoku have around 30–32 givens
Hard sudoku have around 28–30 givens
Very Hard sudoku have less than 28 givens
Note: The minimum of givens required to create a unique (with no multiple solutions) sudoku game is 17.

A hard sudoku game means that at start no cell will have a single candidates and thus require guessing
and trial and error. A very hard will have several layers of multiple candidates for any empty cell.

Task:
Write a function that solves sudoku puzzles of any difficulty. The function will take a sudoku grid,
and it should return a 9x9 array with the proper answer for the puzzle.

Or it should raise an error in cases of: invalid grid (not 9x9, cell with values not in the range 1~9);
multiple solutions for the same puzzle or the puzzle is unsolvable
"""
# import copy
#
#
# def sudoku_solver(puzzle):
#     board_status = copy.deepcopy(puzzle)
#     available_positions = get_available_positions(board_status)
#     if available_positions:
#         updated_board_status, is_solved = get_solution(board_status, available_positions)
#         return updated_board_status
#
#
# def get_available_positions(board_status: list) -> list:
#     """Get the available positions on the board status"""
#     r = 0
#     available_positions = []
#     for row in board_status:
#         c = 0
#         for colum_item in row:
#             if colum_item == 0:
#                 available_positions.append((r, c))
#             c += 1
#         r += 1
#     return available_positions
#
#
# def get_solution(board_status: list, available_positions: list) -> tuple:
#     """Iterate recursively over the available positions to find the right solution"""
#     position = None
#     if available_positions:
#         position = available_positions.pop(0)
#     if position:
#         for digit in range(1, 10):
#             is_valid, is_full, updated_board_status = get_validation(digit, position, board_status)
#             if is_valid and not is_full:
#                 updated_board_status, is_solved = get_solution(updated_board_status, available_positions)
#                 if is_solved:
#                     return updated_board_status, True
#                 else:
#                     continue
#
#             if is_valid and is_full:
#                 return updated_board_status, True
#
#     available_positions.insert(0, position)
#     return board_status, False
#
#
# def get_validation(digit: int, position: tuple, board_status: list) -> tuple:
#     """Validate if digit in that position are valid and return the updated board status """
#     updated_board_status = copy.deepcopy(board_status)
#
#     # create a list with the column values and get the specific row
#     col = [updated_board_status[rows][position[1]] for rows in range(len(updated_board_status))]
#     row = updated_board_status[position[0]]
#
#
#     is_valid = False
#     if digit not in row and digit not in col:
#         is_valid = True
#
#     if is_valid:
#         updated_board_status[position[0]][position[1]] = digit
#
#     # Check if the board is filled
#     is_full = True
#     for row in updated_board_status:
#         if not is_full:
#             break
#         for column_item in row:
#             if column_item == 0:
#                 is_full = False
#
#     return is_valid, is_full, updated_board_status

M = 9


def solve(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False

    for x in range(9):
        if grid[x][col] == num:
            return False

    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True


def sudoku_solver(grid, row, col):
    if row == 8 and col == 9:
        return grid
    if col == 9:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return sudoku_solver(grid, row, col + 1)
    for num in range(1, 10, 1):

        if solve(grid, row, col, num):

            grid[row][col] = num
            if sudoku_solver(grid, row, col + 1):
                return grid
        grid[row][col] = 0
    return False


if __name__ == "__main__":
    puzzle = [
        [0, 0, 6, 1, 0, 0, 0, 0, 8],
        [0, 8, 0, 0, 9, 0, 0, 3, 0],
        [2, 0, 0, 0, 0, 5, 4, 0, 0],
        [4, 0, 0, 0, 0, 1, 8, 0, 0],
        [0, 3, 0, 0, 7, 0, 0, 4, 0],
        [0, 0, 7, 9, 0, 0, 0, 0, 3],
        [0, 0, 8, 4, 0, 0, 0, 0, 6],
        [0, 2, 0, 0, 5, 0, 0, 8, 0],
        [1, 0, 0, 0, 0, 2, 5, 0, 0]
    ]

    # solution = [
    #     [3, 4, 6, 1, 2, 7, 9, 5, 8],
    #     [7, 8, 5, 6, 9, 4, 1, 3, 2],
    #     [2, 1, 9, 3, 8, 5, 4, 6, 7],
    #     [4, 6, 2, 5, 3, 1, 8, 7, 9],
    #     [9, 3, 1, 2, 7, 8, 6, 4, 5],
    #     [8, 5, 7, 9, 4, 6, 2, 1, 3],
    #     [5, 9, 8, 4, 1, 3, 7, 2, 6],
    #     [6, 2, 4, 7, 5, 9, 3, 8, 1],
    #     [1, 7, 3, 8, 6, 2, 5, 9, 4]
    # ]

    print(sudoku_solver(puzzle, 0, 0))
# [
#     [3, 4, 6, 1, 2, 7, 9, 5, 8],
#     [6, 8, 1, 2, 9, 4, 7, 3, 5],
#     [2, 1, 3, 6, 8, 5, 4, 9, 7],
#     [4, 9, 5, 3, 6, 1, 8, 7, 2],
#     [8, 3, 2, 5, 7, 6, 1, 4, 9],
#     [5, 6, 7, 9, 4, 8, 2, 1, 3],
#     [7, 5, 8, 4, 1, 9, 3, 2, 6],
#     [9, 2, 4, 7, 5, 3, 6, 8, 1],
#     [1, 7, 9, 8, 3, 2, 5, 6, 4]
# ]
