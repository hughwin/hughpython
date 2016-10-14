import time
import random 
import webbrowser

#Import the argument from the command line. 
from sys import argv 
script, file1 = argv

# Check the various files 
file = open(file1, 'r')
list = file.readlines()
for item in list: 
	print item
	
newlist = [] 
newlist += list
print newlist

print len(newlist)

pick = random.randrange(len(newlist))
print pick

#Ask the user what time the alarm should go off
print "When do you want to wake up?" 
print "\nYou should enter the time you want to wake up as HH:MM:SS"
alarm = raw_input("Input time>")
 
 #Pick which videos will play
 
print "This is the video that will play", newlist[pick]

#Print the current time

print(time.strftime())

clock = time.strftime("%H:%M:%S")

while clock != alarm:
	print "The time is: %r" + clock
	clock = time.strftime("%H:%M:%S")
	time.sleep(1)
	
if alarm == clock:
	webbrowser.open(newlist[pick])