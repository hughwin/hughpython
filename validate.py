from sys import argv 
script, filename = argv

print "Opening the file" 

target = open(filename, 'w' )
target.truncate() 

line1 = raw_input("Line 1")
line2 = raw_input("Line 2")
line3 = raw_input("Line 3") 

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n") 
target.write(line3) 
print "Done!" 
