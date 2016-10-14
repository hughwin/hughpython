# We are going to do some gnarly maths involving functions
def add (a, b):
	return (a + b)

def subtract(a, b): 
	return (a - b)
	
def multiply(a, b):
	return (a * b)
	
def divide(a, b):
	return (a / b)
	
	

	

a = int(input("What is the first number you'd like to input: \n>"))
b = int(input("\nAnd the second? \n:"))

print "Those numbers added up are: %s" % add(a, b)
print "\nThose numbers subtracted are: %s" % subtract(a, b)
print "\nThose numbers multiplied are: %s" % multiply(a, b)
print "\nThose numbers divided are: %s" % divide(a, b)