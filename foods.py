# Asks the user for their favourite foods and then prints the answer. 

print "This program will ask you for your two favourite foods, and then combine them into a super dish. \n Sound good? Let's continue."
favefoodone =  raw_input("What is your first favourite food >")
favefoodtwo = raw_input("What is your second favourite food? >")
print "Thinking"
print "Still thinking" 
print "Done! Your perfect meal is: %s" % (favefoodone + favefoodtwo)
raw_input("Press any key to exit the program!")