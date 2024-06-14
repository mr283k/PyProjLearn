# Exercise 3: Print characters from a string that are present at an even index number

# def even_string(word):
#     for i in range(0,len(word)):
#         print(i)
#         if i % 2 == 0:
#             print(word[i])
#
# print(even_string('Hello'))


# accept input string from a user
word = input('Enter word ')
print("Original String:", word)

index = list(word)
print(index)
for i in index[0::2]:
    print(i)


# def even_string(word):
#     even_chars = ""
#     for i in range(0, len(word)):
#         if i % 2 == 0:
#             even_chars += word[i]
#     return even_chars
#
# print(even_string('Hello'))
