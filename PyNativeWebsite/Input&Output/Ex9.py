# Exercise 9: Check file is empty or not

import os

x = os.stat('/Users/mahikarinna/learn/temp/test.txt').st_size

print(x)