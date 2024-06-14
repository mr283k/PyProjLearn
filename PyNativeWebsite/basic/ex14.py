# Print downward Half-Pyramid Pattern with Star (asterisk)

# * * * * *
# * * * *
# * * *
# * *
# *

def ast(num):
    while num > 0:
        for i in range(num):
            print("*", end = " ")
        num -= 1
        print("\n")

ast(5)
