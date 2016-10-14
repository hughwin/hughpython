print "Enter the beginning and ending of your slice"

word = "pizza"

start = None
while start != " ":
	start = raw_input("\n Start: ") 
	
	if start:
		start = int(start) 
	
		finish = int(raw_input("Finish: ")) 
		print "word[", start, ":", finish, "] is", word[start:finish]
	
	else: 
		print "You need to input an integer!"