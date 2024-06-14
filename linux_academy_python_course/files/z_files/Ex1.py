with open('/Users/mahi.kalakota/dev/test.txt', 'w') as the_file:
    the_file.write('This is line one.\nThis is line two.\nFinally, we are on the third and last line of the file')
with open('/Users/mahi.kalakota/dev/test.txt', 'r') as the_file:
    print(the_file.read())
with open('/Users/mahi.kalakota/dev/test.txt') as the_file:
    print('appended file')
    i = 1
    for line in the_file:
        print('{}: {}'.format(i, line.rstrip()))
        i = i + 1
        # the_file.write('{}: {}'.format(line.count(),line))
#print(the_file.read())
