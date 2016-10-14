# Simulates a battle with a troll! 

health = 10 
damage = 3
troll = 0


while health > 0:
	troll += 1 
	health -= damage
	
	
	print "The hero takes a swing at the mighty troll and does %s damage" % damage
	
	
	
else:
	print "The troll has been vanquished!"