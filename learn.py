from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "out_file exisits? %s"  % exists(out_file) 

in_file = open(from_file)
in_data = in_file.read()




