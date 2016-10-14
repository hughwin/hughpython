# This program will hopefully show that I understand tuples, lists and dictionaries. 
while True:
	user = ""
	print """
Welcome to this program. If will hopefully demonstrate that Hugh fully
understands tuples, lists and dictionaries as well as how they can be manipulated. 
Hugh will also demonstrate his competence with if, elif and else statements. 
	
	Let's continue. 
	
	1 - Tuples
	2 - Lists 
	3 - Dictionary
	0 - Quit
	
	"""
	user += (raw_input("Make your selection, 1 - 3\n:"))
	
	if user == "1":
		print "Starting the tuple module... \n\n"
		family = ("Hugh", "Jeremy", "Louise", "Amana", "John")
		print "So your family contains:" 
		print family
		raw_input("\nPress any key to continue")
		q1 = raw_input("Would you like to take a slice? y/n \n>")
		if q1 == "y":
			begin = int(raw_input("Where would you like your slice to begin? 0 - 4"))
			finish = int(raw_input("Where would you like your slice to finish? 0 -4"))
			print "Taking slice"
			print (family[begin:finish])
			raw_input("Press enter to go back to the main menu")
			continue
		elif q1 == "n":
			continue
			
	if user == "2":
		list = []
		list2 = ["a", "b", "c"]
		list.append(raw_input("Please input three of your favourite things seperated by commas"))
		for item in list2: 
			print item
		raw_input("Press any key to continue")
		q2 = ""
		q2 += raw_input("Are you sure those are your favourite things? y/n")
		if q2 == "y":
			print "Okay then"
			continue
			raw_input()
		if q2 == "n": 
			change = int(raw_input("Which one would you like to replace?"))
			replacement = raw_input("What would you like to replace it with?")
			list2[change] = replacement
			print list2
		
	if user == "3":
		dick = {"Pen": "Something to write with", "Pencil": "Something to write with"}
		print dick
		raw_input()
		print "Wanna see the definition again?" 
		defi = raw_input("Wanna get a definition? \nEnter a word to define:")
		print dick[defi]
		raw_input("...")
		
			
		
		
	elif user == "0":
		quit()
	
	else:
		print "I'm sorry, that is not a valid selection."
		("\nPress any key to return")
		continue
		
		
		# import pickle letters=['A','B','C']
#Writing the letters list into the file.
#fh = open("list.pkl", 'wb')
#pickle.dump(letters, fh)
#fh.close()


		