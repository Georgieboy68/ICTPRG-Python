#Write a program that keeps asking a user for a number, 
#until the number is within the range of 50 and  70. 
#START
# Ask for number
number=int(input('Enter Number: '))
# while number is not  between 50 to 70 
while number <50 or number >70:
    print("Not within range")
    # Ask for number
    number=int(input('Enter Number: '))
print("Within Range")

 


