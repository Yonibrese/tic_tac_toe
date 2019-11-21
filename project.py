'''tic tac toe'''

def display_board():
	top = board[0][0]+"|"+board[0][1]+"|"+board[0][2]
	middle = board[1][0]+"|"+board[1][1]+"|"+board[1][2]
	bottom = board[2][0]+"|"+board[2][1]+"|"+board[2][2]
	line = "-"*12
	print(top)
	print(line)
	print(middle)
	print(line)
	print(bottom)

def user_input1():
	user_input = input(" player One place a column number and row number ")
	ab=tuple(user_input.split())
	return ab

def user_input2():
	user_input = input(" player Two place a column number and row number ")
	ab=tuple(user_input.split())
	return ab

def replace_with_X(ab):
	a,b = ab
	a = int(a)
	b = int(b)
	board[a][b] = "x"
	return



def replace_with_O(ab):
	a,b = ab
	a = int(a)
	b = int(b)
	board[a][b] = "o"
	return


def check_row(board,x):
	win_x_1 = [x,x,x]
	if (win_x_1 in board):
		return True



def check_column(board,x):
	transposed = [[board[j][i] for j in range(len(board))]for i in range(len(board[0]))]
	win_x_1 = [x,x,x]
	if (win_x_1 in transposed):
		return True

def check_diaginal(board,x):
	if board[0][0] == x and board[1][1] == x and board[2][2] == x:
		return True
	elif board[2][2] == x and board[1][1] == x and board[0][2] == x:
		return True



def check_all(board, x = "x"):
	row = check_row(board, x)
	column = check_column(board, x)
	diaginal = check_diaginal(board , x)
	if row or column or diaginal:
		print(x +" wins the game")
		return True
	else:
		return False




board = [["0:0","0:1","0:2"],["1:0","1:1","1:2"],["2:0","2:1","2:2"]]


def tic_tac_toe(board):
	display_board()
	for i in range(1,10):
		replace_with_X(user_input1())
		display_board()
		if check_all(board,"x") == True:
			break
		replace_with_O(user_input2())
		display_board()
		if check_all(board,"o") == True:
			break
	else:
		print("tie")


tic_tac_toe(board)