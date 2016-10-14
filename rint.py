# Produces a random number and asks the player to guess it! 
import random

print "\t\t\t Welcome! \n\n" 
print "The aim of the game is to guess what number the computer is thinking of!" 


num = random.randint(1, 100)
guess = int(input("What is your guess!? \n ?"))
tries = 0
tries_remaining = 5

while guess != num:

	if tries_remaining == 0:
		raw_input("Sorry, game over! Press any button to continue")
		

	if guess > num:
		print "Go lower!"
		tries_remaining += -1 
		tries += 1
		print tries
		guess = int(input("Have another go!"))
	
	else: 
		print "Go higher!"	
		tries_remaining += -1 
		tries += 1
		print tries	
		guess = int(input("Have another go!"))
	
	
