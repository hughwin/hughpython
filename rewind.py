# I am going to try and write my own file manipulation program functions
from sys import argv 
script, in_file = argv
# Set's up the argument in the command line. I.e. Script first (this) followed by the file that is to be worked on (test.txt)

def read_file(f):
	print f.read()
	
# Defines the function read file. The f in the argument is the file which is opened later in the script. The function of this
# function is to read the file, and print what is being read from the input file in the command line. 

def rewind(f): 
	f.seek(0)
	
# The function of this function is to go back to the first byte of data. The Function essentially rewinds the script back to the start. 

def individual(line_count, f):
	print (line_count, f.readline())
	
line_count = 1
currentline = 1 

currentfile = open(in_file)

read_file(currentfile)

rewind(currentfile)

individual(currentline, currentfile  )
currentline += 1 
line_count += 1

individual(currentline, currentfile  )
currentline += 1 
line_count += 1

individual(currentline, currentfile  )
currentline += 1 
line_count += 1

individual(currentline, currentfile  )
currentline += 1 
line_count += 1

individual(currentline, currentfile  )
currentline += 1 
line_count += 1

	