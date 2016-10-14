# computer picks a random word and jumbles it
import random 

WORDS = ("Hugh", "Jeremy", "Louise", "Amana", "John")
word = random.choice(WORDS)
correct = word 

jumble = ""

while word: 

	position = random.randrange(len(word))
	jumble += word[position]
	
	word = word[:position] + word[(position + 1):]
	
# Start the game
print(

""" 
\t\t\t Welcome to Word Jumble
\n Unscramble the letters to make a word. 
Press the enter key at any point to quit. 

"""
)
print "The jumble is: %s" % jumble

guess = raw_input("Enter your guess: ")
while guess != correct and guess != "": 
	print "Sorry, that's not it."
	guess = input("Your guess:")
	
	if guess == correct: 
		print "That's it! You guessed it! \n" 
		
print "Thanks for playing."

raw_input("\n\n Press the enter key to exit")
