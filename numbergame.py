# Produces a random number and asks the player to guess it! 
import random

print "\t\t\t Welcome! \n\n" 
print "The aim of the game is to guess what number the computer is thinking of!" 


num = random.randint(1, 100)
guessnum = 1
tries = guessnum + 1


guess = input("What is your guess!? \n ?")
while guess != num:

	if guess < num :
		print "Go lower!" 
		print tries
		break
	
	if guess > num : 
		print "Go higher!"
		print tries
		
guess = input("What is your guess!? \n ?")
	
	
