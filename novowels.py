# Takes the vowels out of a message 

message = raw_input("Enter your message: ")
vowels = "aeiou"
nmessage = " "

for letter in message: 
	if letter.lower() not in vowels:
		nmessage += letter
		print "Here is your message without vowels: %s" % nmessage
		
