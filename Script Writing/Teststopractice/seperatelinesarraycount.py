#PYTHON ARRAYS/LISTS
#3. Modify your above code to output the below on separate lines.
#   a.	The first word
#   b.	The 3rd word (if there are 3 or more words)
#   c.	Every word excluding the first and last one (if there are 3 or more words)
#Description.
#prompt user to enter a string
#parse the string and break into substrings using whitespace as a delimiter.
#create a new list and copy each substring into it.
#loop through the list and count the number of entries.
#print count as number of words entered by user.
#print the first entry in list
#print the third entry in list
#if there are 3 or more entries print the second to the last-1 entry in list
#
#BEGIN pseudo code
#    string1=input("Enter something")
#    copy string1 to list1 broken by whitespace
#    for count=0, index in list1 do
#       count++
#    end for
#    print ("You entered ", count, " number of words")
#    print ("The first word you entered was > " list(1)
#    print ("The third word you entered was > " list(3)
#    newlist=list[1cls to 3]+list[4 to -1]
#    print ("The remaining words you entered were > " newlist)
#
#END pseudo code
#
# BEGIN program

UserInput=input ("Enter a line of text > ")
print ("You entered ", len(UserInput), " charactars")
WordList=UserInput.split()
NumWords=0
for index in WordList:
    NumWords+=1
print ("and ", NumWords, " Words")
print ("The first word you entered was > ", WordList[0])
print ("The third word you was > ", WordList[2])
if NumWords >= 3:
    print ("and the remaining words you entered were > ", WordList[1:2], WordList[3:])

# END program




