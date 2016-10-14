# A version of the alarm clock with a working GUI. 
import time
import threading

from tkinter import * 


print(time.strftime("%H:%M:%S"))

running = True # Global flag

root = Tk()
root.title('Timer')
root.state('zoomed')

sec = 0

class Application(Frame): 
	def __init__(self, master):
		super(Application, self).__init__(master)
		
		self.grid()
		self.create_widgets()
		
		
	def create_widgets(self): 
		#Explain the program
		Label(self, text = "This is a basic alarm clock program").grid(row = 0, column = 0, columnspan = 2, sticky = W)
		
		#Set the alarm time
		Label(self, text = "Enter what time you want the alarm to go off at").grid(row = 1, column = 0, sticky = W)
		self.alarmtime = Entry(self)
		self.alarmtime.grid(row = 1, column = 3, sticky = W)
		
		#Set the URL for the Youtube video
		Label(self, text = "Enter the URL of the Youtube video you want to be woken up by").grid(row = 2, column = 0, sticky = W)
		self.video_url = Entry(self)
		self.video_url.grid(row = 2, column = 3, sticky = W)
		self.bttn1 = Button(self, text = "Submit", command = self.alarm).grid(row = 5, column = 0)
		self.bttn2 = Button(self, text = "Quit", command = self.quit).grid(row = 5, column = 2)
		self.bttn3 = Button(self, text = "Stop", command = self.stop).grid(row = 5, column = 1)
		
		#Timer 		
	def tick(self):
		global sec
		sec += 1
		time = Label(root, fg='green')
		time.pack()
		time['text'] = sec
		# Take advantage of the after method of the Label
		time.after(1000, self.tick)


        
	def alarm(self):
		#Get the time and URL from the user
		sound = self.alarmtime.get()
		video = self.video_url.get()
		#Show both inputs in terminal
		print(sound)
		print(video)
		#Print starting time
		print(time.strftime("%H:%M:%S"))
		the_time = (time.strftime("%H:%M:%S"))
		while running  == True and sound != the_time:
			self.tick()
		if sound == the_time:
			print(video)
			quit()
			
	
	def quit(self):
		quit()
		
	def stop(self):
		running = False
		
		

#Main

app = Application(root) 
root.mainloop()