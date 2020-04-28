'''
# planets = ["Earth", "Mars", "Saturn", "Jupiter"]
planets = ["Earth", "Mars", "Saturn", "Jupiter"]
planets2 = ["Mercury", "Pluto", "Uranus"]
planets3 = planets + planets2
print (planets3)
'''
user = input("Enter a five word sentence: ")
#3a First word
print (user.split()[0])
#3b third word
print (user.split()[2])
#c.	Every word excluding the first and last one (if there are 3 or more words)
print (user.split()[1:-1])
