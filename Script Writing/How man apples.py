#Display :  Starting with 100 apples,  Keep subtracting an entered amount of apples eaten until the entered value is x. Print how many is left
#Initialise total_apples to 100
#Input : How many apples eaten:
#While apples_eaten != 'x'
#     total_apples = total_apples - apples eaten
#     Input : How many apples eaten:
#Display : There are <total_apples> left

total_apples=100
firstnum=input("how many apples eaten:")
while firstnum != "x":
    total_apples=total_apples-int(firstnum)
    firstnum=input("How many apples eaten: ",)
print("There are", total_apples, "left",)



