#This file is created for code demonstration, divided by Chapters.

from datetime import datetime
from math import pi


#Chapter 1 - Printing
    #Printing file name with suffix of actual date
now = datetime.now()
module = 'Kasli'
ver = '3.4'
date = str(now)

print ( 'Test file name is %s_%s_%s' %(module, ver, date))


#Chapter 2 - Arithmetics
    #Volume calculation for regular quadrangular pyramid, where x=2 cm and h=3 cm

def function(x,h):
    return 1/3* x**2 *h

output = function(2,3)
print ('Congratulations, given regular quadrangular pyramid volume is %s [cm^3]' %(output))


#Chapter 3 - Loops
    #The loop is printing all the positive numbers, from given set of numbers and compare to the value of PI
number_list = [0, 1, 123, -10, -3.3, -2137, 3.1415, 3.1416]

print ('In the number_list we have positive numbers, such as:')
for i in number_list:
    if i <= 0:
        continue
    print (i)
    if i > pi:
        print ('Number is greater than PI')
    elif i < pi:          
        print ('Number is lower than PI')
    else:
        print ('Number is equal to PI')

