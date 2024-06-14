# Exercise 12: Calculate income tax for the given income by adhering to the below rules
# Taxable Income	Rate (in %)
# First $10,000	0
# Next $10,000	10
# The remaining	20
# Expected Output:
#
# For example, suppose the taxable income is 45000 the income tax payable is
#
# 10000*0% + 10000*10%  + 25000*20% = $6000.

def tax(income):
    tax1 = 10000
    tax2 = 10000
    if income > 0 and income < tax1:
        return 0
    elif income > tax1 and income < (tax1 + tax2):
        print('tax2')
        return (income - tax1) * .1
    else:
        print('above 20k')
        return (tax2) * .1 + (income - tax1 - tax2) * .2

print(tax(45000))

