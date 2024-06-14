#Exercise 4: Remove first n characters from a string
# Write a program to remove characters from a string starting from zero up to n and return a new string.

# sentence = input('Enter a string:')
# print("entered string is :",sentence)
#
# char_rem = int(input('enter no of char to remove:'))
#
# print(sentence[char_rem::])

def split_word(word,n):
    print(word)
    return word[n::]

print(split_word('positive',3))