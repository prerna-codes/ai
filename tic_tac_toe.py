def tic_tac_toe():

    print("Game is starting...", end="\n")
    play_again = True
    player_name_1 = input("Enter first player name: ")
    player_name_2 = input("Enter Second player name: ")

    while play_again:
        board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        player = 1
        print("{0}, Select your mark:".format(player_name_1), end='')
        symbol = input()
        player_1, player_2 = set_symbol(symbol)

        while True:
            if player > 2:
                player = 1
            if player == 1:
                print(f'{player_name_1}, Enter your move position: ')
            if player == 2:
                print(f'{player_name_2}, Enter your move position: ')

            pos = int(input())

            if check_pos(pos, board):
                continue
            if player == 1:
                set_board(board, player_1, pos)
            else:
                set_board(board, player_2, pos)
            display(board)

            if player == 1:
                if check_win(board, player_1):
                    print(player_name_1, " has won.")
                    break

            else:
                if check_win(board, player_2):
                    print(player_name_2, " has won.")
                    break

            if check_space(board):
                print("Draw!!!")
                break

            player += 1

        if rematch():
            play_again = True

def set_symbol(symbol):
    if symbol == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'

def check_pos(pos, board):
    if board[pos] == ' ':
        return False
    else:
        return True

def set_board(board, symbol, pos):
    board[pos] = symbol

def display(board):
    print(f'{board[7]} | {board[8]} | {board[9]}')
    print("------------------------")
    print(f'{board[4]} | {board[5]} | {board[6]}')
    print("------------------------")
    print(f'{board[1]} | {board[2]} | {board[3]}')
    print("------------------------")

def check_win(board, symbol):
    return (board[1] == symbol and board[2] == symbol and board[3] == symbol or
            board[4] == symbol and board[5] == symbol and board[6] == symbol or
            board[7] == symbol and board[8] == symbol and board[9] == symbol or
            board[1] == symbol and board[4] == symbol and board[7] == symbol or
            board[2] == symbol and board[5] == symbol and board[8] == symbol or
            board[3] == symbol and board[6] == symbol and board[9] == symbol or
            board[1] == symbol and board[5] == symbol and board[9] == symbol or
            board[3] == symbol and board[5] == symbol and board[7] == symbol)

def check_space(board):
    if ' ' in board:
        return False
    else:
        return True

def rematch():
    print("Do you want to play again: ", end='')
    ans = input("Y for play\nN for Exit.\n")
    if ans == 'y' or ans == 'y':
        return True
    else:
        print("Thanks for play.")
        exit()


if __name__ == '__main__':
    tic_tac_toe()
