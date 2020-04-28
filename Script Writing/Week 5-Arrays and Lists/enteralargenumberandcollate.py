#Write a program that asks the user for a large number, and then sums all of the digits in that number: Example:
#Enter a large number: 29834892
#Sum of the digits: 2 + 9 + 8 + 3 + 4 + 8 + 9 + 2 = 45
num = int(input("Enter a Number: "))
result = 0
hold = num

# while loop to iterate through all the digits of input number
while num > 0:
    rem = num % 10
    result = result + rem
    num = int(num/10)

# displaying output
print("Sum of the digits: ", hold, "=", result)