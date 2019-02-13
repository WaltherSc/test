ROW_COUNT = 6                               # Creating the board.   # Connect four game in Python
COLUMN_COUNT = 7                                                    # Made by Danyel, Wouter and Daan. Group INF1I.

Board = []
for x in range(ROW_COUNT): Board.append(list([0] * COLUMN_COUNT))

def drop_piece(Board, row, Column, piece):  # Placing a piece on the board.
    Board[row][Column] = piece

def is_valid_location(Board, Column):       # Checking for a valid location on the board.
    return Board[-1][Column] == 0

def get_next_open_row(Board, Column):       # Checking if the Row is empty.
    for r in range(ROW_COUNT):
        if Board[r][Column]==0:
            return r

gameOver = False
turn = True

while not gameOver:                         # Asking for and executing user input for player 1 and 2.
    if turn: player = 1
    else: player = 2
    UserInput = input("Player " + str(player) + ", Make your turn(0-6):")
    if UserInput.isdigit():
        Column = int(UserInput)
    else:
        print("Your input has to be between 0 and 6!")
        UserInput = input("Player " + str(player) + ", Make your turn(0-6):")

    if Column != 0 and Column != 1 and Column != 2 and Column != 3 and Column != 4 and Column != 5 and Column != 6:
       print("Your input has to be between 0 and 6!")
       UserInput = input("Player " + str(player) + ", Make your turn(0-6):")
    else:
        if is_valid_location(Board, Column):
            row = get_next_open_row(Board, Column)
            drop_piece(Board, row, Column, player)
            turn = not turn
        else: print("Invalid selection")

        for row in reversed(Board):
            print(row)
            for C in range(COLUMN_COUNT - 3):                   # Horizontal check for player 1.
                for R in range(ROW_COUNT):
                    if Board[R][C] == 1 and Board[R][C + 1] == 1 and Board[R][C + 2] == 1 and Board[R][C + 3] == 1:
                        print("Player one has won!")
                        gameOver = True
            for C in range(COLUMN_COUNT):                       # Vertical check for player 1.
                for R in range(ROW_COUNT - 3):
                    if Board[R][C] == 1 and Board[R + 1][C] == 1 and Board[R + 2][C] == 1 and Board[R + 3][C] == 1:
                        print("Player one has won!")
                        gameOver = True
            for C in range(COLUMN_COUNT - 3):                   # Diagonal check for player 1.
                for R in range(ROW_COUNT - 3):
                    if Board[R][C] == 1 and Board[R + 1][C + 1] == 1 and Board[R + 2][C + 2] == 1 and Board[R + 3][
                        C + 3] == 1:
                        print("Player one has won!")
                        gameOver = True
            for C in range(COLUMN_COUNT - 3):                   # Horizontal check for player 2.
                for R in range(ROW_COUNT):
                    if Board[R][C] == 2 and Board[R][C + 1] == 2 and Board[R][C + 2] == 2 and Board[R][C + 3] == 2:
                        print("Player two has won!")
                        gameOver = True
            for C in range(COLUMN_COUNT):                       # Vertical check for player 2.
                for R in range(ROW_COUNT - 3):
                    if Board[R][C] == 2 and Board[R + 1][C] == 2 and Board[R + 2][C] == 2 and Board[R + 3][C] == 2:
                        print("Player two has won!")
                        gameOver = True
            for C in range(COLUMN_COUNT - 3):                   # Diagonal check for player 2.
                for R in range(ROW_COUNT - 3):
                    if Board[R][C] == 2 and Board[R + 1][C + 1] == 2 and Board[R + 2][C + 2] ==2 and Board[R + 3][
                        C + 3] == 2:
                        print("Player two has won!")
                        gameOver = True