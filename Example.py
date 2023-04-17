#This file is created for code demonstration, divided by Chapters.

#Chapter 0 - Modules importing
    #Import of Python modules
from datetime import datetime
from math import pi


#Chapter 1 - Printing the test file name with updated version
    ##Define the variables
now = datetime.now()
module = 'Kasli'
issue = ['1', '2']
review =['1', '2', '3', '4', '5']
date = str(now)

    ##Update the issue list of a new issue +1
issue.append(len(issue) +1)

    ##Update the review list of a new review +1
review.append(len(review) +1)

    ##Define version which consist of updated issue and review in given form: issue.review
version = (str(issue[-1]) + '.' + str(review[-1]))

    ##Print the latest version 
print ( 'Latest version is', version)

    ##Print the file name which consist of module, latest version and actual date in given form: module_issue.reviev_date
print ( 'Test file name is %s_%s_%s' %(module, version, date))


#Chapter 2 - Arithmetics
    ##Volume calculation for regular quadrangular pyramid, where x=2 cm and h=3 cm

def function(x,h):
    return 1/3* x**2 *h

output = function(2,3)
print ('Congratulations, test regular quadrangular pyramid volume is %s [cm^3]' %(output))


#Chapter 3 - Loop example with comparison and result printing
    
    ##Define the number list
number_list = [0, 1, 123, -10, -3.3, -2137, 3.1415, 3.1416]

    ##Print all the positive numbers, from given set of numbers
print ('In the number_list we have positive numbers, such as:')
for i in number_list:
    if i <= 0:
        continue
    print (i)
    ## Compare the number inside the loop to the value of PI and print result each time
    if i > pi:
        print ('Number is greater than PI')
    elif i < pi:          
        print ('Number is lower than PI')
    else:
        print ('Number is equal to PI')

