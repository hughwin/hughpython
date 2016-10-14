# message analyser! 

message = raw_input("Write your message! \n") 
print "The length of your mesage is: %s"  % len(message)
print "\n The most common letter in the English language is ''e''. Does your message contain e?" 

if "e" in message:
	print "\n Yes it does" 
	
else: 
	print "\n Wierdly, no it doesn't."
