#Write a program that keeps asking the user for a number, and adds it to a total. 
# Ensure that pressing x stops entering numbers. 
# Example:

firstnum=input("Enter Number: ")
sum=0
while firstnum != "x":
    sum=sum+int(firstnum)
    firstnum=input("Enter Number: ")
print("Total: ",sum)    
