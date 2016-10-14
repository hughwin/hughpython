from sys import argv
script, file1 = argv 

file = open(file1, 'w')

file.write("Python is a great language to learn")
file.close()
print "Finished"