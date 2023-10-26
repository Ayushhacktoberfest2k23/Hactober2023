def print_board(board):
    for row in board:
        print("|".join(row))
        print("-----")


def check_win(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    while True:
        print_board(board)
        row = int(input(f"Player {current_player}, choose row (0-2): "))
        col = int(input(f"Player {current_player}, choose column (0-2): "))
        if board[row][col] != " ":
            print("Cell already taken. Try again.")
            continue
        board[row][col] = current_player
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if all([cell != " " for row in board for cell in row]):
            print_board(board)
            print("It's a tie!")
            break
        current_player = "O" if current_player == "X" else "X"


tic_tac_toe()
