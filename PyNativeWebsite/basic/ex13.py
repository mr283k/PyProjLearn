# Exercise 13: Print multiplication table form 1 to 10
# 1  2 3 4 5 6 7 8 9 10
# 2  4 6 8 10 12 14 16 18 20
# 3  6 9 12 15 18 21 24 27 30
# 4  8 12 16 20 24 28 32 36 40
# 5  10 15 20 25 30 35 40 45 50

def multi(num):
    for i in range(1,num+1):
        for x in range(1,num+1):
            print(i * x, end = " ")
        print("\t\t")

multi(5)