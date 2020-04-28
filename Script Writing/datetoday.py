#Design a program which will ask the user to enter the date in the form dd/mm/yyyy. Example 23/08/2019
#then displayed as 
#Day
#Month
#Year
from itertools import groupby 
todaydate=input("input today's date in the form of dd/mm/yyyy: ")
dateArray=[''.join(j).strip('/') for sub in todaydate for k, j in groupby(sub, str.isdigit)]
print (dateArray)
print("The Date is: " + dateArray[0]+ dateArray[1])
print("The Month is: " + dateArray[3]+ dateArray[4])
print("The Year is: " + dateArray[6]+ dateArray[7]+ dateArray[8]+ dateArray[9])