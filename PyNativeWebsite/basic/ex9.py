# Exercise 9: Check Palindrome Number
# Write a program to check if the given number is a palindrome number.
#
# A palindrome number is a number that is same after reverse. For example 545, is the palindrome numbers

# original number 121
# Yes. given number is palindrome number
#
# original number 125
# No. given number is not palindrome number

# def pilan(num):
#     x = list(str(num))
#     print(x)
#     y = x[::-1]
#     print(y)
#     if x == y:
#         return True
#     else:
#         return False
#
# print(pilan(65456))

def palindrome(number):
    print("original number", number)
    original_num = number

    # reverse the given number
    reverse_num = 0
    while number > 0:
        reminder = number % 10
        print(f"reminder {reminder}")
        reverse_num = (reverse_num * 10) + reminder
        print(f"reverse num {reverse_num}")
        number = number // 10
        print(f"number {number}")

    # check numbers
    if original_num == reverse_num:
        print("Given number palindrome")
    else:
        print("Given number is not palindrome")

palindrome(12321)
# palindrome(125)