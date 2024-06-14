#Exercise 6: Write all content of a given file into a new file by skipping line number 5

with open('/Users/mahikarinna/learn/temp/test.txt','r') as f:
    lines = f.readlines()

with open('/Users/mahikarinna/learn/temp/out.txt','w') as out:
    counter = 0
    for line in lines:
        if counter == 4 :
            counter = counter + 1
            continue
        else:
            out.write(line)
        counter = counter + 1

