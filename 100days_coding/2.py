import random

# r_integer = random.randint(1,10)
# print(r_integer)
#
# r_float = random.random()
# print(r_float)
#
# #between 0 - 5
#
# r_flt_btw = r_integer * r_float
# print(r_flt_btw)
names = ["sbd","sadf","43ta","q3efas"]
len_rand = len(names)
#print(len_rand)
get_rand_position = random.randint(1, len_rand - 1)
print(get_rand_position)
print(names[get_rand_position])