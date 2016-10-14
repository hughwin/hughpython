# Labeler
# Demonstrates a label

from tkinter import *

# create the root window
root = Tk()
root.title("Labeler")
root.geometry("200x100")

# create a frame in the window to hold other widgets
app = Frame(root)
app.grid()

# create a label in the frame
lbl = Label(app, text = "I'm a label!")
lbl.grid()

bttn1 = Button(app, text = "I do nothing")
bttn1.grid()

bttn2 = Button(app)
bttn2.grid()

bttn2.configure(text = "Me too!")

bttn3 = Button(app, text = "I'm the third button!")
bttn3.grid()

# kick off the window's event loop
root.mainloop()
