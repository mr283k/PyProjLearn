#Exercise 7: Accept any three string from one input() call

# x = input('enter 3 input names:')
# print(f"name 1 : {x.split(sep=' ')[0]}")

str1, str2, str3 = input('enter 3 names:').split(sep=' ')
print('name1:',str1)
print('name2:',str2)