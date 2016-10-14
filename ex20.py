from sys import argv
script, in_file = argv 

def print_all(f):
	print f.read()
	
def rewind(f):
	f.seek(0)
	
def print_a_line(linecount, f):
	print line_count, f.readline()
	
current_file = open(in_file)

print "First let's print the whole file!"

print_all(current_file)

print "Now let's rewind like a tape."

rewind(current_file)

print "Let's do all three lines!" 

line_count = 1
current_line = 1 
print_a_line(current_line, current_file)
line_count += 1

current_line = current_line + 1 
print_a_line(current_line, current_file)
line_count += 1


current_line = current_line + 1 
print_a_line(current_line, current_file)
line_count += 1
