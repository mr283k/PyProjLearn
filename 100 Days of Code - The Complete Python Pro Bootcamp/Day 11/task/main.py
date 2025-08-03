import random
from art import logo



def deal_card():
    """return a random card from deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) == 22 and len(cards) == 2:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score):
    if c_score == u_score:
        return "its a draw"
    elif c_score == 0:
        return "computer win"
    elif u_score == 0:
        return "user win"
    elif u_score > 21:
        return "You went over, you loose"
    elif c_score > 21:
        return "Opponent went over, you win"
    else:
        if c_score > u_score:
            return "computer win"
        else:
            return "user win"

def play_game():
    # print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"your cards: {user_cards}, current score : {user_score}")
        print(f"computer first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_want_todeal = input("type y to get another card type n to pass :")
            if user_want_todeal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)


    print(f"your cards: {user_cards}, current score : {user_score}")
    print(f"computer cards: {computer_cards},current score : {computer_score}")
    print(compare(u_score=user_score, c_score=computer_score))

while input("do you want to play a game black jack ? type y or n: ") == 'y':
    print("\n" * 20 )
    play_game()


#     total_score = sum(cards)
#     if cards.count() == 2 and total_score == 21:
#         return  0
#     if total_score > 21:
#         if 11 in cards:
#             cards.
#     return total_score



























# def black_jack():
#     user_choice = input("do you want to play a game of black jack ? Type 'y' or 'n': ")
#     if user_choice == 'n':
#         exit()
#     user_cards = [deal_card(),deal_card()]
#     current_score = sum(user_cards)
#     print(f"user cards: {user_cards}, current score : {current_score} ")
#
#     computer_card = [deal_card()]
#     current_computer_score = sum(computer_card)
#     print(f"computer first card: {computer_card}")
#
#     user_hit_flag = True
#     while user_hit_flag:
#         user_hit = input("type 'y' to get another card, type 'n' to pass:")
#         if user_hit == 'y':
#             user_cards.append(deal_card())
#             print(user_cards)
#             current_score = sum(user_cards)
#             print(f"user cards: {user_cards}, current score : {current_score} ")
#             print(f"computer first card: {computer_card}")
#             if current_score > 21:
#                 print("you loose")
#                 user_hit_flag = False
#         else :
#             user_hit_flag = False
#
#     print(f"user final cards: {user_cards}, user final score : {current_score} ")
#
#     dealer_limit = 17
#     while current_computer_score < dealer_limit:
#         computer_card.append(deal_card())
#         current_computer_score = sum(computer_card)
#
#     print(f"computer final card: {computer_card}, computer final score: {current_computer_score} ")
#     if current_computer_score == 21:
#         print("Dealer win")
#     elif current_score == 21:
#         print("you win")
#     elif current_computer_score > 21:
#         print("you win")
#     elif current_score > current_computer_score:
#         print("you win")
#     elif current_score == current_computer_score:
#         print("push")
#     else:
#         print("dealer win")
#
#     black_jack()
#
# black_jack()

