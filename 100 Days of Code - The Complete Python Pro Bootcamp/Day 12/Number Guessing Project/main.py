import random


# def decrease_attempts(no_of_guess):
#     return no_of_guess - 1
#
# def game():
#     print("Welcome to the number Guessing game!")
#     print("I am thinking of a number between 1 and 100")
#     difficulty_mode = input("Choose a difficulty. choose 'easy' or 'hard':")
#
#     num_to_guess = random.randint(1, 100)
#     print(f"Pssst, the correct answer is {num_to_guess}")
#
#     if difficulty_mode == 'easy':
#         no_of_guess = 10
#     else:
#         no_of_guess = 5
#
#     turn = no_of_guess
#
#     user_guess = 0
#
#     while user_guess != num_to_guess:
#
#         print(f"you have {turn} attempts remaining to guess")
#
#         user_guess = int(input("Make a guess: "))
#
#         if num_to_guess == user_guess:
#             print("Your guess is right")
#             return
#         elif num_to_guess > user_guess:
#             print("Too Low")
#             turn -= 1
#         else:
#             print("Too High")
#             turn -= 1
#
#         if turn == 0:
#             print("you have ran out of guess")
#             return
#         else:
#             print("guess again")
#
# game()

# +++++++++++
# code based on the funcitons

import random

EASY_LEVEL_GUESS = 10
HARD_LEVEL_GUESS = 5


def difficulty_level(mode):
    if mode == 'easy':
        return EASY_LEVEL_GUESS
    else:
        return HARD_LEVEL_GUESS

def check_guess(num_to_guess, user_guess, turn):
    if num_to_guess == user_guess:
        print("Your guess is right")
        return
    elif num_to_guess > user_guess:
        print("Too Low")
        return turn - 1
    else:
        print("Too High")
        return turn - 1


def game():
    print("Welcome to the number Guessing game!")
    print("I am thinking of a number between 1 and 100")
    difficulty_mode = input("Choose a difficulty. choose 'easy' or 'hard':")

    num_to_guess = random.randint(1, 100)
    print(f"Pssst, the correct answer is {num_to_guess}")

    turn = difficulty_level(mode=difficulty_mode)

    user_guess = 0

    while user_guess != num_to_guess:

        print(f"you have {turn} attempts remaining to guess")

        user_guess = int(input("Make a guess: "))

        turn = check_guess(num_to_guess,user_guess,turn)

        if turn == 0:
            print("you have ran out of guess")
            return
        else:
            print("guess again")

game()

