def ConnectFourWinner(strArr):
    # code goes here
    board_status, turn = generate_board_status(strArr)

    available_positions = get_available_positions(board_status)

    return get_winner_movement(available_positions, board_status, turn)


def generate_board_status(original_board):
    """
      receives an argument like the following:
      [
        "R",
        "(R,R,R,Y,x,x,x)",
        "(x,x,x,Y,R,x,x)",
        "(x,x,Y,Y,R,Y,x)",
        "(x,x,x,R,x,x,x)",
        "(x,x,x,x,R,x,x)",
        "(x,x,x,x,x,R,x)",
      ]
      and determine the current turn, and the board status
    """
    turn = original_board.pop(0)
    board_status = []
    for row in original_board:
        row = row.replace("(", "").replace(")", "").split(",")
        board_status.append(row)

    return board_status, turn


def get_available_positions(board_status):
    """This function is intended to obtain the available positions in the board"""
    r = 0
    available_positions = []
    for row in board_status:
        c = 0
        for colum_item in row:
            if colum_item == "x":
                available_positions.append((r, c))
            c += 1
        r += 1
    return available_positions


def get_winner_movement(available_positions, board_status, turn):
    """
    This function receives the available positions as the following example:
    available_positions = [(2,3), (3,4), (3,2)]
    and return the and return an str indicating the winner movement.
    """
    for row, col in available_positions:
        board_status[row][col] = turn
        is_consecutive = check_consecutive(board_status, row, col, turn)
        board_status[row][col] = "x"
        if is_consecutive:
            return f"({row + 1}x{col + 1})"

    return None


def check_consecutive(board, row_position, col_position, turn):
    """
    this function receives the following args:
      board: list of lists,
      row_position: int,
      col_position: int,
      turn: str

    and returns True if is consecutive else returns False
    """
    # horizontal move
    row = board[row_position]
    if check_sequence(turn, row):
        return True

    # vertical move
    col = [board[rows][col_position] for rows in range(len(board))]
    if check_sequence(turn, col):
        return True

    # diagonal down-right
    diag_dr = build_diagonal(board, turn, direction="dr")
    if check_sequence(turn, diag_dr):
        return True

    # diagonal down-left
    diag_dl = build_diagonal(board, turn)
    if check_sequence(turn, diag_dl):
        return True

    return False


def check_sequence(turn, item_list):
    """
    this function receives the following args:
      turn: str, ex: "R"
      item_list: list of strings, ex: ["x", "R", "x", "R", "R", "x", "x"]
    and returns True if the sequence is correct else False
    """
    count = 0
    for item in item_list:
        if (
                item == turn and
                item_list.index(item) + 1 < len(item_list) and
                (
                        item_list[item_list.index(item) - 1] == turn or
                        item_list[item_list.index(item) + 1] == turn
                )
        ):
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    return False


def build_diagonal(board, turn, direction=None):
    """
    This functions receives the following args:
      board: list of list,
      turn: str,
      direction

    and return a list with strings
    """
    diag = []
    col_index = None
    for row_index, row in enumerate(board):
        for item in row:
            if item == turn:
                col_index = row.index(item)

            if col_index is not None:
                break

        if col_index is not None:
            break

    for i, row in enumerate(board):
        if row_index <= i:
            if col_index < len(row):
                diag.append(row[col_index])
                if direction == "dr":
                    col_index += 1
                else:
                    col_index -= 1

    return diag


# Additional Test
print(ConnectFourWinner([
  "Y",
  "(Y,Y,Y,x,x,x,x)",
  "(x,x,x,x,x,x,x)",
  "(x,x,x,x,x,x,x)",
  "(x,x,x,x,x,x,x)",
  "(x,x,x,x,x,x,x)",
  "(x,x,x,x,x,x,x)",
]))

print(ConnectFourWinner([
  "R",
  "(R,R,R,Y,x,x,x)",
  "(x,x,x,x,x,x,x)",
  "(x,x,x,x,x,x,x)",
  "(x,x,x,x,x,x,x)",
  "(x,x,x,x,x,x,x)",
  "(x,x,x,x,x,x,x)",
]))

print(ConnectFourWinner([
  "Y",
  "(R,R,R,Y,x,x,x)",
  "(x,x,x,Y,x,x,x)",
  "(x,x,x,Y,x,x,x)",
  "(x,x,x,x,x,x,x)",
  "(x,x,x,x,x,x,x)",
  "(x,x,x,x,x,x,x)",
]))

print(ConnectFourWinner([
  "R",
  "(R,R,R,Y,x,x,x)",
  "(x,x,x,Y,x,x,x)",
  "(x,x,x,Y,x,x,x)",
  "(x,x,x,R,x,x,x)",
  "(x,x,x,x,R,x,x)",
  "(x,x,x,x,x,R,x)",
]))

print(ConnectFourWinner([
  "Y",
  "(R,R,R,Y,x,x,x)",
  "(x,x,x,Y,x,x,x)",
  "(x,x,Y,Y,x,Y,x)",
  "(x,x,x,R,x,x,x)",
  "(x,x,x,x,R,x,x)",
  "(x,x,x,x,x,R,x)",
]))

print(ConnectFourWinner([
  "R",
  "(R,R,R,Y,x,x,x)",
  "(x,x,x,Y,R,x,x)",
  "(x,x,Y,Y,R,Y,x)",
  "(x,x,x,R,x,x,x)",
  "(x,x,x,x,R,x,x)",
  "(x,x,x,x,x,R,x)",
]))


