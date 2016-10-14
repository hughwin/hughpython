import time
import webbrowser
print time.ctime()
print "Press cntrl + C to stop the madness \n\n"


addviews = int(raw_input("How many views would you like to add to your YouTube video? \n>"))
url = raw_input("Paste the url in to the command line \n>")
views = 0

if url == "":
	print "Big mistake pal"
	addviews += 10 
	while (views < addviews): 
		webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
		views +=1
		
	

print("Starting\n")
while(views < addviews):
    time.sleep(5) # suspends the code for 5 seconds
    webbrowser.open(url)
    views += 1

print "Finished:,"
print time.ctime()
# Script is very annoying if lots of additional views are requested. You basically DoS poor old Youtube. 