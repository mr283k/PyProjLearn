# def display_game():
#     row1 = [1,2,3]
#     row2 = [4,5,6]
#     row3 = [7,8,9]
#     print(row1)
#     print(row2)
#     print(row3)
# display_game()

# def user_pos_choice():

def display_board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


test_board = ['O','X','O','X','O','X','O','O','O','O']
display_board(test_board)

#Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'.
# Think about using while loops to continually ask until you get a correct answer.

# def player_input():
#     choice = ''
#     while not (choice == 'X' or choice == 'O') :
#         choice = input('player 1 choose x/o :').upper
#     if choice == 'X':
#         return ['x','O']
#     else:
#         return ['o','x']

def player_input():
    marker = ''

    while not(marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


print(player_input())

def place_marker(board, marker, position):
    # all you are doing is just replacing positon in the list.
    board[position] = marker

place_marker(test_board,'#',1)
display_board(test_board)

def win_check(board, mark):
    # take the board items replace will what ever the player chooses
    # let palyer choose the mark then replace it for all positions on the board
    # so we need to continue doing while until who ever wins.
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))

print(win_check(test_board,'X'))


import random

def choose_first():
    player = random.randint(1,2)
    return print(f"Player {player} started")



