# This will test whether I will be able to learn to code using this machine!
from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_bttn()

    def create_bttn(self):
        self.bttn1 = Label(self, text = "Hugh")
        self.bttn1.grid(row = 0, column = 0, sticky = N)
        
root = Tk()
root.title("Hugh")
root.geometry("500x500")
app = Application(root)
root.mainloop()

