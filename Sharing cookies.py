#Display :  Sharing cookies
print("Sharing Cookies, ")
#Input : Enter the number of cookies
firstnum=int(input("Enter the number of cookies we have:"))
#Input : Enter the number of people
secondnum=int(input("Enter the number of people to share amongst:"))
#Display :   <total number of cookies> cookies shared among <number of people> friends is <share of cookies> cookies each
print(firstnum,  "cookies shared among", secondnum , "friends is", int(firstnum/secondnum), "cookies each")