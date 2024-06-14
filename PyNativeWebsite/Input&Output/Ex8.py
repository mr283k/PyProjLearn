#Exercise 8: Format variables using a string.format() method.

totalMoney = 1000
quantity = 3
price = 450

# I have 1000 dollars so I can buy 3 football for 450.00 dollars.

print("I have {1} dollars so I can buy {0} football for {2:.2f} dollars".format(quantity,totalMoney,price))