# Fortune cookie prints out one of five random fourtunes

import random 
fortune = random.randint(1, 5)
print fortune

if fortune == 1:
	print "one"
	
if fortune == 2:
	print "two"
				
if fortune == 3:
	print "three"
					
if fortune == 4:
	print "four"
							
if fortune == 5: 
	print "five"
	
print "The program will now close"