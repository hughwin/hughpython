# Picks a random card 

import random 

while True: 
	pick = random.randint(0, 10)
	suit_pick = random.randint(0, 3)
	number = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "Jack", "Queen", "King"]
	suit = ["Clubs", "Spades", "Diamonds", "Hearts"]
	print "Press enter to pick a random card"
	raw_input(">")
	print ("Your card is the", number[pick], "of", suit[suit_pick])
	number2 = [1, 2, 1, 4, 1, 6 , 7]
	print number2.sort()
	
	
	