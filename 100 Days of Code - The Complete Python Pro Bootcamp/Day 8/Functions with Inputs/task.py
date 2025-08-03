# def greet():
#     print("Hello world")
#     print("consistent")
#     print("no fear")
#
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"how you doing {name}")
#     print("no fear")
#
# greet_with_name("mahi")


def calculate_love_score(name1, name2):
    combine_name = name1.lower() + name2.lower()
    t = 0
    l = 0
    for true in "true":
        print(f"{true}")
        print(f"{combine_name}")
        if true in combine_name:
            x = combine_name.count(true)
            print(f"x value is {x}")
            t += combine_name.count(true)
            print(f"print t {t}")
    for love in "love":
        print(f"{love}")
        print(f"{combine_name}")
        if love in combine_name:
            l += combine_name.count(love)
            print(f"print l {l}")

    combine_number = str(t) + str(l)
    print(f"Love Score = {combine_number}")


# calculate_love_score("romeo", "juliet")
# calculate_love_score("x", "y")
# calculate_love_score("Kanye West", "Kim Kardashian")
calculate_love_score("Angela Yu", "Jack Bauer")