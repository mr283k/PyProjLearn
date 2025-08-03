import random
from random import randint
import art
# Get the logo
from game_data import data

print(art.logo)
user_guess_correct_flag = True
score =0

def format_data(account, user_position):
    account_name = account["name"]
    account_desc = account["description"]
    account_user_cnt = account["country"]
    return print(f"compare {user_position} :  {account_name}, a {account_desc}, from {account_user_cnt}")

def follower_count(account):
    account_follower_cnt = account["follower_count"]
    return account_follower_cnt

def check_answer(user_input, account_a_followers, account_b_followers):
    if account_a_followers > account_b_followers:
        return user_input == 'A'
    else:
        return user_input == 'B'

account_b = random.choice(data)


while user_guess_correct_flag:

    account_a = account_b

    while account_a == account_b:
        account_b = random.choice(data)

    format_data(account_a,'A')
    print(art.vs)
    format_data(account_b, 'B')

    no_of_followers_a = follower_count(account_a)
    no_of_followers_b = follower_count(account_b)

    user_choice = input("Who has more followers ? type 'A' or 'B':").upper()

    print("\n" * 20 )
    print(art.logo)

    is_correct = check_answer(user_choice,no_of_followers_a,no_of_followers_b)

    if is_correct:
        score += 1
        print(f"you're right! current score is : {score}")
    else:
        print(f"sorry that's wrong. Your score is : {score}")
        user_guess_correct_flag = False




