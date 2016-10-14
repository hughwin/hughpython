# Demonstrates use of global values 

value = 10 
print value

def shadowvalue():
	value = -20
	print "In shadowglobal the value is %d " % value
	
print "The value outside of the function is still equal to: %d" % value
	
print "\nHowever, the global value can be changed with in a function"

def globalvalue():
	global value
	value = -10
	print "global value", value

shadowvalue()
globalvalue()


print "The global value is now changed", value