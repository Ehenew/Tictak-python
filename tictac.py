board = [" "] * 10


def display_board(board):
    print("\n Current Board")
    print("   |    |   ")
    print(board[7] + "  | " + board[8] + "  | " + board[9])
    print("   |    |   ")
    print("-------------")
    print("   |    |   ")
    print(board[4] + "  | " + board[5] + "  | " + board[6])
    print("   |    |   ")
    print("-------------")
    print("   |    |   ")
    print(board[1] + "  | " + board[2] + "  | " + board[3])


def player_input():
    marker = ""

    while marker.upper() not in ["X", "O"]:
        marker = input("Do you want to be X or O? ").strip().upper()

    player1 = marker
    player2 = "O" if player1 == "X" else "X"

    return (player1, player2)


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    win_combinations = [
        (1, 2, 3),  # top row
        (4, 5, 6),  # middle row
        (7, 8, 9),  # bottom row
        (1, 4, 7),  # left column
        (2, 5, 8),  # middle column
        (3, 6, 9),  # right column
        (1, 5, 9),  # main diagonal
        (3, 5, 7),  # other diagonal
    ]
    return any(board[a] == board[b] == board[c] == mark for a, b, c in win_combinations)


import random


def choose_first():
    flip = random.randint(0, 1)

    if flip == 0:
        return "Player 1"
    else:
        return "Player 2"


def space_check(board, position):
    return board[position] == " "


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False

    return True


def player_choice(board):
    while True:
        try:
            position = int(input("Choose a position (1-9): "))
            if position in range(1, 10) and space_check(board, position):
                return position
            else:
                print("Invalid or occupied position. Try again.")
        except ValueError:
            print("Please enter a number between 1 and 9.")


def replay():
    choice = input("Do you want to play the game again? Enter yes or no: ")

    return choice == "yes" or choice == "Yes"


def player_turn(board, player_name, marker):
    display_board(board)
    print(f"{player_name} turn:")
    position = player_choice(board)
    place_marker(board, marker, position)

    if win_check(board, marker):
        display_board(board)
        print(f"{player_name} has won 🏆")
        return True  # Game over
    elif full_board_check(board):
        display_board(board)
        print("TIE GAME 🤝")
        return True  # Game over
    return False  # Game continues


# Main
print("Welcome to Tic Tac Toe!")
while True:
    the_board = [" "] * 10
    display_board(the_board)

    turn = choose_first()
    print(f"{turn} will go first.")
    player1_marker, player2_marker = player_input()

    play_game = input("Ready to play? y or n: ")
    game_on = play_game.lower() == "y"

    while game_on:
        if turn == "Player 1":
            game_on = not player_turn(the_board, "Player 1", player1_marker)
            turn = "Player 2" if game_on else turn
        else:
            game_on = not player_turn(the_board, "Player 2", player2_marker)
            turn = "Player 1" if game_on else turn

    if not replay():
        break
