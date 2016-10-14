# Give and return 

def display(message): 
	print(message)
	
def give_me_five():
	five = 5 
	return five
	
def ask_yes_no(x): 
	""" Ask a yes no question""" 
	response = None
	while response not in ("y", "n"):
		response = input(x).lower()
	return response
	
	
display("Here's a message for you\n")

number = give_me_five()
print ("Here's what I got from give_me_five():", number)

x = raw_input("enter 'y' or 'n'")

ask_yes_no(x)
print("Thanks for entering: ", answer)

input("\n\nPress the enter key to exit.")