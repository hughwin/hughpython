# Using radio buttons 

from tkinter import * 

class Application(Frame):
	def __init__(self, master):
		super(Application, self).__init__(master):
		self.grid()
		self.create_widgets()
		
	def create_widgets(self):
		Label(self, text = "Choose your favourite type of movie").grid(row = 0, column = 0, sticky = W)
		
		Label(self, text = "Select one").grid(row = 1, column = 0, sticky = W) 
		
		self.favourite = StringVar()
		self.favourite.set(None)
		
		Radiobutton(self, text = "Comedy", variable = self.favourite, value = "comedy.", command = self.update_text).grid(row = 2, column = 0, sticky = W)
		
		Radiobutton(self, text = "Drama", variable = self.favourite, value = "drama.", command = self.update_text).grid(row = 3, column = 0, sticky = W)
		
		Radiobutton(self, text = "Romance", variable = self.favourite, value = "romance.", command = self.update_text).grid(row = 4, column = 0, sticky = W)
		
		self.results_txt = Text(self, width = 40, height = 5, wrap = WORD)
		self.results_text.grid(row = 5, column = 0, columnspan = 3)
		
	def update_text(self):
		message = "Your favourite type of movie is" 
		message += self.favourite.get()
		
	self.results_txt.delete(0.0, END)
	self.results_txt.insert(0.0, message)
	
# main 
root = Tk()
root.title("Movie Chooser 2"
app = Application(root) 
root.mainloop()
	