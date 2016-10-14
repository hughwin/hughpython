# highscore program 


scores = []

choice = None 

while choice != "0": 
	print (""" 
	High Scores 2.0
	1 - Show scores 
	2 - Add a score 
	3 - Delete a score 
	4 - Sort a scores
	5 - Print score
	
	"""
	)
	choice = (raw_input("Pick an option 1 - 4. Press 0 to quit."))

# exit 
	if choice == "0": 
		print "Cya!"
	
	elif choice == "1":
		print "High Scores:"
		for score in scores:
			print score
		
	elif choice == "2":
		score = int(input("Add your score: "))
		scores.append(score)

# removes the scores
	elif choice == "3": 
		score = int(input("Which score do you want to remove?"))
		if score in scores: 
			scores.remove(score)
		else: 
			print "Sorry, that score isn't in the high score list."
		
	elif choice == "4": 
		scores.sort(reverse=True)
		
	elif choice == "5": 
		print score
		
	else:
		print "Sorry, that isn't a valid choice"
	