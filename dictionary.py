# Dictionary
geek = {"404": "Clueless. From the web error 404 page not found", 
"Googling": "To look something up on Google",
"Keyboard Plaque": "The collection of debris found on computer keyboards"}


# I will now attempt to write a dictionary
print "Welcome to the dictionary"
print "\nThis dictionary will attempt define a word that you give it." 
choice = "5"
while choice != "0":
	print( """
	
	1 - Get a definition
	2 - Add a word
	0 - Quit 
	
	""" )
	choice = raw_input("What's your selection?") 
	
	if choice == "1": 
		query = raw_input("What is the word you're looking for? >")
		if query in geek:
			definition = geek[query]
			print ("\n", query, "means", definition)
		else:
			print "\nThat word isn't in the database, sorry"
			
	if choice == "2":
		word = raw_input("What is the word you'd like to add: ")
		if word not in geek:
			define = raw_input("What is the definition for the word you've just added? \n>")
			geek[word] = define
			print "\nThe term has been added."
	else:
		print "That word already exisits!"
			
		
