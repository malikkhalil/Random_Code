from os import system
from random import randint
from sys import exit
ROWS = 10
COLUMNS = 10
LEGAL_INPUTS =['a','s','d','r']

class Tetris:
	def __init__(self):
		"""
			Constructor. Sets up the playing field.
		"""
		self.matrix = [ ['-']*COLUMNS for x in range(ROWS)]
		self.round = 1
		self.current_letter = 'a'
	def play(self):
		"""
			Displays controls and initiates the game.
		"""
		print(("Welcome to Malik's Tetris game."
			"\nCommands:"
			"\na : move left"
			"\ns : do nothing"
			"\nd : move right"
			"\nr : rotate clockwise"
			"\nMemorize above then type 'standy' to play. "))
		if input().strip() == "standy":
			self._game_loop()

	def _game_loop(self):
		"""
			Game loop.
		"""
		system("clear")
		current_block = Block()
		self._draw_block(current_block)
		self.display_board()
		while True:
			cmd = None
			while(cmd not in LEGAL_INPUTS):
				print("\nEnter command: ", end="")
				cmd = input().strip()
			if cmd == 'a':
				self._erase_block(current_block)
				current_block.left()
			elif cmd == 'd':
				self._erase_block(current_block)
				current_block.right()
			elif cmd == 's':
				self._erase_block(current_block)
				current_block.nothing()
			elif cmd == 'r':
				self._erase_block(current_block)
				current_block.rotate()
			if self._check_collision(current_block):
				self._draw_block(current_block)
				current_block = Block()
				self._next_letter()
				if self._check_collision(current_block):
					print("Game over!")
					exit(0)
			self._draw_block(current_block)
			self.display_board()
			self.round += 1


	def _check_collision(self, block):
		"""
			Tests if the passed block at its proposed new location
			would collide with an existing block.
		"""
		if isinstance(block, Block):
			for location in block.get_locations():
				if self.matrix[location[0]][location[1]] != '-':
					return True
				elif location[0] == ROWS-1:
					return True
			return False
		else:
			raise Exception("Block object expected")

	def _erase_block(self, block):
		"""
			Erase a block's old position before it moves
		"""
		if isinstance(block, Block):
			for location in block.get_locations():
				self.matrix[location[0]][location[1]] = '-'
		else:
			raise Exception("Block object expected")

	def _draw_block(self, block):
		"""
			Draws the current block to the board
		"""
		if isinstance(block, Block):
			for location in block.get_locations():
				if self.matrix[location[0]][location[1]] != '-':
					raise Exception("Oops, this move shouldn't have been allowed.")
				else:
					self.matrix[location[0]][location[1]] = self.current_letter
		else:
			raise Exception("Block object expected")
	def display_board(self):
		"""
			Prints out the game board.
		"""
		system("clear")
		print("Round:", str(self.round))
		for i in range(COLUMNS+1):
			print(str(i) + " ", end="")
		for i in range(ROWS):
			print("\n" + str(i+1), end="")
			for j in range(COLUMNS):
				print(" " + str(self.matrix[i][j]), end="")
		print() 

	def _next_letter(self):
		"""
			Sets the new char for the next block
		"""
		self.current_letter = chr(ord(self.current_letter)+1)


class Block:
	PIECES = [ [[0, 0], [1, 0], [2, 0], [3, 0]], 
				[[0, 0], [1, 0], [2, 0], [2, 1]], 
				[[0, 1], [1, 1], [2, 0], [2, 1]], 
				[[0, 0], [0, 1], [1, 0], [1, 1]] ]
	def __init__(self):
		self.locations = self.PIECES[randint(0, 3)]

	def get_locations(self):
		return self.locations

	def set_locations(self, new_locations):
		self.locations = new_location

	def nothing(self):
		for location in self.locations:
			location[0]+=1

	def left(self):
		for location in self.locations:
			if location[1] == 0:
				self.nothing()
				return
		for location in self.locations:
			location[1] = location[1] - 1
		self.nothing()
	def right(self):
		for location in self.locations:
			if location[1] == COLUMNS-1:
				self.nothing()
				return
		for location in self.locations:
			location[1] = location[1] + 1
		self.nothing()
	def rotate(self):
		self.nothing()


if __name__ == '__main__':
	game = Tetris()
	game.play()