# print following pattern
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

def pyramid(n):
    for i in range(n):
        #print(f"outer {i}")
        for x in range(i):
            #print(f"inner {x}")
            print(i, end =" ")
        print("\n")


pyramid(5)