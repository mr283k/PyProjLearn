# Iterate the given list of numbers and print only those numbers which are divisible by 5

x =  [10, 20, 33, 46, 55]

def num_div_5(x):
    for num in x:
        if num % 5 == 0:
            print(num)


num_div_5(x)

