NoOfMiles = int(input('Enter no of miles to travel:'))
if NoOfMiles <= 3 :
    print('I suggest you to walk')
elif NoOfMiles > 3 and NoOfMiles < 300 :
    print('I suggest you to Drive')
else:
    print('I auggest you tp Fly')
print('Hope you listen to my suggestion')