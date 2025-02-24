def create_board():
    board = []
    for i in range(3):
        line = [" ", " ", " "]
        board.append(line)
    return board


def write_board(board):
    for line in board:
        print("|".join(line))
        print("-----")

# write_board(create_board())

def make_move(board, player, line, gab):
    if board[line][gab] == " ":
        board[line][gab] =  player
        return True
    else:
        return False

def winner_check(board, player):
    for line in range(3):
        if board[line][0] == board[line][1] == board[line][2] == player:
            return True

    for gab in range(3):
        if board[0][gab] == board[1][gab] == board[2][gab] == player:
            return True

    if board[0][0] == board[1][1] == board[2][2] == player or \
       board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

def uncertainty_check(board):
    for line in board:
        if " " in line:
            return False
    return True

def tic_tac_toe():
    board = create_board()
    current_player = "X"

    while True:
        write_board(board)

        try:
            line = int(input(f"Spiler {current_player}, wähle deine zeile"))
            gab = int(input(f"Spiler {current_player}, wähle spalte"))
            if line < 0 or line > 2 or gab < 0 or gab > 2:
                print("du darfst nur Zuge zwischen 0 und 2 setzen!")
            else:
                if not make_move(board, current_player, line, gab):
                    print("Ungultig, versuche es erneut!")
        except ValueError:
            print("Gibt doch bitte eine Ganzzahl ein")

        if winner_check(board, current_player):
            write_board(board)
            print(f"Hey, du hast gewonnen spiler {current_player}")
            break
        elif uncertainty_check(board):
            write_board(board)
            print("Unentschiden!")
            break

        current_player = "0" if current_player == "X" else "X"

tic_tac_toe()