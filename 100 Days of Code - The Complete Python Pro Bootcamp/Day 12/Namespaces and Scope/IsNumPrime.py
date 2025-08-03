import math

def is_prime_num(user_input):

    if user_input <= 1:
        return False

    half_input = math.ceil(user_input / 2) + 1
    for i in range(2, half_input):
        if user_input % i == 0:
            return False

    else:
        return True

print(is_prime_num(4))