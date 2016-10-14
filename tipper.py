# Asks the user to input how much they spent on food and drinks, and works out how much of a tip they should give. 
print "\t\t\t Tipper"
print "\n This program asks how much you spent on food and drinks and then works out how much of a tp you should give"

drinks = input("\n How much money did you spend on drinks? >")
food = input("\n\n How much money did you spend on food? >")

print "\n\n Computing"
total = (drinks + food)
service = total *.15
tips = total *.20

print "Your total bill was: %s" % total
print "\n The service charge was: %s" % service
print "\n\n You should tip your server 20 percent if you thought you had good service. \n The recommended tip is: %s" % tips
print "The overall bill was: %s" % (total + service + tips)

print "\n\n Press any button to quit."




