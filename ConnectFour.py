#Connect four

from os import system
from sys import exit
DEFAULT_NUM_ROWS = 6
DEFAULT_NUM_COLS = 7
UNOCCUPIED_SPACE = 0

class Space:
	def __init__(self):
		"""
			Creates a space class. If player is -1, the space is unoccupied 
		"""
		self.player = UNOCCUPIED_SPACE
	def set_player(self, player):
		"""
			Sets the player,  player parameter should be an int
		"""
		self.player = player

	def __str__(self):
		return str(self.player)

class ConnectFour:
	def __init__(self):
		self.board = [[Space() for x in range(DEFAULT_NUM_COLS)] 
		for y in range(DEFAULT_NUM_ROWS)]
	def print_board(self):
		for i in range(len(self.board)):
			for j in range(len(self.board[0])):
				print(self.board[i][j], end="")
			print()
	def insert_piece(self, player, column):
		"""
			Inserts a piece for player player at given column
			Returns false if column is already full, else true
		"""
		index = 0
		if str(self.board[index][column]) != str(UNOCCUPIED_SPACE): 
			return False
		while str(self.board[index][column]) == str(UNOCCUPIED_SPACE) and index < DEFAULT_NUM_ROWS-1:
			index = index + 1
		if str(self.board[index][column]) != str(UNOCCUPIED_SPACE):
			index -=1
		self.board[index][column].set_player(player)
		return [index, column]
	def _prompt_input(self, player):
		print("\nPlayer {}, input column to insert piece: ".format(str(player))
			, end="")
		return int(input().strip())

	def _check_winner(self, player, index=[]):
		return self._check_horizontal(player, index) or \
		self._check_vertical(player, index) or \
		self._check_diagonal(player, index)

	def _check_diagonal(self, player, index=[]):
		consecutive_pieces = 1
		row, col = index
		#check left diagonal
		while row < DEFAULT_NUM_ROWS-1 and col > 0:
			row +=1
			col -=1
			if str(self.board[row][col]) == str(player):
				consecutive_pieces += 1
				if consecutive_pieces == 4:
					return True
			else:
				consecutive_pieces = 1
		row, col = index
		while row > 0 and col < DEFAULT_NUM_COLS-1:
			row -=1
			col +=1
			if str(self.board[row][col]) == str(player):
				consecutive_pieces += 1
				if consecutive_pieces == 4:
					return True
			else:
				consecutive_pieces = 1
		return False


	def _check_horizontal(self, player, index=[]):
		consecutive_pieces = 0
		for i in range(0, index[1]):
			if str(self.board[index[0]][i]) == str(player):
				consecutive_pieces += 1
				if consecutive_pieces == 4:
					return True
			else:
				consecutive_pieces = 0

		#consecutive_pieces += 1
		if consecutive_pieces == 4:
					return True

		for i in range(index[1], DEFAULT_NUM_COLS):
			if str(self.board[index[0]][i]) == str(player):
				consecutive_pieces +=1
				if consecutive_pieces == 4:
					return True
			else: 
				consecutive_pieces = 0
		return False

	def _check_vertical(self, player, index=[]):
		consecutive_pieces = 0
		for i in range(0, index[0]):
			if str(self.board[i][index[1]]) == str(player):
				consecutive_pieces += 1
				if consecutive_pieces == 4:
					return True
			else:
				consecutive_pieces = 0

		#consecutive_pieces += 1
		if consecutive_pieces == 4:
					return True

		for i in range(index[0], DEFAULT_NUM_ROWS):
			if str(self.board[i][index[1]]) == str(player):
				consecutive_pieces +=1
				if consecutive_pieces == 4:
					return True
			else: 
				consecutive_pieces = 0
		return False
	def play_game(self):
		system("clear")
		while True:
			current_player = 1
			system("clear")
			self.print_board()
			inserted = False
			idx_last_insert = []
			while not inserted:
				result = self.insert_piece(current_player, 
					self._prompt_input(current_player))
				if result:
					inserted = True
					idx_last_insert = result
					self._check_winner(current_player, idx_last_insert)
				else:
					print("You inserted at an invalid location.")
			system("clear")
			self.print_board() 
			if self._check_winner(current_player, idx_last_insert):
				print("Player {} won!".format(str(current_player)))
				exit(0)
			inserted = False
			current_player = 2
			while not inserted:
				result = self.insert_piece(current_player, 
					self._prompt_input(current_player))
				if result:
					inserted = True
					idx_last_insert = result
					self._check_winner(current_player, idx_last_insert)
				else:
					print("You inserted at an invalid location.")
			if self._check_winner(current_player, idx_last_insert):
				system("clear")
				self.print_board()
				print("Player {} won!".format(str(current_player)))
				exit(0)



testCF = ConnectFour()
testCF.play_game()
