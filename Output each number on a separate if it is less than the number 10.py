#Given the following python code:
#values = [66, 43, 1, 6, 2, 99, 4]
#Output each number on a separate line if it is less than the number 10. 
values=[66, 43, 1, 6, 2, 99, 4]
f=0
while f < len(values):
    if values[f] < 10:
        print(values[f])
    f+=1

