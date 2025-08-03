def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def multi(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1/n2


operations = {
    '+': add,
    '-': sub,
    '*': multi,
    '/': div
}

# print(operations["-"](2,4))
# 4 operations[*]

# input("type the first number:")
# input("type the operator:")
# input("type the second number:")
#
# end_operation = True
# a = float(input("type the first number:"))
# while end_operation:
#     print(operations.keys())
#     o = input("Pick an operator:")
#     b = float(input("type the second number:"))
#     result = operations[o](a, b)
#     print(f"{a} {o} {b} = {result}")
#     user_choice = input(f"type 'y' to continue calculate {result}, or type 'n' to start a new calculation:")
#     if user_choice == 'y':
#         recur_operation = True
#         while recur_operation:
#             print(operations.keys())
#             a = result
#             o = input("Pick an operator:")
#             b = float(input("type the second number:"))
#             result = operations[o](a, b)
#             print(f"{a} {o} {b} = {result}")
#             user_choice = input(f"type 'y' to continue calculate {result}, or type 'n' to start a new calculation:")
#             if user_choice == 'y':
#                 recur_operation = True
#             else:
#                 recur_operation = False
#         end_operation = False


end_operation = True
a = float(input("type the first number:"))
while end_operation:
    print(operations.keys())
    o = input("Pick an operator:")
    b = float(input("type the second number:"))
    result = operations[o](a, b)
    print(f"{a} {o} {b} = {result}")
    user_choice = input(f"type 'y' to continue calculate {result}, or type 'n' to start a new calculation:")
    if user_choice == 'y':
        a = result
    else:
        end_operation = False
        print("\n" * 20)
