'''# This is a guess the number game.
#START
get random number

Variables

init randomNumber = random.randint(0, 25)
guessCount = 0
correctGuess = False
totalCount = 7
items = []

set	guessCount < 7 and correctguess = False
    INPUT Var guess ( randomNumber )			
    update Var guessCount
    ADD randomnumber to array items
	IF guess < randomNumber		
	    output (Too low)
	    output ( you have how many guesses left str TotalCount - guessCount + guesses left )
	
	read guess > randomNumber		
	    PRINT (Too high)
	    PRINT ( you have how many guesses left str TotalCount - guessCount + guesses left )

	determine 
	    display("guess is correct")
        	    correctGuess = True
                    print(items)
	
	ENDIF
	
ENDWHILE

END
'''
import random
  
guessesTaken = 0
  
print('Hello! What is your name?')
myName = input()
  
number = random.randint(1, 25)
print('Well, ' + myName + ', I am thinking of a number between 1 and 25.')
 
while guessesTaken < 7:
     print('Take a guess.') 
     guess = input()
     guess = int(guess)
 
     guessesTaken = guessesTaken + 1
 
     if guess < number:
         print('Your guess is too low.') 
 
     if guess > number:
         print('Your guess is too high.')
 
     if guess == number:
         break
 
if guess == number:
     guessesTaken = str(guessesTaken)
     print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')
 
if guess != number:
     number = str(number)
     print('Guess count has been exceeded FOOL. The number I was thinking of was ' + number)