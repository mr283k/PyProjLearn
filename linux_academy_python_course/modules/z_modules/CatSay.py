#!/usr/bin/env python3
#using plain print
def CatTalk(CatSay):
    LenCatTxt=len(CatSay)
    print(' ' * 11 + '-' * LenCatTxt)
    print(' ' * 11 + '<' + CatSay + '>')
    print(' ' * 11 +  '_' * LenCatTxt)
    print('          /\n /\_/\   /\n( 0.0 )\n > ^ <')

def main():
    CatSpk=input('what would cat like to say ? ')
    LenCatTxt=len(CatSpk)
    print('Executed in main program')
    print(' ' * 11 + '-' * LenCatTxt)
    print(' ' * 11 + '<' + CatSpk + '>')
    print(' ' * 11 +  '_' * LenCatTxt)
    print('          /\n /\_/\   /\n( 0.0 )\n > ^ <')

if __name__ == '__main__':
    main()