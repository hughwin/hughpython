# Hero's inventory

inventory = ()

#treat tuple as a condition
if not inventory:
	print "You are empty handed"
	
raw_input("Press the enter key to continue")

#create a tuple with some items 
inventory = ("sword",
			 "armour",
			 "shield", 
			 "healing potion")
			 
# Print the tuple

print "\n The tuple inventory is: "
print inventory 

# print each item 
for item in inventory: 
	print(item)
	
raw_input("Press any key to exit")