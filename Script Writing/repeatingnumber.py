#Write a program to ask the user for numbers, and then print any repeating numbers in a list. Example:
"""Enter a number: 5
Enter a number: 2
Enter a number: 6
Enter a number: 98
Enter a number: 7
Enter a number: 6
Enter a number: 5
Enter a number: x
Repeating numbers: [5, 6]
"""
print('Enter a number or x to exit')

numb_list = []       
repeat_numb = set()     
numb = input('Enter a number: ') 
while numb.lower() != 'x':
    if int(numb) in numb_list:
        repeat_numb.add(int(numb))
    numb_list.append(int(numb))
    numb = input('Enter a number: ')
print('Repeating numbers: ', list(repeat_numb))