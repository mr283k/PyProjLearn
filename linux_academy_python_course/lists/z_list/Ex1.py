

#user_input = input('enter to do list :')
#to_do = [user_input]

to_do = []
finished = False
while not finished :
    user_input = input('enter to do list :')
    if user_input == '' :
        finished = True
    else:
        to_do.append(user_input)
        finished = False

print('your To-Do List is :')
print('-' * 10 )
for user_input in to_do:
    print(user_input)