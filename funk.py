def resources(number1, number2):
	print "We have %r number1, and %r number2" % (number1, number2)
	
def widgets(bolts, screws):
	print "There are %r bolts, and %r screws." % (bolts, screws)
	
bolts = int(raw_input("How many bolts do you have? \n")) + 50
screws = int(raw_input("How many screws do you have? \n")) + 25
	
number1 = (50 + 4)
number2 = (50 - 10)
resources(number1, number2)
widgets(bolts, screws)
