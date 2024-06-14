#print('{0} * 10 \n {1} * 10 \n {2}'.format('_', input(), '-' )

#using plain print
CatSpk=input('what would cat like to say ? ')
LenCatTxt=len(CatSpk)
print(' ' * 11 + '-' * LenCatTxt)
print(' ' * 11 + '<' + CatSpk + '>')
print(' ' * 11 +  '_' * LenCatTxt)
print('          /\n /\_/\   /\n( 0.0 )\n > ^ <')

#using spaces option 2 using format
""" This code will tell us how to do the comments
in the multiple lines.
"""
"""
#variable takes input
CatSpk=input('what would cat like to say ? ')
#variable calculates length
LenCatTxt=len(CatSpk)
#builds the speech text
print(' {}'.format('_') * LenCatTxt)
print('< {} >'.format(CatSpk))
print(' {}'.format('-' * LenCatTxt))
"""