# Exercise 2: Print the sum of the current number and the previous number

def add_prv_num():
    # first create range 1, 2 ..10
    # take first num 0 and then add then assign the value
    x = 0
    print('Printing current and previous number sum in a range(10)')
    for i in range(0,10):
        #print(i)
        total = i + x
        print(f'Current Number {i} Previous Number  {x}  Sum:  {total}')
        x = i

add_prv_num()