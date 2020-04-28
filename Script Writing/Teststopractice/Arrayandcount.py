#PYTHON ARRAYS/LISTS
#2.Develop an application that can accept an input from the user and output how many words they have entered. 
#Description.
#prompt user to enter a string
#parse the string and break into substrings using whitespace as a delimiter.
#create a new list and copy each substring into it.
#loop through the list and count the number of entries.
#print count as number of words entered by user.
#
#BEGIN pseudo code
#    string1=input("Enter something")
#    copy string1 to list1 broken by whitespace
#    for count=0, index in list1 do
#       count++
#    end for
#    print ("You entered ". count, " number of words")
#END pseudo code
#
# BEGIN program

UserInput=input ("Enter a line of text > ")
print ("You entered ", len(UserInput), " characters")
WordList=UserInput.split()
NumWords=0
for index in WordList:
    NumWords+=1
print ("and ", NumWords, " Words")

# END program

