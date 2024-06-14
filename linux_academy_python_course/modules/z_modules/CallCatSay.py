#!/usr/bin/env python3
#def display_cat(talking)

import CatSay
def main():
    CatSay.CatTalk('Feed me.')
    CatSay.CatTalk('Pet me.')
    CatSay.CatTalk('Purr. Purr.')

if __name__ == '__main__':
    main()

"""
# trying to do through the list method. 
import CatSay
Usr_inp = input('what did cat say ?')
message = []
if Usr_inp != '':
    messages.append(Usr_inp)
else:
    exit(1)

messages = ['feed me','pet me']
for message in messages:
    CatSay.CatTalk(message)
"""