"Lets go and practice everything" 
poem = """ 
---------------
     POEM
\tHugh's life. 

The lonely world 
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation 
\n\t\t where there is none

-------------
"""

print poem.upper()

five = 10 - 2 + 3 - 6
print "This should be equal to five... %s" % five
def secret_formula(start_point): 
	jelly_beans = start_point * 500
	jars = jelly_beans / 1000 
	crates = jars / 100 
	return jelly_beans, jars, crates 
	
start_point = 10000 
beans, jars, crates = secret_formula(start_point)

print "with a starting point of %s" % start_point
print "We'd have %d beans, %d jars, and %d crates" % (beans, jars, crates)

start_point = start_point / 10 