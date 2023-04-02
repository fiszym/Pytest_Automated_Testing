#This file is created for code demonstration, divided by Chapters.

#Chapter 1 - Printing

module = "Kasli"
ver = '3.4'
date = str(20230402)


print ( "Test file name is %s_%s_%s" %(module, ver, date))

#Chapter 2 - Arithmetics

def function(x,h):
    return 1/3* x**2 *h

output = function(2,3)
print ('Congratulations, given regular quadrangular pyramid volume is %s' %(output))


#Chapter 3 - Loops

number_list = [0, 1, 123, -10, -3.3, -2137]
print ("In the number_list we have positive numbers, such as:")
for i in number_list:
    if i <= 0:
        continue
    print (i)
