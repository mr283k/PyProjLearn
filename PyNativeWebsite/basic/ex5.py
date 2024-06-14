# Exercise 5: Check if the first and last number of a list is the same
# Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.

def list_ver(x):
    if x[0] == x[-1]:
        return True
    else:
        return False

print(list_ver([9,4,2,9]))