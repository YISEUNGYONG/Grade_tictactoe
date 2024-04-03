import random

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def available_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                moves.append((i, j))
    return moves

def player_move(board):
    while True:
        row = int(input("행을 선택하세요 (0-2): "))
        col = int(input("열을 선택하세요 (0-2): "))
        if board[row][col] == " ":
            return row, col
        else:
            print("해당 위치에 이미 놓인 돌이 있습니다. 다른 위치를 선택하세요.")

def computer_move(board):
    return random.choice(available_moves(board))

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("틱택토 게임을 시작합니다!")

    for _ in range(9):
        print_board(board)

        if current_player == "X":
            row, col = player_move(board)
        else:
            row, col = computer_move(board)

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            if current_player == "X":
                print("사람이 이겼습니다!")
            else:
                print("컴퓨터가 이겼습니다!")
            return

        current_player = "O" if current_player == "X" else "X"

    print_board(board)
    print("무승부입니다!")

tic_tac_toe()