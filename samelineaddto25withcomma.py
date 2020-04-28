# Write a program that counts from 0 to 25, outputting each number on the same line, separated by commas.
number = 0
output = ''
# while number <= 25
while number <= 25:
#   append number in a line
    #output = output + str(number) +", "
    print(str(number) +",", end='')
#   add 1 to number
    number = number + 1
# end 