# Hero's inventory, which demonstrates lists. 
# Create a list with some items and display with a for loop. 
inventory = ["sword", "armour", "shield", "healing potion"] 
print "Your items: "
for item in inventory: 
	print item
	
raw_input("Press any key to continue")

print "You have %s items in your inventory." % inventory

raw_input("Press any key to continue")

# test for membership. 
if "healing potion" in inventory: 
	print "You will live to fight another day!" 

#index 
index = int(raw_input("\n Enter a number for an item in the inventory: "))
print ("At index", index, "is", inventory[index])

# display a slice
start = int(raw_input("Enter the index num,ber for which you want to start a slice: "))
finish = int(raw_input("Enter the index number to end the slice: "))

# concatenating lists
chest = ["gold", "gems"] 
print "You find a chest which contains: %s" % chest
print "\nYou add the contents of the chest to your inventory."
inventory += chest
print "\n Your inventory now contains: %s" % inventory

raw_input("Press any key to continue")

# Demonstrates list mutability 

print "\nYou find a crossbow and decide to swap it for a crossbow. Sounds like a good idea I guess." 
inventory[0] = "crossbow"
print "Your inventory now contains %s: " % inventory

# Assigning by slice

print("You use your gold and gems to buy an orb of future telling.")
inventory[4:6] = ["orb of future telling"] 
print"\nYour inventory is now: %s" % inventory 
raw_input("Press any button to continue.")

# deleting a list element
print "Oh no, you've dropped your crossbow"
del inventory[0]
print inventory
