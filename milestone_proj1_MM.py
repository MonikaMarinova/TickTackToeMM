# local variables for play board, num pad mapping, player 1 and 2 characters in the game
board = [[' _ ', ' _ ', ' _ '],
         [' _ ', ' _ ', ' _ '],
         [' _ ', ' _ ', ' _ ']]


num_pad = [['7', '8', '9'],
           ['4', '5', '6'],
           ['1', '2', '3']]

player1_character = ' '
player2_character = ' '


# Welcome method
def welcome_in_game():
    print("Welcome in Tic Tac Toe game!\n"
          "Here is your playing board:")
    print_matrix(board)

    print("It is mapped to your num pad as follows:")
    print_matrix(num_pad)

    print("\n If you want to reset the game enter 'r' instead of number for move or 'q' to quit. \n")


# Choosing character, changing the local variables player1_character and player2_character
def choose_character():
    print("Choose X or O:")
    user_input = input().lower()
    global player1_character, player2_character

    if user_input == 'x':
        player1_character = ' X '
        player2_character = ' O '
        print('''Let's play''')
        return True

    elif user_input.lower() == 'o':
        player1_character = ' O '
        player2_character = ' X '
        print('''Let's play''')
        return True

    else:
        print("Wrong input! Bye!")
        exit(0)


# Method for checking if position is empty
def check_if_position_is_empty(index_x, index_y):
    return board[index_x][index_y] == ' _ '


# Method for making move, passes move if field isn't empty
def make_move(choice, player_character):
    global board
    index_pair =[(index, row.index(choice)) for index, row in enumerate(num_pad) if choice in row]
    index_x = index_pair[0][0]
    index_y = index_pair[0][1]

    if check_if_position_is_empty(index_x, index_y):
        board[index_x][index_y] = player_character
    else:
        pass


# Print Board
def print_matrix(mat):
    for row in mat:
        print(row)


# Method for clear screen
def clear_screen():
    print('\n'*100)


# Clear board and reset game
def reset_game():
    #clear_screen()
    global board
    board = [[' _ ', ' _ ', ' _ '],
             [' _ ', ' _ ', ' _ '],
             [' _ ', ' _ ', ' _ ']]
    choose_character()


# Method for checking if player is winning
def is_winning(play_board, player_character):
    # check in row
    for index_x in range(0, 3):
        if play_board[index_x][0] == play_board[index_x][1] == play_board[index_x][2] == player_character:
            return True

    # check in column
    for index_y in range(0, 3):
        if play_board[0][index_y] == play_board[1][index_y] == play_board[2][index_y] == player_character:
            return True

    # check in diagonal 1: index_x == index_y
    if play_board[0][0] == play_board[1][1] == play_board[2][2] == player_character:
        return True

    # check in diagonal 2:
    elif play_board[0][2] == play_board[1][1] == play_board[2][0] == player_character:
        return True

    return False


# Lets start:
welcome_in_game()
choose_character()

while True:
    # player 1:
    print("Player 1: Choose your move(1-9), you also can reset or quit game:")
    player1_choice = input()
    if player1_choice.lower() == 'r':
        reset_game()
        continue
    elif player1_choice.lower() == 'q':
        break
    else:
        make_move(player1_choice, player1_character)
        print_matrix(board)
        if is_winning(board, player1_character):
            print("Winner is {}!".format(player1_character))
            reset_game()
            continue
        elif not any(' _ ' in row for row in board):
            print("Result 0:0!")
            reset_game()
        else:
            pass

    # player 2:
    print("Player 2: Choose your move(1-9):")
    player2_choice = input()
    make_move(player2_choice, player2_character)
    print_matrix(board)
    if is_winning(board, player2_character):
        print("Winner is {}!".format(player2_character))
        reset_game()
        continue
    elif not any(' _ ' in row for row in board):
        print("Result 0:0!")
        reset_game()
    else:
        print("Next Round!\n")


