# Receive and return 
# Demonstrates parameters and return values

def display(message):
	print(message)
	
def give_me_five():
	five = 5 
	return 5 
	
def ask_yes_no(question):
	"Asks a yes no question" 
	response = None
	while response not in ("y", "n"):
		response = input(question).lower()
		
	return response
	
# Main 
display("Here's a message for you")

number = give_me_five()
print("Here's what I got from give_me_five():", number)

answer = ask_yes_no("Please enter 'y' or 'n': ")
print ("Thanks for entering", answer)

input("any key to exit")