#Click counter 
#Demonstrates binding an event with an event handler

from tkinter import *

class Application(Frame):
	"""GUI application which contains button clicks""" 
	def __init__(self, master):
		"""Initalise the frame""" 
		super(Application, self).__init__(master)
		self.grid()
		self.bttn_clicks = 0 #The number pof button clicks
		self.create_widget()
	
	def create_widget(self):
		""" Create button which displays the number of clicks """
		self.bttn = Button(self)
		self.bttn["text"] = "Total Clicks: 0"
		self.bttn["command"] = self.update_count
		self.bttn.grid()
		
	def update_count(self): 
		"""Increase click count and display new total"""
		self.bttn_clicks += 1 
		self.bttn["text"] = "Total Clicks: " + str(self.bttn_clicks)
		
# main 
root = Tk()
root.title("Click Counter")
root.geometry("200x50")

app = Application(root)

root.mainloop()