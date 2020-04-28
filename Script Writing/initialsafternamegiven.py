#Write a program that enters a string containing a person's full name and then output their initials. Example:
#Full Name: Lachlan van der Velden
#Initials: LVDV
#Full Name: Dave Verg Douglas
#Initials: DVD
n = input('Enter your full name:')

name = ''
for i,j in enumerate(n):
    if i == 0:
        name+=(j+'.')
    elif j == ' ':
        print("Initials: ")
        name += (n[i+1]+'.')

print(name)
