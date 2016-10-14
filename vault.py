# Hugh's attempt at a GUI with buttons


from tkinter import *

class Application(Frame):
	def __init__(self, master):
		super(Application, self).__init__(master)
		self.grid()
		self.count = 0
		self.bttn_create()

		
		
			
	def bttn_create(self):
		self.bttn = Button(self, text = "Add one")
		self.bttn.grid(row = 0, column = 0, sticky = W)
		self.bttn["command"] = self.display_count
	
	
	def display_count(self):
		self.count += 1 
		self.lbl = Label(self, text = "Count is: " + str(self.count))
		self.lbl.grid(row = 1, column = 1, sticky = S)
		
		
root = Tk()
root.title("Hugh")
root.geometry("500x500")
app = Application(root)
root.mainloop()
				