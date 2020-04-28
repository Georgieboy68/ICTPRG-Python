#Sum all of the numbers and output the result
#Average all of the numbers and output the result
#Output the maximum number in the list

list1 = [89, 456, 4, 55, 232, 2, 54, 78, 65, 45, 12, 459, 35616, 45 ,78]
list1.sort()
length=len(list1)
total=0
i=0
while i < len(list1):
    total = total + list1 [i]
    i = i + 1
print("the sum of number is: ", total)
avg = float(total/length)
print('The average number is:', avg )
print("Maximum Number is: ",  list1 [length-1])

