import random
win = [1, 2, 3], [4, 5, 6], [ 7, 8, 9], [1, 5, 9], [7, 5, 3], [2, 5, 8], [3, 6, 9]
print(win)

human_moves = [4, 1, 2, 3] 
if human_moves in win:
	print("Winner!")

human_moves[2] = "x"
print(human_moves)

pick = random.randrange(1, 5)
print(pick)
print(win[pick])