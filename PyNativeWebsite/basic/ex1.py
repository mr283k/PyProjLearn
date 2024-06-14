# Exercise 1: Calculate the multiplication and sum of two numbers
# Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.

def cal_num(x,y):
    if x * y < 1000:
        return x * y
    else:
        return x + y

print(cal_num(4,5))