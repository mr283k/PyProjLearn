# TODO-1: Ask the user for input

# TODO-2: Save data into dictionary {name: price}


def highest_bidder(bid_dic):
    highest_bid = 0
    winner = ""

    for bidder in bid_dic:
        current_bid = bid_dic[bidder]
        if current_bid > highest_bid:
            winner = bidder
            highest_bid = current_bid
    print(f"name of per win: {winner}")
    print(f"name of per win bid: {dic[winner]}")


# TODO-3: Whether if new bids need to be added
dic = {}
new_user = True
while new_user:
    name = input("user name :")
    bid = int(input("bid amount :"))
    dic[name] = bid
    # dic += {name: bid}
    new_user_flag = input("are there more users type yes/no :")
    print("\n" * 20)
    if new_user_flag == "no":
        highest_bidder(bid_dic = dic)
        new_user = False

# print(dic)
# TODO-4: Compare bids in dictionary


# print(max(dic, key=dic.get))
# print(dic[max(dic, key=dic.get)])





