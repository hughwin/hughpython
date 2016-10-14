# Adventure game, sees if the user can survive. 

from sys import exit 

def dead(why):
	print(why, "good job")



def start():
	print "You enter a room full of gold. How much gold will you take?"
	choice = int(raw_input(">"))
	if choice == 0:
		print "Well done for not stealing"
	if choice < 50:
		print "You've lined your pockets, but at least you didn't wake the troll" 
		exit(0)
	else: 
		print dead("You woke the troll and it crushed you to death")
start()