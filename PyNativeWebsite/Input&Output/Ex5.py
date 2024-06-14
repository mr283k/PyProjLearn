# Exercise 5: Accept a list of 5 float numbers as an input from the user

def flot_num():
    init_list = []
    for i in range(5):
        x = float(input('Enter floating num:'))
        init_list.append(x)
        print(init_list)
    return print(init_list)


flot_num()
