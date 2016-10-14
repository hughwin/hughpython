# import the modules required

import random 
moves = []
legal_moves = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
win_conditions = ((1, 2, 3),
				  (4, 5, 6),
				  (7, 8, 9),
				  (1, 5, 9),
				  (7, 5, 3), 
				  (2, 5, 8), 
				  (3, 6, 9))
human_moves = []
computer_moves = []
human_goes_first = False
computer_goes_first = False



# Introducing the game

print("""Welcome to noughts and crosses. You are about to battle the most fearsome opponent known to man: the computer. 

----------------------
      |       |
  1   |   2   |   3
      |       |
----------------------
      |       |
  4   |   5   |   6
      |       |
----------------------    
      |       |
   7  |   8   |   9
      |       | 
      
		1) Start game
		2) Quit """)
						
	
def goesfirst():
	starts = random.randint(1 , 2)
	if starts == 1 or 2:
		print("Your turn first human")
		human_goes_first = True
		human_turn()
	if starts == 3:
		print("Ah ah! Me first!")
		computer_goes_first = True
		computer_turn()
		
def start():						
	game = input("Enter an option: ")
	if game == "1":
		print("Starting game")
		goesfirst()
		legal = legal_moves
		print(legal)
	if game == "2": 
		print("Quitting...")
		quit()
		
def human_turn():
	human_move = str(input("Enter your move" + str(legal_moves)))
	if human_move not in legal_moves:
		print("That's an invalid move")
		human_turn()
	human_moves.append(human_move)
	legal_moves[int(human_move)] = "o"
	board(human_move, "human")
	
			
		
		
def computer_turn():
	
	computer_move = str(random.randrange(1, 9))
	if computer_move not in legal_moves:
		computer_turn()
	legal_moves[int(computer_move)] = "o"
	board(computer_move, "computer")
		
# Win conditions

# Start the program 
start()

# List of moves


if human_moves in win_conditions: 
	print("The human wins. Go humans!")
if computer_moves in win_conditions:
	print("You've blown it. Computers will enslave us all")
		
# Start the game

# Who goes first? 



# Winning positions 



