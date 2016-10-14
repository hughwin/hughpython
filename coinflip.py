# Simulates a coin flipping 100 times

import random
tries = 1 
heads = 1
tails = 1

while tries != 100:

	coinflip = random.randint(1, 2)
	print coinflip

	if coinflip == 1:
		heads += 1 
		tries +=1
		
	if coinflip == 2: 
		tails += 1
		tries +=1

		
print "Heads: %s" % heads 
print "Tails: %s" % tails