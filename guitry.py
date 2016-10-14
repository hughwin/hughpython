# Repeat after me: GUI

from tkinter import * 

class Application(Frame):
	def __init__(self, master):
		super(Application, self).__init__(master)
		self.grid()
		self.bttn_create()
		
	def bttn_create(self):
		self.bttn1 = Button(self, text = "Hugh")
		self.bttn1.grid()
		
	
	
	
	
root = Tk()
root.title("Hugh")
root.geometry("500x500")

app = Application(root)
root.mainloop()