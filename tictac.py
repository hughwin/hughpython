# It's been a while code
# Plays a game of tictactoe against a human opponent. 

# Global constants 
X = "X" 
O = "0" 
EMPTY = " " 
TIE = "TIE" 
NUM_SQUARES = 9 

def display_instruct(): 
	""" Display game instructions""" 
	print( """
Welcome to the greatest intellectual challenge of all time: Tic-Tac Toe. 
This will be  a showdown between your human brain and my silicon processor. 
	
You will make your move known by entering a number, 0 - 8. The number 
will correspond to the board position as illustrated: 
	
			0 | 1 | 2 
			---------
			3 | 4 | 5 
			---------
			6 | 7 | 8
			
Prepare yourself human, the ultimate battle is about to begin. \n 
	
	"""
	)
def ask_yes_no(question):
	"Asks a yes or no question"
	response = None 
	while response not in ("y", "n"):
		response = input(question.lower())
	return response
	
def ask_number(question, low, high):
	"""Asks for a question within a range"""
	response = None
	while response not in range(low, high):
		response = int(input(question))
		
def pieces(): 
	"""Determine if the player or the computer gioes first""" 
	go_first = ask_yes_no("Do you require the first move? (y/n): ") 
	if go_first == "y": 
		print("\nThen take the first move. You will need it.")
		human = X 
		computer = O
	else: 
	print("Your bravery will be your undoing!") 
	computer = X 
	human = O
	
def new_board(): 
	"""Create new game board"""
	board = [] 
	for square in range (NUM_SQUARES): 
		board.append(EMPTY)
	return board
	
def display_board(): 
	"""Display game board on screen""" 
	print("\n\t", board[O], "|", board[1], "|", board[2])
	print("\t", "---------") 
	print("\t" board[3], "|", board[4], "|", board[5])
	print("\t", "---------") 
	print("\t" board[6], "|", board[7], "|", board[8]), "\n")

def legal_moves(board):
	"""Create list of legal moves""" 
	moves = [] 
	for square in range(NUM_SQUARES):
		if board[square] == EMPTY:
			Mmoves.append(square)
	return moves 
	
def winner(board):
	WAYS_TO_WIN = ((0, 1, 2), 
				   (3, 4, 5), 
				   (6, 7, 8),
				   (0, 3, 6),
				   (1, 4, 7),
				   (2, 5, 8), 
				   (0, 4, 8), 
				   (2, 4, 6))
	for rows in WAYS_TO_WIN:
		if board[row[0]] == board[row[[1] == board[row[2]] != EMPTY:
			winner = board[row[0]]
			return winner
		if EMPTY not in board: 
			return TIE
		return None
		
def human_move(board, human):
	"""Get human move""" 
	legal = legal_moves(board)
	move = None
	while move not in legal:
		move = ask_number("Where will you move? (0 - 8):", 0, NUM_SQUARES)
		if move not in legal:
			print("\nThat square is already occupied, foolish human. Choose another. \n") 
		print("Fine") 
		return move 	

	

ask_yes_no(raw_input(">"))
display_instruct()