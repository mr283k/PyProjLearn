#Program to get the cost of server
#getting no of days in a given year
from calendar import monthrange
Year = int(input('Enter Year:'))
Month = int(input('Enter Month:'))
# x = print(monthrange(Year,Month)[1])
DaysInMonth = monthrange(Year,Month)[1]
CostPerHr = 0.51
CostPerDay = 0.51 * 24
#print(DaysInMonth)
#print(Year,Month,CostPerHr,DaysInMonth)
#print('cost per server for one day : {}'.format(CostPerDay))
print('cost per server for one day : ${:.2f}'.format(CostPerHr * 24))
print('cost per server for the month : ${}'.format(CostPerHr * 24 * DaysInMonth))
print('cost 20 server for one day  : ${}'.format(CostPerHr * 24 * 20))
print('cost 20 server for the month : ${}'.format(CostPerHr * 24 * DaysInMonth * 20))
print('no.of days for 1 server can rum with investment: {}'.format(918/(CostPerDay)))