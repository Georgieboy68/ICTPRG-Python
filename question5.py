#START
#INPUT: NUM
#SET SUM = 0
#WHILE NUM IS NOT X
           #SUM=SUM +NUM 
           #INPUT NUM
#ENDWHILE 
#PRINT SUM
#END

sum=0 
firstnum=input("Enter Number: ")
while firstnum != "x":
    sum=sum+int(firstnum)
    firstnum=input("Enter Number: ")
print("Total: ", sum) 
    
