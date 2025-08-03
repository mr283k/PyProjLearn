from random import randint

# Get the logo
import art
import game_data

win_flag = True
hold_comp_b = []
rand_num_a = -1
rand_num_b = -1
score =0


while win_flag:
    print(art.logo)
    # print if you are right or wrong with current score
    print(f"you're right! current score is : {score}")

    # compare A :
    # 1. take list and select the random name for the first iteration
    # 2. next iteration get the value from the compare B

    # length_data = len(game_data.data)
    # print(length_data)
    if rand_num_a < 0:
        rand_num_a = randint(0, 49)
        print(f"compare A :  {game_data.data[rand_num_a]["name"]} , a {game_data.data[rand_num_a]["description"]}, from {game_data.data[rand_num_a]["country"]}")
        no_of_followers_a = game_data.data[rand_num_a]["follower_count"]
    else:
        rand_num_a = rand_num_b
        print(f"compare A :  {game_data.data[rand_num_a]["name"]} , a {game_data.data[rand_num_a]["description"]}, from {game_data.data[rand_num_a]["country"]}")
        no_of_followers_a = game_data.data[rand_num_a]["follower_count"]

    # logo again
    print(art.vs)
    # compare B : take the list and select the random name
    # b) then get the random value in next iteration as well.

    rand_num_b = randint(0,49)
    while rand_num_a == rand_num_b:
        rand_num_b = randint(0, 49)

    print(f"compare B :  {game_data.data[rand_num_b]["name"]} , a {game_data.data[rand_num_b]["description"]}, from {game_data.data[rand_num_b]["country"]}")
    no_of_followers_b = game_data.data[rand_num_b]["follower_count"]


    # give user an option to select A or B, ask who has more followers


    # compare counts of followers from A to B and then select the winner.

    user_choice = input("Who has more followers ? type 'A' or 'B':")
    # remember that you can get the random number that you choose form A in B as well
    # so need to take that into account
    if (no_of_followers_a > no_of_followers_b and user_choice == "A") or (no_of_followers_a < no_of_followers_b and user_choice == "B"):
        # win_flag= True
        #print("win")
        score += 1
        print("\n" * 20)
        hold_comp_b = [game_data.data[rand_num_a]]
        # print(f"logic to capture b in a : {hold_comp_b}")
    else:
        win_flag = False

    print("\n" * 20)
    print(art.logo)
    print(f"sorry that's wrong. Your score is : {score}")


