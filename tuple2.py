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
	
print ("You have", len(inventory), 'items in your possession.')
	
raw_input("Press any key to exit")
index = int(input ("\n Enter a number for an item in the inventory: "))
print ("At index", index, "is", inventory[index])

# Display a slice
start = int(input("\n Enter the index number to begin a slice: "))
finish = int(input("\n Enter the index number to end a slice: ")) 
print inventory[start:finish]