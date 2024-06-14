#Exercise 10: Read line number 4 from the following file

with open('/Users/mahikarinna/learn/temp/test.txt','r') as fp:
    lines = fp.readlines()
    print(lines[3])
    # counter = 0
    # for line in lines:
    #     if counter == 3:
    #         print(line)
    #     else:
    #         continue
    #     counter = counter + 1

